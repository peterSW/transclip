#!/usr/bin/env python

import unittest

from transclip import transclip
from transactions import Transaction
from transactions import TransactionFormat

class TestSingleTransaction(unittest.TestCase):
    def setUp(self):
        self.transaction1 = Transaction(date = "03/12/2013",
                                        description="PayPal PAYPAL WITHDRAWAL",
                                        debit=0.01,
                                        balance=87.49)
        self.transaction2 = Transaction(date = "02/12/2013",
                                        description="Cash deposit",
                                        credit=1.01,
                                        balance=87.50)
        formater = TransactionFormat(
              separator = '\t',
              field_order = ["date", "description", "credit", "debit", "balance"],
              field_postfix = ' ',
              transaction_postfix = '\t')
        
        self.text = formater.output(self.transaction1)
        
        
    def test_extract_transaction(self):
        result = transclip(self.text)
        self.assertEqual(
             self.transaction1,
             result,
             ("expected:\n", str(self.transaction1), "got:\n", str(result)))
    def test_extract_date(self):
        self.assertEqual(self.transaction1.date, transclip(self.text).date)
        
    def test_extract_description(self):
        self.assertEqual(self.transaction1.description, transclip(self.text).description)
        
    def test_extract_debit(self):
        self.assertEqual(self.transaction1.debit, transclip(self.text).debit)
        
    def test_extract_credit(self):
        self.assertEqual(self.transaction1.credit, transclip(self.text).credit)
        
    def test_extract_balance(self):
        self.assertEqual(self.transaction1.balance, transclip(self.text).balance)

if __name__ == '__main__':
    unittest.main()

