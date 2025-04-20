from fastapi import FastAPI
from supabase import create_client, Client, ClientOptions
import os
import dotenv


dotenv.load_dotenv()
supaBase_url = os.getenv("project_url")
api_key = os.getenv("api_key")



supabase: Client = create_client(supaBase_url, api_key, options=ClientOptions(
    schema="public"
))

def test_connection():
    try:
        client = supabase.create_client(supaBase_url, api_key)
        print("Supabase connection successful.")
        return client
    except Exception as e:
        print(f"Error connecting to Supabase: {e}")
        return None

def getOneTransactions(id=None):
    try:
        response = supabase.table("transaction").select("*").eq("id", id).execute()
        transactions = response.data
        return transactions
    except Exception as e:
        print(error_message(e))
        return None
    
def getListOfAllSales():
    try:
        response = supabase.table("transaction").select("*").eq("type", "Sale").execute()
        transactions = response.data
        return transactions
    except Exception as e:
        print(error_message(e))
        return None
    

def getListOfAllPayments():
    try:
        response = supabase.table("transaction").select("*").eq("type", "Payment").execute()
        transactions = response.data
        return transactions
    except Exception as e:
        print(error_message(e))
        return None


def getSumOfAllPayments():
    try:
        response = supabase.table("transaction").select("*").eq("type", "Payment").execute();
        payments = response.data
        sum = 0
        for p in payments:
            sum += p["amount"]
        return ["Sum of all Payments: ", sum]
    except Exception as e:
        print(error_message(e))
        return None



def getSumOfAllSales():
    try:
        response = supabase.table("transaction").select("*").eq("type", "Sale").execute();
        sales = response.data
        sum = 0
        for s in sales:
            sum += s["amount"]
        return ["Sum of all Sale: ", sum]
    except Exception as e:
        print(error_message(e))
        return None




def error_message(error):
    return print(f"Error retrieving transactions:{error})")