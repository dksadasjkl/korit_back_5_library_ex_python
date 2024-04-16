from BookService import BookService
from BookEntity import Book

class BookController:

    @classmethod
    def addBookRequest(cls):
        book = Book(bookName="테스트", authorName="테스트 저자명", publisherName="테스트 출판사", isbn="13213213")
        BookService.addBook(book=book)