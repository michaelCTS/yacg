# Attention, this file is generated. Manual changes get lost with the next
# run of the code generation.
# created by yacg (template: pythonBeans.mako v1.0.0)

from enum import Enum
import yacg.model.model


class OperationBase:
    def __init__(self, dictObj=None):

        #: unique identifier for this operation
        self.operationId = None

        #: some words to explain to topic
        self.summary = None

        #: some words to explain to topic
        self.description = None

        #: some words to explain to topic
        self.message = None

        #: amqp 0.9.1 related binding parameters
        self.amqpBinding = None

        if dictObj is not None:
            self.initFromDict(dictObj)

    def initFromDict(self, dictObj):
        if dictObj is None:
            return

        self.operationId = dictObj.get('operationId', None)

        self.summary = dictObj.get('summary', None)

        self.description = dictObj.get('description', None)

        subDictObj = dictObj.get('message', None)
        if subDictObj is not None:
            self.message = Message(subDictObj)

        subDictObj = dictObj.get('amqpBinding', None)
        if subDictObj is not None:
            self.amqpBinding = OperationBindingAmqp(subDictObj)


class Message:
    """ Container that describes the messages are sent
    """

    def __init__(self, dictObj=None):

        #: either a basic or a complex type
        self.payload = None

        #: additional message parameters
        self.amqpBindings = None

        if dictObj is not None:
            self.initFromDict(dictObj)

    def initFromDict(self, dictObj):
        if dictObj is None:
            return

        subDictObj = dictObj.get('payload', None)
        if subDictObj is not None:
            self.payload = Payload(subDictObj)

        subDictObj = dictObj.get('amqpBindings', None)
        if subDictObj is not None:
            self.amqpBindings = MessageBindingsAmqp(subDictObj)


class OperationBindingAmqp:
    """ specific AMQP binding properties
    """

    def __init__(self, dictObj=None):

        self.expiration = None

        self.mandatory = None

        self.replyTo = "amq.rabbitmq.reply-to"

        if dictObj is not None:
            self.initFromDict(dictObj)

    def initFromDict(self, dictObj):
        if dictObj is None:
            return

        self.expiration = dictObj.get('expiration', None)

        self.mandatory = dictObj.get('mandatory', None)

        self.replyTo = dictObj.get('replyTo', amq.rabbitmq.reply-to)


class AsyncApiType (yacg.model.model.Type):
    """ Base type to identify AsyncApi types
    """

    def __init__(self, dictObj=None):
        super(yacg.model.model.Type, self).__init__()
        pass

        if dictObj is not None:
            self.initFromDict(dictObj)

    def initFromDict(self, dictObj):
        if dictObj is None:
            return


class AsyncApiInfo (AsyncApiType):
    """ Subset of the info object attribs: https://www.asyncapi.com/docs/specifications/v2.0.0#infoObject
    """

    def __init__(self, dictObj=None):
        super(AsyncApiType, self).__init__()

        self.title = None

        self.version = None

        self.description = None

        if dictObj is not None:
            self.initFromDict(dictObj)

    def initFromDict(self, dictObj):
        if dictObj is None:
            return

        self.title = dictObj.get('title', None)

        self.version = dictObj.get('version', None)

        self.description = dictObj.get('description', None)


class AsyncApiServer (AsyncApiType):
    """ one entry of the servers section
    """

    def __init__(self, dictObj=None):
        super(AsyncApiType, self).__init__()

        self.name = None

        self.url = None

        self.description = None

        self.protocol = None

        self.protocolVersion = None

        if dictObj is not None:
            self.initFromDict(dictObj)

    def initFromDict(self, dictObj):
        if dictObj is None:
            return

        self.name = dictObj.get('name', None)

        self.url = dictObj.get('url', None)

        self.description = dictObj.get('description', None)

        self.protocol = dictObj.get('protocol', None)

        self.protocolVersion = dictObj.get('protocolVersion', None)


