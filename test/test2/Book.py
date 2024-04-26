class Book:
    def __init__(self, bookId = 0, bookName = "", author = "", publisher = ""):
        self.bookId = bookId
        self.bookName = bookName
        self.author = author
        self.publisher = publisher

    def __str__(self):
        return f"""Book[
bookId: {self.bookId},  
bookName: {self.bookName},
author: {self.author},
publisher : {self.publisher}
        ]"""