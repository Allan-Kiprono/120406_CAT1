class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f'Book "{self.title}" has been borrowed.')
        else:
            print(f'Book "{self.title}" is already borrowed.')

    def mark_as_returned(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f'Book "{self.title}" has been returned.')
        else:
            print(f'Book "{self.title}" was not borrowed.')


class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.mark_as_borrowed()
            self.borrowed_books.append(book)
        else:
            print(f'Sorry, the book "{book.title}" is currently not available.')

    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
        else:
            print(f'You have not borrowed the book "{book.title}".')

    def list_borrowed_books(self):
        if not self.borrowed_books:
            print("No books currently borrowed.")
        else:
            print("Borrowed books:")
            for book in self.borrowed_books:
                print(f'- {book.title} by {book.author}')


# Sample books
book1 = Book("Siku Njema", "Ken Walibora")
book2 = Book("The River Between", "Ngugi wa Thiongo")
book3 = Book("The Hunger Games", "Suzanne Collins")
books = [book1, book2, book3]

# Create a library member
member = LibraryMember("Allan", "M001")

# Interactive menu
def display_books():
    print("\nAvailable books:")
    for i, book in enumerate(books):
        status = "Available" if not book.is_borrowed else "Borrowed"
        print(f"{i + 1}. {book.title} by {book.author} - {status}")

def menu():
    while True:
        print("\nLibrary Menu:")
        print("1. List all books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. View borrowed books")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_books()

        elif choice == "2":
            display_books()
            try:
                selection = int(input("Enter book number to borrow: ")) - 1
                if 0 <= selection < len(books):
                    member.borrow_book(books[selection])
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            if not member.borrowed_books:
                print("You have no books to return.")
                continue
            member.list_borrowed_books()
            try:
                selection = int(input("Enter number of book to return: ")) - 1
                if 0 <= selection < len(member.borrowed_books):
                    member.return_book(member.borrowed_books[selection])
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            member.list_borrowed_books()

        elif choice == "5":
            print("Exiting library system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the menu
menu()
