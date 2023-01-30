from datetime import datetime
from datetime import timedelta


class Loans:
    def __init__(self,cust_id, book_id, loan_date):
        self.cust_id = cust_id
        self.book_id = book_id
        self.loan_date = loan_date

    def loan_a_book(self):
        loan_file = (open('Loans.csv', 'a'))
        book_file = (open('Books.csv', 'r'))
        new_customer_id = self.cust_id
        new_book_id = self.book_id
        new_loan_date = (datetime.strptime((str((self.loan_date))), '%Y%m%d'))
        new_format_for_new_loan_date = new_loan_date.strftime('%d/%m/%Y')
        new_return_date = datetime(1, 1, 1)
        book_id_type = {}
        for col in book_file.readlines()[1::]:
            book_id_books = col.split(',')
            book_id_type[book_id_books[0]] = book_id_books[4]
        if str(self.book_id) in book_id_type:
            if book_id_type.get(self.book_id) == '1\n':
                new_return_date = new_loan_date + timedelta(days = 10)
            if book_id_type.get(self.book_id) == '2\n':
                new_return_date = new_loan_date + timedelta(days = 5)
            if book_id_type.get(self.book_id) == '3\n':
                new_return_date = new_loan_date + timedelta(days = 2)
        new_format_new_return_date = new_return_date.strftime('%d/%m/%Y')
        ls = [str(new_customer_id), str(new_book_id), str(new_format_for_new_loan_date), str(new_format_new_return_date)]
        i = ','.join(ls)
        loan_file.write(i + '\n')
        print('\nThe loan information has been added to the system you may take the book.')
        book_file.close()
        loan_file.close()