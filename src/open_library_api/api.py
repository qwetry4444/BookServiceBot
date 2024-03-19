import olclient.entity_helpers.work
from olclient import Book, BookHead
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
        print(results)
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
    def book_to_str(book: Book):
        print(
            f"{book.title}\nАвтор: {book.primary_author['name']}\nГод издательства: {book.publish_date}\nЖанр: {book.list_subjects()}")



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
