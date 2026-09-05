from functools import reduce
import sys

ARGSV_COUNT = 3
COMMAND_TYPES = ["filter","sort"]
SORT_TYPES = ["author","book"]

BOOKS = {
'A Game of Thrones': 'George R.R. Martin', 
'A Clash of Kings': 'George R.R. Martin', 
'The Fellowship of the Ring': 'J.R.R. Tolkien', 
"Harry Potter and the Sorcerer's Stone": 'J.K. Rowling', 
'Moby-Dick': 'Herman Melville', 
'Воскресение': 'Лев Николаевич Толстой'
}

  
def print_books(books_map): # type: ignore

    result = reduce(lambda acc, book: acc + f"{book['Книга'].ljust(40)} | {book['Автор']}\n", books_map,"") # type: ignore

    print("-"*70)
    print("Книга".ljust(40), "| ", "Автор")
    print("-"*70)
    print(result)
    print("-"*70)
    
# start programm
if len(sys.argv) != ARGSV_COUNT :
    print("Ошибка аргументов командной строки.")
    exit()

action: str      = str(sys.argv[1]).strip().lower()
action_txt: str  = str(sys.argv[2]).strip()


books = dict(BOOKS)
books_mapped = map(lambda book: {'Книга': book[0], 'Автор': book[1]}, books.items()) # type: ignore

match action:
    case "filter":
        books_filtred = filter(lambda book: action_txt in book["Автор"], books_mapped) # type: ignore
        print_books(books_filtred)
    case "sort":
        if action_txt in SORT_TYPES :
            if action_txt == "author":
                books_sorted = sorted(books_mapped, key = lambda book: book["Автор"]) # type: ignore
                print_books(books_sorted)               
            elif action_txt == "book":
                books_sorted = sorted(books_mapped, key = lambda book: book["Книга"]) # type: ignore
                print_books(books_sorted)
            else:
                print(f"Ошибка аргумента команды 'sort'. Используйте: {', '.join(SORT_TYPES)}")
        else:
            print(f"Ошибка аргумента команды 'sort'. Используйте: {', '.join(SORT_TYPES)}")
    case _:
        print(f"Ошибка в команде. Используйте {', '.join(COMMAND_TYPES)}")

