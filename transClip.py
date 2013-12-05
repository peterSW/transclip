#!/usr/bin/python
r"""
transClip takes text and gives you a trasaction object.
The intention is to allow copying and pasteing from an online bank service
or statment pdf and getting an output for easy processing of the transaction.

For example:

>>> transClip("03/12/2013 \tPayPal PAYPAL WITHDRAWAL \t\t0.01 \t86.49 \t").date
'03/12/2013'

>>> transClip("03/12/2013 \tPayPal PAYPAL WITHDRAWAL \t\t0.01 \t86.49 \t").description
'PayPal PAYPAL WITHDRAWAL'

"""

class Transaction:
    def __init__(self, string):
        self.date,sep,remain = string.partition('\t')
        self.date = self.date.strip()
        self.description,sep,remain = remain.partition('\t')
        self.description = self.description.strip()
        

def transClip(string):
    return Transaction(string)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
