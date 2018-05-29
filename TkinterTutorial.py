# -*- coding: utf-8 -*-
"""
Created on Mon May 21 14:13:48 2018

@author: Soumik Mitra
"""

# We are going to make our first Python GUI using Tkinter

# Create your first GUI application
from tkinter import *
window = Tk()
window.title("Welcome to Soumik's Tutorial")

# Setting window size
window.geometry('350x200')

# Create a label Widget

# Set label font size to make it bigger or bold or change font style you change Label function
lbl = Label(window,text = "Hello", font=("Arial Bold",50))

# Then we will set its position on the form using the grid function and give it a location like this
lbl.grid(column=0,row=0)

# Add TextBox Tkinter
txt = Entry(window,width=10)
txt.grid(column=1,row=0)
txt.focus_set()

# Now when you clicked the button, it will show the same old message, what about showing the entered text on the Entry widget
# for that we change the clicked() function
# Handle button Click Event
def clicked():
    #lbl.configure(text = "Button was clicked !!")
    res = "Welcome to " + txt.get() #Previously txt.get()
    lbl.configure(text = res)
# Adding a button widget
# Let's start by adding the button to the window, the button is created and added to the window the same as the label
# Change button foreground and background colors using fg property also you can change background color by bg property
btn = Button(window,text = "Click Me", bg="orange",fg="red",command = clicked)
btn.grid(column=2,row=0) #Previously it was one, after adding txtbox column changed to 2

window.mainloop() # endless loop always keep at the end


# In the previous Python GUI examples, we saw how to add simple widgets, now let's try getting user input using Tkinter
# Entry class(Tkinter textbox)

# You can create a text box using Tkinter Entry class like this
# txt = Entry(window,width=10) then you can add it to the window using grid function as usual


# Everytime we run the code, we need to click on the entry widget to set focus to write the text,
# what about setting the focus automatically. We just need txt.focus()

# Disable entry widget, we set txt = Entry(window,width=10,state='disabled')