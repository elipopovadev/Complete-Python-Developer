class Book:
    def __init__(self, author, title, year):
        self.author = author
        self.title = title
        self.year = year


book1 = Book("Oscar Wilde", "The Picture of Dorian Gray", 1890)
book2 = Book("Charles Dickens", "A Christmas Carol", 1843)
book3 = Book("Charles Dickens", "Hard Times", 1854)
all_Books = []
all_Books.append(book1)
all_Books.append(book2)
all_Books.append(book3)

def generator_func_by_title(all_Books):
    for i in range(len(all_Books)):
        yield all_Books[i].title

for book_title in generator_func_by_title(all_Books):
        print(book_title)