class Channel (AsyncApiType):
    """ one entry of the channels section
    """

    def __init__(self, dictObj=None):
        super(AsyncApiType, self).__init__()

        self.key = None

        self.description = None

        self.parameters = []

        self.publish = None

        self.subscribe = None

        self.amqpBindings = None

        if dictObj is not None:
            self.initFromDict(dictObj)

    def initFromDict(self, dictObj):
        if dictObj is None:
            return

        self.key = dictObj.get('key', None)

        self.description = dictObj.get('description', None)

        arrayParameters = dictObj.get('parameters', [])
        for elemParameters in arrayParameters:
            self.parameters.append(
                Parameter(elemParameters))

        subDictObj = dictObj.get('publish', None)
        if subDictObj is not None:
            self.publish = PublishOperation(subDictObj)

        subDictObj = dictObj.get('subscribe', None)
        if subDictObj is not None:
            self.subscribe = OperationBase(subDictObj)

        subDictObj = dictObj.get('amqpBindings', None)
        if subDictObj is not None:
            self.amqpBindings = ChannelBindingsAmqp(subDictObj)


class Parameter:
    """ Parameters contained in the channel key
    """

    def __init__(self, dictObj=None):

        self.name = None

        self.description = None

        self.type = None

        if dictObj is not None:
            self.initFromDict(dictObj)

    def initFromDict(self, dictObj):
        if dictObj is None:
            return

        self.name = dictObj.get('name', None)

        self.description = dictObj.get('description', None)

        self.type = dictObj.get('type', None)


class PublishOperation (OperationBase):
    """ Configuration parameter needed for publishing
    """

    def __init__(self, dictObj=None):
        super(OperationBase, self).__init__()

        #: covers the responded type in RPC style communication, custom extension
        self.xResponseType = None

        if dictObj is not None:
            self.initFromDict(dictObj)

    def initFromDict(self, dictObj):
        if dictObj is None:
            return

        subDictObj = dictObj.get('xResponseType', None)
        if subDictObj is not None:
            self.xResponseType = XResponseType(subDictObj)


class ChannelBindingsAmqp:
    """ https://github.com/asyncapi/bindings/blob/master/amqp/README.md#channel
    """

    def __init__(self, dictObj=None):

        self.isType = None

        #: channel queue parameters
        self.queue = None

        #: channel exchange parameters
        self.exchange = None

        if dictObj is not None:
            self.initFromDict(dictObj)

    def initFromDict(self, dictObj):
        if dictObj is None:
            return

        self.isType = ChannelBindingsAmqpIsTypeEnum.valueForString(dictObj.get('isType', None))

        subDictObj = dictObj.get('queue', None)
        if subDictObj is not None:
            self.queue = ChannelBindingsAmqpQueue(subDictObj)

        subDictObj = dictObj.get('exchange', None)
        if subDictObj is not None:
            self.exchange = ChannelBindingsAmqpExchange(subDictObj)


class ChannelBindingsAmqpIsTypeEnum(Enum):
    QUEUE = 'queue'
    ROUTINGKEY = 'routingKey'

    @classmethod
    def valueForString(cls, stringValue):
        lowerStringValue = stringValue.lower() if stringValue is not None else None
        if lowerStringValue is None:
            return None
        elif lowerStringValue == 'queue':
            return ChannelBindingsAmqpIsTypeEnum.QUEUE
        elif lowerStringValue == 'routingkey':
            return ChannelBindingsAmqpIsTypeEnum.ROUTINGKEY
        else:
            return None

    @classmethod
    def valueAsString(cls, enumValue):
        if enumValue is None:
            return ''
        elif enumValue == ChannelBindingsAmqpIsTypeEnum.QUEUE:
            return 'queue'
        elif enumValue == ChannelBindingsAmqpIsTypeEnum.ROUTINGKEY:
            return 'routingKey'
        else:
            return ''



class ChannelBindingsAmqpQueue:
    """ channel queue parameters
    """

    def __init__(self, dictObj=None):

        self.name = None

        self.durable = None

        self.exclusive = None

        self.autodelete = None

        if dictObj is not None:
            self.initFromDict(dictObj)

    def initFromDict(self, dictObj):
        if dictObj is None:
            return

        self.name = dictObj.get('name', None)

        self.durable = dictObj.get('durable', None)

        self.exclusive = dictObj.get('exclusive', None)

        self.autodelete = dictObj.get('autodelete', None)


