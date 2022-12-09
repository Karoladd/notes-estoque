from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
import time


ws = Tk()
ws.title('ESTOQUE - AUTOMAÇÃO NOTAS')
ws.geometry('500x500') 

def open_file():
    file_path = askopenfile(mode='r', filetypes=[("Excel files", ".xlsx .xls")])
    if file_path is not None:
        pass


def uploadFiles():
    pb1 = Progressbar(
        ws, 
        orient=HORIZONTAL, 
        length=300, 
        mode='determinate'
        )
    pb1.grid(row=4, columnspan=3, pady=20)
    for i in range(5):
        ws.update_idletasks()
        pb1['value'] += 20
        time.sleep(1)
    pb1.destroy()
    Label(ws, text='File Uploaded Successfully!', foreground='green').grid(row=4, columnspan=3, pady=10)

# Add a frame to set the size of the window
frame= Frame(ws)

# Make the frame sticky for every case
frame.grid_rowconfigure(5, weight=1)
frame.grid_columnconfigure(5, weight=1)

# Make the window sticky for every case
ws.grid_rowconfigure(0, weight=1)
ws.grid_columnconfigure(0, weight=1)


ms = Label(
    text='Insira o arquivo Excel ',
    )
ms.grid(row=1, column=0, padx=10)

ms.grid_rowconfigure(1, weight=1)
ms.grid_columnconfigure(1, weight=1)

msbtn = Button(
    text ='Escolher arquivo',  
    command = lambda:open_file()
    ) 
msbtn.grid(row=2, column=0, padx=10)


upld = Button(
    ws, 
    text='Upload Files', 
    command=uploadFiles
    )
upld.grid(row=3, columnspan=3, pady=10)



ws.mainloop()