import tkinter as tk
from tkinter import Button, ttk

def fahrenheitToCelsius(f):
    return (f-32)*5/9

root = tk.Tk()
 
root.title("Tipo~ Converter")
root.geometry('350x100')
root.resizable(False,False)
root.attributes('-topmost',1)


frame=ttk.Frame(root)

options={'padx':5,'pady':5}

#label for app
cov_label=ttk.Label(frame,text="Fahrenheit",background='dodgerblue',foreground='white',font=12)
cov_label.grid(column=0,row=0,sticky='W',**options)

tem_value=tk.StringVar()
tem_entry=ttk.Entry(frame,textvariable=tem_value)
tem_entry.grid(column=1,row=0,**options)
tem_entry.focus()

def converter_fuc():
    fahr=float(tem_value.get())
    c=fahrenheitToCelsius(fahr)
    result_text=f' {fahr} Fahrenheit = {c:.2f} degree Celsius'
    result_lbl.configure(text=result_text,background='gold',foreground='black')


cov_btn=ttk.Button(frame,text='Convert')
cov_btn.grid(column=2,row=0, sticky='W',**options)
cov_btn.configure(command=converter_fuc)

result_lbl=ttk.Label(frame)
result_lbl.grid(columnspan=3,row=1,**options)

frame.grid(padx=10,pady=10)
root.mainloop()

