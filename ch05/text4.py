from tkinter import *


def resize(ev=None):
    lable.config(font='Helvetica -%d bold' % scale.get())


top = Tk()
top.geometry('250x150')

lable = Label(top, text='Hello World')
lable.pack(fill=X, expand=1)

scale = Scale(top, from_=10, to=40, orient=HORIZONTAL, command=resize)
scale.set(12)
scale.pack()

quit_bt = Button(top, text='Quit', command=top.quit, activeforeground='white', activebackground='red')
quit_bt.pack()
mainloop()
