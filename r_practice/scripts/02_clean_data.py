import pandas as pd

print("开始读取原始数据并计算 Gap...")

# 1. 读取刚才抓取的数据
# 注意：如果有编码问题，加上 encoding='utf-8'
cpi_df = pd.read_csv("data_raw/china_cpi.csv")
ppi_df = pd.read_csv("data_raw/china_ppi.csv")

# 2. 提取需要的列，并重命名（把中文变成英文，方便后续跑模型）
# 你的截图显示 CPI 的“全国-当月”在第2列，“月份”在第1列
cpi_clean = cpi_df[['月份', '全国-当月']].copy()
cpi_clean.columns = ['Date', 'CPI']

# PPI 的“当月”在第2列，“月份”在第1列
ppi_clean = ppi_df[['月份', '当月']].copy()
ppi_clean.columns = ['Date', 'PPI']

# 3. 把两个表按“月份”合并在一起
merged_df = pd.merge(cpi_clean, ppi_clean, on='Date', how='inner')

# 4. 计算咱们的核心指标 Gap (PPI - CPI)
merged_df['Gap'] = merged_df['PPI'] - merged_df['CPI']

# 5. 把月份按照从早到晚排序（方便看趋势）
merged_df = merged_df.sort_values('Date')

print("\n=== 清洗后的数据前 5 行 ===")
print(merged_df.head())

# 6. 保存到 data_clean 文件夹
merged_df.to_csv("data_clean/china_gap.csv", index=False)
print("\n成功！文件已保存至 data_clean/china_gap.csv")