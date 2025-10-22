"""
测试分组+堆叠组合柱状图
"""

import matplotlib.pyplot as plt

from src.data import generate_sales_data
from src.plot import PlotGenerator


def test_grouped_stacked_chart():
    """测试分组+堆叠组合柱状图"""
    print("=== 测试分组+堆叠组合柱状图 ===\n")

    # 使用 data.py 生成销售数据
    print("1. 生成销售数据...")
    sales_data = generate_sales_data(products=20, months=4)
    print(f"   ✓ 销售数据生成完成，形状: {sales_data.shape}")

    # 转换为二维表结构用于测试
    data = sales_data.melt(
        id_vars=["product", "month"],
        value_vars=["sales", "revenue"],
        var_name="指标",
        value_name="数值",
    )
    # 添加渠道信息
    data["渠道"] = data["product"].apply(lambda x: "线上" if int(x.split("_")[1]) % 2 == 0 else "线下")
    data["产品"] = data["product"].apply(lambda x: f"产品{x.split('_')[1]}")
    data["季度"] = data["month"].dt.to_period("Q").astype(str)

    # 重命名列以匹配测试需求
    data = data.rename(columns={"数值": "销量"})
    data = data[["季度", "产品", "渠道", "销量"]].copy()

    plotter = PlotGenerator()

    # 1. 纯分组模式 - 使用二维表数据
    print("1. 纯分组模式...")
    fig1 = plotter.bar_chart(
        data,
        x_col="季度",
        y_col="销量",
        group_col="渠道",
        title="季度销售对比（分组）",
        ylabel="销售额",
    )
    plotter.save_figure(fig1, "grouped_only", "png")
    print("   ✓ 已保存: output/grouped_only.png")

    # 2. 纯堆叠模式
    print("2. 纯堆叠模式...")
    fig2 = plotter.bar_chart(
        data,
        x_col="季度",
        y_col="销量",
        stack_col="渠道",
        title="季度销售对比（堆叠）",
        ylabel="销售额",
    )
    plotter.save_figure(fig2, "stacked_only", "png")
    print("   ✓ 已保存: output/stacked_only.png")

    # 3. 分组+堆叠组合模式 - 直接使用二维表数据
    print("3. 分组+堆叠组合模式...")
    fig3 = plotter.bar_chart(
        data,
        x_col="季度",
        y_col="销量",
        group_col="渠道",
        stack_col="产品",
        title="季度销售对比（分组+堆叠）",
        ylabel="销售额",
    )
    plotter.save_figure(fig3, "grouped_stacked", "png")
    print("   ✓ 已保存: output/grouped_stacked.png")

    # 4. 更复杂的分组+堆叠示例
    print("4. 三组堆叠示例...")
    # 使用销售数据创建团队业绩数据
    team_data = sales_data.copy()
    team_data["团队"] = team_data["product"].apply(lambda x: f"团队{chr(65 + int(x.split('_')[1]) % 3)}")
    team_data["类型"] = team_data["sales"].apply(lambda x: "新增" if x > team_data["sales"].median() else "续费")
    team_data["月份"] = team_data["month"].dt.strftime("%m月")
    team_data["业绩"] = team_data["sales"]

    data2 = team_data[["月份", "团队", "类型", "业绩"]].copy()

    fig4 = plotter.bar_chart(
        data2,
        x_col="月份",
        y_col="业绩",
        group_col="团队",
        stack_col="类型",
        title="团队业绩对比",
        xlabel="",
        ylabel="业绩",
    )
    plotter.save_figure(fig4, "three_groups_stacked", "png")
    print("   ✓ 已保存: output/three_groups_stacked.png")

    print("\n=== 测试完成！ ===")
    print("\n生成的图片：")
    print("- output/grouped_only.png")
    print("- output/stacked_only.png")
    print("- output/grouped_stacked.png")
    print("- output/three_groups_stacked.png")

    # 显示图表
    print("\n正在显示图表...")
    plt.show()


if __name__ == "__main__":
    test_grouped_stacked_chart()
