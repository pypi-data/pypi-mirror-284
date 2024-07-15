

HANDLER_ABSTRACT_CLASS_NAME= "AbstractConsumerBase"


class HandlerMeta(type):
    def __new__(cls, name, bases, dct):
        new_cls = super().__new__(cls, name, bases, dct)
        if not hasattr(new_cls, 'handlers'):
            new_cls.handlers = {}
        if HANDLER_ABSTRACT_CLASS_NAME in [base.__name__ for base in bases]:
            new_cls.handlers[new_cls.type]=new_cls
        return new_cls
        
        
        

class AbstractConsumerBase(metaclass=HandlerMeta):
    def __init__(self):
        super().__init__()