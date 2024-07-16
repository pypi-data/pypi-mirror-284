# xbrlapi/api.py
from supabase import create_client, Client

# Base URL for the Supabase database
BASE_URL = "https://ctegcahvqfnbhudovzpy.supabase.co"

# Global variable to store the API key and Supabase client
API_KEY = None
supabase: Client = None

def set_api_key(api_key):
    """
    Set the API key and initialize the Supabase client.

    Args:
        api_key (str): The API key provided by the user.
    """
    global API_KEY, supabase
    API_KEY = api_key
    supabase = create_client(BASE_URL, API_KEY)

def get_data(ticker, year, data_type):
    """
    Fetch financial data for a given ticker, year, and data type from Supabase.

    Args:
        ticker (str): The stock ticker symbol.
        year (str): The year for which data is requested.
        data_type (str): The type of financial data requested.

    Returns:
        list: The financial data in JSON format.

    Raises:
        ValueError: If the API key is not set.
    """
    if API_KEY is None:
        raise ValueError("API key is not set. Use set_api_key() to set it.")
    
    # Example query (adjust according to your table structure)
    response = supabase.table("xbrl_data").select("*").eq("name", ticker).eq("ddate", year).eq("tag", data_type).execute()
    return response.data
