from src.main_service import TitaniumDB
import json
import asyncio
import time


class Main(TitaniumDB):
    def __init__(self, token):
        super().__init__(token)

    def onServerConnect(self, message):
        print("CONNECTED TO SERVER")
        #print(type(message), message)

    def onServerDelete(self, message):
        print("SERVER CONNECTION LOST")
        #print(type(message), message)
    
    def onServerUpdate(self, message):
        print("SERVER UPDATED")
        #print(type(message), message)

    def onCollectionCreate(self, message):
        print("NEW COLLECTION CREATED")
        print(type(message), message)

    def onCollectionUpdate(self, message):
        print("NEW COLLECTION UPDATED")
        print(type(message), message)

    def onCollectioDelete(self, message):
        print("COLLECTION DELETE")
        print(type(message), message)

    def onDocumentCreate(self, message):
        print("NEW DOCUMENT CREATED")
        print(type(message), message)

    def onDocumentUpdate(self, message):
        print("DOCUMENT UPDATED")
        print(type(message), message)

    def onDocumentDelete(self, message):
        print("DOCUMENT DELETED")
        print(type(message), message)

    def onConnect(self, message):
        print("CONNECTED TO SERVER")
        print(type(message), message)
    
    def on_error(self, error):
        print(error)

    def on_close(self):
        print("CLOSED")




    
server = Main('NzAxODA2NjgxOTE0NjA1NjMx.Xp25NQ.8oWjH5u7YXtzzxZFzg98A5_jcko')











