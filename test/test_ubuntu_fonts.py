"""
Ubuntu 系统中文字体测试脚本
"""

import os
import sys

import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import pandas as pd

from src.data import generate_customer_data
from src.plot import PlotGenerator


def check_ubuntu_fonts():
    """检查 Ubuntu 系统中可用的中文字体"""
    print("=== Ubuntu 中文字体检查 ===\n")

    # 获取所有字体
    all_fonts = [f.name for f in fm.fontManager.ttflist]

    # Ubuntu 推荐的中文字体
    ubuntu_fonts = [
        "WenQuanYi Micro Hei",
        "WenQuanYi Zen Hei",
        "Noto Sans CJK SC",
        "Source Han Sans SC",
        "Source Han Sans",
        "Droid Sans Fallback",
        "AR PL UMing CN",
        "AR PL UKai CN",
    ]

    print("检查 Ubuntu 推荐的中文字体：")
    available_fonts = []
    for font in ubuntu_fonts:
        if font in all_fonts:
            print(f"  ✓ {font} - 可用")
            available_fonts.append(font)
        else:
            print(f"  ✗ {font} - 不可用")

    print(f"\n找到 {len(available_fonts)} 个可用的中文字体")

    if not available_fonts:
        print("\n警告：未找到中文字体！")
        print("请运行以下命令安装字体：")
        print("sudo apt install fonts-wqy-microhei fonts-noto-cjk")
        return False

    return True


def test_chinese_display():
    """测试中文显示效果"""
    print("\n=== 测试中文显示效果 ===\n")

    # 创建绘图器
    plotter = PlotGenerator()

    # 生成测试数据
    customer_data = generate_customer_data(customers=30)

    print("1. 测试环形图中文显示...")
    try:
        # 从客户数据中提取年龄分布
        age_groups = pd.cut(
            customer_data["age"],
            bins=[0, 25, 35, 45, 55, 65, 100],
            labels=["18-25岁", "26-35岁", "36-45岁", "46-55岁", "56-65岁", "65岁以上"],
        )
        age_distribution = age_groups.value_counts().to_dict()

        fig1 = plotter.donut_chart(age_distribution, "客户年龄分布")
        plotter.save_figure(fig1, "ubuntu_chinese_test_donut", "png")
        print("   ✓ 环形图已保存到 output/ubuntu_chinese_test_donut.png")
    except Exception as e:
        print(f"   ✗ 环形图生成失败: {e}")

    print("2. 测试折线图中文显示...")
    try:
        import numpy as np

        dates = pd.date_range("2024-01-01", periods=8, freq="D")
        test_data = pd.DataFrame(
            {
                "日期": dates,
                "销售额": np.random.randint(100, 200, 8),
                "利润": np.random.randint(20, 80, 8),
            }
        )

        fig2 = plotter.line_chart(test_data, "日期", ["销售额", "利润"], "销售趋势分析")
        plotter.save_figure(fig2, "ubuntu_chinese_test_line", "png")
        print("   ✓ 折线图已保存到 output/ubuntu_chinese_test_line.png")
    except Exception as e:
        print(f"   ✗ 折线图生成失败: {e}")

    print("3. 测试柱状图中文显示...")
    try:
        product_data = pd.DataFrame(
            {
                "产品名称": ["智能手机", "笔记本电脑", "平板电脑", "智能手表"],
                "销量": [120, 80, 60, 40],
                "收入": [24000, 32000, 18000, 8000],
            }
        )

        fig3 = plotter.bar_chart(
            product_data,
            "产品名称",
            ["销量", "收入"],
            "产品销售数据分析",
            chart_type="grouped",
        )
        plotter.save_figure(fig3, "ubuntu_chinese_test_bar", "png")
        print("   ✓ 柱状图已保存到 output/ubuntu_chinese_test_bar.png")
    except Exception as e:
        print(f"   ✗ 柱状图生成失败: {e}")

    print("\n=== Ubuntu 中文显示测试完成！ ===")
    print("生成的文件:")
    print("- output/ubuntu_chinese_test_donut.png")
    print("- output/ubuntu_chinese_test_line.png")
    print("- output/ubuntu_chinese_test_bar.png")

    # 显示图表
    print("\n正在显示图表...")
    plt.show()


def show_font_installation_guide():
    """显示字体安装指南"""
    print("\n=== Ubuntu 字体安装指南 ===")
    print("如果中文显示异常，请按以下步骤安装字体：")
    print("")
    print("1. 安装文泉驿字体（推荐）：")
    print("   sudo apt install fonts-wqy-microhei fonts-wqy-zenhei")
    print("")
    print("2. 安装 Noto 字体：")
    print("   sudo apt install fonts-noto-cjk")
    print("")
    print("3. 安装思源字体：")
    print("   sudo apt install fonts-source-han-sans")
    print("")
    print("4. 刷新字体缓存：")
    print("   sudo fc-cache -fv")
    print("")
    print("5. 或者运行自动安装脚本：")
    print("   chmod +x install_ubuntu_fonts.sh")
    print("   ./install_ubuntu_fonts.sh")
    print("")
    print("6. 清除 matplotlib 缓存：")
    print("   rm -rf ~/.matplotlib")
    print("")


def main():
    """主函数"""
    print("Ubuntu 系统中文字体测试")
    print("=" * 40)

    # 检查字体
    if check_ubuntu_fonts():
        # 测试中文显示
        test_chinese_display()
    else:
        # 显示安装指南
        show_font_installation_guide()


if __name__ == "__main__":
    main()
