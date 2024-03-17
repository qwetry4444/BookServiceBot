import olclient.entity_helpers.work
from olclient import Book
from olclient.openlibrary import OpenLibrary


# ol = OpenLibrary()
# # work = ol.Work.search(title="Harry")
# work = ol.Work.get("OL82563W")
# book = ol.Work.get()
# print(work)
# editions = work.editions
# print(editions)


def search_books_by_title(title, get_count=1) -> list[Book]:
    ol = OpenLibrary()
    results = ol.Work.search(title=title, get_count=get_count)
    return results


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

ol = OpenLibrary()
x = ol.Work.get("OL34009968M")
print(x)