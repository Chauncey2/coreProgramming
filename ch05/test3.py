import tkinter

top = tkinter.Tk()


def main(top):
    hello = tkinter.Label(top, text='Hello')
    hello.pack()

    quit = tkinter.Button(top, text='QUII', command=top.quit, bg='red', fg='white')
    quit.pack(fill=tkinter.X, expand=1)

    tkinter.mainloop()


if __name__ == '__main__':
    main(top)
