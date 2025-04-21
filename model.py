from pydantic import BaseModel
import datetime

class TransactionCSV:
   def __init__(self, dictionary):
       for key,value in dictionary.items():
              # Check if the value is a list or dictionary
        if key == 'transaction_date':
            key = 'TransactionDate'
        if key == 'Post Date':
            key = 'PostDate'    
        setattr(self, key, value)

class Transaction(BaseModel):
    transaction_date: datetime.date
    post_date: datetime.date
    amount: float
    type: str
    description: str = None
    category: str = None
    memo: str = None
     
    class Config:
        orm_mode = True  # Enable ORM mode to allow Pydantic to work with ORM models directly
