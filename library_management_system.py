def list_all_books():
    with open("books.txt") as books:
        listbooks = books.readlines()
        for i in listbooks:
            if i.strip():
                book = i.strip().split(",")
                print(book[:])

def checked_books():
    with open("books.txt") as books:
        books_info = books.readlines()
        checked_books = []
        for line_info in books_info:
            line_info = line_info.strip().split(",")
            if line_info[-1] == "T":
                checked_books.append(line_info[:-1])
                print(line_info[:-1])

def add_new_book():
        books = open("books.txt" , "a")
        isbn_number = input("Enter ISBN number(ten digits):")
        book_name = input("Enter the book name:")
        author = input("Enter the author name:")
        new_book = str(isbn_number + "," + book_name + "," + author + "," + "F/n")
        books.append(new_book)
        print("Book added.")

def delete_book():
    with open("books.txt" , "r") as file:
        infiles = file.readlines()
        isbn_num = input("Enter the ISBN number:")
        for i in infiles:
            line = i.strip().split(",")
            if isbn_num == line[0]:
                if line[-1] == "T":
                    print(f"{line[1]} is checked up,you can not delete it.")
                    break
                else:
                    del i
                    break

def search_by_isbn():
    isbn = input("Enter the ISBN number:")
    with open("books.txt", "r") as x:
        books_list = []
        line1 = x.readline()
        lines = x.readlines()
        for i in range(len(lines)):
            books_list.append(line1)
            line1 = x.readline()
    books_dict = dict()
    for j in range(len(books_list)):
        if books_dict[books_list[j][:10]] == books_list[j][11:books_list[j].find(",", 11)]:
           print("This book is:", books_dict[str(isbn)])
        else:
            print("There is no book that has this code" , isbn)

def search_by_name():
    book_name = input("Which book do you want to search?")
    with open("books.txt",'r') as file:
        book_list = []



def student_isbn_check():
    student_books_list = []
    file_name = "student_books.txt"
    try:
        with open(file_name, "r") as file:
            for line in file:
                student_books_list.append(eval(line))
    except FileNotFoundError:
        pass
    with open("books.txt", "r", encoding="UTF-8") as file:
        book_lines = file.readlines()
    student_id = input("Please enter the student ID: ")
    book_isbn = input("Please enter ISBN of the book: ")
    with open("students.txt", "r", encoding="UTF-8") as file_2:
        student_lines = file_2.readlines()
    book_info = [book_line.split(',') for book_line in book_lines]
    student_found = False
    book_found = False
    student_dict = None
    for line in student_lines:
        data = line.strip().split()
        if student_id in data:
            student_found = True
            student_dict = {'Student ID': student_id, 'Books': []}
            for book_data in book_info:
                if book_isbn in book_data[0]:
                    book_found = True
                    student_dict['Books'].append(
                        {'Book ID': book_isbn, 'Book Name': book_data[1], 'Status': book_data[2]})
                    print(f"The student named {data[1]} is assigned the book {book_data[1]}")
                    break
    if not student_found:
        print("The student is not found.")
    if not book_found:
        print("The book is not found for this student.")
    else:
        if student_dict:
            student_books_list.append(student_dict)  # Add the dictionary to the list

            with open(file_name, "w") as file:
                for item in student_books_list:
                    file.write(str(item) + "\n")  # Write each dictionary as a string in a new line
    print(student_books_list)
def list_books():
    student_books_dict = {} 
try:
      with open("students.txt", "r") as file:
        for line in file:
            student_data = eval(line)  
            student_id = student_data['Student ID']
            student_books_dict = {} 
            student_books_dict.setdefault(student_id, []).extend(student_data['Books'])
except FileNotFoundError:
    pass  
for student, books in student_books_dict.items():
    if books:  
        print(f"Student: {student}")
        for book in books:
            print(f"Book: {book['Book Name']} (ID: {book['Book ID']}, Status: {book['Status']})")
        print("\n")  


def menu():
    while True:
        print("\n--- Library Management System ---")
        print("1. Add New Book")
        print("2. Delete Book")
        print("3. Search Book by ISBN Number")
        print("4. Search Book by Name")
        print("5. Issue Book to Student")
        print("6. Return Book")
        print("7. Show All Books in Library")
        print("8. Show All Students")
        print("9. Exit")

        choice = input("Please enter an option (1-9): ")

        if choice == "1":
            list_all_books()
        elif choice == "2":
            checked_books
        elif choice == "3":
            add_new_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            search_by_isbn()
        elif choice == "6":
            search_by_name()
        elif choice == "7":
            student_isbn_check()
        elif choice == "8":
            list_books()
        elif choice == "9":
            print("Exiting the program...")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 9.")


menu()