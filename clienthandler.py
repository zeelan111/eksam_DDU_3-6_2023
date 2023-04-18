#from AES_krypt import *
#from network_krypt import *
from UI_krypt import *
from New_client import *

class Handler:

    def __init__(self):
        self.start_client()
        #self.client.disconncet()
        self.ui.name()
        #self.server.connection()
        
    def start_client(self):
        #self.aes = AES(self)
        #self.server = SERVER(self)
        self.client = CLIENT2(self)
        self.ui = UI(self)
    
    def get_name(self, name):
        self.client.name(name)
    
    def recived_message(self):
        self.client.client_receive_thread()
    
    def send_message_click(self, message):
        self.client.client_send_thread(message)

    def got_message(self, message):
        self.ui.got_message(message)
        

if __name__ == '__main__':
    run = Handler()