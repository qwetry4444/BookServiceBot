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
        print(f"AUTHOR{author}")
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
        if author.title:
            author_str += f"<b>{author.title}</b>\n\n"
        elif author.name:
            author_str += f"<b>{author.name}</b>\n\n"
        if author.bio:
            author_str += author.bio

        return author_str

    @staticmethod
    def get_cover_url(book: Book) -> str:
        return f"https://covers.openlibrary.org/b/id/{book.cover_edition_key}-L.jpg"

    @staticmethod
    def get_author_photo_url(author: Author):
        return f"https://covers.openlibrary.org/a/olid/{author.olid}-L.jpg"
# search_query = "Тихий Дон"  # Замените это на название книги, которую вы ищете
# search_results = search_books_by_title(search_query, get_count=5)

# if search_results:
#     print(f"Найдено {(search_results)} книг по запросу '{search_query}':")
#     for book in search_results:
#         print("Название книги:", book.title)
#         print(book.authors)
#         # print("Автор(ы):", ", ".join(book.authors))
#         print("Издательство:", book.publisher if book.publisher else "Unknown")
#         print("Год публикации:", book.publish_date)
#         print("Жанр: ", book.subjects)
#         print("---------------------------------------")
# else:
#     print(f"По запросу '{search_query}' книги не найдены.")

# x = search_books_by_title("love123")
# print(x)
# for i in range(len(x)):
#     send_book(x[i])
