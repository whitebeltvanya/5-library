import sys

ARGSV_COUNT = 3
ACTION_COMMANDS = ["filter","sort"]
SORT_TYPES = ["author","book"]

BOOKS = {
'A Game of Thrones': 'George R.R. Martin', 
'A Clash of Kings': 'George R.R. Martin', 
'The Fellowship of the Ring': 'J.R.R. Tolkien', 
"Harry Potter and the Sorcerer's Stone": 'J.K. Rowling', 
'Moby-Dick': 'Herman Melville', 
'Воскресение': 'Лев Николаевич Толстой'
}

# input args
if len(sys.argv) != ARGSV_COUNT:
    print("Ошибка аргументов командной строки.")
    exit()

action: str      = str(sys.argv[1]).strip().lower() # action
action_parm: str  = str(sys.argv[2]).strip() # action parameter

if action not in ACTION_COMMANDS:
    print(f"Ошибка в команде. Используйте {', '.join(ACTION_COMMANDS)}")
    exit()

if action == "sort" and action_parm not in SORT_TYPES:
    print(f"Ошибка аргумента команды 'sort'. Используйте: {', '.join(SORT_TYPES)}")
    exit()

# filter or sort
books = dict(BOOKS)
match action:
    case "filter":
        books_filtred = filter(lambda book: action_parm in book[0], books.items()) # type: ignore
        books_out = list(map(lambda book: f"{book[0]} - {book[1]}", books_filtred)) # type: ignore
        print(books_out)
    case "sort":
        books_list = list(map(lambda book: f"{book[0]} - {book[1]}", books.items())) # type: ignore
        colum_idx_sort = 1 if action_parm == "author" else 0    
        books_out = sorted(books_list, key = lambda book: book.split("-")[colum_idx_sort]) # type: ignore
        print(books_list)
    case _:
        print("Ошибка в команде")