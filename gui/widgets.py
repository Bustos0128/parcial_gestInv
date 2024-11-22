import tkinter as tk

class LabeledEntry(tk.Frame):
    def __init__(self, parent, label_text, entry_var=None):
        super().__init__(parent)
        self.label = tk.Label(self, text=label_text)
        self.label.pack()
        self.entry = tk.Entry(self, textvariable=entry_var)
        self.entry.pack(pady=5)

class LabeledButton(tk.Button):
    def __init__(self, parent, text, command):
        super().__init__(parent, text=text, command=command)
        self.pack(pady=10)
