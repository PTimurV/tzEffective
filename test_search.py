import unittest
import os
from main import search_records

class TestSearchRecord(unittest.TestCase):

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


    def test_search_by_category(self):
        # Поиск записей с категорией "Доход"
        with open(self.file_path, 'r', encoding='utf-8') as file:
            records = search_records(self.file_path, category='Доход')
            self.assertEqual(len(records), 1)
            self.assertEqual(records[0]['Категория'], 'Доход')
            
            self.assertEqual(records[0]['Сумма'], '1000')
            self.assertEqual(records[0]['Описание'], 'Зарплата')

        # Поиск записей с категорией "Расход"
        with open(self.file_path, 'r', encoding='utf-8') as file:
            records = search_records(self.file_path, category='Расход')
            self.assertEqual(len(records), 1)
            self.assertEqual(records[0]['Категория'], 'Расход')
            self.assertEqual(records[0]['Сумма'], '500')
            self.assertEqual(records[0]['Описание'], 'Еда')
          
    def test_search_by_amount(self):
        # Поиск записей с суммой 1000
        with open(self.file_path, 'r', encoding='utf-8') as file:
            records = search_records(self.file_path, amount=1000)
            self.assertEqual(len(records), 1)
            self.assertEqual(records[0]['Категория'], 'Доход')
            self.assertEqual(records[0]['Сумма'], '1000')
            self.assertEqual(records[0]['Описание'], 'Зарплата')

        # Поиск записей с суммой 500
        with open(self.file_path, 'r', encoding='utf-8') as file:
            records = search_records(self.file_path, amount=500)
            self.assertEqual(len(records), 1)
            self.assertEqual(records[0]['Категория'], 'Расход')
            self.assertEqual(records[0]['Сумма'], '500')
            self.assertEqual(records[0]['Описание'], 'Еда')  
if __name__ == '__main__':
    unittest.main()