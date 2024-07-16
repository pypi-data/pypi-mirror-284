from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
import json


MAIN_GROUP = 'group_MAIN'


class AbstractConsumer(AsyncWebsocketConsumer):
    async def receive(self, text_data=None, bytes_data=None):

        
        payload_converted = json.loads(text_data)

        message_type = payload_converted.get('type', None)

        payload = payload_converted.get('payload', {})

        handler = self.handlers.get(message_type).handle

        await handler(self, payload)

        return await super().receive(text_data, bytes_data)

    async def update_session(self, new_session):
        self.scope['session'].update(new_session)
        await sync_to_async(self.scope["session"].save)()

    async def get_current_session(self):
        current_session_data = await sync_to_async(self.scope["session"].load)()
        return current_session_data

    async def connect(self):

        room_group_names = [MAIN_GROUP]
        self.connection_group_name = []

        self.room_group_names = room_group_names

        self.username = None
        self.id = None
        self.ip = None
        # connection_group = await database_sync_to_async(utils.create_connection)()
        # connection_group_name = connection_group.get_group_name
        # self.connection_group_name = connection_group_name

        # await self.channel_layer.group_add(
        #     MAIN_GROUP,
        #     self.channel_name
        # )

        for room_group_name in room_group_names:
            # await self.channel_layer.group_send(
            #     room_group_name,
            #     {
            #         "type":"MESSAGE",
            #         "payload": f"User joined"
            #     }
            # )
            await self.channel_layer.group_add(
                room_group_name,
                self.channel_name
            )

        await self.accept()

    async def MESSAGE(self, event):
        await self.send(text_data=json.dumps(event))

    async def dispatch(self, event):
        event_type = event['type']
        if "websocket." not in event_type:
            return await self.NOTIFICATION(event)
        return await super().dispatch(event)

    async def NOTIFICATION(self, event):
        await self.send(text_data=json.dumps(event))

    async def send_notification(self, event):

        await self.send(text_data=json.dumps(event))

    async def disconnect(self, code):
        current_session_data = await sync_to_async(self.scope["session"].load)()
        pk = current_session_data.get('id')
        await self.on_disconnect(pk)

        for room_group_name in self.room_group_names:
            await self.channel_layer.group_discard(
                room_group_name,
                self.channel_name
            )
        return await super().disconnect(code)
