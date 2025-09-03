import requests
import pandas as pd
import sqlite3


def extract_data(url):
    """
    This function takes a URL, sends a GET request to it,
    and returns the JSON data if the request is successful.
    """
    # FIX: Corrected typo in the print statement
    print("-> Starting data extraction...")
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("-> Data extraction successful!")
        return response.json()
    # FIX: Corrected the exception name
    except requests.exceptions.RequestException as e:
        print(f"Error during data extraction: {e}")
        return None


def transform_data(raw_data):
    """
    This function takes the raw JSON data, cleans and transforms it
    using pandas, and returns a clean DataFrame.
    """
    print("-> Starting data transformation...")
    if raw_data is None:
        print("-> No data to transform.")
        return None

    price_data = raw_data.get('response', {}).get('data', [])

    # FIX: Added the missing line to create the DataFrame
    df = pd.DataFrame(price_data)

    # --- Data Cleaning Steps ---
    # 1. Select only the columns we need
    df = df[['period', 'value']]

    # 2. Rename columns to be more descriptive
    df = df.rename(columns={'period': 'date', 'value': 'price_usd_per_gallon'})

    # 3. Convert the 'date' column to a proper datetime format
    df['date'] = pd.to_datetime(df['date'])

    # 4. Convert the 'price' column to a numeric format (float)
    df['price_usd_per_gallon'] = pd.to_numeric(df['price_usd_per_gallon'])

    print("-> Data transformation successful!")
    return df


def load_data(clean_df, db_name="gas_prices.db", table_name="weekly_prices"):
    """
    This function takes a clean DataFrame and loads it into a
    SQLite database table.
    """
    print("-> Starting data loading...")
    if clean_df is None:
        print("-> No data to load.")
        return

    try:
        conn = sqlite3.connect(db_name)
        clean_df.to_sql(table_name, conn, if_exists='append', index=False)
        print(f"-> Data loaded successfully into '{table_name}' in '{db_name}'!")
        conn.close()
    except Exception as e:
        print(f"Error during data loading: {e}")


if __name__ == "__main__":
    # --- UPDATE THIS SECTION ---

    # Your API key (no changes here)
    api_key = "WAoIP2J5wcBqR6bXUenH3YcZtmEdT80LPTzyXDZF" # Replace with your key again

    # FIX: Switched to the more modern and reliable v2 API endpoint
    series_id = "PET.EMM_EPM0_PTE_NUS_DPG.W"
    API_URL = f"https://api.eia.gov/v2/seriesid/{series_id}?api_key={api_key}"

    # --- NO CHANGES NEEDED BELOW THIS LINE ---

    # 1. Extract
    raw_json_data = extract_data(API_URL)

    # 2. Transform
    clean_dataframe = transform_data(raw_json_data)

    # 3. Load
    if clean_dataframe is not None and not clean_dataframe.empty:
        load_data(clean_dataframe)
    else:
        print("Pipeline finished, but no new data was processed.")