"""
测试绘图功能
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.plot import PlotGenerator
from src.data import (
    generate_time_series_data, generate_sales_data, generate_customer_data
)
import pandas as pd
import matplotlib.pyplot as plt


def test_plot_functionality():
    """测试绘图功能"""
    print("开始测试绘图功能...")
    
    # 使用 data.py 生成的数据
    print("1. 生成时间序列数据...")
    ts_data = generate_time_series_data(days=30)
    print(f"   ✓ 时间序列数据生成完成，形状: {ts_data.shape}")
    
    print("2. 生成销售数据...")
    sales_data = generate_sales_data(products=10, months=6)
    print(f"   ✓ 销售数据生成完成，形状: {sales_data.shape}")
    
    print("3. 生成客户数据...")
    customer_data = generate_customer_data(customers=100)
    print(f"   ✓ 客户数据生成完成，形状: {customer_data.shape}")
    
    # 创建绘图器
    plotter = PlotGenerator()
    
    print("\n4. 生成环形图（客户年龄分布）...")
    try:
        # 从客户数据中提取年龄分布
        age_groups = pd.cut(
            customer_data['age'],
            bins=[0, 25, 35, 45, 55, 65, 100],
            labels=['18-25', '26-35', '36-45', '46-55', '56-65', '65+']
        )
        age_distribution = age_groups.value_counts().to_dict()
        
        fig1 = plotter.donut_chart(age_distribution, "客户年龄分布")
        plotter.save_figure(fig1, "customer_age_distribution", "png")
        print("   ✓ 环形图已保存到 output/customer_age_distribution.png")
    except Exception as e:
        print(f"   ✗ 环形图生成失败: {e}")
    
    print("5. 生成折线图（时间序列趋势）...")
    try:
        fig2 = plotter.line_chart(ts_data, 'date', ['value'], "时间序列趋势")
        plotter.save_figure(fig2, "time_series_trend", "png")
        print("   ✓ 折线图已保存到 output/time_series_trend.png")
    except Exception as e:
        print(f"   ✗ 折线图生成失败: {e}")
    
    print("6. 生成分组柱状图（产品销售对比）...")
    try:
        # 按产品汇总销售数据
        product_sales = sales_data.groupby('product').agg({
            'sales': 'sum',
            'revenue': 'sum'
        }).reset_index()
        
        fig3 = plotter.bar_chart(
            product_sales, 'product', ['sales', 'revenue'],
            "产品销售对比", chart_type='grouped'
        )
        plotter.save_figure(fig3, "product_sales_comparison", "png")
        print("   ✓ 分组柱状图已保存到 output/product_sales_comparison.png")
    except Exception as e:
        print(f"   ✗ 分组柱状图生成失败: {e}")
    
    print("7. 生成堆叠柱状图（月度销售构成）...")
    try:
        # 按月份汇总销售数据
        monthly_sales = sales_data.groupby('month').agg({
            'sales': 'sum',
            'revenue': 'sum',
            'price': 'mean'
        }).reset_index()
        monthly_sales['month'] = monthly_sales['month'].dt.strftime('%Y-%m')
        
        fig4 = plotter.bar_chart(
            monthly_sales, 'month', ['sales', 'revenue'],
            "月度销售构成", chart_type='stacked'
        )
        plotter.save_figure(fig4, "monthly_sales_composition", "png")
        print("   ✓ 堆叠柱状图已保存到 output/monthly_sales_composition.png")
    except Exception as e:
        print(f"   ✗ 堆叠柱状图生成失败: {e}")
    
    print("\n所有测试完成！")
    print("\n生成的图片文件:")
    print("- output/customer_age_distribution.png")
    print("- output/time_series_trend.png")
    print("- output/product_sales_comparison.png")
    print("- output/monthly_sales_composition.png")
    
    # 显示所有图表
    print("\n正在显示图表...")
    plt.show()


def show_individual_charts():
    """单独展示每个图表"""
    print("=== 单独展示各个图表 ===\n")
    
    # 使用 data.py 生成的数据
    print("生成数据...")
    ts_data = generate_time_series_data(days=30)
    sales_data = generate_sales_data(products=10, months=6)
    customer_data = generate_customer_data(customers=100)
    
    # 创建绘图器
    plotter = PlotGenerator()
    
    # 1. 环形图 - 客户年龄分布
    print("1. 展示环形图（客户年龄分布）...")
    age_groups = pd.cut(
        customer_data['age'],
        bins=[0, 25, 35, 45, 55, 65, 100],
        labels=['18-25', '26-35', '36-45', '46-55', '56-65', '65+']
    )
    age_distribution = age_groups.value_counts().to_dict()
    
    fig1 = plotter.donut_chart(age_distribution, "客户年龄分布")
    plt.figure(fig1.number)
    plt.show()
    
    # 2. 折线图 - 时间序列趋势
    print("2. 展示折线图（时间序列趋势）...")
    fig2 = plotter.line_chart(ts_data, 'date', ['value'], "时间序列趋势")
    plt.figure(fig2.number)
    plt.show()
    
    # 3. 分组柱状图 - 产品销售对比
    print("3. 展示分组柱状图（产品销售对比）...")
    product_sales = sales_data.groupby('product').agg({
        'sales': 'sum',
        'revenue': 'sum'
    }).reset_index()
    
    fig3 = plotter.bar_chart(
        product_sales, 'product', ['sales', 'revenue'],
        "产品销售对比", chart_type='grouped'
    )
    plt.figure(fig3.number)
    plt.show()
    
    # 4. 堆叠柱状图 - 月度销售构成
    print("4. 展示堆叠柱状图（月度销售构成）...")
    monthly_sales = sales_data.groupby('month').agg({
        'sales': 'sum',
        'revenue': 'sum'
    }).reset_index()
    monthly_sales['month'] = monthly_sales['month'].dt.strftime('%Y-%m')
    
    fig4 = plotter.bar_chart(
        monthly_sales, 'month', ['sales', 'revenue'],
        "月度销售构成", chart_type='stacked'
    )
    plt.figure(fig4.number)
    plt.show()
    
    print("所有图表展示完成！")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "show":
        # 运行: python test_plot.py show
        show_individual_charts()
    else:
        # 运行: python test_plot.py
        test_plot_functionality()
