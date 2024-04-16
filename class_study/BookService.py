from BookRepository import BookRepository

class BookService:

    @classmethod
    def addBook(cls, book=None):
        BookRepository.saveBook(book=book)