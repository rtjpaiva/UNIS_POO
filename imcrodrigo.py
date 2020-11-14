from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fonte1 = ("Verdana"), ("12")

        self.brk1 = Frame(master)
        self.brk1["pady"] = 50
        self.brk1.pack()

        self.brk2 = Frame(master)
        self.brk2["padx"] = 100
        self.brk2.pack()

        self.brk3 = Frame(master)
        self.brk3["padx"] = 100
        self.brk3.pack()

        self.brk4 = Frame(master)
        self.brk4["padx"] = 100
        self.brk4.pack()

        self.brk5 = Frame(master)
        self.brk5["padx"] = 100
        self.brk5.pack()

        self.brk6 = Frame(master)
        self.brk6["padx"] = 100
        self.brk6.pack()

        self.nome = Label(self.brk1, text="CALCULO DE INDICE DE MASSA CORPORAL")
        self.nome["font"] = ("Verdana", "12", "bold")
        self.nome.pack()

        self.dgtLabel = Label(self.brk2, text="PESO(KG):", font=self.fonte1)
        self.dgtLabel.pack(side=LEFT)

        self.dgt = Entry(self.brk2)
        self.dgt["width"] = 20
        self.dgt["font"] = self.fonte1
        self.dgt.pack(side=LEFT)

        self.dgt2Label = Label(self.brk3, text="ALTURA(CM):", font=self.fonte1)
        self.dgt2Label.pack(side=LEFT)

        self.dgt2 = Entry(self.brk3)
        self.dgt2["width"] = 20
        self.dgt2["font"] = self.fonte1
        self.dgt2.pack(side=LEFT)

        self.imcLabel = Label(self.brk4, text="I.M.C.:", font=self.fonte1)
        self.imcLabel.pack(side=LEFT)

        self.imcValor = Label(self.brk5, text="", font=self.fonte1)
        self.imcValor.pack(side=RIGHT)

        self.calcular = Button(self.brk6)
        self.calcular["text"] = "CALCULAR"
        self.calcular["font"] = ("Verdama", "10")
        self.calcular["width"] = 12
        self.calcular["command"] = self.calcula
        self.calcular.pack()

    def calcula(self):
        peso = self.dgt.get()
        altura = self.dgt2.get()

        tot = (float(peso)) / ((float(altura)/100) * (float(altura)/100))
        if peso:
            self.imcValor["text"] = round(tot,2),"(KG/M²)"

root = Tk()
Application(root)
root.mainloop()
