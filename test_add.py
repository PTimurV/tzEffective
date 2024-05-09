import unittest
import os
from datetime import datetime
from main import add_record

class TestAddRecord(unittest.TestCase):

    def setUp(self):
        self.file_path = 'test_data.txt'
        with open(self.file_path, 'w') as file:
            file.write('')

    def tearDown(self):
        os.remove(self.file_path)

    # Тест добавления дохода с указанной датой
    def test_add_income_record(self):
        add_record(self.file_path, 'Доход', 1000, 'Зарплата', "2023-03-24")
        with open(self.file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        self.assertEqual(lines[1], 'Дата: 2023-03-24\n')
        self.assertEqual(lines[2], 'Категория: Доход\n')
        self.assertEqual(lines[3], 'Сумма: 1000\n')
        self.assertEqual(lines[4], 'Описание: Зарплата\n')

    # Тест добавления расхода без указанной даты
    def test_add_expense_record(self):
      add_record(self.file_path, 'Расход', 500, 'Еда')
      with open(self.file_path, 'r', encoding='utf-8') as file:
          lines = file.readlines()
      today = datetime.now().strftime('%Y-%m-%d')
      self.assertEqual(lines[1], 'Дата: {}\n'.format(today))
      self.assertEqual(lines[2], 'Категория: Расход\n')
      self.assertEqual(lines[3], 'Сумма: 500\n')
      self.assertEqual(lines[4], 'Описание: Еда\n')

if __name__ == '__main__':
    unittest.main()