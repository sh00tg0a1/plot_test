"""
绘图模块使用示例
"""

import pandas as pd

from plot import PlotGenerator


def main():
    """主函数 - 演示绘图功能"""
    print("=== 绘图模块使用示例 ===\n")

    # 创建绘图器
    plotter = PlotGenerator()

    # 1. 创建示例数据
    print("1. 创建示例数据...")

    # 销售数据
    sales_data = pd.DataFrame(
        {
            "月份": ["1月", "2月", "3月", "4月", "5月", "6月"],
            "销售额": [120, 150, 180, 200, 160, 190],
            "利润": [30, 40, 50, 60, 45, 55],
            "成本": [90, 110, 130, 140, 115, 135],
        }
    )

    # 产品分类数据
    category_data = {"电子产品": 40, "服装": 25, "食品": 20, "图书": 15}

    print("数据创建完成！\n")

    # 2. 生成环形图
    print("2. 生成环形图...")
    fig1 = plotter.donut_chart(category_data, "产品销售占比")
    filepath1 = plotter.save_figure(fig1, "产品销售占比", "png")
    base64_1 = plotter.figure_to_base64(fig1)
    print(f"   ✓ 环形图已保存到: {filepath1}")
    print(f"   ✓ Base64 编码长度: {len(base64_1)} 字符")

    # 3. 生成折线图
    print("\n3. 生成折线图...")
    fig2 = plotter.line_chart(sales_data, "月份", ["销售额", "利润"], "销售趋势")
    filepath2 = plotter.save_figure(fig2, "销售趋势", "png")
    base64_2 = plotter.figure_to_base64(fig2)
    print(f"   ✓ 折线图已保存到: {filepath2}")
    print(f"   ✓ Base64 编码长度: {len(base64_2)} 字符")

    # 4. 生成分组柱状图
    print("\n4. 生成分组柱状图...")
    fig3 = plotter.bar_chart(
        sales_data, "月份", ["销售额", "利润"], "月度销售对比", chart_type="grouped"
    )
    filepath3 = plotter.save_figure(fig3, "月度销售对比", "png")
    base64_3 = plotter.figure_to_base64(fig3)
    print(f"   ✓ 分组柱状图已保存到: {filepath3}")
    print(f"   ✓ Base64 编码长度: {len(base64_3)} 字符")

    # 5. 生成堆叠柱状图
    print("\n5. 生成堆叠柱状图...")
    fig4 = plotter.bar_chart(
        sales_data,
        "月份",
        ["销售额", "利润", "成本"],
        "月度财务数据",
        chart_type="stacked",
    )
    filepath4 = plotter.save_figure(fig4, "月度财务数据", "png")
    base64_4 = plotter.figure_to_base64(fig4)
    print(f"   ✓ 堆叠柱状图已保存到: {filepath4}")
    print(f"   ✓ Base64 编码长度: {len(base64_4)} 字符")

    # 6. 生成仪表板
    print("\n6. 生成综合仪表板...")
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

    fig5 = plotter.create_dashboard(dashboard_config, "综合数据仪表板")
    filepath5 = plotter.save_figure(fig5, "综合数据仪表板", "png")
    base64_5 = plotter.figure_to_base64(fig5)
    print(f"   ✓ 仪表板已保存到: {filepath5}")
    print(f"   ✓ Base64 编码长度: {len(base64_5)} 字符")

    # 7. 演示自定义颜色
    print("\n7. 演示自定义颜色...")
    custom_colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4"]
    fig6 = plotter.donut_chart(category_data, "自定义颜色环形图", colors=custom_colors)
    filepath6 = plotter.save_figure(fig6, "自定义颜色环形图", "png")
    print(f"   ✓ 自定义颜色图表已保存到: {filepath6}")

    print("\n=== 所有图表生成完成！ ===")
    print("生成的文件:")
    print("- output/产品销售占比.png")
    print("- output/销售趋势.png")
    print("- output/月度销售对比.png")
    print("- output/月度财务数据.png")
    print("- output/综合数据仪表板.png")
    print("- output/自定义颜色环形图.png")
    print("\nBase64 编码可用于:")
    print("- 网页显示")
    print("- 数据传输")
    print("- API 响应")


if __name__ == "__main__":
    main()
