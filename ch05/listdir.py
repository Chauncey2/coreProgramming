import os
from time import sleep
from tkinter import *


class DirLit():
    def __init__(self, init_dir=None):
        self.top = Tk()
        self.lable = Label(self.top, text='Directory Lister v1.1').pack()
        self.cwd = StringVar(self.top)

        self.dir1 = Label(self.top, fg='blue', font=('Helvetica', '12', 'bold'))
        self.dir1.pack()

        self.dir_fm = Frame(self.top)
        self.dir_sb = Scrollbar(self.dir_fm)
        self.dir_sb.pack(side=RIGHT, expand=Y)
        self.dirs = Listbox(self.dir_fm, height=15, width=50, yscrollcommand=self.dir_sb.set)
        self.dirs.bind('<Double-1>', self.set_dir_and_go)
        self.dirs.pack(side=LEFT, fill=BOTH)
        self.dir_fm.pack()

        self.dirn = Entry(self.top, width=50, textvariable=self.cwd)
        self.dirn.bind('<Return>', self.doLS)
        self.dirn.pack()

        self.bfm = Frame(self.top)
        self.clr = Button(self.bfm, text='Clear', command=self.clr_dir,
                          activeforeground='white',
                          activebackground='green')
        self.ls = Button(self.bfm, text='List Directory', command=self.doLS,
                         activeforeground='white',
                         activebackground='green')

        self.quit = Button(self.bfm, text='Quit',
                           command=self.top.quit,
                           activeforeground='white',
                           activebackground='green')
        self.clr.pack(side=LEFT)
        self.ls.pack(side=LEFT)
        self.quit.pack(side=LEFT)
        self.bfm.pack()

        if init_dir:
            self.cwd.set(os.curdir)
            self.doLS()

    def clr_dir(self, ev=None):
        self.cwd.set('')

    def set_dir_and_go(self, ev=None):
        self.last = self.cwd.get()
        self.dirs.config(selectbackground='red')
        check = self.dirs.get(self.dirs.curselection())
        if not check:
            check = os.curdir
        self.cwd.set(check)
        self.doLS()

    def doLS(self, ev=None):
        error = ''
        tdir = self.cwd.get()
        if not tdir: tdir = os.curdir
        if not os.path.exists(tdir):
            error = tdir + 'no such file'
        elif not os.path.isdir(tdir):
            error = tdir + 'not a directory'

        if error:
            self.cwd.set(error)
            self.top.update()
            sleep(2)
            if not (hasattr(self, 'last')) and self.last:
                self.last = os.curdir
            self.cwd.set(self.last)
            self.dirs.config(selectbackground='LightSkyBlue')
            self.top.update()
            return

        self.cwd.set('FETCHING DIRECTORY CONTENTS...')
        self.top.update()
        dir_list = os.listdir(tdir)
        dir_list.sort()
        os.chdir(tdir)

        self.dir1.config(text=os.getcwd())
        self.dirs.delete(0, END)
        self.dirs.insert(END, os.curdir)
        self.dirs.insert(END, os.pardir)
        for each_file in dir_list:
            self.dirs.insert(END, each_file)
        self.cwd.set(os.curdir)
        self.dirs.config(selectbackground='LightSkyBlue')


def main():
    d = DirLit(os.curdir)
    print(os.curdir)
    mainloop()


if __name__ == '__main__':
    main()
