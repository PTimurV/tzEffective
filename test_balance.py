import unittest
import os
from main import add_record, show_balance

class TestShowBalance(unittest.TestCase):

    def setUp(self):
        self.file_path = 'test_data.txt'
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.write('')

    def tearDown(self):
        os.remove(self.file_path)

    def test_show_balance(self):
        # Добавляем записи
        add_record(self.file_path, 'Доход', 1000, 'Зарплата', "2023-03-24")
        add_record(self.file_path, 'Расход', 500, 'Еда', "2023-03-25")
        add_record(self.file_path, 'Доход', 2000, 'Премия', "2023-03-26")

        # Выводим общий баланс
        with open(self.file_path, 'r', encoding='utf-8') as file:
            balance = show_balance(self.file_path)

        # Проверяем, что вывод корректен
        expected_balance = "Текущий баланс: 2500\nДоходы: 3000\nРасходы: 500"
        self.assertEqual(balance, expected_balance)

if __name__ == '__main__':
    unittest.main()