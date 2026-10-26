import pandas as pd
import matplotlib.pyplot as plt

print("正在生成中英文两张图表...")

# ==========================================
# 1. 读取数据
# ==========================================
df = pd.read_csv("data_clean/china_gap.csv")
df['Date'] = pd.to_datetime(df['Date'].str.replace('月份', ''), format='%Y年%m')

# ==========================================
# 2. 生成中文图 (保存为 gap_chart_cn.png)
# ==========================================
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Songti SC'] # 解决中文乱码
plt.figure(figsize=(12, 6))

plt.plot(df['Date'], df['PPI'], label='PPI (工业生产者出厂价格)', color='blue', linewidth=2)
plt.plot(df['Date'], df['CPI'], label='CPI (居民消费价格)', color='red', linewidth=2)
plt.fill_between(df['Date'], df['PPI'], df['CPI'], where=(df['PPI'] >= df['CPI']), color='lightblue', alpha=0.5, label='Gap (供强需弱)')
plt.fill_between(df['Date'], df['PPI'], df['CPI'], where=(df['PPI'] < df['CPI']), color='lightcoral', alpha=0.5)

plt.xlabel('年份', fontsize=12)
plt.ylabel('指数 (当月同比)', fontsize=12)
plt.axhline(100, color='gray', linestyle='--', linewidth=1)
plt.legend(loc='upper left', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)

plt.savefig('output/gap_chart_cn.png', dpi=300, bbox_inches='tight')
plt.close() # 关闭当前画布，准备画下一张


# ==========================================
# 3. 生成英文图 (保存为 gap_chart_en.png)
# ==========================================
plt.figure(figsize=(12, 6)) # 重新开一张画布

plt.plot(df['Date'], df['PPI'], label='PPI (Producer Price Index)', color='blue', linewidth=2)
plt.plot(df['Date'], df['CPI'], label='CPI (Consumer Price Index)', color='red', linewidth=2)
plt.fill_between(df['Date'], df['PPI'], df['CPI'], where=(df['PPI'] >= df['CPI']), color='lightblue', alpha=0.5, label='Gap (PPI > CPI)')
plt.fill_between(df['Date'], df['PPI'], df['CPI'], where=(df['PPI'] < df['CPI']), color='lightcoral', alpha=0.5)

plt.xlabel('Year', fontsize=12)
plt.ylabel('Index (Year-on-Year Growth)', fontsize=12)
plt.axhline(100, color='gray', linestyle='--', linewidth=1)
plt.legend(loc='upper left', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)

plt.savefig('output/gap_chart_en.png', dpi=300, bbox_inches='tight')
plt.close()

print("\n大功告成！两张图均已保存至 output 文件夹。")