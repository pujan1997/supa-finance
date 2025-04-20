class Transaction:
   def __init__(self, dictionary):
       for key,value in dictionary.items():
              # Check if the value is a list or dictionary
        if key == 'transaction_date':
            key = 'TransactionDate'
        if key == 'Post Date':
            key = 'PostDate'    
        setattr(self, key, value)


