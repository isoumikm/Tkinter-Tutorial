
from tkinter import *
 
from tkinter import ttk
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
tab_control = ttk.Notebook(window)
 
tab1 = ttk.Frame(tab_control)
 
tab_control.add(tab1, text='First')
 
tab_control.pack(expand=1, fill='both')
 



# You can add many tabs as you want the same way

# Add widgets to Notebooks
# After creating tabs, you can put widgets inside these tabs by assigning the parent
# property to the desired tab
from tkinter import *
 
from tkinter import ttk
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
tab_control = ttk.Notebook(window)
 
tab1 = ttk.Frame(tab_control)
 
tab2 = ttk.Frame(tab_control)
 
tab_control.add(tab1, text='First')
 
tab_control.add(tab2, text='Second')
 
lbl1 = Label(tab1, text= 'label1')
 
lbl1.grid(column=0, row=0)
 
lbl2 = Label(tab2, text= 'label2')
 
lbl2.grid(column=0, row=0)
 
tab_control.pack(expand=1, fill='both')
 
window.mainloop()

# Add spacing for widgets(padding) to make it look well organized using padx and pady properties
lbl1 = Label(tab1,text = 'label1',padx=5,pady=5)