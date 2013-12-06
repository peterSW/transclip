#!/usr/bin/env python

import unittest

from transclip import transclip

class TestSingleTransaction(unittest.TestCase):
    def setUp(self):
        self.text = """03/12/2013 	PayPal PAYPAL WITHDRAWAL 		0.01 	86.49 	"""
        
    def test_extract_date(self):
        self.assertEqual("03/12/2013", transclip(self.text).date)
        
    def test_extract_description(self):
        self.assertEqual("PayPal PAYPAL WITHDRAWAL", transclip(self.text).description)
        
    def test_extract_debit(self):
        self.assertEqual("", transclip(self.text).debit)
        
    def test_extract_credit(self):
        self.assertEqual("0.01", transclip(self.text).credit)
        
    def test_extract_balance(self):
        self.assertEqual("86.49", transclip(self.text).balance)

if __name__ == '__main__':
    unittest.main()

