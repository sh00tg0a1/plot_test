"""
Windows 系统中文字体修复
专门解决 Windows 系统上的中文字体问题
"""

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os


def fix_windows_chinese_font():
    """修复 Windows 系统中文字体"""
    print("=== Windows 中文字体修复 ===")

    # 清除缓存
    try:
        import matplotlib
        cache_dir = matplotlib.get_cachedir()
        if os.path.exists(cache_dir):
            import shutil
            shutil.rmtree(cache_dir)
            print("✓ 已清除 matplotlib 缓存")
    except Exception:
        pass

    # 重建字体管理器
    try:
        fm._rebuild()
        print("✓ 已重建字体管理器")
    except Exception:
        pass

    # 获取所有字体
    all_fonts = [f.name for f in fm.fontManager.ttflist]
    print(f"系统字体总数: {len(all_fonts)}")

    # Windows 中文字体
    windows_chinese_fonts = [
        'Microsoft YaHei',
        'Microsoft YaHei UI', 
        'SimHei',
        'SimSun',
        'KaiTi',
        'FangSong',
        'Microsoft JhengHei',
        'Microsoft JhengHei UI'
    ]

    # 查找可用的中文字体
    available_chinese_fonts = []
    for font in windows_chinese_fonts:
        if font in all_fonts:
            available_chinese_fonts.append(font)

    print(f"找到 {len(available_chinese_fonts)} 个 Windows 中文字体:")
    for font in available_chinese_fonts:
        print(f"  - {font}")

    # 设置字体
    if available_chinese_fonts:
        # 使用第一个可用的中文字体
        selected_font = available_chinese_fonts[0]
        plt.rcParams['font.sans-serif'] = [selected_font]
        plt.rcParams['axes.unicode_minus'] = False
        print(f"✓ 设置字体: {selected_font}")
    else:
        # 如果没有中文字体，尝试其他方案
        print("⚠ 未找到 Windows 中文字体")

        # 尝试使用支持中文的字体
        fallback_fonts = [
            'Arial Unicode MS',
            'Lucida Sans Unicode',
            'Tahoma',
            'Verdana'
        ]

        for font in fallback_fonts:
            if font in all_fonts:
                plt.rcParams['font.sans-serif'] = [font]
                plt.rcParams['axes.unicode_minus'] = False
                print(f"✓ 使用备选字体: {font}")
                break
        else:
            # 最后的备选方案
            plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
            plt.rcParams['axes.unicode_minus'] = False
            print("⚠ 使用默认字体，中文可能显示异常")

    # 测试中文显示
    try:
        fig, ax = plt.subplots(figsize=(8, 6))

        test_texts = [
            'Windows 中文字体测试',
            '数据可视化',
            '图表生成',
            'Python 绘图'
        ]

        for i, text in enumerate(test_texts):
            ax.text(0.5, 0.8 - i*0.15, text, fontsize=16, ha='center')

        ax.set_title('Windows 中文字体显示测试', fontsize=20, fontweight='bold')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')

        # 保存图片
        os.makedirs('output', exist_ok=True)
        plt.savefig('output/windows_chinese_test.png', dpi=150, bbox_inches='tight')
        plt.close(fig)

        print("✓ 测试完成，图片已保存: output/windows_chinese_test.png")

        # 显示图片
        plt.show()

    except Exception as e:
        print(f"✗ 测试失败: {e}")


def check_windows_fonts():
    """检查 Windows 系统字体"""
    print("=== Windows 字体检查 ===")

    all_fonts = [f.name for f in fm.fontManager.ttflist]

    # 查找所有可能的中文字体
    chinese_keywords = [
        'microsoft', 'yahei', 'simhei', 'simsun', 'kaiti', 'fangsong',
        'jhenghei', 'mingliu', 'pmingliu', 'arial', 'unicode'
    ]

    chinese_fonts = []
    for font in all_fonts:
        font_lower = font.lower()
        if any(keyword in font_lower for keyword in chinese_keywords):
            chinese_fonts.append(font)

    print(f"找到 {len(chinese_fonts)} 个可能的中文字体:")
    for font in sorted(chinese_fonts):
        print(f"  - {font}")

    return chinese_fonts


if __name__ == "__main__":
    print("Windows 系统中文字体修复工具")
    print("=" * 50)

    # 检查字体
    check_windows_fonts()
    print()

    # 修复字体
    fix_windows_chinese_font()

    print("\n=== 修复完成 ===")
    print("如果问题仍然存在，请尝试：")
    print("1. 重启 Python 程序")
    print("2. 检查系统语言设置")
    print("3. 安装中文字体包")
