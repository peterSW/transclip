#!/usr/bin/env python

class Transaction:
    """
    Transaction holds the details of a single transaction
    
    >>> aTransaction = Transaction(date = "12/12/2013", description = "A transaction", credit = 1.10)
    >>> aTransaction.get('date')
    '12/12/2013'
    """

    data_types = {
           'date' : str,
           'description' : str,
           'credit' : float,
           'debit' : float,
           'balance' : float}

    def __init__(self, date=None, description=None, credit=None, debit=None, balance=None):
        self.data = {}
        self.set('date', date)
        self.set('description', description)
        self.set('credit', credit)
        self.set('debit', debit)
        self.set('balance', balance)

    def set(self, name, value):
        if value is not None:
            v = self.data_types[name](value)
        else:
            v = None
        setattr(self, name, v)
        self.data[name] = v
        
    def get(self, name):
        return self.data[name]

    def __eq__(self, other):
        """
        Tranactions can be compared.
        >>> Transaction(date = "03/12/2013", description = "A transaction", credit = 1.10) == Transaction(date = "03/12/2013", description = "A transaction", credit = 1.10)
        True
        >>> Transaction(date = "03/12/2013", description = "", credit = 1.10) == Transaction(date = "03/12/2013", description = "A transaction", credit = 1.10)
        False
        """
        return self.__dict__ == other.__dict__
    
    def __str__(self):
        return str(self.data)


class FieldFormat:
    """ A FieldFormat defines how a field is converted to and from text.
    
    For example:
    >>> floatField = FieldFormat(value_type = float, formater = "{0:.2f}")
    >>> floatField.parse("10.10").value
    10.1
    >>> floatField.output()
    '10.10'
    """
    
    def __init__(self, value_type = str, formater = None):
        self.type = value_type
        self.formater = formater
    
    def parse(self, text):
        self.value = self.type(text)
        return self
    
    def output(self):
        if self.formater is None:
            str(self.value)
        else:
            return self.formater.format(self.value)
string_format = FieldFormat()

class TransactionFormat:
    r"""
    >>> aTransaction = Transaction(date = "03/12/2013", description = "A transaction", credit = 1.10)
    >>> TransactionFormat(separator = '\t', field_order = ['date', 'description', 'credit', 'debit', 'balance'], field_postfix = ' ', transaction_postfix = '\t').output(aTransaction)
    '03/12/2013 \tA transaction \t1.10 \t\t\t'
    """
    
    def __init__(self, separator, field_order, field_postfix = '', transaction_postfix = ''):
        self.separator = separator
        self.field_order = field_order
        self.field_postfix = field_postfix
        self.transaction_postfix = transaction_postfix

    def output(self, transaction):
        expanded_fields = [
               self._expandField(transaction.data[field_name])
               for field_name in self.field_order]
        
        result = self.separator.join(expanded_fields)
        return ''.join((result, self.transaction_postfix))

    def _expandField(self, field):
        if field is not None:
            return ''.join(
                   (field if isinstance(field, str) else "{0:.2f}".format(field),
                    self.field_postfix))
        else:
            return ''
    
    def text_to_transaction(self, text):
        if text.endswith(self.transaction_postfix):
            text = text[:-len(self.transaction_postfix)]
        else: raise ValueError("Expected transaction postfix not found.")
        
        transaction = Transaction()
        
        field_strings = text.split(self.separator)
        for field_name, field_string in zip(self.field_order, field_strings):
            if(field_string.endswith(self.field_postfix)):
                field_string = field_string[:-len(self.field_postfix)]
            transaction.set(field_name, 
                            None if field_string == '' else field_string)
            
        return transaction

format1 = TransactionFormat(
         separator = '\t',
         field_order = ['date', 'description', 'credit', 'debit', 'balance'],
         field_postfix = ' ',
         transaction_postfix = '\t')

if __name__ == "__main__":
    import doctest
    doctest.testmod()
