#!/usr/bin/env python

import unittest

from transclip import transclip
from transactions import Transaction
from transactions import Format

class TestSingleTransaction(unittest.TestCase):
    def setUp(self):
        self.transaction1 = Transaction(date = "03/12/2013",
                                        description="PayPal PAYPAL WITHDRAWAL ",
                                        debit=0.01,
                                        balance=87.49)
        self.transaction2 = Transaction(date = "02/12/2013",
                                        description="Cash deposit ",
                                        credit=1.01,
                                        balance=87.50)
        formater = Format(
              separator = '\t',
              fieldOrder = ["date", "description", "credit", "debit", "balance"],
              fieldPostfix = ' ',
              transactionPostfix = '\t')
        
        self.text = formater.output(self.transaction1) + "\n" + formater.output(self.transaction2)
        
        
    def test_extract_transaction(self):
        result = transclip(self.text)
        self.assertEqual(self.transaction1, result, self.transaction1)
    def test_extract_date(self):
        self.assertEqual("03/12/2013", transclip(self.text).date)
        
    def test_extract_description(self):
        self.assertEqual("PayPal PAYPAL WITHDRAWAL", transclip(self.text).description)
        
    def test_extract_debit(self):
        self.assertEqual("", transclip(self.text).debit)
        
    def test_extract_credit(self):
        self.assertEqual("0.01", transclip(self.text).credit)
        
    def test_extract_balance(self):
        self.assertEqual(self.transaction1.balance, transclip(self.text).balance)

if __name__ == '__main__':
    unittest.main()

