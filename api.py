
from fastapi import FastAPI
import Supa

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/transactions")
def read_transactions():
    transactions = Supa.getAllTransactions()
    if transactions:
        return {"transactions": transactions}
    else:
        return {"error": "No transactions found."}
    

@app.get("/transactions/sales")
def read_transactions():
    transactions = Supa.getListOfAllSales()
    if transactions:
        return {"transactions": transactions}
    else:
        return {"error": "No transactions found."}
    
@app.get("/transactions/payments")
def read_transactions():
    transactions = Supa.getListOfAllPayments()
    if transactions:
        return {"transactions": transactions}
    else:
        return {"error": "No transactions found."}   
    
@app.get("/transactions/payments/sum")
def read_transactions():
    transactions = Supa.getSumOfAllPayments()
    if transactions:
        return {"Totals": transactions}
    else:
        return {"error": "No transactions found."}   
    
@app.get("/transactions/sales/sum")
def read_transactions():
    transactions = Supa.getSumOfAllSales()
    if transactions:
        return {"Totals": transactions}
    else:
        return {"error": "No transactions found."}   
    


    
    

@app.get("/transactions/{transaction_id}")
def read_transactions(transaction_id: int):
    transactions = Supa.getOneTransactions(transaction_id)
    if transactions:
        return {"transactions": transactions}
    else:
        return {"error": "No transactions found."}
    
    


    
    
    