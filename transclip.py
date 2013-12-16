#!/usr/bin/env python
from transactions import format1


def transclip(string):
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
    return format1.text_to_transaction(string)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

