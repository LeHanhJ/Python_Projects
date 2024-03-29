import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
from datetime import datetime, timedelta
import time

    #3

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #Sets title of GUI window
        self.master.title("File Transfer")

        #5
        #Creates button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        #Positions source button in GUI using tkinter grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20,10), pady=(30,0))

        #Creates entry for source directory selection
        self.source_dir = Entry(width=75)
        #Positions entry into GUI using tkinter grid() padx and pady are the same as
        #the button to ensure they will line up
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20,10), pady=(30,0))

        #6
        #creates button to select destination of files from destination directory
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        #Positions destination button in the GUI using Tkinter grid()
        #on the next row under the source button
        self.destDir_btn.grid(row=1, column=0, padx=(20,10), pady=(15,10))

        #Creates entry for destination directory selection
        self.destination_dir = Entry(width=75)
        #Positions entry in GUI using tkinter grid() padx and pady are the same as
        #the button to ensure they will line up
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20,10),pady=(15,10))

        #P311 No 13
        #Creates button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        #Positions transfer files button
        self.transfer_btn.grid(row=2, column=1, padx=(200,0), pady=(0,15))

        #p311 No 18
        #Creates an Exit button
        self.exit_btn=Button(text="Exit", width=20, command=self.exit_program)
        #Positions the Exit button
        self.exit_btn.grid(row=2, column=2, padx=(10,40), pady= (0,15))

    #P311 No 5
    #Creates function to select source directory
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #The .delete(0,END) will clear the content that is inserted in the Entry widget,
        #this allows the path to be inserted into the Entry widget properly
        self.source_dir.delete(0,END)
        #The .insert method will insert the user selection to the source_dir Entry
        self.source_dir.insert(0, selectSourceDir)

        #The sourceDir(self) function will ask the user to pick the directory to insert into
        #the source Entry widget

    #P311 No 7
    #Creates function to select destination directory
    def destDir(self):
        selectDestDir=tkinter.filedialog.askdirectory()
        #The .delete(0,END) will clear the content that is inserted in the Entry widget,
        #this allows the path to be inserted into the Entry widget properly
        self.destination_dir.delete(0,END)
        #The .insert method will insert the user selection to the destination_dir Entry widget
        self.destination_dir.insert(0,selectDestDir)



#####

        
    #P311 No 12
    #Creates function to transfer files from one directory to another
    def transferFiles(self):
        
        #gets source directory
        source = self.source_dir.get() #also the "path"?
        #gets destination directory
        destination = self.destination_dir.get()
        
        #gets a list of files in the source directory
        source_files = os.listdir(source)


        
        #for i in the source directory of folder source
        for i in source_files:
            #getmtime() returns a float
            mod_time = os.path.getmtime(source + '/' + i)
            #time.time() turns yesterday variable into a float
            yesterday = (time.time() - 60 * 60 * 24)
            #if the time from variable yesterday IS the same as or is greaterto the last modification time
            if (yesterday >= mod_time) == True:
                #move the files from one folder to another
                shutil.move(source + '/' + i, destination)
                print(i + " has been sitting for 24 hours. It has been successfully transferred.")
            #if it is NOT the same
            else:
                #do nothing and print out the following statement
                print(i + "has not been 24 hours yet. Files will be kept in place.")
                break

            
#####



    #p311 No 17
    #Creates function to exit program
    def exit_program(self):
        #root is the main Gui window, the tkinter destroy method
        #tells python to terminate root.mainloop and all widgets inside the GUI window
        root.destroy()

        
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
