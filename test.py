"""
Тесты по реализованным функциям.

"""

import unittest
from functions import encryption_caesar, decryption_caesar


class TestEncryption(unittest.TestCase):
    def test_1(self):
        self.assertEqual(encryption_caesar("бульдог", 4), 'ечпѐитз')

    def test_2(self):
        self.assertEqual(encryption_caesar("Bulldog", 10), 'Lvvnyq')

    def test_3(self):
        self.assertEqual(encryption_caesar("Первый - First", 9), 'Шощлєт)6)Or{|}')


class TestDecryption(unittest.TestCase):
    def test_1(self):
        self.assertEqual(decryption_caesar('ечпѐитз', 4), 'бульдог')

    def test_2(self):
        self.assertEqual(decryption_caesar('Lvvnyq', 10), "Bulldog")

    def test_3(self):
        self.assertEqual(decryption_caesar('Шощлєт)6)Or{|}', 9), "Первый - First")




