from .abstract_consumer_handler_errors import TypeMissingError, MethodMissingError

HANDLER_ABSTRACT_CLASS_NAME= "AbstractConsumerHandler"


class HandlerMeta(type):
    def __new__(cls, name, bases, class_dict):
        new_cls = super().__new__(cls, name, bases, class_dict)
        if not hasattr(new_cls, 'handlers'):
            new_cls.handlers = {}
        if not AbstractConsumerHandler in bases:
            return new_cls
        if AbstractConsumerHandler in bases and not hasattr(new_cls, 'type'):
            raise TypeMissingError(name)
        if AbstractConsumerHandler in bases and not hasattr(class_dict, 'handle'):
            raise MethodMissingError(name, 'handle')
        new_cls.handlers[new_cls.type]=new_cls                        
        

class AbstractConsumerHandler(metaclass=HandlerMeta):
    '''
    Abstract class for websocket host handlers to subclass from
    Subclassed handlers should have type attribute and handler method    
    '''
    def __init__(self):
        super().__init__()