from tkinter import *
from app2 import App
import tkinter.scrolledtext as st
from tkinter import messagebox

# Init Window
mainWindow = Tk()
mainWindow.geometry("400x200")
mainWindow.resizable(width=FALSE, height=TRUE)

# Init App
app = App()

# ingridList = ""


# Some functions
def addButton():
    l3.configure(state='normal')
    # global ingridList
    string = e1.get()
    # ingridList += string + "\n"
    # l3.config(text=ingridList)
    if len(string.split(",")) != 2:
        messagebox.showerror("Hata!", "Lütfen ürün,miktar formatında giriş yapın. ")
        l3.configure(state='disabled')
    else:
        l3.insert(END, string + '\n')
        l3.see(END)
        app.addIngridient(string)
        l3.configure(state='disabled')

def showRecipes():
    pass
#


l1 = Label(mainWindow, text="Add Ingridient:")
l1.grid(row=0, column=0, sticky=W, pady=10, padx=40)

e1 = Entry(mainWindow)
e1.grid(row=0, column=1, sticky=W, pady=2, padx=4)

b1 = Button(mainWindow, text="Add", command=addButton)
b1.grid(row=0, column=2, sticky=W, pady=2, padx=4)

l2 = Label(mainWindow, text="Ingridients List")
l2.grid(row=4, column=0, sticky=W, pady=10, padx=40)
# l3 = Label(mainWindow, text="")
# l3.grid(row=5, column=0, sticky=W, pady=10,padx=40)

l3 = st.ScrolledText(mainWindow, width=15, height=6)
l3.grid(row=5, column=0, sticky=W, pady=10,padx=40)
l3.configure(state='disabled')


b2 = Button(mainWindow, text="Show Recipes")
b2.grid(row=4, column=1, sticky=W, pady=2, padx=4)

mainWindow.mainloop()
