import customtkinter as tk
from compute import Compute
from PIL import Image, ImageTk

class Calculator(tk.CTk):
    def __init__(self):
        self.numpad = [['AC','C','%','𝒳²'],
                       ['7','8','9','+'],
                       ['4','5','6','-'],
                       ['1','2','3','x'],
                       ['0','.','=','÷']]

        super().__init__()

        #main window
        self.title('Calculator')
        self.geometry('350x530')
        self.resizable(width=False, height=False)

        ico = Image.open('icon.png')
        photo = ImageTk.PhotoImage(ico)
        self.iconphoto(False, photo)

        self.compute = Compute()
        self.value = self.compute.displayValue

        self.display()
        self.numPadRenderer()

    #display section
    def display(self):
        displayContainer = tk.CTkFrame(master=self, width=310, height=70)
        displayContainer.pack(padx=10, pady=10)

        self.displayLabel = tk.CTkLabel(master=displayContainer, text=self.value.get(), anchor="e", width=300, height=70, font=('', 48))
        self.displayLabel.pack(padx=10, pady=10)

    #numpad section
    def numPadRenderer(self):
        numPadContainer = tk.CTkFrame(master=self)
        numPadContainer.pack(padx=10, pady=10)

        for i, rows in enumerate(self.numpad):
            for j, item in enumerate(rows):
                self.numButtonRender(numPadContainer, item, i, j)

    def numButtonRender(self, master, text: str, row: int, col: int):
        def registerClick():
            self.compute.buttonPressed(text)
            self.displayLabel.configure(text=self.value.get())

        numButton = tk.CTkButton(
            master=master, 
            text=text, 
            width=70, 
            height=70, 
            command=registerClick, 
            font=('',32)
        )
        numButton.grid(row=row, column=col, stick=tk.W, padx=5, pady=5)
                

app = Calculator()
app.mainloop()