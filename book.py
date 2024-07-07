import tkinter as tk
from tkinter import ttk, messagebox

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        messagebox.showinfo("Success", f"'{book.title}' added to the library.")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                messagebox.showinfo("Success", f"'{title}' removed from the library.")
                return
        messagebox.showwarning("Error", f"'{title}' not found in the library.")

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                messagebox.showinfo("Found", f"'{book}' found in the library.")
                return
        messagebox.showwarning("Error", f"'{title}' not found in the library.")

    def display_books(self):
        if not self.books:
            messagebox.showinfo("Library", "No books in the library.")
        else:
            books_str = "\n".join(str(book) for book in self.books)
            messagebox.showinfo("Library Books", books_str)

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("500x400")

        self.library = Library()

        self.create_widgets()

    def create_widgets(self):
        # Frame for book details
        details_frame = ttk.Frame(self.root, padding="10")
        details_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        ttk.Label(details_frame, text="Title:").grid(row=0, column=0, sticky="w")
        self.title_entry = ttk.Entry(details_frame, width=40)
        self.title_entry.grid(row=0, column=1, sticky="ew")

        ttk.Label(details_frame, text="Author:").grid(row=1, column=0, sticky="w")
        self.author_entry = ttk.Entry(details_frame, width=40)
        self.author_entry.grid(row=1, column=1, sticky="ew")

        ttk.Label(details_frame, text="Year:").grid(row=2, column=0, sticky="w")
        self.year_entry = ttk.Entry(details_frame, width=40)
        self.year_entry.grid(row=2, column=1, sticky="ew")

        # Frame for buttons
        buttons_frame = ttk.Frame(self.root, padding="10")
        buttons_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        add_button = ttk.Button(buttons_frame, text="Add Book", command=self.add_book)
        add_button.grid(row=0, column=0, padx=5)

        remove_button = ttk.Button(buttons_frame, text="Remove Book", command=self.remove_book)
        remove_button.grid(row=0, column=1, padx=5)

        search_button = ttk.Button(buttons_frame, text="Search Book", command=self.search_book)
        search_button.grid(row=0, column=2, padx=5)

        display_button = ttk.Button(buttons_frame, text="Display Books", command=self.display_books)
        display_button.grid(row=0, column=3, padx=5)

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        year = self.year_entry.get()
        if title and author and year:
            book = Book(title, author, year)
            self.library.add_book(book)
        else:
            messagebox.showwarning("Error", "Please fill in all fields.")

    def remove_book(self):
        title = self.title_entry.get()
        if title:
            self.library.remove_book(title)
        else:
            messagebox.showwarning("Error", "Please enter the title of the book to remove.")

    def search_book(self):
        title = self.title_entry.get()
        if title:
            self.library.search_book(title)
        else:
            messagebox.showwarning("Error", "Please enter the title of the book to search.")

    def display_books(self):
        self.library.display_books()

# Main function
def main():
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
