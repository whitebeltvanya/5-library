import sys

ARGSV_COUNT = 3
COMMAND_TYPES = ["filter","sort"]
SORT_TYPES = ["author","book"]


def filter_books(fiter_txt: str) -> dict[str, str]:
    return dict(filter(
                lambda book: fiter_txt in book[1].lower(), books.items()
                ))
    
def sort_books(sort_type: str) -> dict[str, str]:
    if sort_type == "author":
        return dict(sorted(
            books.items(), key = lambda book: book[1]
            ))
    elif sort_type == "book":
        return dict(sorted(books.items()))
    else:
        return books
        
def print_book_info(books_result: dict[str, str]):

    print("-"*70)
    print("Книга".ljust(40), " | ", "Автор")
    print("-"*70)

    if not books_result :
        print("Ничего не найдено")
    else:   
        for key, value in books_result.items():
            print(key.ljust(40), " | ", value)

    print("-"*70)
    

def init_books () -> dict[str, str]:
    books_new: dict[str, str]= {}
    books_new["A Game of Thrones"] = "George R.R. Martin"
    books_new["A Clash of Kings"]  = "George R.R. Martin"
    books_new["The Fellowship of the Ring"] ="J.R.R. Tolkien"
    books_new["Harry Potter and the Sorcerer's Stone"] ="J.K. Rowling"
    books_new["Moby-Dick"] = "Herman Melville"
    books_new["Воскресение"] = "Лев Николаевич Толстой"
    return books_new


# start programm
if len(sys.argv) != ARGSV_COUNT :
    print("Ошибка аргументов командной строки.")
    exit()

action: str      = str(sys.argv[1]).strip().lower()
action_txt: str  = str(sys.argv[2]).strip()


books = init_books()
match action:
    case "filter":
        ret = filter_books(action_txt)
        print_book_info(ret)
    case "sort":
        if action_txt in SORT_TYPES :
            ret = sort_books(action_txt)
            print_book_info(ret)
        else:
            print(f"Ошибка аргумента команды 'sort'. Используйте: {', '.join(SORT_TYPES)}")
    case _:
        print(f"Ошибка в команде. Используйте {', '.join(COMMAND_TYPES)}")