from graia.broadcast.entities.dispatcher import BaseDispatcher
from graia.broadcast.interfaces.dispatcher import DispatcherInterface
from graia.application.protocol.entities.message.chain import MessageChain


class MessageChainCatcher(BaseDispatcher):
    @staticmethod
    def catch(interface: "DispatcherInterface"):
        if interface.annotation is MessageChain:
            return interface.event.messageChain