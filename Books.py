class Books:
    def __init__(self, id, Name, Author, Year_Published, Type):
        self.id = id
        self.Name = Name
        self.Author = Author
        self.Year_Published = Year_Published
        self.Type = Type

    def add_book(self):
        bfile = open('Books.csv', 'a')
        new_id = self.id
        new_name = self.Name
        new_author = self.Author
        new_year = self.Year_Published
        new_type = self.Type
        ls = [new_id, new_name, new_author, new_year, new_type]
        text_line = ','.join(ls)
        bfile.write(text_line + '\n')
        print('\nNew book has been added.')
        bfile.close()