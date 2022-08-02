
import tkinter
from tkinter import *



class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master #self.master references master in def__init__(self,master) which references (Frame)
        self.master.resizable(width=False, height=False)#References self.master and resizes Frame by using .resizable.
            #(width=False, height=False) makes the window frame become unsizable. True on width makes only width resizable
        self.master.geometry('{}x{}'.format(700, 400))#.geometry gives it dimensions by using the string, and giving the
            #pixels in parameters
        self.master.title('Learning Tkinter!')#.title makes a title, duh
        self.master.config(bg='lightgray')#.config(bg='') makes the background oclor of the window

        self.varFName = StringVar() #StringVar() sets a variable for First name and Last name
        self.varLName = StringVar() #see above



        self.lblFName = Label(self.master,text="First Name: ",font=("Helvetica", 16), fg='black', bg='lightgray') #Label makes a
            #label to be unedited
        self.lblFName.grid(row=0,column=0, padx=(30,0), pady=(30,0)) #.grid makes a grid; padx and pady gives padding to the grid
            #horizontally and vertically, respectfully

        self.lblLName = Label(self.master,text="Last Name: ",font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblLName.grid(row=1, column=0, padx=(30,0), pady=(30,0))



        self.lblDisplay = Label(self.master,text=" ",font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblDisplay.grid(row=3, column=1, padx=(30,0), pady=(30,0))


        
        self.txtFName = Entry(self.master, text=self.varFName, font=("Helvetica", 16), fg='black', bg='lightblue') #Entry is kind
            #of like input in JS. whatever is entered is transferred to varFName by using self.varFName
        self.txtFName.grid(row=0, column=1, padx=(30,0), pady=(30,0))

        self.txtLName = Entry(self.master, text=self.varLName, font=("Helvetica", 16), fg='black', bg='lightblue')
        self.txtLName.grid(row=1, column=1, padx=(30,0), pady=(30,0))



        self.btnSubmit = Button(self.master, text="Submit", width=10, height = 2, command = self.submit) #self.submit is the function
            #we will create
        self.btnSubmit.grid(row=2, column=1, padx=(0,0), pady=(30,0), sticky = NE)

        self.btnCancel = Button(self.master, text="Cancel", width=10, height = 2, command=self.cancel)#self.cancel is the function
            #we will create
        self.btnCancel.grid(row=2, column=1, padx=(0,90), pady=(30,0), sticky = NE)

    def submit(self): #"self" is class, "submit" is method 
        fn = self.varFName.get() #pressing submit button will store into FName, taken from txtFName's text property
        ln = self.varLName.get()
        self.lblDisplay.config(text='Hello {} {}!'.format(fn, ln))

    def cancel(self):
        self.master.destroy()



if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
