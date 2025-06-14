from pathlib import Path
import pandas as pd
from model import StockPrice

PROJECT_FOLDER = Path(__file__).parent #也就是 read data.py 所在的文件夹
#print(PROJECT_FOLDER) #output: c:\Users\Administrator\Desktop\python program\data_analytics_sherry
DATA_FOLDER = PROJECT_FOLDER.joinpath('data')

#Task 1: Read the stock data from a CSV file and filter it by stock name(make sure stock name is insensitive) and 
# date range.
# The function get_stock_data takes a stock name, start date, and end date as input parameters.
# It reads the stock data from a CSV file, filters it by the specified stock name and date range,
# and returns the filtered data as a pandas DataFrame.

def get_stock_data(stock_name: str, start_date:str, end_date:str) -> pd.DataFrame:
    """
    Retrieves stock data for a specific stock within a given date range.

    This function reads stock data from a CSV file, filters it by the specified stock name
    and date range, and returns the filtered data as a pandas DataFrame.

    Args:
        stock_name (str): The name of the stock to filter.
        start_date (str): The start date of the range in 'YYYY-MM-DD' format.
        end_date (str): The end date of the range in 'YYYY-MM-DD' format.

    Returns:
        pd.DataFrame: A DataFrame containing the filtered stock data with columns such as
                      'Date', 'Stock', and other stock-related metrics.

    """
    stock_data_path = DATA_FOLDER.joinpath('stock_data.csv')
    df = pd.read_csv(stock_data_path)
    df[StockPrice.DATE] = pd.to_datetime(df[StockPrice.DATE])
    mask = (df[StockPrice.DATE] >= start_date) & (df[StockPrice.DATE] <= end_date) & (df[StockPrice.TICKER].str.lower() == stock_name.lower()) 
    filtered_df = df.loc[mask]  

    return filtered_df  

'''
Notes:
    为什么不直接写成df[]而是要加mask和df.loc?直接查gpt,虽然没有看懂
    df_filtered = df[(df[StockPrice.DATE] >= start_date) & (df[StockPrice.DATE] <= end_date) & (df[StockPrice.TICKER].str.lower() == stock_name.lower()) ]
    
'''
    
def get_sector_data() -> pd.DataFrame:
    """
    Retrieves sector data from a CSV file.

    This function reads sector data from a CSV file and returns it as a pandas DataFrame.

    Returns:
        pd.DataFrame: A DataFrame containing the sector data with columns such as
                      'Ticker', 'Sector', and 'Industry'.

    """
    sector_data_path = DATA_FOLDER.joinpath('sector_info.csv')
    df = pd.read_csv(sector_data_path)
    return df

 #  test function
df_filtered = get_stock_data("a", "2023-12-20", "2023-12-29")
print("\nFiltered Rows:\n", df_filtered)


#  test function
df_selected = get_sector_data()
print("\nSelected Columns:\n", df_selected)


