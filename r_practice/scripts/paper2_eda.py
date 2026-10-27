import akshare as ak
import pandas as pd
import matplotlib.pyplot as plt

# 设置中文字体，解决图表乱码
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Songti SC']
plt.rcParams['axes.unicode_minus'] = False

print("正在抓取消费数据...")

try:
    # ==========================================
    # 1. 抓取并清洗消费数据（需求端）
    # ==========================================
    consumption_df = ak.macro_china_consumer_goods_retail()
    
    # 提取“月份”和“当月”数值
    consumption_df = consumption_df[['月份', '当月']].copy()
    consumption_df.columns = ['Date', 'Consumption']
    
    # 反转顺序（从早到晚），并将“2023年01月份”转为标准时间格式
    consumption_df = consumption_df.iloc[::-1].reset_index(drop=True)
    consumption_df['Date'] = pd.to_datetime(consumption_df['Date'].str.replace('月份', ''), format='%Y年%m')
    consumption_df['Consumption'] = pd.to_numeric(consumption_df['Consumption'], errors='coerce')
    
    # 顺便把清洗好的消费数据存到本地，方便以后直接用
    consumption_df.to_csv("/Users/meiyani/Desktop/phd-thesis/r_practice/data_raw/real_consumption.csv", index=False)
    print("消费数据抓取成功并已保存到本地！")

    # ==========================================
    # 2. 读取本地信贷数据（供给端）
    # ==========================================
    credit_df = pd.read_csv("/Users/meiyani/Desktop/phd-thesis/r_practice/data_raw/real_credit_loan.csv")
    credit_df['Date'] = pd.to_datetime(credit_df['Date'])
    print("信贷数据读取成功！")

    # ==========================================
    # 3. 合并数据并处理时间断线
    # ==========================================
    # 用 outer 合并，保留所有月份（解决断线问题）
    merged_df = pd.merge(credit_df, consumption_df, on='Date', how='outer')
    
    # 按日期排序
    merged_df = merged_df.sort_values('Date')
    
    # 强制按月对齐，并把缺失的值用前一个月的数据填补（ffill），保证线条连续
    merged_df = merged_df.set_index('Date').asfreq('MS').ffill().reset_index()

    # ==========================================
    # 4. 画双轴折线图
    # ==========================================
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # 左轴：信贷（供给）—— 红色实线
    color = 'tab:red'
    ax1.set_xlabel('年份', fontsize=12)
    ax1.set_ylabel('新增人民币贷款 (亿元)', color=color, fontsize=12)
    ax1.plot(merged_df['Date'], merged_df['Credit'], color=color, linewidth=1.5, label='信贷供给')
    ax1.tick_params(axis='y', labelcolor=color)

    # 右轴：消费（需求）—— 蓝色实线，加粗
    ax2 = ax1.twinx() 
    color = 'tab:blue'
    ax2.set_ylabel('社零总额当月 (亿元)', color=color, fontsize=12)
    ax2.plot(merged_df['Date'], merged_df['Consumption'], color=color, linewidth=2.5, label='消费需求')
    ax2.tick_params(axis='y', labelcolor=color)

    plt.title('中国信贷供给与居民消费需求的长期对比', fontsize=16)
    fig.tight_layout()

    # ==========================================
    # 5. 保存图表
    # ==========================================
    plt.savefig("/Users/meiyani/Desktop/phd-thesis/r_practice/output/credit_vs_consumption.png", dpi=300, bbox_inches='tight')
    print("\n成功！对比图已保存至 output/credit_vs_consumption.png")

except Exception as e:
    print(f"\n执行失败，错误信息: {e}")