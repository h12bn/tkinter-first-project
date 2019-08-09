from tkinter import *
import tkinter as tk
from PIL import ImageTk,Image
from functools import partial
root = Tk()

root.geometry("400x300")
root.minsize(350,150)
root.resizable(False, False)

     #background image
filename = ImageTk.PhotoImage(Image.open("design.jpg"))
label = Label(root, image=filename)
label.place(x=0, y=0, relwidth=1,relheight=1)
label.image = filename

     #the Menubar tool
def donothing():
    print("Welcom Again , Out Of Service")

menu = Menu(root)
root.config(menu=menu)
         #######################
submenu = Menu(menu,tearoff=0)
menu.add_cascade(label="File",menu=submenu)
submenu.add_command(label="New Project",command=donothing,)
submenu.add_command(label="New File",command=donothing)
submenu.add_command(label="New ",command=donothing)
           ######################
editmenu = Menu(menu,tearoff=0)
menu.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Redo",command=donothing)
           ######################
exitmenu = Menu(menu,tearoff=0)
menu.add_cascade(label="Exit",menu=exitmenu)
exitmenu.add_command(label="exit",command=donothing)
           #######################
quitmenu = Menu(menu,tearoff=0)
menu.add_cascade(label="Quit!", menu=quitmenu)
quitmenu.add_command(label="Quit!", command=root.quit)

    #the label parameter
label = Label(root, height=15, width=35 ,anchor=E)
label.place(x=80, y=60)

texty = Label(root, text=" Welcome To Our Site ")
texty.place(x=120,y=200)

text = Label(root, text="BECOME A TKY MEMBRE ")
text.place(x=120,y=20)

      ######################################################

# fileimg = ImageTk.PhotoImage(Image.open("tel.jpg"))
# l1 = Label(label, image=filename)
# l1.place(x=0, y=0, relwidth=1,relheight=1)
# l1.image = fileimg



           #sign app prametre
def call_result(label_result, n1, n2):

    ntext = number1.get()
    ntext1 = number2.get()
    lbel = Label(texty,text = " Welcome "+ntext+ " "+ntext1).pack()
    #lbel1 = Label(root,text = ntext1).pack()
    return

number1 = tk.StringVar()
number2 = tk.StringVar()

Label(label,text='First Name').grid(row = 0, sticky = W , padx=4)
e1 = Entry(label, textvariable=number1).grid(row=0,column=1,sticky = E,pady=4)


Label(label,text='Last Name').grid(row = 1, sticky = W , padx=4)
e2 = Entry(label , textvariable=number2).grid(row=1,column=1,sticky=E,pady=4 )

result = partial(call_result, label ,number1, number2)

c = Checkbutton(label,text="Are you membre ?!")
c.grid(column=1)
Button(label,text='Submit',command=result).grid(row=6,column=1,sticky = W)


root.mainloop()
