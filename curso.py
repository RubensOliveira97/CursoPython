from tkinter import *


def actionBlue():
    print("Led Azul Ligado")

def actionGreen():
    print("Led Verde Ligado")

def actionRed():
    print("Led Vermelho Ligado")


window = Tk()

window.title('Arduino Control')
window.geometry('750x750')
text1 = Label(text='Ligar Led Azul', fg='blue')
text1.grid(row=0,column=0,padx=100)

text2 = Label(text='Ligar Led Verde', fg='green')
text2.grid(row=0,column=1,padx=100)

text3 = Label(text='Ligar Led Vermelho', fg='red')
text3.grid(row=0,column=2,padx=100)

button1 = Button(text='Ligar led azul', command=actionBlue)
button1.grid(row=1,column=0,padx=100)

button2 = Button(text='Ligar led Verde', command=actionGreen)
button2.grid(row=1,column=1,padx=100)

button3 = Button(text='Ligar led Vermelho', command=actionRed)
button3.grid(row=1,column=2,padx=100)
window.mainloop()
