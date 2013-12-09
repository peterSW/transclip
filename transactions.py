#!/usr/bin/env python

class Transaction:
    """
    Transaction holds the details of a single transaction
    
    >>> aTransaction = Transaction(date = "12/12/2013", description = "A transaction", credit = 1.10)
    >>> aTransaction.date
    '12/12/2013'
    """

    def __init__(self, date, description, credit=None, debit=None, balance=None):
        self.data = {
             'date' : date, 
             'description' : description,
             'credit' : credit,
             'debit' : debit,
             'balance' : balance} 
        
        self.date = date
        self.description = description
        self.credit = credit
        self.debit = debit
        self.balance = balance

    def __eq__(self, other):
        """
        Tranactions can be compared.
        >>> Transaction(date = "03/12/2013", description = "A transaction", credit = 1.10) == Transaction(date = "03/12/2013", description = "A transaction", credit = 1.10)
        True
        >>> Transaction(date = "03/12/2013", description = "", credit = 1.10) == Transaction(date = "03/12/2013", description = "A transaction", credit = 1.10)
        False
        """
        return self.__dict__ == other.__dict__

class Format:
    r"""
    >>> aTransaction = Transaction(date = "03/12/2013", description = "A transaction", credit = 1.10)
    >>> Format(separator = '\t', fieldOrder = ['date', 'description', 'credit', 'debit', 'balance'], fieldPostfix = ' ', transactionPostfix = '\t').output(aTransaction)
    '03/12/2013 \tA transaction \t1.10 \t\t\t'
    """
    
    def __init__(self, separator, fieldOrder, fieldPostfix = '', transactionPostfix = ''):
        self.separator = separator
        self.fieldOrder = fieldOrder
        self.fieldPostfix = fieldPostfix
        self.transactionPostfix = transactionPostfix

    def output(self, transaction):
        result = self._expandField(transaction.data[self.fieldOrder[0]])
        for fieldName in self.fieldOrder[1:]:
            result += self.separator
            result += self._expandField(transaction.data[fieldName])
        result += self.transactionPostfix
        return result

    def _expandField(self, field):
        result = ''
        if field:
            if isinstance(field, str):
                result += field
            else:
                result += "{0:.2f}".format(field)

            result += self.fieldPostfix
        return result
    
    def input(self, text):
        newTransaction = Transaction()
        for field in self.fieldOrder:
            newTransaction.data[field],sep,text = text.partition(self.separator)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
