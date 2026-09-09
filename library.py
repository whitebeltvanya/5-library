import sys

ARGSV_COUNT = 3
ACTION_COMMANDS = ["filter","sort"]
SORT_TYPES = ["author","book"]
SPLITTER = " — "

BOOKS = {
'A Game of Thrones': 'George R.R. Martin', 
'A Clash of Kings': 'George R.R. Martin', 
'The Fellowship of the Ring': 'J.R.R. Tolkien', 
"Harry Potter and the Sorcerer's Stone": 'J.K. Rowling', 
'Moby-Dick': 'Herman Melville', 
'Воскресение': 'Лев Николаевич Толстой'
}
#Ошибки
class ActionEror(Exception):
    """Базовый класс ошибок входящих аргументов"""

class ArgsCountError(ActionEror):
    """Ошибка кол-ва аргументов ком. строки"""

class NotExistAction(ActionEror):
    """Не существующая команда"""

class EmptyFilterValue(ActionEror):
    """Пустое значение фильтра"""

class NotExistSortType(ActionEror):
    """Не существующий тип сортировки"""

# filter or sort
def filter_sort (b: dict[str,str], act: str, act_parm: str):
    """Фильтрация или сортировка списка книг"""
    match act:
        case "filter":
            books_filtred = filter(lambda book: act_parm in book[0], b.items()) # type: ignore
            books_out = list(map(lambda book: f"{book[0]}{SPLITTER}{book[1]}", books_filtred)) # type: ignore
            print('\n'.join(books_out))
        case "sort":
            books_list = list(map(lambda book: f"{book[0]}{SPLITTER}{book[1]}", b.items())) # type: ignore
            colum_idx_sort = 1 if act_parm == "author" else 0    
            books_out = sorted(books_list, key = lambda book: book.split(SPLITTER)[colum_idx_sort]) # type: ignore
            print('\n'.join(books_out))
        case _:
            raise NotExistAction ("Не существующая команда")
    
# main
try:
    if len(sys.argv) != ARGSV_COUNT:
        raise ArgsCountError("Неверное кол-во аргументов командной строки")

    action: str        = str(sys.argv[1]).strip().lower() # action
    action_parm: str   = str(sys.argv[2]).strip() # action parameter

    if action not in ACTION_COMMANDS:
        raise NotExistAction(f"Не существующая команда. Используйте: {', '.join(ACTION_COMMANDS)}")

    if action == "filter" and not action_parm:
        raise EmptyFilterValue("Отсутствует значение для фильтра")

    if action == "sort" and action_parm not in SORT_TYPES:
        raise NotExistSortType(f"Ошибка аргумента команды 'sort'. Используйте: {', '.join(SORT_TYPES)}")

    books = dict(BOOKS)
    filter_sort(books, action, action_parm)

except ActionEror as e:
    print(f"Ошибка: {e}")
finally:
    print("---Завершение работы программы---")