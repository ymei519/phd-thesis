import akshare as ak
import pandas as pd
import matplotlib.pyplot as plt
import os

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Songti SC']
plt.rcParams['axes.unicode_minus'] = False

print("正在从 AKShare 抓取长周期真数据（新增人民币贷款）...")

try:
    # 核心替换：使用极度稳定的央行信贷接口
    df = ak.macro_china_new_financial_credit()
    
    # 查看列名，确认数据结构（你可以取消注释看看）
    # print(df.columns.tolist())
    
    # 数据清洗：取“月份”和“当月”两列，重命名
    # 注意：这个接口返回的数据可能是倒序的（最新在最前），我们需要反转一下
    df = df[['月份', '当月']].copy()
    df.columns = ['Date', 'Credit']
    df = df.iloc[::-1].reset_index(drop=True) # 反转数据顺序，让时间从早到晚
    
    # 把“月份”转成时间格式，并设为索引
    df['Date'] = pd.to_datetime(df['Date'].str.replace('月份', ''), format='%Y年%m')
    df = df.set_index('Date')
    
    # 把数值列强制转成数字
    df['Credit'] = pd.to_numeric(df['Credit'], errors='coerce')
    df = df.dropna()

    print(f"\n数据抓取成功！共 {len(df)} 个月的数据。")
    print(df.head())
    
    # 画出长周期趋势图（从2008年至今）
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['Credit'], color='darkred', linewidth=1.5)
    
    plt.title('中国新增人民币贷款长周期趋势 (2008至今)', fontsize=16)
    plt.xlabel('年份', fontsize=12)
    plt.ylabel('新增贷款 (亿元)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    
    # 保存数据到 data_raw，方便以后直接读本地文件（不再依赖网络）
    csv_path = os.path.abspath("../data_raw/real_credit_loan.csv")
    df.to_csv(csv_path)
    print(f"\n真数据已保存至: {csv_path}")
    
    # 保存图片到 output
    fig_path = os.path.abspath("../output/real_credit_chart.png")
    plt.savefig(fig_path, dpi=300, bbox_inches='tight')
    print(f"长周期图表已保存至: {fig_path}")

except Exception as e:
    print(f"\n抓取失败，错误信息: {e}")