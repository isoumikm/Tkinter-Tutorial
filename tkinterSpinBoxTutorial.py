# -*- coding: utf-8 -*-
"""
Created on Mon May 21 15:11:25 2018

@author: Soumik Mitra
"""

from tkinter import *
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
window.geometry('350x200')
 
spin = Spinbox(window, from_=0, to=100, width=5)
 
spin.grid(column=0,row=0)
 
window.mainloop()

# You can specify the numbers for the SpinBox instead of using the whole range like
# Eg.
spin = Spinbox(window,values=(3,8,11),width=5)

# Set the default value for Spinbox
var = IntVar()
var.set(36)
spin = Spinbox(window,from_=0, to=100,width=5,textvariable=var)