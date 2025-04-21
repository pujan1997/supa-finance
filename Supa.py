from fastapi import FastAPI
from supabase import AuthApiError, create_client, Client, ClientOptions
import os
import json
import dotenv


dotenv.load_dotenv()
supaBase_url = os.getenv("project_url")
api_key = os.getenv("api_key")



supabase: Client = create_client(supaBase_url, api_key, options=ClientOptions(
    schema="public"
))


#Test connection
def test_connection():
    try:
        client = supabase.create_client(supaBase_url, api_key)
        print("Supabase connection successful.")
        return client
    except Exception as e:
        print(f"Error connecting to Supabase: {e}")
        return None




    
#Get One transaction by ID
def getOneTransactions(id=None):
    try:
        response = supabase.table("transaction").select("*").eq("id", id).execute()
        transactions = response.data
        return transactions
    except Exception as e:
        print(error_message(e))
        return None
    
    
    
#Get a list of all transactions
def getAllTransactions():
    try:
        response = supabase.table("transaction").select("*").execute()
        transactions = response.data
        return transactions
    except Exception as e:
        print(error_message(e))
        return None
    
    


#Get All the transactions by sales    
def getListOfAllSales():
    try:
        response = supabase.table("transaction").select("*").eq("type", "Sale").execute()
        transactions = response.data
        return transactions
    except Exception as e:
        print(error_message(e))
        return None
    
#Gets all the list of payments
def getListOfAllPayments():
    try:
        response = supabase.table("transaction").select("*").eq("type", "Payment").execute()
        transactions = response.data
        return transactions
    except Exception as e:
        print(error_message(e))
        return None



#Gets all of the sum of payments
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


#Gets the sum of all the sales
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

#Creates a new transaction
def insertToSupa(t):
        print(t)
        tDate = t.transaction_date.isoformat()
        pDate = t.post_date.isoformat()
        desc = t.description
        cate = t.category
        tType = t.type 
        amt = t.amount
        memo = t.memo

        try:
            response = (supabase.table("transaction").insert(
                    {"transcation_date": tDate, "post_date": pDate, "description": desc, "category": cate, "type": tType, "amount": amt, "memo": memo})
                    .execute()
                )
            print(response)
        except AuthApiError as e:
            print(f"APIError: {e}")   


def getNumberOfAllTransactions():
    try:
        response = supabase.table("transaction").select("*").execute()
        data = response.data
        num_transactions = len(data)
        if num_transactions > 0 :
            return num_transactions
        else:
            return 0
    except Exception as e:
        print(error_message(e))
        return None

def deleteTransaction(id=None):
    try:
        response = supabase.table("transaction").delete().eq("id", id).execute()
        return response.data
    except Exception as e:
        print(error_message(e))
        return None



def getTransactionsByCategory(category=None):
    try:
        response = supabase.table("transaction").select("*").eq("category",category).execute()
        transactions = response.data
        return transactions
    except Exception as e:
        print(error_message(e))
        return None

def error_message(error):
    return print(f"Error retrieving transactions:{error})")