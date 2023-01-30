from datetime import datetime
from Customers import Customers
from Books import Books
from Loans import Loans
import pandas
import csv


def display_menu():
    print("\n------------------------- Library management software ------------------------- ")
    print("Enter the number of the service you wish to use.")
    print("Main Menu:")
    print("1. Add a new customer")
    print("2. Add a new book")
    print("3. loan a book")
    print("4. Return a book")
    print("5. Display all books information")
    print("6. Display all customers information")
    print("7. Display all loans information")
    print("8. Display late loans information")
    print("9. Find book by name")
    print("10. Find customer by name")
    print("11. Remove a book by book ID")
    print("12. Remove a customer by customer ID")
    print("13. Exit the program")


def add_customer():
    print("\nPlease enter new customer information")
    customers_entity = Customers(input('Please enter ID: '),
                                 input('Please enter name: '),
                                 input('Please enter city: '),
                                 input('Please enter age: '))
    customers_entity.new_customer()


def new_book():
    print("\nPlease enter new book information")
    books_entity = Books(input('Please enter ID: '),
                         input('Please enter Name: '),
                         input('Please enter Author: '),
                         input('Please enter Year published: '),
                         input('Please enter Type: '))
    books_entity.add_book()


def loan_new():
    print("\nPlease enter loan information")
    new_loan_entity = Loans(input('Please enter customer ID: '),
                            input('Please enter book ID: '),
                            input('Please enter the loan date at this format -- YearMonthDay -- 19960329 = 29/03/1996: '))
    new_loan_entity.loan_a_book()


def return_a_book(book_id):
    read_loan_file = open('Loans.csv', 'r')
    lines = read_loan_file.readlines()
    read_loan_file.close()
    for col in lines:
        if book_id in col:
            var = col
    write_loan_file = open('Loans.csv', 'w')
    for line in lines:
        if line != str(var):
            write_loan_file.write(line)
    write_loan_file.close()
    print('\nThe book returned successfully')


def books_display():
    print('\n------------------------ Books ------------------------')
    df = pandas.read_csv('Books.csv')
    print(df)


def customers_display():
    print('\n------------------------ Customers ------------------------')
    df = pandas.read_csv('Customers.csv')
    print(df)


def loans_display():
    print('\n------------------------ Loans ------------------------')
    df = pandas.read_csv('Loans.csv')
    print(df)


def display_late_loans():
    print('\n------------------------ Late Loans ------------------------')
    c_file = (open('Loans.csv', 'r'))
    for col in c_file.readlines()[1::]:
        split_col = col.split(',')
        for letters in split_col[3]:
            if letters == '\n':
                x = split_col[3].replace('\n', '')
        str_to_date = datetime.strptime(str(x), '%d/%m/%Y')
        if str_to_date < datetime.utcnow():
            late_loans_data = '\t\t'.join(split_col)
            print('CustID, BookID, Loandate, Returndate', '\n', late_loans_data)
    c_file.close()


def book_by_name(book_name):
    bfile = open('Books.csv', 'r')
    for line in bfile.readlines():
        row = line.split(',')
        if row[1] == book_name:
            print(f'\nID: {row[0]} | Name: {row[1]} | Author: {row[2]} | Year Published: {row[3]} | Type: {row[4]}')
    bfile.close()


def customer_by_name(customer_name):
    cfile = open('Customers.csv', 'r')
    for line in cfile.readlines():
        row = line.split(',')
        if row[1] == customer_name:
            print(f'\nID: {row[0]} | Name: {row[1]} | City: {row[2]} | Age: {row[3]}')
    cfile.close()


def remove_book(book_id):
    bfile = open('Books.csv', 'r')
    csvr = csv.reader(bfile)
    found = 0
    ml = []
    for r in csvr:
        if r[0] != book_id:
            ml.append(r)
        else:
            found = 1
    bfile.close()
    if found == 0:
        print('\nBook ID not Found')
    else:
        bfile = open('Books.csv', 'w', newline='')
        csvr = csv.writer(bfile)
        csvr.writerows(ml)
        print('\nBook have been deleted successfully')
        bfile.close()


def remove_customer(customer_id):
    cfile = open('Customers.csv', 'r')
    csvr = csv.reader(cfile)
    found = 0
    ml = []
    for r in csvr:
        if r[0] != customer_id:
            ml.append(r)
        else:
            found = 1
    cfile.close()
    if found == 0:
        print('\nCustomer ID not Found')
    else:
        cfile = open('Customers.csv', 'w', newline='')
        csvr = csv.writer(cfile)
        csvr.writerows(ml)
        print('\nCustomer has been deleted successfully')
        cfile.close()


def quit_program():
    print("\n*SHUT - DOWN* Thank you for using Library management software BYE BYE !")
    exit()

#######################################################################################################################
                                            ### menu display ###


if __name__ == '__main__':
    loop = True
    while loop:
        display_menu()
        user_input = input("Please enter a choice by number 1..13: ")
        if user_input == '1':
            add_customer()
        if user_input == '2':
            new_book()
        if user_input == '3':
            loan_new()
        if user_input == '4':
            return_a_book(input('Please enter the book ID you wish to return: '))
        if user_input == '5':
            books_display()
        if user_input == '6':
            customers_display()
        if user_input == '7':
            loans_display()
        if user_input == '8':
            display_late_loans()
        if user_input == '9':
            book_by_name(input('Please enter the name of the book you wish to find: '))
        if user_input == '10':
            customer_by_name(input('Please enter the name of the customer you wish to find: '))
        if user_input == '11':
            remove_book(input('Please enter the book ID you wish to delete: '))
        if user_input == '12':
            remove_customer(input('Please enter the customer ID you wish to delete: '))
        if user_input == '13':
            quit_program()
            # loop = False