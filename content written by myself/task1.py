from pathlib import Path
import pandas as pd


################################## stock_data ##################################
# 1.Create DataFrame

# 这种写法读取不到路劲：df = pd.read_csv(r'..\data\stock_data.csv')

# 获取 task1.py 所在目录
BASE_DIR = Path(__file__).parent

# 拼接 data 路径
STOCK_DATA_FILE = BASE_DIR.parent / 'data' / 'stock_data.csv'

# 读取数据
df = pd.read_csv(STOCK_DATA_FILE)

# 2. make stock_name case-insensitive

df['Ticker'] = df['Ticker'].str.upper()

df['Date'] = pd.to_datetime(df['Date'])

# test
print(df.head()) 
'''
    
    # Filters rows matching the given stock_name (case-insensitive) and the date range between start_date and end_date.

    sql:
    select * from table
        where table.Ticker=stock_name & date>=start_date & date<=end_date
'''

def get_stock_data(stock_name: str, start_date: str, end_date: str) -> pd.DataFrame:
    
    # make stock_name case-insensitive
    stock_name=stock_name.upper()

    df_filtered = df[
        (df['Ticker'] == stock_name) &
        (df['Date'] >= start_date) &
        (df['Date'] <= end_date)
    ]
    return df_filtered

#  test function
df_filtered = get_stock_data("a", "2023-12-20", "2023-12-29")
print("\nFiltered Rows:\n", df_filtered)



################################## sector_data ##################################

'''


get_sector_data() -> pd.DataFrame

    Located in: read_data.py
    Loads sector and industry information from sector_info.csv.
    Returns a DataFrame with columns such as Ticker, Sector, and Industry.


'''

# 1.Create DataFrame
# 拼接 data 路径
SECTOR_INFO_FILE = BASE_DIR.parent / 'data' / 'sector_info.csv'

# 读取数据
df_sector = pd.read_csv(SECTOR_INFO_FILE)

# test
print(df_sector.head()) 

def get_sector_data() -> pd.DataFrame:
    
    df_selected = df_sector[
        ['Ticker','Sector','Industry']
    ]
    return df_selected

#  test function
df_selected = get_sector_data()
print("\nSelected Columns:\n", df_selected)