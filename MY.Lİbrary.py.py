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
            if line_info[-1] == "F":
                checked_books.append(line_info[:-1])
                print(line_info[:-1])
                break

def add_new_book():
        books = open("books.txt", "a")
        isbn_number = input("Enter ISBN number(ten digits):")
        book_name = input("Enter the book name:")
        author = input("Enter the author name:")
        new_book = str(isbn_number + "," + book_name + "," + author + "," + "F/n")
        with open('books.txt', 'a') as books:
            books.write('new_book')
        print("Book added.")


def delete_book():
    with open("books.txt", "r") as file:
        infiles = file.readlines()

    isbn_num = input("Enter the ISBN number: ")
    found = False

    for i in infiles:
        line = i.strip().split(",")
        if isbn_num == line[0]:
            found = True
            if line[-1] == "T":
                print(f"{line[1]} is checked out, you cannot delete it.")
            else:
                print("Deleted Data:")
                infiles.remove(i)
                for data in infiles:
                    print(data.strip())
            break

    if not found:
        print("ISBN not found in the file.")



def search_by_isbn():
    isbn = input("Enter the ISBN number: ")
    books_dict = {}

    with open("books.txt", "r") as x:
        lines = x.readlines()

    for line in lines:
        isbn_key = line[:10].strip()
        book_name = line[11:].strip()

        books_dict[isbn_key] = book_name

    if isbn in books_dict:
        print(f"This book is: {books_dict[isbn]}")
    else:
        print("There is no book that has this code:", isbn)



def search_by_name():
    book_name = input("Enter the book name: ")
    books_dict = {}

    with open("books.txt", "r") as file:
        for line in file:
            line = line.strip().split(',')
            if len(line) >= 2:
                isbn_key = line[0].strip()
                book = line[1].strip()

                books_dict[book] = isbn_key

    if book_name in books_dict:
        print(f"The ISBN for {book_name} is: {books_dict[book_name]}")
    else:
        print(f"There is no book named {book_name}")

def check_out_book():
    student_id = input("Please enter the student Id:")
    book_isbn = input("Pşease enter the book ISBN number:")
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
            student_books_list.append(student_dict)

            with open("checked_out_books.txt", "w") as file:
                for item in student_books_list:
                    file.write(str(item) + "\n")
    return student_books_list


def list_books():
    student_books_list = []
    with open("checked_out_books.txt", "r") as file:
        for line in file.readlines():
            student_data = eval(line.strip())
            student_books_list.append(student_data)
    with open("checked_out_books.txt", "w") as file:
        for student_dict in student_books_list:
            file.write(f"Student ID: {student_dict['Student ID']}\n")
            for book in student_dict['Books']:
                file.write(f"- Book ID: {book['Book ID']}, Book Name: {book['Book Name']}, Status: {book['Status']}\n")
            file.write("\n")



def menu():
    while True:
        print("Main Menu:")
        print("1)List all the books in the library.")
        print("2)List all the books that are checked out.")
        print("3)Add a new book.")
        print("4)Delete a book.")
        print("5)Search a book by ISBN number.")
        print("6)Search a book by name.")
        print("7)Check out a book to a student.")
        print("8)List all the students.")
        print("9)If you want to exit,you should enter the q letter.")

        choice = input("Please enter an option (1-9): ")

        if choice == "1":
            list_all_books()
        elif choice == "2":
            checked_books()
        elif choice == "3":
            add_new_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            search_by_isbn()
        elif choice == "6":
            search_by_name()
        elif choice == "7":
            check_out_book()
        elif choice == "8":
            list_books()
        elif choice == "9":
            print("Exiting the program...")
            break
        else:
            print("Invalid option. Please enter a number between 1 and 9.")

menu()