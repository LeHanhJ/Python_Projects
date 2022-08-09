import tkinter as tk
from tkinter import *
import tkinter.simpledialog
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        #title of window
        self.master.title("Web Page Generator")
        #creates button to open up an HTML page by using command
        self.btn = Button(self.master, text = "Default HTML Page", width=30, height=2, command=self.defaultHTML)
        #aligns button in a grid
        self.btn.grid(row=2, column=1, padx=(10,10),pady=(10,10),sticky=SE)

        ##creating a button for custom text
        self.create_btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.create_txt)
        #aligns button in grid and adds padding
        self.create_btn.grid(row=2, column=2, padx=(10,10), pady=(10,10),sticky=SE)

    def defaultHTML(self):
        #sets variable htmlText
        htmlText = "Stay tuned for our amazing summer sale!"
        #sets variable htmlFile to open an index.html file and opening the file for writing, truncating the file first
        htmlFile = open("index.html", "w")
        #assigns variable htmlContent to write up elements of an html page, while also inserting the htmlText between elements
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</html>\n</body>\n</h1>"

        #this line opens an index.html and writes whatever is given in variable htmlContent (which is writing up html tags for the html file
        #and printing out the htmlText as written above
        htmlFile.write(htmlContent)
        
        htmlFile.close()
        #open index.html in a new tab in a webbrowser
        webbrowser.open_new_tab("index.html")


######
        # TASK: CREATE A NEW FUNCTION WITHIN PARENTWINDOW CLASS THAT TAKES USER INPUT AS TEXT AND THEN DISPLAYS THE CUSTOM TEXT
            #ON THE GENERATED WEB PAGE

        #GUI SHOULD OPEN THE HTML FILE IN A NEW TAB WITHIN THE BROWSER
        
    
        
    def create_txt(self):

        # self.create= Entry makes an entry point for users to enter their text
        self.create = Entry(width=100)

        #this opens a dialog box for users to input any text they would like
        enterCustom = tk.simpledialog.askstring("Enter your custom text for your webpage", "Please enter your custom text here, or press Cancel and the Default HTML Page")
        #this will clear content that is inserted into the Entry widget
        self.create.delete(0,END)
        #.insert method will insert the enterCustom to the create entry
        self.create.insert(0,enterCustom)
        
        #sets variable htmlFile to open an index.html file and opening the file for writing, truncating the file first
        createWebsite = open("index.html", "w")
        #assigns variable htmlContent to write up elements of an html page, while also inserting the custom text inputted by users between elements
        websiteContent = "<html>\n<body>\n<h1>" + enterCustom + "</html>\n</body>\n</h1>"

        #this line opens an index.html and writes whatever is given in variable htmlContent (which is writing up html tags for the html file
        #and printing out the htmlText as written above
        createWebsite.write(websiteContent)
        
        createWebsite.close()
        #open index.html in a new tab in a webbrowser
        webbrowser.open_new_tab("index.html")

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
