import unittest
import os
from datetime import datetime
from main import edit_record

class TestEditRecord(unittest.TestCase):

    def setUp(self):
        self.file_path = 'test_data.txt'
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.write('\n')
            file.write('Дата: 2023-03-24\n')
            file.write('Категория: Доход\n')
            file.write('Сумма: 1000\n')
            file.write('Описание: Зарплата\n')
            file.write('\n')
            file.write('Дата: 2023-03-25\n')
            file.write('Категория: Расход\n')
            file.write('Сумма: 500\n')
            file.write('Описание: Еда\n')

    def tearDown(self):
        os.remove(self.file_path)

    # Тест изменения дохода с указанной датой
    def test_edit_income_record(self):
        edit_record(self.file_path, 0, "2023-03-26", "Доход", 2000, "Зарплата")
        with open(self.file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        self.assertEqual(lines[1], 'Дата: 2023-03-26\n')
        self.assertEqual(lines[2], 'Категория: Доход\n')
        self.assertEqual(lines[3], 'Сумма: 2000\n')
        self.assertEqual(lines[4], 'Описание: Зарплата\n')
        self.assertEqual(lines[6], 'Дата: 2023-03-25\n')
        self.assertEqual(lines[7], 'Категория: Расход\n')
        self.assertEqual(lines[8], 'Сумма: 500\n')
        self.assertEqual(lines[9], 'Описание: Еда\n')

    # Тест изменения расхода без указанной даты
    def test_edit_expense_record(self):
        edit_record(self.file_path, 1, None, "Расход", 1000, "Покупки")
        with open(self.file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        today = datetime.now().strftime('%Y-%m-%d')
        self.assertEqual(lines[1], 'Дата: 2023-03-24\n')
        self.assertEqual(lines[2], 'Категория: Доход\n')
        self.assertEqual(lines[3], 'Сумма: 1000\n')
        self.assertEqual(lines[4], 'Описание: Зарплата\n')
        self.assertEqual(lines[6], 'Дата: 2023-03-25\n')
        self.assertEqual(lines[7], 'Категория: Расход\n')
        self.assertEqual(lines[8], 'Сумма: 1000\n')
        self.assertEqual(lines[9], 'Описание: Покупки\n')

if __name__ == '__main__':
    unittest.main()