from tkinter import*
import tkinter as tk
from tkinter import ttk


class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Used Book Data Base")
        self.root.geometry("1400x800+10+10") #marking screen size and starting point

        lbltitle = Label(self.root, text="Used Book Registration System", bg="sky blue", fg="black", bd=20, 
                        relief=RIDGE, font=("times new roman", 50,"bold"),padx=2, pady=6 ) #making the main label
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd = 12, relief = RIDGE, 
                      padx = 20, bg = "powder blue") #creating the lower frame
        frame.place(x=0, y=130, width=1420, heigh=450)

        #---------------Data Frame Left----------------------------------------------

        DataFrameLeft = LabelFrame(frame, text="Used Book Registration System", bg="powder blue",
                      fg="green", bd=12, relief=RIDGE, font=("times new roman", 20, "bold"))#creating a new frame
        DataFrameLeft.place(x=0, y=5, width=850, height=350)

        lblMember=Label(DataFrameLeft, bg = "powder blue", text="Member Type", font=("times new roman", 20, "bold"), padx=2, pady=6)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=ttk.Combobox(DataFrameLeft,font=("times new roman", 20, "bold"), width=27, state="readonly")
        comMember["value"]=("Admin Staff", "Student", "Professor")
        comMember.grid(row=0,column=1)

        lblIDNUMBER=Label(DataFrameLeft, bg = "powder blue", text="ID Number", font=("times new roman", 20, "bold"), padx=2, pady=6)
        lblIDNUMBER.grid(row=1,column=0,sticky=W)

        textIDNUMBER=Entry(DataFrameLeft,font=("times new roman", 20, "bold"), width=29)
        textIDNUMBER.grid(row=1,column=1)
        
        DataFrameRight = LabelFrame(frame, text="Book Details", bg="powder blue",
                      fg="green", bd=12, relief=RIDGE, font=("times new roman", 20, "bold"))#creating a new frame
        DataFrameRight.place(x=860, y=5, width=450, height=350)

        #---------------Buttons Frame----------------------------------------------

        FrameButton = Frame(self.root, bd = 12, relief = RIDGE, 
                      padx = 20, bg = "powder blue") #creating frame for buttons
        FrameButton.place(x=0, y=585, width=1420, heigh=70)

        #---------------Information Frame----------------------------------------------

        FrameDetails = Frame(self.root, bd = 12, relief = RIDGE, 
                      padx = 20, bg = "powder blue") #creating frame for information
        FrameDetails.place(x=0, y=660, width=1420, heigh=150)

if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()
