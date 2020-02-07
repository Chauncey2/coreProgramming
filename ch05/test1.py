import tkinter


def main_lable():
    top = tkinter.Tk()
    labe1 = tkinter.Label(top, text='Hello World')
    labe1.pack()  # 放置标签
    tkinter.mainloop()  # 最后一行代码，将GUI程序放入无线主循环中执行


def main_button():
    top = tkinter.Tk()
    button = tkinter.Button(top, text="Hello", command=top.quit)
    button.pack()
    tkinter.mainloop()


if __name__ == '__main__':
    # main_lable()
    main_button()
