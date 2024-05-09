Личный финансовый кошелек

Документация (ее можно вызвать командой "python main.py -h"):

positional arguments:
  file_path             Путь к файлу с данными

optional arguments:
  -h, --help            show this help message and exit
  --add ADD [ADD ...]   Добавить запись (аргументы: Категория Сумма Описание [Дата])
  --edit EDIT [EDIT ...]
                        Редактировать запись (аргументы: Индекс [--date Дата] [--category Категория] [--amount Сумма] [--description Описание])
  --search [SEARCH [SEARCH ...]]
                        Поиск записей (аргументы: [--date Дата] [--category Категория] [--amount Сумма])
  --date DATE           Новая дата записи
  --category CATEGORY   Новая категория записи
  --amount AMOUNT       Новая сумма записи
  --description DESCRIPTION
                        Новое описание записи

Посмотреть баланс: python main.py data.txt

Добавить новую запись (Дата не обязательное поле (если не указывать будет сегодняшняя дата)): python main.py data.txt --add Расход 4000 "Покупка" "2023-12-12"

Редактировать запись: python main.py data.txt --edit 0 --date "2024-11-11" --category "Расход" --amount 5000 --description "Покупка продуктов2"
Каждое из полей не является обязательным и можно их записывать в любом порядке, 0-индекс записи

Поиск записей:  python main.py data.txt --search 1 --date 2024-05-09 --amount 4000 --category "Доход"
Поля не являются обязательными но при этом реализован и совместный поиск сразу по нескольким полям. (1-просто любое число, у --search должно быть значение (любое) без этого не работает)

Тест добавления: python test_add.py
Тест изменения: python test_edit.py
Тест поиска: python test_search.py
Тест вывода баланса: python test_balance.py