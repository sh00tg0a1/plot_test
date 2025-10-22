"""
测试新的配色方案
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from plot import PlotGenerator


def test_new_color_palette():
    """测试新的配色方案"""
    print("=== 测试新的配色方案 ===\n")

    # 创建测试数据
    np.random.seed(42)

    # 创建更多分类数据来展示所有颜色
    category_data = {"电子产品": 30, "服装": 25, "食品": 20, "图书": 15, "家居": 10}

    # 时间序列数据
    dates = pd.date_range("2024-01-01", periods=8, freq="M")
    sales_data = pd.DataFrame(
        {
            "月份": [d.strftime("%Y-%m") for d in dates],
            "销售额": [120, 150, 180, 200, 160, 190, 220, 250],
            "利润": [30, 40, 50, 60, 45, 55, 65, 75],
            "成本": [90, 110, 130, 140, 115, 135, 155, 175],
        }
    )

    # 创建绘图器
    plotter = PlotGenerator()

    print("1. 展示新的配色方案...")
    print("配色序列：")
    for i, color in enumerate(plotter.COLOR_PALETTE):
        print(f"   {i+1}. {color}")

    print("\n2. 生成环形图（展示配色）...")
    fig1 = plotter.donut_chart(category_data, "产品销售占比（新配色）")
    plotter.save_figure(fig1, "new_color_donut", "png")
    print("   ✓ 环形图已保存到 output/new_color_donut.png")

    print("\n3. 生成折线图（展示配色）...")
    fig2 = plotter.line_chart(
        sales_data, "月份", ["销售额", "利润", "成本"], "销售趋势（新配色）"
    )
    plotter.save_figure(fig2, "new_color_line", "png")
    print("   ✓ 折线图已保存到 output/new_color_line.png")

    print("\n4. 生成柱状图（展示配色）...")
    fig3 = plotter.bar_chart(
        sales_data,
        "月份",
        ["销售额", "利润", "成本"],
        "月度财务数据（新配色）",
        chart_type="grouped",
    )
    plotter.save_figure(fig3, "new_color_bar", "png")
    print("   ✓ 柱状图已保存到 output/new_color_bar.png")

    print("\n5. 生成堆叠柱状图（展示配色）...")
    fig4 = plotter.bar_chart(
        sales_data,
        "月份",
        ["销售额", "利润", "成本"],
        "月度财务数据（新配色）",
        chart_type="stacked",
    )
    plotter.save_figure(fig4, "new_color_stacked", "png")
    print("   ✓ 堆叠柱状图已保存到 output/new_color_stacked.png")

    print("\n6. 生成综合仪表板（展示配色）...")
    dashboard_config = [
        {"type": "donut", "data": category_data, "title": "产品分类"},
        {
            "type": "line",
            "data": sales_data,
            "x_col": "月份",
            "y_cols": ["销售额"],
            "title": "销售趋势",
        },
        {
            "type": "bar",
            "data": sales_data,
            "x_col": "月份",
            "y_cols": ["销售额", "利润"],
            "subtype": "grouped",
            "title": "月度对比",
        },
        {
            "type": "bar",
            "data": sales_data,
            "x_col": "月份",
            "y_cols": ["销售额", "利润", "成本"],
            "subtype": "stacked",
            "title": "财务数据",
        },
    ]

    fig5 = plotter.create_dashboard(dashboard_config, "新配色综合仪表板")
    plotter.save_figure(fig5, "new_color_dashboard", "png")
    print("   ✓ 仪表板已保存到 output/new_color_dashboard.png")

    print("\n=== 新配色方案测试完成！ ===")
    print("生成的文件:")
    print("- output/new_color_donut.png")
    print("- output/new_color_line.png")
    print("- output/new_color_bar.png")
    print("- output/new_color_stacked.png")
    print("- output/new_color_dashboard.png")

    # 显示图表
    print("\n正在显示图表...")
    plt.show()


if __name__ == "__main__":
    test_new_color_palette()
