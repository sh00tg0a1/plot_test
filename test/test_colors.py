"""
测试新的配色方案
"""

import matplotlib.pyplot as plt

from src.data import generate_sales_data
from src.plot import PlotGenerator


def test_new_color_palette():
    """测试新的配色方案"""
    print("=== 测试新的配色方案 ===\n")

    # 使用 data.py 生成测试数据
    print("1. 生成测试数据...")
    sales_data_raw = generate_sales_data(products=15, months=8)

    # 创建分类数据（从销售数据中提取）
    category_counts = sales_data_raw["category"].value_counts()
    category_data = category_counts.to_dict()

    # 创建月度汇总数据
    monthly_summary = (
        sales_data_raw.groupby(sales_data_raw["month"].dt.strftime("%Y-%m"))
        .agg({"sales": "sum", "revenue": "sum"})
        .reset_index()
    )
    monthly_summary.columns = ["月份", "销售额", "利润"]
    monthly_summary["成本"] = monthly_summary["销售额"] - monthly_summary["利润"]

    sales_data = monthly_summary
    print(f"   ✓ 数据生成完成，形状: {sales_data.shape}")

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
    # 转换为二维表数据格式
    sales_data_long = sales_data.melt(
        id_vars=["月份"],
        value_vars=["销售额", "利润", "成本"],
        var_name="指标",
        value_name="数值",
    )
    fig3 = plotter.bar_chart(
        sales_data_long,
        x_col="月份",
        y_col="数值",
        group_col="指标",
        title="月度财务数据（新配色）",
    )
    plotter.save_figure(fig3, "new_color_bar", "png")
    print("   ✓ 柱状图已保存到 output/new_color_bar.png")

    print("\n5. 生成堆叠柱状图（展示配色）...")
    fig4 = plotter.bar_chart(
        sales_data_long,
        x_col="月份",
        y_col="数值",
        stack_col="指标",
        title="月度财务数据（新配色）",
    )
    plotter.save_figure(fig4, "new_color_stacked", "png")
    print("   ✓ 堆叠柱状图已保存到 output/new_color_stacked.png")

    print("\n=== 新配色方案测试完成！ ===")
    print("生成的文件:")
    print("- output/new_color_donut.png")
    print("- output/new_color_line.png")
    print("- output/new_color_bar.png")
    print("- output/new_color_stacked.png")

    # 显示图表
    print("\n正在显示图表...")
    plt.show()


if __name__ == "__main__":
    test_new_color_palette()
