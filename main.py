from w_2_num_new import convert_to_num
from tkinter import *


def clicked():

    lbl3.configure(text=convert_to_num(txt.get()))




window = Tk()
window["bg"] = "white"

window.geometry('1920x1080')

window.title("Переводчик чисел с немецкого")

lbl1 = Label(window, text="Введите число на немецком (0-999)", font=("Arial", 40), foreground="green", background="white" )
lbl4 = Label(window, text="", font=("Arial", 40), foreground="green", background="white")
btn = Button(window, text="Перевести", font=("Arial", 40), command=clicked, foreground="green", background="white")
lbl5 = Label(window, text="", font=("Arial", 40), foreground="green", background="white")
txt = Entry(window, width=30, font=("Arial", 35), foreground="green", background="white")
lbl2 = Label(window, text="Результат:", font=("Arial", 40), foreground="green", background="white")
lbl3 = Label(window, text="", font=("Arial", 30), foreground="green", background="white")

txt.focus()

lbl1.pack()
lbl4.pack()
txt.pack()
btn.pack()
lbl5.pack()
#lbl2.pack()
lbl3.pack()

window.mainloop()
