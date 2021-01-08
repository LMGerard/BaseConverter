import tkinter as tk
import re


class App:
    def __init__(self):
        # Defining the window
        self.window = tk.Tk()
        self.window.resizable(False, False)

        # Defining variables
        self.number = tk.StringVar(self.window, value=10, name="number_var")
        self.base = tk.StringVar(value=10)
        self.result = tk.StringVar(value=10)

        # Creating the widgets
        self.create()

        # Running the app
        self.window.mainloop()

    def create(self):
        # Number
        tk.Label(text="Number to convert :").grid(row=0, column=0, sticky=tk.E)
        tk.Entry(textvariable=self.number).grid(row=1, column=0)

        # Base
        tk.Label(text="Base", anchor=tk.CENTER).grid(row=2, column=0)
        tk.Entry(textvariable=self.base).grid(row=3, column=0)

        # Convert button
        tk.Button(text="Convert", command=self.convert_base).grid(row=4, column=0)

        # Result
        tk.Label(textvariable=self.result).grid(row=5, column=0)

        # Tracing variables
        self.number.trace_add("write", lambda *_: self.number_only(self.number))
        self.base.trace_add("write", lambda *_: self.number_only(self.base))

    def convert_base(self):
        number = int(self.number.get())
        base = int(self.base.get())
        result = []
        while number:
            result.insert(0, str(number % base))
            number = number // base
        self.result.set("".join(result))

    @staticmethod
    def number_only(var):
        var.set("".join(re.findall("[\d]+", var.get())))


if __name__ == '__main__':
    App()
