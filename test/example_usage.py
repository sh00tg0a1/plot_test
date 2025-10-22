"""
绘图模块使用示例
"""

import pandas as pd

from src.data import generate_sales_data
from src.plot import PlotGenerator


def main():
    """主函数 - 演示绘图功能"""
    print("=== 绘图模块使用示例 ===\n")

    # 创建绘图器
    plotter = PlotGenerator()

    # 1. 创建示例数据
    print("1. 创建示例数据...")

    # 使用 data.py 生成销售数据
    sales_data_raw = generate_sales_data(products=10, months=6)

    # 转换为示例格式
    monthly_summary = (
        sales_data_raw.groupby(sales_data_raw["month"].dt.strftime("%m月"))
        .agg({"sales": "sum", "revenue": "sum"})
        .reset_index()
    )
    monthly_summary.columns = ["月份", "销售额", "利润"]
    monthly_summary["成本"] = monthly_summary["销售额"] - monthly_summary["利润"]

    sales_data = monthly_summary

    # 产品分类数据（从销售数据中提取）
    category_counts = sales_data_raw["category"].value_counts()
    category_data = category_counts.to_dict()

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
    fig2 = plotter.line_chart(
        sales_data, "月份", ["销售额", "利润"], "销售趋势", show_values=True
    )
    filepath2 = plotter.save_figure(fig2, "销售趋势", "png")
    base64_2 = plotter.figure_to_base64(fig2)
    print(f"   ✓ 折线图已保存到: {filepath2}")
    print(f"   ✓ Base64 编码长度: {len(base64_2)} 字符")

    # 4. 生成分组柱状图
    print("\n4. 生成分组柱状图...")
    # 创建二维表数据用于演示新的API
    sales_data_long = pd.DataFrame(
        {
            "月份": [
                "1月",
                "1月",
                "2月",
                "2月",
                "3月",
                "3月",
                "4月",
                "4月",
                "5月",
                "5月",
                "6月",
                "6月",
            ],
            "指标": [
                "销售额",
                "利润",
                "销售额",
                "利润",
                "销售额",
                "利润",
                "销售额",
                "利润",
                "销售额",
                "利润",
                "销售额",
                "利润",
            ],
            "数值": [120, 30, 150, 40, 180, 50, 200, 60, 160, 45, 190, 55],
        }
    )
    fig3 = plotter.bar_chart(
        sales_data_long,
        x_col="月份",
        y_col="数值",
        group_col="指标",
        title="月度销售对比",
        show_values=True,
    )
    filepath3 = plotter.save_figure(fig3, "月度销售对比", "png")
    base64_3 = plotter.figure_to_base64(fig3)
    print(f"   ✓ 分组柱状图已保存到: {filepath3}")
    print(f"   ✓ Base64 编码长度: {len(base64_3)} 字符")

    # 5. 生成堆叠柱状图
    print("\n5. 生成堆叠柱状图...")
    # 创建二维表数据用于演示堆叠图
    finance_data_long = pd.DataFrame(
        {
            "月份": [
                "1月",
                "1月",
                "1月",
                "2月",
                "2月",
                "2月",
                "3月",
                "3月",
                "3月",
                "4月",
                "4月",
                "4月",
                "5月",
                "5月",
                "5月",
                "6月",
                "6月",
                "6月",
            ],
            "类型": [
                "销售额",
                "利润",
                "成本",
                "销售额",
                "利润",
                "成本",
                "销售额",
                "利润",
                "成本",
                "销售额",
                "利润",
                "成本",
                "销售额",
                "利润",
                "成本",
                "销售额",
                "利润",
                "成本",
            ],
            "数值": [
                120,
                30,
                90,
                150,
                40,
                110,
                180,
                50,
                130,
                200,
                60,
                140,
                160,
                45,
                115,
                190,
                55,
                135,
            ],
        }
    )
    fig4 = plotter.bar_chart(
        finance_data_long,
        x_col="月份",
        y_col="数值",
        stack_col="类型",
        title="月度财务数据",
    )
    filepath4 = plotter.save_figure(fig4, "月度财务数据", "png")
    base64_4 = plotter.figure_to_base64(fig4)
    print(f"   ✓ 堆叠柱状图已保存到: {filepath4}")
    print(f"   ✓ Base64 编码长度: {len(base64_4)} 字符")

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
    print("- output/自定义颜色环形图.png")
    print("\nBase64 编码可用于:")
    print("- 网页显示")
    print("- 数据传输")
    print("- API 响应")


if __name__ == "__main__":
    main()
