"""
Windows 中文字体测试
"""

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import platform
import os


def test_windows_font():
    """测试 Windows 中文字体"""
    print("=== Windows 中文字体测试 ===")
    
    # 清除缓存
    try:
        import matplotlib
        cache_dir = matplotlib.get_cachedir()
        if os.path.exists(cache_dir):
            import shutil
            shutil.rmtree(cache_dir)
            print("✓ 已清除 matplotlib 缓存")
    except Exception as e:
        print(f"✗ 清除缓存失败: {e}")
    
    # 获取所有字体
    all_fonts = [f.name for f in fm.fontManager.ttflist]
    print(f"系统字体总数: {len(all_fonts)}")
    
    # 查找 Windows 中文字体
    windows_fonts = [
        'Microsoft YaHei',
        'Microsoft YaHei UI',
        'SimHei',
        'SimSun',
        'KaiTi',
        'FangSong',
        'Microsoft JhengHei',
        'Microsoft JhengHei UI'
    ]
    
    available_fonts = []
    for font in windows_fonts:
        if font in all_fonts:
            available_fonts.append(font)
    
    print(f"找到 {len(available_fonts)} 个 Windows 中文字体:")
    for font in available_fonts:
        print(f"  - {font}")
    
    # 设置字体
    if available_fonts:
        selected_font = available_fonts[0]
        plt.rcParams['font.sans-serif'] = [selected_font]
        plt.rcParams['axes.unicode_minus'] = False
        print(f"✓ 使用字体: {selected_font}")
    else:
        print("⚠ 未找到 Windows 中文字体，使用默认设置")
        plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
        plt.rcParams['axes.unicode_minus'] = False
    
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
        plt.savefig('output/windows_font_test.png', dpi=150, bbox_inches='tight')
        plt.close(fig)
        
        print("✓ 测试完成，图片已保存: output/windows_font_test.png")
        
        # 显示图片
        plt.show()
        
    except Exception as e:
        print(f"✗ 测试失败: {e}")


if __name__ == "__main__":
    test_windows_font()
