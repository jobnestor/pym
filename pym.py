#Imports Tkinter (now available for use)
from Tkinter import *

#Sets up the basic parameters of the GUI
tk = Tk()
tk.title("PYM")
tk.geometry("500x500")
#Create the welcome screen
app = Frame(tk)
label = Label(app, text="Welcome! What would you like to do?")
label.grid()
app.grid()
New = Button(app, text="Create new server.proprties")
Old = Button(app, text="Import server.properties")
New.grid()
Old.grid()
#Now that I have the basics, I need to add functions to these buttons
def new2():
     
    
#Mainloop keeps GUI running (ALWAYS AT BOTTOM OF SCRIPT!!)
tk.mainloop()
