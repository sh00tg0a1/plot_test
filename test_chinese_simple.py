"""
简单的中文字体测试
"""

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os


def test_chinese_simple():
    """简单的中文字体测试"""
    print("=== 简单中文字体测试 ===")
    
    # 设置字体
    plt.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei', 'SimHei', 'DejaVu Sans']
    plt.rcParams['axes.unicode_minus'] = False
    
    # 创建测试图形
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # 测试文本
    test_texts = [
        '中文字体测试',
        '数据可视化',
        '图表生成',
        'Python 绘图',
        'matplotlib 中文支持'
    ]
    
    for i, text in enumerate(test_texts):
        ax.text(0.5, 0.8 - i*0.15, text, fontsize=16, ha='center')
    
    ax.set_title('中文字体显示测试', fontsize=20, fontweight='bold')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    # 保存图片
    os.makedirs('output', exist_ok=True)
    plt.savefig('output/simple_chinese_test.png', dpi=150, bbox_inches='tight')
    plt.close(fig)
    
    print("✓ 测试完成，图片已保存: output/simple_chinese_test.png")
    
    # 检查字体
    available_fonts = [f.name for f in fm.fontManager.ttflist]
    chinese_fonts = [f for f in available_fonts if any(x in f.lower() for x in ['wenquanyi', 'noto', 'source', 'han', 'sans', 'cjk', 'sc'])]
    
    print(f"找到 {len(chinese_fonts)} 个中文字体:")
    for font in chinese_fonts[:5]:  # 只显示前5个
        print(f"  - {font}")
    
    if not chinese_fonts:
        print("⚠ 未找到中文字体！")
        print("请运行: python fix_chinese_font.py")


if __name__ == "__main__":
    test_chinese_simple()
