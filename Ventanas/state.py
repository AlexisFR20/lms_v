from tkinter import Tk
from tkinter import Listbox
from tkinter import Label


ventana = Tk()

label = Label(ventana)
label.config(text="Test")
label.place(x=50,y=50)

listbox = Listbox(ventana)
listbox.config(width=50,height=30)
listbox.place(x=30,y=30)
label.lift(listbox)

ventana.mainloop()