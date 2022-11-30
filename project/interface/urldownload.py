# Importing Required Module
from tkinter import *
import requests

# Defining  Downloder Class
class Downloader:
  # Defining Constructor
  def __init__(self,root):
    self.root = root
    # Title of the window
    self.root.title("Downloader Application")
    # Window Geometry
    self.root.geometry("600x100+200+200")
    # Declaring Url Variable
    self.url = StringVar()
    # Declaring Status Variable
    self.status = StringVar()
    # Initialising Status Variable
    self.status.set("-------------------------")

    # Creating Frame for downloader
    download_frame = Frame(self.root,background="grey",width=600,height=100).place(x=0,y=0)
    # Adding text widget lable for url
    url_lbl = Label(download_frame,text="URL",compound=LEFT,font=("times new roman",15,"bold"),bg="grey",fg="gold").grid(row=1,column=0,padx=10,pady=10)
    # Adding text widget for url
    url_txt = Entry(download_frame,bd=2,width=25,textvariable=self.url,relief=SUNKEN,font=("times new roman",15)).grid(row=1,column=1,padx=10,pady=10)
    # Adding the Download button
    dwn_btn = Button(download_frame,text="Download",command=self.download,width=10,font=("times new roman",14,"bold"),bg="gold",fg="navyblue").grid(row=1,column=2,padx=10,pady=10)
    # Adding the Status Label
    status_lbl = Label(download_frame,textvariable=self.status,font=("times new roman",14,"bold"),bg="grey",fg="white").grid(row=2,column=1)

  # Defining Download Function
  def download(self):
    # Cheaking if URL Entry is not Null
    try:
      # Updating Status
      self.status.set("Downloading...")
      self.root.update()
      # Getting the response of request
      Request = requests.get(self.url.get())
      # Cheaking if status code is not bad
      if Request.status_code == requests.codes.ok:
        # Opening File to write bytes
        file = open("PF.txt","wb")
        file.write(Request.content)
        file.close()
        # Updating Status
        self.status.set("Download Completed")
      else:
        self.status.set(Request.status_code)
    except:
      self.status.set("Error in Downloading")

# Crting TK Container
root = Tk()
# Passing Root to Downloader Class
Downloader(root)
# Root Window Looping
root.mainloop()