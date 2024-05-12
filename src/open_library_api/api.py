import olclient.entity_helpers.work
from olclient import Book, BookHead, Author
from olclient.openlibrary import OpenLibrary


# ol = OpenLibrary()
# # work = ol.Work.search(title="Harry")
# work = ol.Work.get("OL82563W")
# book = ol.Work.get()
# print(work)
# editions = work.editions
# print(editions)

class ApiHelper:
    @staticmethod
    def search_books_by_title(title) -> list[Book]:
        ol = OpenLibrary()
        results = ol.Work.search(title=title)
        return results

    @staticmethod
    def search_bookheads_by_title(title) -> list[BookHead]:
        ol = OpenLibrary()
        results = ol.Work.search_bookhead(title=title)
        # print(results)
        return results

    @staticmethod
    def search_books_by_author(author) -> list[Book]:
        ol = OpenLibrary()
        results = ol.Work.search(author=author)
        return results

    @staticmethod
    def search_books_by_subject(subject) -> list[Book]:
        ol = OpenLibrary()
        results = ol.Work.search_by_subject(subject=subject)
        return results

    @staticmethod
    def search_book_by_key(key: str) -> Book:
        ol = OpenLibrary()
        if key.count('/') > 1:
            key = key.split('/')[2]
        x = ol.Work.get(key)
        book = ol.Work.get(key).to_book()
        # book = ol.get_
        print(book)
        return book

    @staticmethod
    def get_author_of_book(book: Book) -> Author:
        ol = OpenLibrary()
        author = ol.Author.get(book.authors[0]['author']['key'].split('/')[2])
        return author

    @staticmethod
    def book_to_str(book: Book):
        ol = OpenLibrary()
        author = ol.Author.get(book.authors[0]['author']['key'].split('/')[2])
        book_str = ""
        if book.title:
            book_str += f"<b>{book.title}</b>\n\n\n"
        if author:
            book_str += f"Автор:  {author.name}\n\n"
        if book.publish_date:
            book_str += f"Год издательства:  {book.publish_date}\n\n"
        if book.title:
            book_str += f"Жанр:  {', '.join(book.list_subjects().split(', ')[:5])}\n\n"

        return book_str

    @staticmethod
    def author_to_str(author: Author) -> str:
        author_str = ""
        try:
            if author.title:
                author_str += f"<b>{author.title}</b>\n\n"
            elif author.name:
                author_str += f"<b>{author.name}</b>\n\n"
            if author.bio:
                author_str += author.bio

            return author_str
        except AttributeError:
            try:
                if author.name:
                    author_str += f"<b>{author.name}</b>\n\n"
                if author.bio:
                    author_str += f"{'.'.join(author.bio[:500].split('.')[:-1])}."
                return author_str
            except AttributeError:
                return "Не удалось найти информацию об авторе"


    @staticmethod
    def get_cover_url(book: Book) -> str:
        return f"https://covers.openlibrary.org/b/id/{book.cover_edition_key}-L.jpg"

    @staticmethod
    def get_author_photo_url(author: Author):
        return f"https://covers.openlibrary.org/a/olid/{author.olid}-L.jpg"
