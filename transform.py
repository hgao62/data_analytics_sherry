import pandas as pd

from model import StockPrice
from read_data import get_stock_data

'''
    note:
    .pct_change():百分比变化率
    .pct_change=(Xt-Xt-1)/Xt-1

    .cumprod() :累积连乘(CUMulative PRODuct)
    .cumprod=X1*X2*X3...*Xt

    有涨有跌时：
    累计回报是整体趋势，不被中间的涨跌所误导。
    逐日连乘法(累积连乘)可以记录每一步变化，适合分析策略、画图、分析风险。

'''
'''
create add_stock_returns(df: pd.DataFrame) -> pd.DataFrame function 
so it takes the data loaded from get_stock_data above 
and add daily_return column and cumulative_return column
'''
def add_stock_returns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.sort_values(by=StockPrice.DATE).copy()
    df['daily_return'] = df['Close'].pct_change()
    df['cumulative_return'] = (1 + df['daily_return']).cumprod() - 1

    return df

# test
# df=get_stock_data("meta", "2024-01-02", "2024-01-10")
# df = add_stock_returns(df)



'''
Notes:
.mean() 是 Pandas 中的函数，用来计算平均值（mean / arithmetic average）。
.rolling(window=3).mean()：就是计算滑动窗口平均。第一个widonw是rolling的parameter name
第3天的平均 = (第1天收盘价 + 第2天收盘价 + 第3天收盘价) / 3
'''

'''
create calculate_moving_average(df: pd.DataFrame, window: int) -> pd.DataFrame 
function so it calculate the moving average of stock close price based 
on the window parameter
'''
def calculate_moving_average(df: pd.DataFrame, window: int) -> pd.DataFrame:
    df = df.sort_values(by=StockPrice.DATE).copy()
    df[f'moving_average_{window}'] = df['Close'].rolling(window=window).mean()
    return df


# test
# df=calculate_moving_average(df,5)


'''
.std() 是 Pandas 里计算**标准差（standard deviation）**的函数。
'''

'''
    波动率（Volatility）通常就是一段时间内每日收益率（daily return）的标准差。
'''
def add_stock_volatility(df: pd.DataFrame, window: int) -> pd.DataFrame:
    df = df.sort_values(by=StockPrice.DATE).copy()
    df[f'volatility_{window}'] = df['daily_return'].rolling(window=window).std()
    return df

# test
# df = add_stock_volatility(df, window=5)
# print(df)
