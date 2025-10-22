"""
测试中文字体显示
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.plot import PlotGenerator
from src.data import generate_customer_data
import pandas as pd


def test_chinese_font():
    """测试中文字体显示"""
    print("=== 测试中文字体显示 ===\n")

    # 生成测试数据
    customer_data = generate_customer_data(customers=50)

    # 创建绘图器
    plotter = PlotGenerator()

    print("1. 测试环形图中文显示...")
    try:
        # 从客户数据中提取年龄分布
        age_groups = pd.cut(
            customer_data['age'],
            bins=[0, 25, 35, 45, 55, 65, 100],
            labels=['18-25岁', '26-35岁', '36-45岁', '46-55岁', '56-65岁', '65岁以上']
        )
        age_distribution = age_groups.value_counts().to_dict()
        
        fig1 = plotter.donut_chart(age_distribution, "客户年龄分布")
        plotter.save_figure(fig1, "chinese_font_test_donut", "png")
        print("   ✓ 环形图已保存到 output/chinese_font_test_donut.png")
    except Exception as e:
        print(f"   ✗ 环形图生成失败: {e}")
    
    print("2. 测试折线图中文显示...")
    try:
        # 创建简单的时间序列数据
        import numpy as np
        dates = pd.date_range('2024-01-01', periods=10, freq='D')
        test_data = pd.DataFrame({
            '日期': dates,
            '销售额': np.random.randint(100, 200, 10),
            '利润': np.random.randint(20, 80, 10)
        })
        
        fig2 = plotter.line_chart(test_data, '日期', ['销售额', '利润'], "销售趋势分析")
        plotter.save_figure(fig2, "chinese_font_test_line", "png")
        print("   ✓ 折线图已保存到 output/chinese_font_test_line.png")
    except Exception as e:
        print(f"   ✗ 折线图生成失败: {e}")
    
    print("3. 测试柱状图中文显示...")
    try:
        # 创建产品数据
        product_data = pd.DataFrame({
            '产品名称': ['智能手机', '笔记本电脑', '平板电脑', '智能手表', '耳机'],
            '销量': [120, 80, 60, 40, 90],
            '收入': [24000, 32000, 18000, 8000, 4500]
        })
        
        fig3 = plotter.bar_chart(
            product_data, '产品名称', ['销量', '收入'],
            "产品销售数据分析", chart_type='grouped'
        )
        plotter.save_figure(fig3, "chinese_font_test_bar", "png")
        print("   ✓ 柱状图已保存到 output/chinese_font_test_bar.png")
    except Exception as e:
        print(f"   ✗ 柱状图生成失败: {e}")
    
    print("4. 测试堆叠柱状图中文显示...")
    try:
        # 创建月度数据
        monthly_data = pd.DataFrame({
            '月份': ['一月', '二月', '三月', '四月', '五月'],
            '线上销售': [100, 120, 110, 130, 140],
            '线下销售': [80, 90, 85, 95, 100],
            '批发销售': [60, 70, 65, 75, 80]
        })
        
        fig4 = plotter.bar_chart(
            monthly_data, '月份', ['线上销售', '线下销售', '批发销售'],
            "月度销售渠道分析", chart_type='stacked'
        )
        plotter.save_figure(fig4, "chinese_font_test_stacked", "png")
        print("   ✓ 堆叠柱状图已保存到 output/chinese_font_test_stacked.png")
    except Exception as e:
        print(f"   ✗ 堆叠柱状图生成失败: {e}")
    
    print("\n=== 中文字体测试完成！ ===")
    print("生成的文件:")
    print("- output/chinese_font_test_donut.png")
    print("- output/chinese_font_test_line.png")
    print("- output/chinese_font_test_bar.png")
    print("- output/chinese_font_test_stacked.png")
    
    # 显示图表
    plotter.show_figure()


if __name__ == "__main__":
    test_chinese_font()
