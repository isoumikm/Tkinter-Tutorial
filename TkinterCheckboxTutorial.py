# -*- coding: utf-8 -*-
"""
Created on Mon May 21 15:00:24 2018

@author: Soumik Mitra
"""

from tkinter import *
 
from tkinter.ttk import *
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
window.geometry('350x200')
 
chk_state = BooleanVar()
 
chk_state.set(True) #set check state
 
chk = Checkbutton(window, text='Choose', var=chk_state)
 
chk.grid(column=0, row=0)
 
window.mainloop()

# Set Check State of a CheckButton
# Here we create a variable of type BooleanVar which is not a standard Python variable
# It's a tkinter variable and then we pass it to the CheckButton class to set the check state as the
# highlighted line in the above example

# You can set the Boolean value to false to make it unchecked.
# Also, you can use IntVar instead of BooleanVar and set the value to 0 or 1
chk_state = IntVar()
chk_state.set(0) #uncheck
chk_state(1) #check
