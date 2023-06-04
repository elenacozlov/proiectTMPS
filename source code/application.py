from tkinter import Frame, Label, StringVar, Radiobutton, Button, messagebox, W
from singleton import SingletonMeta
from entry_field import EntryFieldFactory
from alignment import Alignment
from doc_gen import *

class Application(Frame, metaclass=SingletonMeta):
    def __init__(self, master=None):
        self.email_valid = True
        self.factory = EntryFieldFactory()
        Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.entries = {}
        fields = ["Denumirea completa", "IDNO", "Din", "Termen", "Acte", "Centrul Multifunctional", "Adresa electronica", "Administratori"]

        for field in fields:
            Label(self, text=field).pack()
            if field == "Adresa electronica":
                self.entries[field] = self.factory.create_entry_field("email").create(self, self)
            else:
                self.entries[field] = self.factory.create_entry_field("normal").create(self, self)
            self.entries[field].pack()

        self.doc_format = StringVar()
        self.doc_format.set("pdf")  # Set the default format to PDF

        # Add radio buttons for selecting document format
        Radiobutton(self, text="PDF", variable=self.doc_format, value="pdf").pack(anchor=W)
        Radiobutton(self, text="Word", variable=self.doc_format, value="word").pack(anchor=W)

        self.generate_button = Button(self)
        self.generate_button["text"] = "Genereaza cererea"
        self.generate_button["command"] = self.generate_request
        self.generate_button.pack()
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def notify_request_generated(self):
        for observer in self.observers:
            observer.update("Cererea a fost generata!")
        
        messagebox.showinfo("Notificare", "Cererea a fost generata!")

    def generate_request(self):
        if not self.email_valid:
            messagebox.showerror("Eroare", "Adresa de e-mail nu este valida!")
            return

        lines = [
            ("I.P. „Agentia Servicii Publice”", Alignment.RIGHT),
            ("Departamentul inregistrare si", Alignment.RIGHT),
            ("licentiere a unitatilor de drept",Alignment.RIGHT),
            ("______________", Alignment.LEFT),
            ("data depunerii", Alignment.LEFT),
            ("CERERE", Alignment.CENTER),
            (f"de inregistrare in Registrul de stat al persoanelor juridice a reluarii activitatii {self.entries['Denumirea completa'].get()}", Alignment.CENTER),
            (f"IDNO {self.entries['IDNO'].get()} din {self.entries['Din'].get()}", Alignment.CENTER),
            (f"Solicitam inregistrarea si inscrierea in Registrul de stat al persoanelor juridice, in termen de {self.entries['Termen'].get()} ore", Alignment.CENTER),
            (f"a datelor privind reluarea activitatii {self.entries['Denumirea completa'].get()} {self.entries['IDNO'].get()}", Alignment.CENTER),
            ("intru sustinerea cererii prezintam urmatoarele acte:", Alignment.LEFT),
            (f"1. {self.entries['Acte'].get()}", Alignment.LEFT),
            ("Declaram pe propria raspundere ca datele completate în cerere, precum si cele ce se contin în documentele anexate la cerere sunt veridice, iar documentele anexate sunt autentice.", Alignment.LEFT),
            ("Solicitam eliberarea extrasului din Registrul de stat al persoanelor juridice:", Alignment.LEFT),
            (f"pe suport de hartie la sediul Centrului Multifunctional {self.entries['Centrul Multifunctional'].get()}.", Alignment.LEFT),
            (f"in format electronic la adresa electronica: {self.entries['Adresa electronica'].get()}.", Alignment.LEFT),
            ("Nota: Prelucrarea datelor cu caracter personal se efectueaza în conformitate cu Legea nr.133/2011 privind protectia datelor cu caracter personal.", Alignment.LEFT),
            (f"Administrator(i): {self.entries['Administratori'].get()}", Alignment.CENTER),
            ("Semnatura: _______________", Alignment.CENTER),
        ]

        generator = DocumentGeneratorFacade("/home/lena/uni/3rd year/sem VI/TMPS/proiect de curs/source code/generated")

        if self.doc_format.get() == "pdf":
            generator.generate_pdf(lines, self.entries)
        else:
            generator.generate_word(lines, self.entries)
        
        self.notify_request_generated()


class ApplicationObserver:
    def update(self, message):
        pass

class GUINotifier(ApplicationObserver):
    def update(self, message):
        messagebox.showinfo("Notificare", message)
