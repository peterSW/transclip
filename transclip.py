#!/usr/bin/env python
r"""
transclip takes text and gives you a trasaction object.
The intention is to allow copying and pasteing from an online bank service
or pdf statment and getting an output for easy processing of the transaction.

For example:

>>> transclip("03/12/2013 \tPayPal PAYPAL WITHDRAWAL \t\t0.01 \t86.49 \t").date
'03/12/2013'

>>> transclip("03/12/2013 \tPayPal PAYPAL WITHDRAWAL \t\t0.01 \t86.49 \t").description
'PayPal PAYPAL WITHDRAWAL'

"""

class Transaction:
    def __init__(self, string):
        
        self.separator = '\t'
        self.remain = string
        
        self.date = self.process_field()
        self.description = self.process_field()
        self.debit = self.process_field()
        self.credit = self.process_field()
        self.balance = self.process_field()
        
    def process_field(self):
        
        field,sep,self.remain = self.remain.partition(self.separator)
        field = field.strip()
        return field

def transclip(string):
    return Transaction(string)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

