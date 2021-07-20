from tkinter import *
from tkinter import messagebox
import os
def close():
    os.system("loladredfef")
root = Tk()
root.protocol("WM_DELETE_WINDOW", close)
root['bg'] = 'black'
root.title('Pulatov Kamran inc')
root.geometry('900x300')
root.resizable(False, False)
root.iconbitmap("KP.ico")
def exit():
    root.destroy()
def lol():
    text = inputtext.get()
    if text == "Kamrantop":
        messagebox.showinfo(title="Pulatov Kamran inc", message="Вы спаслись)")
        exit()

    else:
        messagebox.showerror(title="Pulatov Kamran inc", message="Error")
        
title = Label(text='You have been hacked\nEnter password to saving your ass', bg='black', fg="yellow", font='SimSun')
title.place(relx=0.29, rely=0.30)
q = Label(text='Author: Pulatov Kamran(@Callistodev1)', bg='black', fg="yellow", font='SimSun')
q.place(relx=0.65, rely=0.9)
inputtext = Entry(bg='gray', fg='yellow', font='SimSun', show='●')
inputtext.place(relx=0.19, rely=0.47, relwidth=0.6, relheight=0.08)

button = Button(text='Done', bg='red', font='SimSun', fg='yellow', command=lol)
button.place(relx=0.19, rely=0.57, relwidth=0.6, relheight=0.09)
root.mainloop()
