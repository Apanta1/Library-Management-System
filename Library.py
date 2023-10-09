from tkinter import*
import tkinter as tk
from tkinter import ttk


class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1450x800+10+10") #marking screen size and starting point

        lbltitle = Label(self.root, text="Library Management System", bg="sky blue", fg="black", bd=20, 
                        relief=RIDGE, font=("times new roman", 50,"bold"),padx=2, pady=6 ) #making the main label
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd = 12, relief = RIDGE, 
                      padx = 20, bg = "powder blue") #creating the lower frame
        frame.place(x=0, y=130, width=1430, heigh=450)

        #---------------Data Frame Left----------------------------------------------

        DataFrameLeft = LabelFrame(frame, text="Library Management System", bg="powder blue", fg="green", bd=12, relief=RIDGE, font=("times new roman", 20, "bold"))#creating a new frame
        DataFrameLeft.place(x=0, y=5, width=890, height=350)

        #Label for "Member Type"
        lblMember=Label(DataFrameLeft, bg = "powder blue", text="Member Type", font=("times new roman", 20, "bold"), padx=2, pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,font=("times new roman", 20, "bold"), width=25, state="readonly")
        comMember["value"]=("Admin Staff", "Student", "Professor")
        comMember.grid(row=0,column=1)

        #Label for "Book ID"
        lblBOOKID=Label(DataFrameLeft, bg = "powder blue", text="Book ID:", font=("times new roman", 20, "bold"), padx=2, pady=6)
        lblBOOKID.grid(row=0,column=4,sticky=W)

        textBOOKID=Entry(DataFrameLeft,font=("times new roman", 20, "bold"), width=25)
        textBOOKID.grid(row=0,column=5)

        #Label for "PRN Number"
        lblPRNNUM=Label(DataFrameLeft, bg = "powder blue", text="PRN Number", font=("times new roman", 20, "bold"), padx=2, pady=6)
        lblPRNNUM.grid(row=1,column=0,sticky=W)

        textPRNNUM=Entry(DataFrameLeft,font=("times new roman", 20, "bold"), width=25)
        textPRNNUM.grid(row=1,column=1)

        #Label for "Book Title"
        lblBKTITLE=Label(DataFrameLeft, bg = "powder blue", text="Book Title:", font=("times new roman", 20, "bold"), padx=2, pady=6)
        lblBKTITLE.grid(row=1,column=4,sticky=W)

        textIDNUMBER=Entry(DataFrameLeft,font=("times new roman", 20, "bold"), width=25)
        textIDNUMBER.grid(row=1,column=5)

        #Label for "ID Number"
        lblIDNUMBER=Label(DataFrameLeft, bg = "powder blue", text="ID Number:", font=("times new roman", 20, "bold"), padx=2, pady=6)
        lblIDNUMBER.grid(row=2,column=0,sticky=W)

        textIDNUMBER=Entry(DataFrameLeft,font=("times new roman", 20, "bold"), width=25)
        textIDNUMBER.grid(row=2,column=1)

        #Label for "Author Name"
        lblIDNUMBER=Label(DataFrameLeft, bg = "powder blue", text="Author Name:", font=("times new roman", 20, "bold"), padx=2, pady=6)
        lblIDNUMBER.grid(row=2,column=4,sticky=W)

        textIDNUMBER=Entry(DataFrameLeft,font=("times new roman", 20, "bold"), width=25)
        textIDNUMBER.grid(row=2,column=5)

        #Label for "First Name"
        lblIDNUMBER=Label(DataFrameLeft, bg = "powder blue", text="First Name:", font=("times new roman", 20, "bold"), padx=2, pady=6)
        lblIDNUMBER.grid(row=3,column=0,sticky=W)

        textIDNUMBER=Entry(DataFrameLeft,font=("times new roman", 20, "bold"), width=25)
        textIDNUMBER.grid(row=3,column=1)

        #Label for "Date Borrowed"
        lblIDNUMBER=Label(DataFrameLeft, bg = "powder blue", text="Date Borrowed:", font=("times new roman", 20, "bold"), padx=2, pady=6)
        lblIDNUMBER.grid(row=3,column=4,sticky=W)

        textIDNUMBER=Entry(DataFrameLeft,font=("times new roman", 20, "bold"), width=25)
        textIDNUMBER.grid(row=3,column=5)

        #Label for "Last Name"
        lblIDNUMBER=Label(DataFrameLeft, bg = "powder blue", text="Last Name:", font=("times new roman", 20, "bold"), padx=2, pady=6)
        lblIDNUMBER.grid(row=4,column=0,sticky=W)

        textIDNUMBER=Entry(DataFrameLeft,font=("times new roman", 20, "bold"), width=25)
        textIDNUMBER.grid(row=4,column=1)

        #Label for "Date Due"
        lblIDNUMBER=Label(DataFrameLeft, bg = "powder blue", text="Date Due:", font=("times new roman", 20, "bold"), padx=2, pady=6)
        lblIDNUMBER.grid(row=3,column=4,sticky=W)

        textIDNUMBER=Entry(DataFrameLeft,font=("times new roman", 20, "bold"), width=25)
        textIDNUMBER.grid(row=3,column=5)









        #---------------Data Frame Right----------------------------------------------
        DataFrameRight = LabelFrame(frame, text="Book Details", bg="powder blue",
                      fg="green", bd=12, relief=RIDGE, font=("times new roman", 20, "bold"))#creating a new frame
        DataFrameRight.place(x=900, y=5, width=480, height=350)

        #---------------Buttons Frame----------------------------------------------

        FrameButton = Frame(self.root, bd = 12, relief = RIDGE, 
                      padx = 20, bg = "powder blue") #creating frame for buttons
        FrameButton.place(x=0, y=585, width=1430, heigh=70)

        #---------------Information Frame----------------------------------------------

        FrameDetails = Frame(self.root, bd = 12, relief = RIDGE, 
                      padx = 20, bg = "powder blue") #creating frame for information
        FrameDetails.place(x=0, y=660, width=1430, heigh=150)





if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()