import threading
import socket

class SERVER2:

    def __init__(self, code):
        self.code = code
        
    
    def server_connect(self):
        self.host = socket.gethostname()
        print(self.host)
        self.port = 59000
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen()

        self.clients = []
        self.names = []

    # Håndtere clienterne når de skal connecte
    def broadcast(self, message):
        for self.client in self.clients:
            self.client.send(message)

    def handle_client(self, client):
        while True:
            try: 
                message = client.recv(1024)
                self.broadcast(message)
            except:
                self.index = self.clients.index(client) # index har også noget med navne at gøre
                self.clients.remove(client)
                client.close()
                self.name = self.names[self.index]
                #self.broadcast(f'{self.name} has left the server'.encode("utf-8"))
                self.names.remove(self.name)
                break

# Modtagning af clienternes connection
    def recieve(self):
        while True:
            print("The server is running and waiting for clients...")
            self.client, self.address = self.server.accept()
            print(f"connection is connected with {str(self.address)}")
            self.client.send("name?".encode("utf-8"))
            self.name = self.client.recv(1024)
            self.names.append(self.name)
            self.clients.append(self.client)
            print(f"{self.name} has connected".encode("utf-8"))
            #self.broadcast(f"{self.name} has entered the server".encode("utf-8"))
            #self.client.send("you are now connected!".encode("utf-8"))

            # thread.start starter threading. threading.Threat går mod handle client, som går mod client argumentet. Det er den der skal være flere af.
            self.thread = threading.Thread(target = self.handle_client, args=(self.client,))
            self.thread.start()

s = SERVER2("")
s.server_connect()
s.recieve()  


    