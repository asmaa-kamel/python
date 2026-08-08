from abc import ABC, abstractmethod

#classes
 #book class
class book:
    def __init__(self, id, title, author, genre ,available_copies):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.__available_copies = available_copies
        
    def display_info(self):
        print(f"""Book Information:
        ID: {self.id}
        Title: {self.title}
        Author: {self.author}
        Genre: {self.genre}
        Available Copies: {self.__available_copies}""")    
    def borrow_book(self):
        if self.__available_copies > 0:
            self.__available_copies -= 1
            print(f"""You have borrowed '{self.title}'.
                       Enjoy reading!""")
            return True
        else:
            print(f"Sorry, '{self.title}' is currently unavailable.")
            return False
        
    def return_book(self):
        self.__available_copies += 1
        print(f"""You have returned '{self.title}'.
                       Thank you!""")
    
    def get_available_copies(self):
        return self.__available_copies    
        
 # users class   
class User(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    @abstractmethod
    def borrow_book(self, book):
        pass
    
    def show_menu(self):
        print(f"Welcome, {self.name}!")
        print("1. Borrow Book")
        print("2. Return Book")
        print("3. Display Book Info")
        print("4. Display All Books")
        print("5. Display Available Books only")
        print("6. Display Borrowed Books only")
        print("7. Exit")
        
    def view_all_books(self, library):
            print("All books in the library:")
            for book in library:
                book.display_info()
                print("----------------------------------")
                
    def view_available_books(self, library):
            print("Available books in the library:")
            for book in library:
                if book.get_available_copies() > 0:
                    book.display_info()
                    print("----------------------------------")
           
    def view_borrowed_books(self):
            print(f"{self.name}'s borrowed books:")
            for book in self.borrowed_books:
                book.display_info()
                print("----------------------------------")                                
        
    
class Student(User):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            print(f"{self.name} (Student) has reached the borrowing limit of 3 books.")
        else:    
            print(f"{self.name} (Student) is borrowing a book.")
            if book.borrow_book():
                self.borrowed_books.append(book)    
            
class Teacher(User):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if len(self.borrowed_books) >= 5:
            print(f"{self.name} (Teacher) has reached the borrowing limit of 5 books.")
        else:    
            print(f"{self.name} (Teacher) is borrowing a book.")
            if book.borrow_book():
                self.borrowed_books.append(book)    

            
class Librarian(User):
    def __init__(self, id, name):
        super().__init__(id, name)
        self.borrowed_books = []
    
        
    def show_menu(self):
            print(f"Welcome, {self.name}!")
            print("1. Add Book")
            print("2. Remove Book")
            print("3. Return Book ")
            print("4. Search Book ")
            print("5. Display All Books")
            print("6. Display Available Books only")
            print("7. Display Borrowed Books only")
            print("8. Borrow Book") 
            print("9. Exit")  
    
        
    def borrow_book(self, book):
    
        print(f"{self.name} (Librarian) is borrowing a book.")
        if book.borrow_book():
            self.borrowed_books.append(book) 
    
    def add_book(self, new_book, library):
        library.append(new_book)
        print(f"{self.name} (Librarian) added '{new_book.title}' to the library.")

    def remove_book(self, target_book, library):
        library.remove(target_book)
        print(f"{self.name} (Librarian) removed '{target_book.title}' from the library.")

    

    def search_book(self, keyword, library):
        found = [book for book in library if keyword.lower() in book.title.lower()]
        if found:
            print("Found the following books:")
            for book in found:
                book.display_info()
        else:
            print(f"{self.name} (Librarian) did not find any books with '{keyword}'.")
     
        
def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input, please enter a number.")           
        
        
#Excute code

books = [
    book(1, "To Kill a Mockingbird", "Harper Lee", "Fiction", 5),
    book(2, "1984", "George Orwell", "Dystopian", 3),
    book(3, "Pride and Prejudice", "Jane Austen", "Romance", 4),
    book(4, "The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 2),
    book(5, "The Catcher in the Rye", "J.D. Salinger", "Fiction", 6)
]


while True:
    print("----------------------------------")
    print("\nLibrary Management System")
    print("1. Student")
    print("2. Teacher")
    print("3. Librarian")
    print("4. Exit")
    print("----------------------------------")
    
    choice = input("Enter your choice: ")
    #student menu
    if choice == '1':
        student = Student(1, "Asmaa")
        while True: 
            print("----------------------------------")               
            student.show_menu()
            std_choice = get_valid_int("Enter your choice: ")
            print("----------------------------------")
            if std_choice == 1:
                book_choice = get_valid_int("Enter the ID of the book to borrow: ")
                print("----------------------------------")
                for b in books:
                    if b.id == book_choice:
                        student.borrow_book(b)
                        break
                else:
                    print("Invalid book ID.")
            elif std_choice == 2:
                book_choice = get_valid_int("Enter the ID of the book to return: ")
                print("----------------------------------")
                for b in student.borrowed_books:
                    if b.id == book_choice:
                        b.return_book()
                        student.borrowed_books.remove(b)
                        break
                else:
                    print("You did not borrow this book!!!!")
            elif std_choice == 3:
                book_choice = get_valid_int("Enter the ID of the book to display info: ")
                print("----------------------------------")
                for b in books:
                    if b.id == book_choice:
                        b.display_info()
                        break
                else:
                    print("Invalid book ID.")
            elif std_choice == 4:
                student.view_all_books(books)
                print("----------------------------------")
            elif std_choice == 5:
                student.view_available_books(books)
                print("----------------------------------")
            elif std_choice == 6:
                student.view_borrowed_books()
                print("----------------------------------")            
            elif std_choice == 7:
                print("Exiting Student Menu.")
                break         
    #teacher menu
    elif choice == '2':
        teacher = Teacher(2, "Mr. Mohamed")
        while True:
            print("----------------------------------")
            teacher.show_menu()
            teach_choice = get_valid_int("Enter your choice: ")
            print("----------------------------------")
            if teach_choice == 1:
                book_choice = get_valid_int("Enter the ID of the book to borrow: ")
                print("----------------------------------")
                for b in books:
                    if b.id == book_choice:
                        teacher.borrow_book(b)
                        break
                else:
                    print("Invalid book ID.")
                    print("Exiting Teacher Menu.")
            elif teach_choice == 2:
                book_choice = get_valid_int("Enter the ID of the book to return: ")
                print("----------------------------------")
                for b in teacher.borrowed_books:
                    if b.id == book_choice:
                        b.return_book()
                        teacher.borrowed_books.remove(b)
                        break
                else:
                    print("You did not borrow this book!!!!")
            elif teach_choice == 3:
                book_choice = get_valid_int("Enter the ID of the book to display info: ")
                print("----------------------------------")
                for b in books:
                    if b.id == book_choice:
                        b.display_info()
                        break
                else:
                    print("Invalid book ID.")
                    print("----------------------------------")
            elif teach_choice == 4:
                teacher.view_all_books(books)
                print("----------------------------------")
            elif teach_choice == 5:
                teacher.view_available_books(books)
                print("----------------------------------")
            elif teach_choice == 6:
                teacher.view_borrowed_books()
                print("----------------------------------")                
            elif teach_choice == 7:
                print("Exiting Teacher Menu.")
                print("----------------------------------")
                break  
        
    #librarian menu
    elif choice == '3':
        librarian = Librarian(3, "Mrs. Mariam")
        while True:
            print("----------------------------------")               
            librarian.show_menu()
            action = get_valid_int("Enter your choice: ")
            print("----------------------------------")
            
            if action == 1:
                new_book=book(
                    id=get_valid_int("Enter new book ID: "),
                    title=input("Enter new book title: "),
                    author=input("Enter new book author: "),
                    genre=input("Enter new book genre: "),
                    available_copies=get_valid_int("Enter number of available copies: ")
                )
                librarian.add_book(new_book, books)
            
            elif action == 2:
                print("----------------------------------")
                remove_book_id = get_valid_int("Enter the ID of the book to remove: ")
                print("----------------------------------")
                for b in books:
                    if b.id == remove_book_id:
                        librarian.remove_book(b, books)   
                        break
                else:
                    print("Invalid book ID.")
                    print("----------------------------------")
                    
            elif action == 3:
                book_choice = get_valid_int("Enter the ID of the book to return: ")
                print("----------------------------------")
                for b in librarian.borrowed_books:
                    if b.id == book_choice:
                        b.return_book()
                        librarian.borrowed_books.remove(b)
                        break
                else:
                    print("You did not borrow this book!!!!")        
            
            elif action == 4:
                print("----------------------------------")
                search_book_id = get_valid_int("Enter the ID of the book to search: ")
                print("----------------------------------")
                for b in books:
                    if b.id == search_book_id:
                        b.display_info()
                        break 
                else:
                    print("Invalid book ID.")
                    print("----------------------------------")                
            
            elif action == 5:
                librarian.view_all_books(books)
                print("----------------------------------")
          
            elif action == 6:
                librarian.view_available_books(books)
                print("----------------------------------")
                
            elif action == 7:
                librarian.view_borrowed_books()
                print("----------------------------------") 
                 
            elif action == 8:
                book_choice = get_valid_int("Enter the ID of the book to borrow: ")
                print("----------------------------------")
                for b in books:
                    if b.id == book_choice:
                        librarian.borrow_book(b)
                        break
                else:
                    print("Invalid book ID.")
                    print("Exiting Librarian Menu.") 
                    print("----------------------------------")  
                             
            elif action == 9:
                print("Exiting Librarian Menu.")
                print("----------------------------------")
                break
            
            else:
                print("Invalid action.")
                print("----------------------------------")    
    elif choice == '4':
        print("----------------------------------")
        print("Exiting Library Management System.")
        break             
    else :
        print("----------------------------------")
        print("Invalid choice. Please try again.") 
        print("----------------------------------")               