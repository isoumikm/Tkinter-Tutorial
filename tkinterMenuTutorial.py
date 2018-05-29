from tkinter import *
 
from tkinter import Menu
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
menu = Menu(window)
 
new_item = Menu(menu)
 
new_item.add_command(label='New')
 
menu.add_cascade(label='File', menu=new_item)
 
window.config(menu=menu)
 
window.mainloop()


###############################################
# using this way , you can add as many meny items

from tkinter import *
 
from tkinter import Menu
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
menu = Menu(window)
 
new_item = Menu(menu)
 
new_item.add_command(label='New')
 
new_item.add_separator()
 
new_item.add_command(label='Edit')
 
menu.add_cascade(label='File', menu=new_item)
 
window.config(menu=menu)
 
window.mainloop()

# Here we add another meny item called Edit with a menu separator
# You may notice a dashed line at the beginning, well, if you click that line, it will
# show the menu items in a small separate window
# You can disable this feature by disabling the tearoff feature like:
new_item = Menu(menu,tearoff=0)



# I don't need to remind you that you can type any code that works when the user clicks
# clicks on any menu item by specifying the command property.
new_item.add_command(label='New',command=clicked)
