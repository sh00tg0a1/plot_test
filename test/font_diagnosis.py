"""
中文字体诊断脚本
用于诊断和解决中文字体显示问题
"""

import os
import platform
import subprocess

import matplotlib.font_manager as fm
import matplotlib.pyplot as plt


def check_system_info():
    """检查系统信息"""
    print("=== 系统信息 ===")
    print(f"操作系统: {platform.system()} {platform.release()}")
    print(f"Python 版本: {platform.python_version()}")
    print(f"matplotlib 版本: {plt.matplotlib.__version__}")
    print()


def check_available_fonts():
    """检查可用字体"""
    print("=== 可用字体检查 ===")

    # 获取所有字体
    all_fonts = [f.name for f in fm.fontManager.ttflist]

    # 中文字体关键词
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
        "kaiti",
        "fangsong",
        "simsun",
        "pingfang",
        "hiragino",
        "stheit",
        "arial",
        "unicode",
    ]

    # 查找可能的中文字体
    chinese_fonts = []
    for font in all_fonts:
        font_lower = font.lower()
        if any(keyword in font_lower for keyword in chinese_keywords):
            chinese_fonts.append(font)

    print(f"找到 {len(chinese_fonts)} 个可能的中文字体:")
    for font in sorted(chinese_fonts):
        print(f"  - {font}")

    if not chinese_fonts:
        print("⚠ 未找到中文字体！")
        print("请安装中文字体包：")
        if platform.system().lower() == "linux":
            print("  sudo apt install fonts-wqy-microhei fonts-noto-cjk")
        elif platform.system().lower() == "windows":
            print("  Windows 系统通常自带中文字体")
        elif platform.system().lower() == "darwin":
            print("  macOS 系统通常自带中文字体")

    print()
    return chinese_fonts


def test_font_rendering():
    """测试字体渲染"""
    print("=== 字体渲染测试 ===")

    # 测试不同字体
    test_fonts = [
        "WenQuanYi Micro Hei",
        "Noto Sans CJK SC",
        "Source Han Sans SC",
        "Microsoft YaHei",
        "SimHei",
        "PingFang SC",
        "DejaVu Sans",
    ]

    for font in test_fonts:
        try:
            # 设置字体
            plt.rcParams["font.sans-serif"] = [font]
            plt.rcParams["axes.unicode_minus"] = False

            # 创建测试图形
            fig, ax = plt.subplots(figsize=(6, 4))
            ax.text(0.5, 0.5, "中文字体测试", fontsize=16, ha="center", va="center")
            ax.set_title(f"字体: {font}")
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)

            # 保存测试图片
            test_file = f'output/font_test_{font.replace(" ", "_")}.png'
            os.makedirs("output", exist_ok=True)
            plt.savefig(test_file, dpi=100, bbox_inches="tight")
            plt.close(fig)

            print(f"✓ {font} - 测试图片已保存: {test_file}")

        except Exception as e:
            print(f"✗ {font} - 测试失败: {e}")


def check_font_cache():
    """检查字体缓存"""
    print("=== 字体缓存检查 ===")

    try:
        cache_dir = plt.matplotlib.get_cachedir()
        print(f"缓存目录: {cache_dir}")

        if os.path.exists(cache_dir):
            cache_files = os.listdir(cache_dir)
            print(f"缓存文件数量: {len(cache_files)}")

            # 检查字体缓存文件
            font_cache_files = [f for f in cache_files if "font" in f.lower()]
            if font_cache_files:
                print(f"字体缓存文件: {font_cache_files}")
            else:
                print("未找到字体缓存文件")
        else:
            print("缓存目录不存在")

    except Exception as e:
        print(f"缓存检查失败: {e}")

    print()


def clear_font_cache():
    """清除字体缓存"""
    print("=== 清除字体缓存 ===")

    try:
        cache_dir = plt.matplotlib.get_cachedir()
        if os.path.exists(cache_dir):
            import shutil

            shutil.rmtree(cache_dir)
            print(f"✓ 已清除缓存目录: {cache_dir}")
        else:
            print("缓存目录不存在，无需清除")

        # 重新构建字体管理器
        fm._rebuild()
        print("✓ 已重新构建字体管理器")

    except Exception as e:
        print(f"✗ 清除缓存失败: {e}")

    print()


def install_fonts_ubuntu():
    """Ubuntu 系统字体安装"""
    if platform.system().lower() != "linux":
        return

    print("=== Ubuntu 字体安装 ===")

    try:
        # 检查是否已安装字体
        result = subprocess.run(["fc-list", ":lang=zh"], capture_output=True, text=True)

        if result.returncode == 0 and result.stdout.strip():
            print("✓ 已安装中文字体")
            print("已安装的字体:")
            for line in result.stdout.strip().split("\n")[:5]:  # 只显示前5个
                print(f"  - {line}")
        else:
            print("⚠ 未检测到中文字体")
            print("正在安装中文字体...")

            # 安装字体
            install_commands = [
                "sudo apt update",
                "sudo apt install -y fonts-wqy-microhei fonts-noto-cjk",
                "sudo fc-cache -fv",
            ]

            for cmd in install_commands:
                print(f"执行: {cmd}")
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                if result.returncode == 0:
                    print(f"✓ 成功: {cmd}")
                else:
                    print(f"✗ 失败: {cmd}")
                    print(f"错误: {result.stderr}")

    except Exception as e:
        print(f"✗ 字体安装检查失败: {e}")

    print()


def main():
    """主函数"""
    print("中文字体诊断工具")
    print("=" * 50)

    # 检查系统信息
    check_system_info()

    # 检查可用字体
    chinese_fonts = check_available_fonts()

    # 检查字体缓存
    check_font_cache()

    # 清除字体缓存
    clear_font_cache()

    # Ubuntu 系统字体安装
    install_fonts_ubuntu()

    # 测试字体渲染
    if chinese_fonts:
        test_font_rendering()
    else:
        print("⚠ 未找到中文字体，跳过渲染测试")

    print("=== 诊断完成 ===")
    print("如果问题仍然存在，请尝试：")
    print("1. 重启 Python 程序")
    print("2. 重启系统")
    print("3. 手动安装中文字体")
    print("4. 检查系统语言设置")


if __name__ == "__main__":
    main()
