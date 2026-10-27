import akshare as ak
import pandas as pd

print("正在抓取并清洗数据...")

try:
    # 1. 抓取信贷数据（供给端）
    credit_df = ak.macro_china_new_financial_credit()
    credit_df = credit_df[['月份', '当月']].copy()
    credit_df.columns = ['Date', 'Credit']
    credit_df = credit_df.iloc[::-1].reset_index(drop=True)
    credit_df['Date'] = pd.to_datetime(credit_df['Date'].str.replace('月份', ''), format='%Y年%m')
    credit_df['Credit'] = pd.to_numeric(credit_df['Credit'], errors='coerce')
    
    # 保存信贷数据
    credit_df.to_csv("/Users/meiyani/Desktop/phd-thesis/r_practice/data_raw/real_credit_loan.csv", index=False)
    print("信贷数据已保存！")

    # 2. 抓取消费数据（需求端）
    consumption_df = ak.macro_china_consumer_goods_retail()
    consumption_df = consumption_df[['月份', '当月']].copy()
    consumption_df.columns = ['Date', 'Consumption']
    consumption_df = consumption_df.iloc[::-1].reset_index(drop=True)
    consumption_df['Date'] = pd.to_datetime(consumption_df['Date'].str.replace('月份', ''), format='%Y年%m')
    consumption_df['Consumption'] = pd.to_numeric(consumption_df['Consumption'], errors='coerce')
    
    # 保存消费数据
    consumption_df.to_csv("/Users/meiyani/Desktop/phd-thesis/r_practice/data_raw/real_consumption.csv", index=False)
    print("消费数据已保存！")

except Exception as e:
    print(f"抓取失败: {e}")