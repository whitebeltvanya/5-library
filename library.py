books: dict[str, str]= {}

books["A Game of Thrones"] = "George R.R. Martin"
books["A Clash of Kings"]  = "George R.R. Martin"
books["The Fellowship of the Ring"] ="J.R.R. Tolkien"
books["Harry Potter and the Sorcerer's Stone"] ="J.K. Rowling"
books["Moby-Dick"] = "Herman Melville"

authors: set[str] = set()
authors = set (books.values())

print("Список всех книг:")
for book in sorted(books):
    print(f"Название книги:{book}")

print("-"*40)
print("Список авторов:")
for author in sorted(authors):
    print(f"Автор книг:{author}")
