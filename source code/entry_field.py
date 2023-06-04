from tkinter import Entry
import re

class EntryField:
    def create(self, master, application):
        pass

class NormalEntryField(EntryField):
    def create(self, master, application):
        entry = Entry(master)
        return entry

class EmailEntryField(EntryField):
    def create(self, master, application):
        entry = Entry(master)
        entry.bind("<FocusOut>", lambda event, application=application: self.validate(event, application))
        return entry

    def validate(self, event, application):
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(email_regex, event.widget.get()):
            event.widget.config(bg='red')
            application.email_valid = False
        else:
            event.widget.config(bg='white')
            application.email_valid = True

class EntryFieldFactory:
    def create_entry_field(self, field_type):
        if field_type == "normal":
            return NormalEntryField()
        elif field_type == "email":
            return EmailEntryField()