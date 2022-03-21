from tkinter import* 
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

root = Tk()
root.geometry("655x455")
root.title("Untitled-Notepad")
root.wm_iconbitmap(r"D:\pycharm\Notepad.ico")




def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0,END)


def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),
    ("Text Document","*.txt")])

    if file== "":
        file = None

    else:
        root.title(os.path.basename(file)+ "- Notepad")
        TextArea.delete(1.0,END)
        f = open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",
        filetypes=[("All Files","*.*"),("Text Document","*.txt")])
        
        if file =="":
            file= None

        else:
            f = open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()

            root.title(os.path.basename(file)+ "- Notepad")
            print("file saved")

    else:
        f = open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()

def  quitApp():
    root.destroy()

def copy():
    TextArea.event_generate(("<<Copy>>"))

def cut():
    TextArea.event_generate(("<<Cut>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad","Notepad by Saurabh Mishra")


#   Add Text area


TextArea = Text(root,font="lucida 13")
TextArea.pack(expand=True, fill=BOTH)
file = None


#  Lets create Menubar

MenuBar = Menu(root)
filemenu =Menu(MenuBar,tearoff = 0)

# To open new file

filemenu.add_command(label="New",command=newFile)

# To open a file form filemenu
filemenu.add_command(label="Open",command=openFile)

#  To save a file 

filemenu.add_command(label="Save",command=saveFile)
filemenu.add_separator()
filemenu.add_command(label = "Exit",command=quitApp)
MenuBar.add_cascade(label = "File",menu=filemenu)

# Edit  Menu starts
EditMenu  = Menu(MenuBar,tearoff=0)

EditMenu.add_command(label="Copy",command=copy)
EditMenu.add_command(label="Cut",command=cut)
EditMenu.add_command(label="Paste",command=paste)

MenuBar.add_cascade(label="Edit",menu=EditMenu)

# Help menu start
HelpMenu = Menu(MenuBar,tearoff=0)
HelpMenu.add_command(label="About Notepad",command=about)

MenuBar.add_cascade(label="Help",menu=HelpMenu)


root.config(menu=MenuBar)


#  Adding scrollBar
Scroll=Scrollbar(TextArea)
Scroll.pack(side=RIGHT,fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)


root.mainloop()

