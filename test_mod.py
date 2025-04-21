import os
import pytest
from supabase import create_client, Client
import dotenv
import requests
import Supa
import Model
import datetime

dotenv.load_dotenv()
localhost = os.getenv("localhost")


@pytest.fixture
def test_supabase_client():
    url = os.getenv("project_url")
    key = os.getenv("api_key")
    supabase: Client = create_client(url, key)
    return supabase  



def test_supabase_client():
    connection = test_supabase_client
    assert connection is not None, "Failed to create Supabase Client"


    
def test_transaction_creation():
    getNumberOfTransactionsBefore = Supa.getNumberOfAllTransactions()
    tDate = datetime.date(2023, 10, 2).isoformat()
    pDate = datetime.date(2023, 10, 2).isoformat()
    transaction = Model.Transaction(
        transaction_date=tDate,
        post_date=pDate,
        amount=100.0,
        type="Sale",
        description="Test transaction",
        category="Test category",
        memo="Test memo",
    )
    
    TransObject = Supa.insertToSupa(transaction)
    print(TransObject)
    getNumberOfTransactionsAfter = Supa.getNumberOfAllTransactions()
    
    if getNumberOfTransactionsAfter > getNumberOfTransactionsBefore :
        assert True, "Transaction created successfully"

def test_get_transactions():
    transactions = Supa.getAllTransactions()
    if len(transactions) > 0:
        assert True, "Transactions retrieved"
    else:
        assert False, "Transactions Not Retrieved"


def test_get_transactions_by_category():
    transaction1 = Supa.getTransactionsByCategory("Entertainment")
    transaction2 = Supa.getTransactionsByCategory("entertainment")
    if len(transaction1) > 0 and len(transaction2) <= 0:
        assert True
    else:
        assert False
