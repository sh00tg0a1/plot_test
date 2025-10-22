"""
简单的中文字体测试
"""

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import matplotlib.font_manager as fm
import matplotlib.pyplot as plt


def test_simple_chinese():
    """简单的中文字体测试"""
    print("=== 简单中文字体测试 ===")

    # 清除缓存并重建字体管理器
    try:
        import matplotlib

        cache_dir = matplotlib.get_cachedir()
        if os.path.exists(cache_dir):
            import shutil

            shutil.rmtree(cache_dir)
            print("✓ 已清除 matplotlib 缓存")
    except Exception:
        pass

    try:
        fm._rebuild()
        print("✓ 已重建字体管理器")
    except Exception:
        pass

    # 获取可用字体
    available_fonts = [f.name for f in fm.fontManager.ttflist]
    print(f"系统中共有 {len(available_fonts)} 个字体")

    # 查找中文字体
    chinese_keywords = [
        "wenquanyi",
        "noto",
        "source",
        "han",
        "sans",
        "cjk",
        "sc",
        "microsoft",
        "yahei",
        "simhei",
    ]
    chinese_fonts = [
        f for f in available_fonts if any(kw in f.lower() for kw in chinese_keywords)
    ]

    print(f"找到 {len(chinese_fonts)} 个可能的中文字体:")
    for font in chinese_fonts[:10]:  # 只显示前10个
        print(f"  - {font}")

    # 尝试设置字体
    fonts_to_try = [
        "WenQuanYi Micro Hei",
        "Noto Sans CJK SC",
        "Source Han Sans SC",
        "Microsoft YaHei",
        "SimHei",
        "DejaVu Sans",
    ]

    font_set = False
    for font in fonts_to_try:
        if font in available_fonts:
            try:
                plt.rcParams["font.sans-serif"] = [font]
                plt.rcParams["axes.unicode_minus"] = False
                print(f"✓ 成功设置字体: {font}")
                font_set = True
                break
            except Exception as e:
                print(f"✗ 设置字体失败: {font}, 错误: {e}")

    if not font_set:
        print("⚠ 未找到合适的中文字体，使用默认设置")
        plt.rcParams["font.sans-serif"] = ["DejaVu Sans", "Arial", "sans-serif"]
        plt.rcParams["axes.unicode_minus"] = False

    # 测试中文显示
    try:
        fig, ax = plt.subplots(figsize=(8, 6))

        test_texts = ["中文字体测试", "数据可视化", "图表生成", "Python 绘图"]

        for i, text in enumerate(test_texts):
            ax.text(0.5, 0.8 - i * 0.2, text, fontsize=16, ha="center")

        ax.set_title("中文字体显示测试", fontsize=20, fontweight="bold")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis("off")

        # 保存图片
        os.makedirs("output", exist_ok=True)
        plt.savefig("output/simple_chinese_test.png", dpi=150, bbox_inches="tight")
        plt.close(fig)

        print("✓ 测试完成，图片已保存: output/simple_chinese_test.png")

        # 显示图片
        plt.show()

    except Exception as e:
        print(f"✗ 测试失败: {e}")


if __name__ == "__main__":
    test_simple_chinese()
