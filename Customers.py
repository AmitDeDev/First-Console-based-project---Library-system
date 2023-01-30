class Customers:
    def __init__(self, customer_id, name, city, age):
        self.customer_id = customer_id
        self.name = name
        self.city = city
        self.age = age

    def new_customer(self):
        cfile = open('Customers.csv', 'a')
        new_id = self.customer_id
        new_name = self.name
        new_city = self.city
        new_age = self.age
        ls = [new_id, new_name, new_city, new_age]
        text_line = ','.join(ls)
        cfile.write(text_line + '\n')
        print('\nNew customer has been added.')
        cfile.close()