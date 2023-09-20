import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1400x800+10+10")

        # Database connection
        self.db = mysql.connector.connect(
            host="your_host",
            user="your_user",
            password="your_password",
            database="library"  # Use the database you created
        )
        self.cursor = self.db.cursor()

        lbltitle = Label(self.root, text="Library Management System", bg="sky blue", fg="black", bd=20,
                        relief=RIDGE, font=("times new roman", 50, "bold"), padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1420, height=450)

        # Data Frame Left
        DataFrameLeft = LabelFrame(frame, text="Member Registration", bg="powder blue",
                                   fg="green", bd=12, relief=RIDGE, font=("times new roman", 20, "bold"))
        DataFrameLeft.place(x=0, y=5, width=850, height=350)

        lblMember = Label(DataFrameLeft, bg="powder blue", text="Member Type", font=("times new roman", 20, "bold"),
                          padx=2, pady=6)
        lblMember.grid(row=0, column=0, sticky=W)

        comMember = ttk.Combobox(DataFrameLeft, font=("times new roman", 20, "bold"), width=27, state="readonly")
        comMember["value"] = ("Admin Staff", "Student", "Professor")
        comMember.grid(row=0, column=1)

        lblIDNUMBER = Label(DataFrameLeft, bg="powder blue", text="ID Number", font=("times new roman", 20, "bold"),
                            padx=2, pady=6)
        lblIDNUMBER.grid(row=1, column=0, sticky=W)

        textIDNUMBER = Entry(DataFrameLeft, font=("times new roman", 20, "bold"), width=29)
        textIDNUMBER.grid(row=1, column=1)

        # Data Frame Right
        DataFrameRight = LabelFrame(frame, text="Book Details", bg="powder blue",
                                    fg="green", bd=12, relief=RIDGE, font=("times new roman", 20, "bold"))
        DataFrameRight.place(x=860, y=5, width=450, height=350)

        lblTitle = Label(DataFrameRight, bg="powder blue", text="Title", font=("times new roman", 20, "bold"),
                         padx=2, pady=6)
        lblTitle.grid(row=0, column=0, sticky=W)

        textTitle = Entry(DataFrameRight, font=("times new roman", 20, "bold"), width=29)
        textTitle.grid(row=0, column=1)

        lblAuthor = Label(DataFrameRight, bg="powder blue", text="Author", font=("times new roman", 20, "bold"),
                          padx=2, pady=6)
        lblAuthor.grid(row=1, column=0, sticky=W)

        textAuthor = Entry(DataFrameRight, font=("times new roman", 20, "bold"), width=29)
        textAuthor.grid(row=1, column=1)

        lblISBN = Label(DataFrameRight, bg="powder blue", text="ISBN", font=("times new roman", 20, "bold"),
                        padx=2, pady=6)
        lblISBN.grid(row=2, column=0, sticky=W)

        textISBN = Entry(DataFrameRight, font=("times new roman", 20, "bold"), width=29)
        textISBN.grid(row=2, column=1)

        # Buttons Frame
        FrameButton = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameButton.place(x=0, y=585, width=1420, height=70)

        btnInsert = Button(FrameButton, text="Insert Member Data", command=self.insert_member_data,
                           font=("times new roman", 15, "bold"))
        btnInsert.grid(row=0, column=0, padx=10)

        btnInsertBook = Button(FrameButton, text="Insert Book Details", command=self.insert_book_details,
                               font=("times new roman", 15, "bold"))
        btnInsertBook.grid(row=0, column=1, padx=10)

        btnShowMembers = Button(FrameButton, text="Show Members", command=self.show_members,
                                font=("times new roman", 15, "bold"))
        btnShowMembers.grid(row=0, column=2, padx=10)

        btnShowBooks = Button(FrameButton, text="Show Books", command=self.show_books,
                              font=("times new roman", 15, "bold"))
        btnShowBooks.grid(row=0, column=3, padx=10)

        # Information Frame
        FrameDetails = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameDetails.place(x=0, y=660, width=1420, height=150)

        self.member_listbox = Listbox(FrameDetails, font=("times new roman", 15, "bold"), width=37, height=4)
        self.member_listbox.grid(row=0, column=0, padx=10, pady=5)

        self.book_listbox = Listbox(FrameDetails, font=("times new roman", 15, "bold"), width=37, height=4)
        self.book_listbox.grid(row=0, column=1, padx=10, pady=5)

        self.show_members()
        self.show_books()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def insert_member_data(self):
        member_type = comMember.get()
        id_number = textIDNUMBER.get()

        if not member_type or not id_number:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        query = "INSERT INTO members (member_type, id_number) VALUES (%s, %s)"
        values = (member_type, id_number)

        try:
            self.cursor.execute(query, values)
            self.db.commit()
            messagebox.showinfo("Success", "Member data inserted successfully!")
            self.show_members()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def insert_book_details(self):
        title = textTitle.get()
        author = textAuthor.get()
        isbn = textISBN.get()

        if not title or not author or not isbn:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        query = "INSERT INTO books (title, author, ISBN) VALUES (%s, %s, %s)"
        values = (title, author, isbn)

        try:
            self.cursor.execute(query, values)
            self.db.commit()
            messagebox.showinfo("Success", "Book details inserted successfully!")
            self.show_books()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_members(self):
        self.member_listbox.delete(0, END)
        query = "SELECT member_type, id_number FROM members"
        self.cursor.execute(query)
        members = self.cursor.fetchall()

        for member in members:
            self.member_listbox.insert(END, f"Type: {member[0]}, ID: {member[1]}")

    def show_books(self):
        self.book_listbox.delete(0, END)
        query = "SELECT title, author, ISBN FROM books"
        self.cursor.execute(query)
        books = self.cursor.fetchall()

        for book in books:
            self.book_listbox.insert(END, f"Title: {book[0]}, Author: {book[1]}, ISBN: {book[2]}")

    def on_closing(self):
        self.db.close()
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()
