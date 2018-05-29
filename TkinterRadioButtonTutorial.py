# -*- coding: utf-8 -*-
"""
Created on Mon May 21 15:03:01 2018

@author: Soumik Mitra
"""

from tkinter import *
 
from tkinter.ttk import *
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
window.geometry('350x200')
 
rad1 = Radiobutton(window,text='First', value=1)
 
rad2 = Radiobutton(window,text='Second', value=2)
 
rad3 = Radiobutton(window,text='Third', value=3)
 
rad1.grid(column=0, row=0)
 
rad2.grid(column=1, row=0)
 
rad3.grid(column=2, row=0)
 
window.mainloop()

# Also, you can set the command of any of these radio buttons to a specific function,
# so if the user clicks on any one of them, it runs the function code.
# eg.
rad1 = Radiobutton(window,text = 'First',value=1,command = clicked)
def clicked():
    #do what you need