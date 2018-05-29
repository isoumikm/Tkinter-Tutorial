# -*- coding: utf-8 -*-
"""
Created on Mon May 21 14:58:20 2018

@author: Soumik Mitra
"""

from tkinter import *
 
from tkinter.ttk import *
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
window.geometry('350x200')
 
combo = Combobox(window)
 
combo['values']= (1, 2, 3, 4, 5, "Text") #Tuple
 
combo.current(1) #set the selected item
 
combo.grid(column=0, row=0)
 
window.mainloop()

# To set the selected item, you can pass the index of the desired item to the current function
# To get the select item, you can use the get function like this: combo.get()
