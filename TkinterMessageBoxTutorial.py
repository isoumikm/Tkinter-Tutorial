# -*- coding: utf-8 -*-
"""
Created on Mon May 21 15:08:04 2018

@author: Soumik Mitra
"""
from tkinter import *
 
from tkinter import messagebox
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
window.geometry('350x200')
 
def clicked():
 
    messagebox.showinfo('Message title', 'Message content')
 
btn = Button(window,text='Click here', command=clicked)
 
btn.grid(column=0,row=0)
 
window.mainloop()

# Show warning and error messages
# eg.
messagebox.showwarning('Message title','Message content')
messagebox.showerror('Message title','Message content')

# Show askquestion dialogs
# To show a yes no message box to the user,
# Eg.
from tkinter import messagebox
 
res = messagebox.askquestion('Message title','Message content')
 
res = messagebox.askyesno('Message title','Message content')
 
res = messagebox.askyesnocancel('Message title','Message content')
 
res = messagebox.askokcancel('Message title','Message content')
 
res = messagebox.askretrycancel('Message title','Message content')

# You can choose the appropriate message style according to your needs. Just replace the showinfo 
# function line from the previous line and run it.
# Also, you can check what button was clicked using the result variable
# If you click OK or yes or retry, it will return True value, but if you choose no or cancel, it will 
# return False.
# The only function that returns one of three values is askyesnocancel function, it returns True or 
# False or None.