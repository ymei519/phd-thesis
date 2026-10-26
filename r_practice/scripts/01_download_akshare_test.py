import akshare as ak
import pandas as pd

print("正在从网络抓取中国的 PPI 和 CPI 数据，请稍等...")

# 获取 PPI 数据
try:
    ppi_df = ak.macro_china_ppi()
    print("\n=== PPI 数据抓取成功！前5行数据如下 ===")
    print(ppi_df.head())
    
    # 把它保存到咱们刚才建好的 data_raw 文件夹里
    ppi_df.to_csv("data_raw/china_ppi.csv", index=False)
    print("PPI 数据已保存到 data_raw/china_ppi.csv")

except Exception as e:
    print(f"\nPPI 抓取失败，错误信息: {e}")

# 获取 CPI 数据
try:
    cpi_df = ak.macro_china_cpi()
    print("\n=== CPI 数据抓取成功！前5行数据如下 ===")
    print(cpi_df.head())
    
    # 保存到 data_raw 文件夹
    cpi_df.to_csv("data_raw/china_cpi.csv", index=False)
    print("CPI 数据已保存到 data_raw/china_cpi.csv")

except Exception as e:
    print(f"\nCPI 抓取失败，错误信息: {e}")

print("\n程序运行结束！")