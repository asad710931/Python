
import tkinter as tk
#from ctypes import windll
from tkinter import ttk
import time



#initiating tkinder for using
root=tk.Tk()

#Change title of Application
root.title('My Books')

#initiate windows size
root.geometry('400x260+0+50')

#make resizable on  x,y
root.resizable(True,False)

#attributes for some operation on application
#use or increase or decrease opacity of window
root.attributes('-alpha',0.99)
#keep your application on top of other 
#root.attributes('-topmost',0)
#root.iconbitmap('./asset/ico/1.ico')



label=tk.Label(root,text='In the Name of ALLAH !')
label.pack()
keep=False

def keepOnTop():
   global keep
   top_int=0
   text='Normal Mode'
  
   if keep!=True:
      top_int=1
      keep=True
      text="Top Mode"
   else:
      keep=False
      top_int=0
      text='Normal Mode'

   root.attributes('-topmost',top_int)   
   textlebel=ttk.Label(root,text=text)
   textlebel.pack()
      
   

button1=ttk.Button(root,text='keep Top/Below',command=keepOnTop).pack()


#this block of code for cross platform purpose


totalTime=''

def runFun():
   global totalTime
   st=time.perf_counter()
   for i in range(10000):
      print(i,' times Printing...')
   en=time.perf_counter()
   print('Whole Prosses take about ',round(en-st,3))
   totalTime=str(round(en-st,3))
   label1=ttk.Label(root,text=f'{totalTime}s').pack()

btn1=ttk.Button(root,text='start',command=runFun).pack()


def exit():
   root.destroy()
   
btn2=ttk.Button(root,text='Exit',command=exit).pack()


try:
   windll.shcore.SetProcessDpiAwareness(1)
finally:
   root.mainloop()

#to run GUI development kit only use
root.mainloop()
 
