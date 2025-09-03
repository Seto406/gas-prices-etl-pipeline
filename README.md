# gas-prices-etl-pipeline
A Python ETL pipeline that extracts weekly US gas prices from the EIA API, transforms the data with Pandas, and loads it into a SQLite database.
# US Weekly Gas Prices ETL Pipeline ⛽

A simple ETL (Extract, Transform, Load) pipeline built with Python that collects weekly retail gasoline price data from the U.S. Energy Information Administration (EIA) API, cleans it, and stores it in a SQLite database.

This project was built as a foundational data engineering portfolio piece to demonstrate core skills in data extraction, processing, and storage.

---

## Features

* **Extract:** Fetches data directly from the public EIA REST API.
* **Transform:** Uses the Pandas library to clean the raw data by:
    * Selecting relevant columns.
    * Renaming columns for clarity.
    * Converting data types for dates and prices.
* **Load:** Loads the cleaned data into a local SQLite database, appending new data with each run to build a historical record.

---

## Tech Stack

* **Language:** Python
* **Libraries:**
    * Pandas (for data transformation)
    * Requests (for API communication)
    * SQLite3 (for database interaction)

---

## How to Run This Project

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/gas-prices-etl-pipeline.git](https://github.com/your-username/gas-prices-etl-pipeline.git)
    cd gas-prices-etl-pipeline
    ```

2.  **Install dependencies:**
    *(It's a best practice to use a virtual environment)*
    ```bash
    pip install -r requirements.txt
    ```

3.  **Get an API Key:**
    You will need a free API key from the [EIA website](https://www.eia.gov/opendata/register.php).

4.  **Update the script:**
    Open `pipeline.py` and replace `"YOUR_API_KEY_HERE"` with the key you received.

5.  **Run the pipeline:**
    ```bash
    python pipeline.py
    ```
    After running, a `gas_prices.db` file will be created in the project folder with the clean data.
