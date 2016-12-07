# -*- coding: <UTF-8> -*-
import unittest
from cashmachine import cashMachine

class TestCashMachine(unittest.TestCase):
    def test_CashMachine(self):
        notes = [100.0 , 50.0 , 20.0 , 10.0]
        self.assertEqual(cashMachine(180, notes), [100.0,50.0,20.0,10.0])
        self.assertEqual(cashMachine(30, notes), [20.0,10.0])
        self.assertEqual(cashMachine(200, notes), [100.0,100.0])
        self.assertEqual(cashMachine(10, notes), [10.0])
        self.assertEqual(cashMachine(20, notes), [20.0])
        self.assertEqual(cashMachine(50, notes), [50.0])
        self.assertEqual(cashMachine(100, notes), [100.0])
        self.assertEqual(cashMachine(190, notes), [100.0,50.0,20.0,20.0])
        self.assertEqual(cashMachine(0, notes), [])

if __name__ == '__main__':
    unittest.main()
