
from datetime import date
import json
import os

liberary = {}
student_details = {}

def create_db():
    if not os.path.exists("one.json"):
        with open("one.json", "w") as file:
            json.dump({}, file)
    else:
        print("Database already exists.")

def load_user():
    with open("one.json", "r") as file:
        return json.load(file)

def save_users(users):
    with open("one.json", "w") as file:
        json.dump(users, file, indent=4)


def add_books():
    book_number = int(input("Enter the book number: "))

    if book_number in liberary:
        print("Book already exists; choose a different book number.")
        return

    liberary[book_number] = {
     "name": input("Enter book name:"),
        "genure": input("Enter the genre:"),
        "author": input("Enter author name:"),
    }

    print("Book added successfully.")


def search_books():
    book_number = int(input("Enter the book number: "))

    if book_number in liberary:
        book = liberary[book_number]

        print("Book found successfully.")
        print("Name:", book["name"])
        print("Genre:", book["genure"])
        print("Author:", book["author"])

    else:
        print("Book not found.")


def issue_book():
    book_number = int(input("Enter the book number: "))

    if book_number in liberary:

        if book_number in student_details:
            print("Book is already issued.")
            return

        student_name = input("Enter student name: ")

        issued_date = date.today()
        issued_deadline = date.fromordinal(issued_date.toordinal() + 7)

        student_details[book_number] = {
            "STUDENT_NAME": student_name,
            "ISSUED_DATE": str(issued_date),
            "ISSUED_DEADLINE": str(issued_deadline),
        }

        print("Book issued successfully.")
        print("Issue date:", issued_date)
        print("Deadline:", issued_deadline)

    else:
        print("Book not found.")


def return_book():
    book_number = int(input("Enter your book number: "))
    student_name = input("Enter your name: ")

    if book_number not in liberary:
        print("Book not found.")
        return

    if book_number not in student_details:
        print("This book has not been issued.")
        return

    if student_details[book_number]["STUDENT_NAME"] == student_name:
        del student_details[book_number]
        print("Book returned successfully.")
    else:
        print("Student name does not match.")


def display_books(choice):

    if choice == "5":

        if liberary:
            print("display all books in the library:")

            for book_number, book in liberary.items():
                print("Book Number:", book_number)
                print("Name:", book["name"])
                print("Genre:", book["genure"])
                print("Author:", book["author"])
                print()

        else:
            print("No books available.")

    elif choice == "6":

        if student_details:
            print("display issued books:")

            for book_number, details in student_details.items():
                print("Book Number:", book_number)
                print("Student Name:", details["STUDENT_NAME"])
                print("Issued Date:", details["ISSUED_DATE"])
                print("Deadline:", details["ISSUED_DEADLINE"])
                print()

        else:
            print("No books have been issued.")


while True:

    print("Welcome to the Library Management System")
    print("1. Add Books")
    print("2. Search Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display All Books")
    print("6. Display Issued Books")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_books()

    elif choice == "2":
        search_books()

    elif choice == "3":
        issue_book()

    elif choice == "4":
        return_book()

    elif choice == "5":
        display_books(choice)

    elif choice == "6":
        display_books(choice)

    elif choice == "7":
        print("Thank you for using Library Management System.")
        break

    else:
        print("Invalid choice.")

