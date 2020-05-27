import json
import pprint
# web-socket client library.
import websocket
import _thread as thread
import time
import asyncio
from abc import ABCMeta, abstractmethod
from rx import Observable



class TitaniumDB:
    def __init__(self, token):
        self.token = token
        
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp("wss://gateway.discord.gg/?v=6&encoding=json",
                                    on_message = self.on_message,
                                    on_error = self.on_error,
                                    on_close = self.on_close)
        self.ws.on_open = self._on_open
        self.ws.run_forever()


    def _on_open(self):
        print("=======+++++++++INITIATING TITANIUM DB LOGGER+++++++++=======")
    
        # initial heartbeat
        heartbeat = '{"op": 1,"d": 251}'
        h_json = json.dumps(json.loads(heartbeat))
        self.ws.send(h_json)


        # initial identity
        p = {"op": 2,"d": {"token": self.token,"properties": {"$os": "linux","$browser": "disco","$device": "disco"}},"s": "null","t": "null"}
        p_json = json.dumps(p)
        self.ws.send(p_json)

        def run(*args):
            while True:
                time.sleep(30)
                # heartbeats
                self.ws.send(h_json)
            self.ws.close()
            print("thread terminating...")
        thread.start_new_thread(run, ())

   
    # Event Handlers
    def on_message(self,message):
        message = json.loads(message)
        if(message['t']=='READY'):
            self.onReady(message)

        #a = self.on(message).get()
        
        # Global Listeners
        if(message['t']=='GUILD_CREATE'):
            self.onServerConnect(message)
        if(message['t']=='GUILD_DELETE'):
            self.onServerDelete(message)
        if(message['t']=='GUILD_UPDATE'):
            self.onServerUpdate(message)
        if(message['t']=='CHANNEL_CREATE'):
            self.onCollectionCreate(message)
        if(message['t']=='CHANNEL_UPDATE'):
            self.onCollectionUpdate(message)
        if(message['t']=='CHANNEL_DELETE'):
            self.onCollectionUpdate(message)
        if(message['t']=='MESSAGE_CREATE'):
            self.onDocumentCreate(message)
        if(message['t']=='MESSAGE_UPDATE'):
            self.onDocumentUpdate(message)
        if(message['t']=='MESSAGE_DELETE'):
            self.onDocumentDelete(message)

        

        # scoped listseners
        self.on(message)
        

    @abstractmethod
    def onReady(self, message):
        pass

    @abstractmethod
    def onServerConnect(self, message):
        pass

    @abstractmethod
    def onServerUpdate(self, message):
        pass

    @abstractmethod
    def onServerDelete(self, message):
        pass

    @abstractmethod
    def onCollectionCreate(self, message):
        pass

    @abstractmethod
    def onCollectionUpdate(self, message):
        pass

    @abstractmethod
    def onCollectionDelete(self, message):
        pass

    @abstractmethod
    def onDocumentCreate(self, message):
        pass

    @abstractmethod
    def onDocumentUpdate(self, message):
        pass

    @abstractmethod
    def onDocumentDelete(self, message):
        pass

    @abstractmethod
    def on_error(self,error):
        pass

    @abstractmethod
    def on_close(self):
        pass

    @abstractmethod
    def on(self, message):
        pass




        
      
    

