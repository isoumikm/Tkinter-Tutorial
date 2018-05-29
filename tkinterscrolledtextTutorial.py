# -*- coding: utf-8 -*-
"""
Created on Mon May 21 15:06:31 2018

@author: Soumik Mitra
"""

from tkinter import *
 
from tkinter import scrolledtext
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
window.geometry('350x200')
 
txt = scrolledtext.ScrolledText(window,width=40,height=10)
 
txt.grid(column=0,row=0)
 
window.mainloop()

# Set scrolledtext content
txt.insert(INSERT,'Your text goes here')

# Delete/Clear Scrolledtext content
txt.delete(1.0,END)