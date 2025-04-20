from dotenv import load_dotenv
import os
from supabase import AuthApiError, create_client, Client , ClientOptions
import pandas as pd
import model
import itertools

load_dotenv()


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


def load_csv():
    try:
        df = pd.read_csv("chase_data.csv")
        print("CSV loaded successfully.")
        return df
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return None





def dataframe_to_Object():
    df = load_csv()
    df.fillna('', inplace=True)  # Fill NaN values with empty strings
    data_object = df.to_dict(orient='records')
    print(data_object)
    transactions = []
   
    for record in data_object:
        # transactions.append(model.Transaction(
        #     transaction_date = record['transaction_date'],
        #     post_date = record['Post Date'],
        #     description = record['Description'],
        #     category = record['Category'],
        #     tType = record['Type'],
        #     amount = record['Amount'],
        #     memo = record['Memo']
        # ))
        transaction = model.Transaction(record)
        transactions.append(transaction)
   
    return transactions   
        

def insertIntoSupaBase():
    transactions = dataframe_to_Object()
    
    for t in transactions:
       insertToSupa(t)

        
        
def insertToSupa(t):
        transactionDate = t.TransactionDate
        postDate = t.PostDate
        description = t.Description
        category = t.Category
        tType = t.Type
        amount = t.Amount
        memo = t.Memo
        try:
            response = (supabase.table("transaction").insert(
                    {"transcation_date": transactionDate, "post_date": postDate, "description": description, "category": category, "type": tType, "amount": amount, "memo": memo})
                    .execute()
                )
        except AuthApiError as e:
            print(f"APIError: {e}")    
        
insertIntoSupaBase()

