import tkinter as tk
from tkinter import Canvas, ttk

win=tk.Tk()

win.title("HI Who ?")
win.attributes('-topmost',1)
#win.iconbitmap('./asset/ico/1.ico')

btnStyle=set()
tk.Button(win,text='Mybutton',fg='white',bg='green',height=2,width=10,font=10,).pack()





win.mainloop()