import json
import os

# ------------------ Book Class ------------------

class Book:
    def __init__(self, book_id, title, author, is_issued=False):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = is_issued

    def issue_book(self):
        if not self.is_issued:
            self.is_issued = True
            return True
        return False

    def return_book(self):
        if self.is_issued:
            self.is_issued = False
            return True
        return False

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "is_issued": self.is_issued
        }

# ------------------ Library Class ------------------

class Library:
    def __init__(self):
        self.books = {}
        self.filename = "library.json"
        self.load_data()

    def add_book(self):
        book_id = input("Enter Book ID: ")

        if book_id in self.books:
            print("Book ID already exists!")
            return

        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(book_id, title, author)
        self.books[book_id] = book

        self.save_data()
        print("Book Added Successfully!")

    def search_book(self):
        keyword = input("Enter Title or Author to Search: ").lower()

        found = False

        for book in self.books.values():
            if keyword in book.title.lower() or keyword in book.author.lower():
                self.display_book(book)
                found = True

        if not found:
            print("No Book Found!")

    def issue_book(self):
        book_id = input("Enter Book ID to Issue: ")

        if book_id in self.books:
            if self.books[book_id].issue_book():
                print("Book Issued Successfully!")
            else:
                print("Book Already Issued!")
        else:
            print("Book Not Found!")

        self.save_data()

    def return_book(self):
        book_id = input("Enter Book ID to Return: ")

        if book_id in self.books:
            if self.books[book_id].return_book():
                print("Book Returned Successfully!")
            else:
                print("Book Was Not Issued!")
        else:
            print("Book Not Found!")

        self.save_data()

    def view_books(self):
        if not self.books:
            print("No Books Available!")
            return

        print("\n----- All Books -----")
        for book in self.books.values():
            self.display_book(book)

    def generate_report(self):
        total_books = len(self.books)

        issued_books = 0

        for book in self.books.values():
            if book.is_issued:
                issued_books += 1

        available_books = total_books - issued_books

        print("\n----- Library Report -----")
        print("Total Books :", total_books)
        print("Issued Books:", issued_books)
        print("Available Books:", available_books)

    def display_book(self, book):
        status = "Issued" if book.is_issued else "Available"

        print("---------------------------")
        print("Book ID :", book.book_id)
        print("Title   :", book.title)
        print("Author  :", book.author)
        print("Status  :", status)

    def save_data(self):
        data = {}

        for book_id, book in self.books.items():
            data[book_id] = book.to_dict()

        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                data = json.load(file)

                for book_id, details in data.items():
                    self.books[book_id] = Book(
                        details["book_id"],
                        details["title"],
                        details["author"],
                        details["is_issued"]
                    )

# ------------------ Main Program ------------------

library = Library()

while True:
    print("\n===== LIBRARY BOOK INVENTORY MANAGER =====")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. View All Books")
    print("6. Generate Report")
    print("7. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.search_book()

    elif choice == "3":
        library.issue_book()

    elif choice == "4":
        library.return_book()

    elif choice == "5":
        library.view_books()

    elif choice == "6":
        library.generate_report()

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
