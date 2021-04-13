from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
#from PIL import Image,ImageTk

Folder_Name = ""

#file location
def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")

    else:
        locationError.config(text="Please Choose Folder!!",fg="red")

#donwload video
def DownloadVideo():
    choice = hydchoices.get()
    url = hydEntry.get()

    if(len(url)>1):
        hydError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice == choices[3]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            hydError.config(text="Paste Link again!!",fg="red")


    #download function
    select.download(Folder_Name)
    hydError.config(text="Download Completed!!")



root = Tk()
root.title("HYD Downloader")
root.iconbitmap(r'favicon.ico')
#load = Image.open('images\\background.jpg')
#render = PhotoImage(file = 'images\\background.jpg')
#img = Label(root, image = render)
#img.grid(x = 0, y = 0)
root.geometry("450x350")

#root.config(backgound="blue")
root.columnconfigure(0,weight=1)#set all content in center.

#HEADLINE
hydHead = Label(root, text = "Haxor The Youtube Downloader", font=("times new roman", 20, "bold"), fg = 'purple')
hydHead.grid()

#HYD Link Label
hydLabel = Label(root,text="Enter the URL of the Video",font=("jost",15))
hydLabel.grid()

#Entry Box
hydEntryVar = StringVar()
hydEntry = Entry(root,width=50,textvariable=hydEntryVar)
hydEntry.grid()

#Error Message
hydError = Label(root,text="Error Message",fg="red",font=("jost",10))
hydError.grid()

#Asking save file label
saveLabel = Label(root,text="Save the Video File",font=("jost",15,"bold"))
saveLabel.grid()

#Buuton of save file
saveEntry = Button(root,width=10,bg="red",fg="white",text="Choose Path",command=openLocation)
saveEntry.grid()

#Error Message location
locationError = Label(root,text="Error Message of Path",fg="red",font=("jost",10))
locationError.grid()

#Download Quality
hydQuality = Label(root,text="Select Quality",font=("jost",15))
hydQuality.grid()

#combobox
choices = ["1080p", "720p","144p","Only Audio"]
hydchoices = ttk.Combobox(root,values=choices)
hydchoices.grid()

#donwload buttonn
downloadbtn = Button(root,text="Download",width=10,bg="red",fg="white",command=DownloadVideo)
downloadbtn.grid()

#developer Label
developerlabel = Label(root,text="Haxor365", fg = 'purple', font=("jost",15))
developerlabel.grid()
btnQuit = Button(root, text = "Quit", width = 10, bg = "red", fg = "white", command = exit)
btnQuit.grid()
root.mainloop()