class ChannelBindingsAmqpExchange:
    """ channel exchange parameters
    """

    def __init__(self, dictObj=None):

        self.name = None

        self.type = None

        self.durable = None

        self.autodelete = None

        if dictObj is not None:
            self.initFromDict(dictObj)

    def initFromDict(self, dictObj):
        if dictObj is None:
            return

        self.name = dictObj.get('name', None)

        self.type = ChannelBindingsAmqpExchangeTypeEnum.valueForString(dictObj.get('type', None))

        self.durable = dictObj.get('durable', None)

        self.autodelete = dictObj.get('autodelete', None)


class ChannelBindingsAmqpExchangeTypeEnum(Enum):
    TOPIC = 'topic'
    DIRECT = 'direct'
    FANOUT = 'fanout'
    DEFAULT = 'default'
    HEADERS = 'headers'

    @classmethod
    def valueForString(cls, stringValue):
        lowerStringValue = stringValue.lower() if stringValue is not None else None
        if lowerStringValue is None:
            return None
        elif lowerStringValue == 'topic':
            return ChannelBindingsAmqpExchangeTypeEnum.TOPIC
        elif lowerStringValue == 'direct':
            return ChannelBindingsAmqpExchangeTypeEnum.DIRECT
        elif lowerStringValue == 'fanout':
            return ChannelBindingsAmqpExchangeTypeEnum.FANOUT
        elif lowerStringValue == 'default':
            return ChannelBindingsAmqpExchangeTypeEnum.DEFAULT
        elif lowerStringValue == 'headers':
            return ChannelBindingsAmqpExchangeTypeEnum.HEADERS
        else:
            return None

    @classmethod
    def valueAsString(cls, enumValue):
        if enumValue is None:
            return ''
        elif enumValue == ChannelBindingsAmqpExchangeTypeEnum.TOPIC:
            return 'topic'
        elif enumValue == ChannelBindingsAmqpExchangeTypeEnum.DIRECT:
            return 'direct'
        elif enumValue == ChannelBindingsAmqpExchangeTypeEnum.FANOUT:
            return 'fanout'
        elif enumValue == ChannelBindingsAmqpExchangeTypeEnum.DEFAULT:
            return 'default'
        elif enumValue == ChannelBindingsAmqpExchangeTypeEnum.HEADERS:
            return 'headers'
        else:
            return ''



class XResponseType:
    """ type that is responded in RPC style communication
    """

    def __init__(self, dictObj=None):

        self.description = None

        #: true - if the property is an array
        self.isArray = False

        #: defined minimum of elements in the array/list
        self.arrayMinItems = None

        #: defined maximum of elements in the array/list
        self.arrayMaxItems = None

        #: the elements in the array/list have to be unique
        self.arrayUniqueItems = None

        #: either a basic or a complex type
        self.type = None

        if dictObj is not None:
            self.initFromDict(dictObj)

    def initFromDict(self, dictObj):
        if dictObj is None:
            return

        self.description = dictObj.get('description', None)

        self.isArray = dictObj.get('isArray', False)

        self.arrayMinItems = dictObj.get('arrayMinItems', None)

        self.arrayMaxItems = dictObj.get('arrayMaxItems', None)

        self.arrayUniqueItems = dictObj.get('arrayUniqueItems', None)

        subDictObj = dictObj.get('type', None)
        if subDictObj is not None:
            self.type = yacg.model.model.Type(subDictObj)


class Payload:
    def __init__(self, dictObj=None):

        #: meta model type that is passed in the body
        self.type = None

        self.isArray = False

        if dictObj is not None:
            self.initFromDict(dictObj)

    def initFromDict(self, dictObj):
        if dictObj is None:
            return

        subDictObj = dictObj.get('type', None)
        if subDictObj is not None:
            self.type = yacg.model.model.Type(subDictObj)

        self.isArray = dictObj.get('isArray', False)


class MessageBindingsAmqp:
    """ https://github.com/asyncapi/bindings/blob/master/amqp/README.md#message-binding-object
    """

    def __init__(self, dictObj=None):

        #: A MIME encoding for the message content.
        self.contentEncoding = None

        #: Application defined text
        self.messageType = None

        if dictObj is not None:
            self.initFromDict(dictObj)

    def initFromDict(self, dictObj):
        if dictObj is None:
            return

        self.contentEncoding = dictObj.get('contentEncoding', None)

        self.messageType = dictObj.get('messageType', None)


