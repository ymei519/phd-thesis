import pandas as pd
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Songti SC']
plt.rcParams['axes.unicode_minus'] = False

print("正在读取本地数据并计算同比增速...")

try:
    # 1. 读取本地已存好的两个真数据 CSV
    credit_df = pd.read_csv("/Users/meiyani/Desktop/phd-thesis/r_practice/data_raw/real_credit_loan.csv")
    consumption_df = pd.read_csv("/Users/meiyani/Desktop/phd-thesis/r_practice/data_raw/real_consumption.csv")

    credit_df['Date'] = pd.to_datetime(credit_df['Date'])
    consumption_df['Date'] = pd.to_datetime(consumption_df['Date'])

    # 2. 合并（outer 保留所有月份，防止线条断裂）
    merged_df = pd.merge(credit_df, consumption_df, on='Date', how='outer')
    merged_df = merged_df.sort_values('Date')
    merged_df = merged_df.set_index('Date').asfreq('MS').ffill().reset_index()

    # 3. 计算同比增速（当前月与去年同月相比，periods=12）
    # pct_change 会自动计算百分比变化，乘 100 转为百分数
    merged_df['Credit_YoY'] = merged_df['Credit'].pct_change(periods=12) * 100
    merged_df['Consumption_YoY'] = merged_df['Consumption'].pct_change(periods=12) * 100

    # 4. 画图（单轴，单位都是 %，这才是学术规范）
    plt.figure(figsize=(12, 6))
    
    plt.plot(merged_df['Date'], merged_df['Credit_YoY'], color='tab:red', linewidth=1.5, label='信贷同比增速')
    plt.plot(merged_df['Date'], merged_df['Consumption_YoY'], color='tab:blue', linewidth=2.0, label='消费同比增速')
    
    # 加一条 0 刻度线，区分正负增长
    plt.axhline(0, color='black', linestyle='--', linewidth=1.2)

    plt.title('中国信贷供给与居民消费需求的增速对比（同比%）', fontsize=16)
    plt.xlabel('年份', fontsize=12)
    plt.ylabel('同比增速 (%)', fontsize=12)
    plt.legend(fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    
    # 保存图表
    plt.savefig("/Users/meiyani/Desktop/phd-thesis/r_practice/output/credit_vs_consumption_yoy.png", dpi=300, bbox_inches='tight')
    print("\n成功！增速对比图已保存至 output/credit_vs_consumption_yoy.png")

except Exception as e:
    print(f"\n执行失败: {e}")