import threading
import socket
from AES_krypt import *

class CLIENT2:
    def __init__(self, code):
        self.code = code
        self.message_check = False
    
    def name(self, name):
        self.name = name
        self.client_connect()
    
    def client_connect(self):
        self.aes = AES(self)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(('DESKTOP-3PL5RI8', 59000))
        self.client_receive_thread()

    def client_receive(self):
        #while True:
        try:
            message = self.client.recv(1024).decode('utf-8')
            if message == "name?":
                self.client.send(self.name.encode('utf-8'))
                #self.code.got_message(message)
            
            elif not self.message_check:
                print(message)
                self.code.got_message(self.aes.decrypt_data(message))
            
            else:
                self.message_check = False

        
        except:
            print('Error!')
            #self.client.close()
            


    def client_send(self, message):
        #while True:
        try:
            name_and_message = f'{self.name}: {message}'
            
            self.client.send(self.aes.encrypt_data(name_and_message).encode('utf-8'))
        
        except:
            pass
        


    def client_receive_thread(self):
        receive_thread = threading.Thread(target = self.client_receive)
        receive_thread.start()
            

    def client_send_thread(self, message):
        self.message_check = True
        send_thread = threading.Thread(target = self.client_send(message))
        send_thread.start()

    def run(self):
        while True:
            self.client_receive_thread()
            #self.client_send_thread()

if __name__ == "__main__": # denne kode søger for at programmet ikke starter med de andre programmer når du fx starter severen 
    client = CLIENT2("test")
    client.name("Malte")
    client.run()