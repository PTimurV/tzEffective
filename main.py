import os
import argparse
from datetime import datetime

# Функция для вывода баланса
def show_balance(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        income = 0
        expense = 0
        for line in file:
            if line.startswith("Категория: Доход"):
                income += int(next(file).split(":")[1].strip())
            elif line.startswith("Категория: Расход"):
                expense += int(next(file).split(":")[1].strip())
    result = f"Текущий баланс: {income - expense}\nДоходы: {income}\nРасходы: {expense}"
    print(result)
    return result

# Функция добавления записи
def add_record(file_path, category, amount, description, date=None):
    if not date:
        date = datetime.now().strftime('%Y-%m-%d')
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(f"\nДата: {date}\n")
        file.write(f"Категория: {category}\n")
        file.write(f"Сумма: {amount}\n")
        file.write(f"Описание: {description}\n")

# Функция изменения записи
def edit_record(file_path, record_index, date=None, category=None, amount=None, description=None):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Проверяем, существует ли запись с указанным индексом
    if record_index < 0 or record_index * 5 >= len(lines):
        print("Ошибка: Запись с указанным индексом не найдена")
        return

    # Сохраняем текущие значения записи
    record = {
        "date": lines[record_index * 5 + 1].split(":")[1].strip(),
        "category": lines[record_index * 5 + 2].split(":")[1].strip(),
        "amount": lines[record_index * 5 + 3].split(":")[1].strip(),
        "description": lines[record_index * 5 + 4].split(":")[1].strip()
    }

    # Меняем данные записи
    if date:
        record["date"] = date
    if category:
        record["category"] = category
    if amount:
        record["amount"] = amount
    if description:
        record["description"] = description

    # Перезаписываем файл с обновленными данными
    new_lines = []
    for i in range(len(lines)):
        if i == record_index * 5 + 1:
            new_lines.append(f"Дата: {record['date']}\n")
        elif i == record_index * 5 + 2:
            new_lines.append(f"Категория: {record['category']}\n")
        elif i == record_index * 5 + 3:
            new_lines.append(f"Сумма: {record['amount']}\n")
        elif i == record_index * 5 + 4:
            new_lines.append(f"Описание: {record['description']}\n")
        else:
            new_lines.append(lines[i])

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

# Функция поиска записей
def search_records(file_path, category=None, date=None, amount=None):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    found_records = []
    record = {}
    for line in lines:
        if line.startswith("Дата:"):
            if record:
                found_records.append(record)
            record = {}
            record["Дата"] = line.split(":")[1].strip()
        elif line.startswith("Категория:"):
            record["Категория"] = line.split(":")[1].strip()
        elif line.startswith("Сумма:"):
            record["Сумма"] = line.split(":")[1].strip()
        elif line.startswith("Описание:"):
            record["Описание"] = line.split(":")[1].strip()
    if record:
        found_records.append(record)

    Answer=[]
    # Проверяем условия поиска и выводим найденные записи
    for rec in found_records:
        if (not category or category == rec.get("Категория")) and \
           (not date or date == rec.get("Дата")) and \
           (not amount or amount == int(rec.get("Сумма"))):
            Answer.append(rec)
            print(rec)

    # Если не найдено ни одной записи, сообщаем об этом
    if not found_records:
        print("Нет записей, соответствующих заданным условиям.")
    return Answer

def main():
    # Определение аргументов командной строки
    parser = argparse.ArgumentParser(description="Личный финансовый кошелек")
    parser.add_argument("file_path", help="Путь к файлу с данными")
    parser.add_argument("--add", nargs="+", help="Добавить запись (аргументы: Категория(Доход/Расход) Сумма Описание [Дата])")
    parser.add_argument("--edit", nargs="+", help="Редактировать запись (аргументы: Индекс [--date Дата] [--category Категория] [--amount Сумма] [--description Описание])")
    parser.add_argument("--search", nargs="*", help="Поиск записей (аргументы: [--date Дата] [--category Категория] [--amount Сумма])")
    parser.add_argument("--date", help="Новая дата записи")
    parser.add_argument("--category", help="Новая категория записи")
    parser.add_argument("--amount", type=int, help="Новая сумма записи")
    parser.add_argument("--description", help="Новое описание записи")

    args = parser.parse_args()

    if not os.path.exists(args.file_path):
        print("Ошибка: Файл не существует")
        return

    if args.add:
        add_record(args.file_path, *args.add)

    elif args.edit:
        edit_args = args.edit
        record_index = int(edit_args.pop(0))  # Извлекаем индекс записи

        # Вызываем функцию редактирования с переданными аргументами
        edit_record(args.file_path, record_index, args.date, args.category, args.amount, args.description)

    elif args.search:
        search_records(args.file_path, category=args.category, date=args.date, amount=args.amount)

    else:
        show_balance(args.file_path)

if __name__ == "__main__":
    main()