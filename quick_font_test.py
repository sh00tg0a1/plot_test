"""
快速中文字体测试
"""

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os


def quick_test():
    """快速测试中文字体"""
    print("=== 快速中文字体测试 ===")
    
    # 1. 检查可用字体
    all_fonts = [f.name for f in fm.fontManager.ttflist]
    print(f"系统字体总数: {len(all_fonts)}")
    
    # 2. 查找中文字体
    chinese_fonts = []
    keywords = ['wenquanyi', 'noto', 'source', 'han', 'sans', 'cjk', 'sc', 'microsoft', 'yahei', 'simhei']
    
    for font in all_fonts:
        if any(kw in font.lower() for kw in keywords):
            chinese_fonts.append(font)
    
    print(f"找到中文字体: {len(chinese_fonts)}")
    for font in chinese_fonts[:5]:
        print(f"  - {font}")
    
    # 3. 设置字体
    if chinese_fonts:
        font = chinese_fonts[0]
        plt.rcParams['font.sans-serif'] = [font]
        plt.rcParams['axes.unicode_minus'] = False
        print(f"✓ 使用字体: {font}")
    else:
        plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
        plt.rcParams['axes.unicode_minus'] = False
        print("⚠ 使用默认字体")
    
    # 4. 测试显示
    try:
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.text(0.5, 0.5, '中文字体测试', fontsize=20, ha='center', va='center')
        ax.set_title('测试标题')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
        
        os.makedirs('output', exist_ok=True)
        plt.savefig('output/quick_test.png', dpi=100, bbox_inches='tight')
        plt.close(fig)
        
        print("✓ 测试图片已保存: output/quick_test.png")
        
    except Exception as e:
        print(f"✗ 测试失败: {e}")


if __name__ == "__main__":
    quick_test()
