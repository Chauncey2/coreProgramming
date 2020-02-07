"""
路标偏函数GUI应用

"""
from functools import partial as pto
from tkinter import Tk, Button, X
from tkinter.messagebox import showerror, showwarning, showinfo

WARN = 'warn'
CRIT = 'crit'
REGU = 'regu'

SIGNS = {
    'do not enter': CRIT,
    'railroad crossing': WARN,
    'SS\nspeed limit': REGU,
    'wrong way': CRIT,
    'merging traffic': WARN,
    'one way': REGU
}
critCB = lambda: showerror('Error', 'Error Button Pressed!')
warnCB = lambda: showwarning('waring', 'warning Button Pressed!')
infoCB = lambda: showinfo('Info', 'Info Button Pressed!')

top = Tk()
top.title("Road Signs")
Button(top, text='QUIT', command=top.quit).pack()

my_button = pto(Button, top)
crit_button = pto(my_button, command=critCB, bg='white', fg='red')
warn_button = pto(my_button, command=warnCB, bg='goldenrod1')
regu_button = pto(my_button, command=infoCB, bg='white')

# for each_sign in SIGNS:
#     sign_type = SIGNS[each_sign]
#     cmd = '%sButton(text=%r%s).pack(fill=X,expand=True)'%(sign_type.title(),each_sign),'.upper()' if sign_type == CRIT else '.title()')
#     eval(cmd)
top.mainloop()