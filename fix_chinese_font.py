"""
中文字体修复脚本
快速修复中文字体显示问题
"""

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import platform
import os
import subprocess


def fix_chinese_font():
    """修复中文字体问题"""
    print("=== 中文字体修复工具 ===")
    
    # 1. 清除缓存
    print("1. 清除 matplotlib 缓存...")
    try:
        cache_dir = plt.matplotlib.get_cachedir()
        if os.path.exists(cache_dir):
            import shutil
            shutil.rmtree(cache_dir)
            print(f"✓ 已清除缓存: {cache_dir}")
    except Exception as e:
        print(f"✗ 清除缓存失败: {e}")
    
    # 2. 重新构建字体管理器
    print("2. 重新构建字体管理器...")
    try:
        fm._rebuild()
        print("✓ 字体管理器重建完成")
    except Exception as e:
        print(f"✗ 重建失败: {e}")
    
    # 3. 根据系统设置字体
    system = platform.system().lower()
    print(f"3. 检测到系统: {system}")
    
    if system == 'linux':
        # Ubuntu/Linux 系统
        print("正在为 Linux 系统设置字体...")
        
        # 尝试安装字体
        try:
            print("检查并安装中文字体...")
            result = subprocess.run([
                'sudo', 'apt', 'install', '-y',
                'fonts-wqy-microhei', 'fonts-noto-cjk'
            ], capture_output=True, text=True, timeout=60)
            
            if result.returncode == 0:
                print("✓ 字体安装成功")
            else:
                print("⚠ 字体安装失败，尝试使用现有字体")
        except Exception as e:
            print(f"⚠ 字体安装跳过: {e}")
        
        # 刷新字体缓存
        try:
            subprocess.run(['sudo', 'fc-cache', '-fv'],
                          capture_output=True, text=True)
            print("✓ 字体缓存已刷新")
        except Exception as e:
            print(f"⚠ 缓存刷新失败: {e}")
        
        # 设置字体
        fonts_to_try = [
            'WenQuanYi Micro Hei',
            'Noto Sans CJK SC',
            'Source Han Sans SC',
            'Droid Sans Fallback'
        ]
        
    elif system == 'windows':
        # Windows 系统
        print("正在为 Windows 系统设置字体...")
        fonts_to_try = [
            'Microsoft YaHei',
            'SimHei',
            'KaiTi',
            'FangSong'
        ]
        
    elif system == 'darwin':
        # macOS 系统
        print("正在为 macOS 系统设置字体...")
        fonts_to_try = [
            'PingFang SC',
            'Hiragino Sans GB',
            'STHeiti',
            'Arial Unicode MS'
        ]
        
    else:
        print("未知系统，使用通用字体设置...")
        fonts_to_try = [
            'WenQuanYi Micro Hei',
            'Noto Sans CJK SC',
            'DejaVu Sans'
        ]
    
    # 4. 尝试设置字体
    print("4. 尝试设置字体...")
    font_set = False
    
    for font in fonts_to_try:
        try:
            # 检查字体是否可用
            available_fonts = [f.name for f in fm.fontManager.ttflist]
            if font in available_fonts:
                plt.rcParams['font.sans-serif'] = [font]
                plt.rcParams['axes.unicode_minus'] = False
                print(f"✓ 成功设置字体: {font}")
                font_set = True
                break
            else:
                print(f"✗ 字体不可用: {font}")
        except Exception as e:
            print(f"✗ 设置字体失败: {font}, 错误: {e}")
    
    if not font_set:
        print("⚠ 未找到合适的中文字体，使用默认设置")
        plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'sans-serif']
        plt.rcParams['axes.unicode_minus'] = False
    
    # 5. 测试中文显示
    print("5. 测试中文显示...")
    try:
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # 测试文本
        test_texts = [
            '中文字体测试',
            '数据可视化',
            '图表生成',
            'Python 绘图'
        ]
        
        for i, text in enumerate(test_texts):
            ax.text(0.5, 0.8 - i*0.2, text, fontsize=16, ha='center')
        
        ax.set_title('中文字体显示测试', fontsize=20)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
        
        # 保存测试图片
        os.makedirs('output', exist_ok=True)
        plt.savefig('output/chinese_font_test.png', dpi=150, bbox_inches='tight')
        plt.close(fig)
        
        print("✓ 中文显示测试完成，图片已保存: output/chinese_font_test.png")
        
    except Exception as e:
        print(f"✗ 中文显示测试失败: {e}")
    
    print("\n=== 修复完成 ===")
    print("如果问题仍然存在，请运行: python test/font_diagnosis.py")


if __name__ == "__main__":
    fix_chinese_font()
