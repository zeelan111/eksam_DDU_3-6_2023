from concurrent.futures import thread
from email import message
import time
import tkinter as tk # først importere vi tkinter Siden Vi har brug for nogle af dens værktøjer.
from tkinter import * 
from pynput import keyboard # fra pynput importere vi keyboard 
#import win32com.client as comclt

class UI: # vi laver en class så vi kan kalde dem sener

    def __init__(self,code): # denne funktion starter programmets faner
        self.code = code
        
    
    def on_press(self, key): # vi definerer hvad der skal ske, når man trykker på enter-knappen
        self.message_recived_check()
        self.cmb = [{keyboard.Key.enter}] # vi siger til programmet at det er enter-knappen, vi vil have fat i
        self.current = set()
        if any([key in z for z in self.cmb]): # Denne linjekode er med til at få programmet til at registrere når vi klikker på enter
            self.current.add(key)
            
            if any((k in self.current for k in z) for z in self.cmb): # Disse 2 linjer koder er dem der sørger for at når enter-knappen klikkes, så kører den send_message som bliver defineret længere nedde
                self.send_message(self.text_box.get("0.0", END))
                
    def name (self): # denne del af koden lader brugeren vælge sit bruger-navne
        self.id = tk.Tk()
        title_name = Label(self.id, text="skriv dit navn").pack()
        user_name = Entry(self.id)
        user_name.pack()
        save_name = Button(self.id, text= "save name", command= lambda:self.get_name(user_name.get())).pack()
        self.id.mainloop()
        self.design()

    def design (self): # nu begynder vi at lave designet for den user interface, som brugeren skal se
         
        self.font = ("Arial", 20) # Vi sætter skrifttypen til areal og størrelsen af skriften til 20
        with keyboard.Listener(on_press = self.on_press) as listener: # Denne linje kode er med til at kalde den definition vi har oven over så den kan køre funktionen
            root = tk.Tk() # denne kode laver "root'en" der bliver det primære vindue
            h = Scrollbar(root) # disse to linjer kode laver Scrollbaren i vinduet
            h.pack(side = RIGHT, fill = Y)
            title = Label(root, text="Chatroom", font=self.font).pack() # Denne kode er titlen på chatrummet og sørger for at der står chatroom oppe i toppen
            self.Messages = Text(root, width=40, height=20, state= DISABLED, bg= "black", fg= "white", yscrollcommand = h.set, wrap = NONE) # sherry baggrundsfarven for chatboksen farven For beskeden man sætter ind samtidig med vi også de signerer vor høj og bred selve chatboksen er
            self.Messages.tag_configure("right", justify=RIGHT)
            self.Messages.tag_add("right", 1.0, "end")
            h.config(command=self.Messages.yview)
            self.Messages.pack(side=TOP, fill=Y) # man skal have pack() ellers kommer den ikke frem på displayet
            self.text_box = Text(root, width=40, height=5,) # Denne kode beskriver hvor stor den boks du skriver din besked ind i er
            self.text_box.get(1.0, END) # Her tager vi alt det som personen skriver i tekstboksen
            self.text_box.pack() # man skal have pack() ellers kommer den ikke fram på displayet
            send_text = Button(root, text= "send", bg= "lightblue", width= 10, height=5, command= lambda:self.send_message(self.text_box.get("1.0", END))).pack(side=RIGHT) # Her laver vi den knap som der skal sende beskeden videre Og får den til at køre kommandoen send_message som vi definere nedenunder
            luk = Button(root, text= "close", bg= "red", width= 10, height=5, command= lambda:self.quit()).pack(side=LEFT) # Denne knap er lige under send knap og bliver brugt til at lukke programmet           
            root.mainloop() # Denne kode sørger for at programmet holder sig selv kørende og ikke lukker med det samme efter et input
            
            #listener.join()
        

    def get_name(self, user_name): # denne funktion gemmer bruger navnet så den kommer med på teksten man skriver
        self.user_name = str(user_name + ": ")
        self.id.destroy()
        self.code.get_name(user_name)


    def message_recived_check(self):
        self.code.recived_message()

    def got_message(self, message):  
        self.Messages.config(state=NORMAL) # Gør det muligt at indsætte den nye besked i chatboksen
        self.Messages.insert(END, message) # Vi indsætter beskeden som man har sendt på den nederste linje i chatboks
        self.Messages.insert(END,"\n")
        self.Messages.config(state=DISABLED) # Sørger for at man ikke kan skrive direkte ind i chatboksen

    def send_message(self, message="test22"): # Her definerer vi funktionen og at sende en besked
        self.message = str(message) # Starter med at lave beskeden om til en string
        self.text_box.delete("1.0", END) # Vi sletter derefter Alt det der står inde i boksen så man kan skrive en ny besked
        if len(self.message) == 1: # denne gør at man ikke kan sende tomme beskeder
            self.text_box.delete("1.0", END)
        else:
            self.Messages.config(state=NORMAL) # Gør det muligt at indsætte den nye besked i chatboksen
            self.Messages.insert(END, self.user_name)
            self.Messages.insert(END, self.message) # Vi indsætter beskeden som man har sendt på den nederste linje i chatboks
            self.Messages.insert(END,"\n")
            self.code.send_message_click(message)
        
        self.Messages.config(state=DISABLED) # Sørger for at man ikke kan skrive direkte ind i chatboksen

        
    def quit(self): # Disse 2 linjer af koden sørger for at man kan slukke programmet, når man trykker på quit knappen
        exit()

if __name__ == "__main__": # denne kode søger for at programmet ikke starter med de andre programmer når du fx starter severen 
    ui = UI("test")