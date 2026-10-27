import akshare as ak
import pandas as pd

# 1. 再次抓取消费数据
df = ak.macro_china_consumer_goods_retail()

# 2. 只取“月份”和“当月”
df = df[['月份', '当月']].copy()

# 3. 看看总共有多少行？
print(f"原始数据总共有 {len(df)} 行。")

# 4. 看看开头和结尾
print("\n=== 前 5 行（最新数据） ===")
print(df.head())
print("\n=== 后 5 行（最老数据） ===")
print(df.tail())

# 5. 找找看有没有奇怪的行（比如不是“xxxx年xx月份”的格式）
print("\n=== 格式可能不标准的行 ===")
for index, row in df.iterrows():
    date_str = str(row['月份'])
    if "月份" not in date_str or len(date_str) > 8: 
        print(f"第 {index} 行格式异常: {row['月份']}，数值: {row['当月']}")