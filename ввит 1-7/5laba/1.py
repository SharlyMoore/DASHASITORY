class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return(f"Название книги: {self.title},  Автор: {self.author}, Год издания: {self.year}")

Book1 = Book("'Дом, в котором'", "Мариам Петросян", 2007)
Book2 = Book("'Часодеи. Часовой ключ'", "Наталья Щерба", 2014)

print(Book1.get_info())
