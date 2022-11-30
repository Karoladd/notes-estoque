
# Python program to create
# a file explorer in Tkinter
  
# import all components
# from the tkinter library
from tkinter import *

# import filedialog module
from tkinter import filedialog
import time
# Function for opening the
# file explorer window
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes=[("Excel files", ".xlsx .xls")])
    # Change label contents
    label_file_explorer.configure(text="Caminho do arquivo: "+filename)


# Create the root window
window = Tk()

# Set window title
window.title('File Explorer')
  
# Set window size
window.geometry("700x500")
  
#Set window background color
window.config(background = "white")
  
# Create a File Explorer label
label_file_explorer = Label(window,
                            text = "File Explorer using Tkinter",
                            width = 100, height = 4,
                            fg = "blue")
ms = Label(
    window,
    width = 100, height = 4,
    text='Insira o arquivo Excel ',
    )
      
button_explore = Button(window,
                        width = 50, height = 2,
                        text = "Escolher Arquivo",
                        command = browseFiles)
upld = Button(
    window, 
    width = 100, height = 4,
    text='Enviar', 
    )
      
button_exit = Button(window,
                    width = 100, height = 4,
                     text = "SAIR",
                     command = exit)
  
# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column = 1, row = 1)

ms.grid(row=2, column=1, padx=10)

button_explore.grid(column = 1, row = 3)
  
upld.grid(column = 1, row = 4)

button_exit.grid(column = 1,row = 5)
  
# Let the window wait for any events
window.mainloop()