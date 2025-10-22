#!/bin/bash

# Ubuntu 中文字体安装脚本
# 用于解决 matplotlib 中文显示问题

set -e  # 遇到错误时退出

echo "=== Ubuntu 中文字体安装脚本 ==="
echo "正在安装中文字体包..."

# 检查是否为 Ubuntu/Debian 系统
if ! command -v apt &> /dev/null; then
    echo "错误: 此脚本仅适用于 Ubuntu/Debian 系统"
    exit 1
fi

# 检查 sudo 权限
if ! sudo -n true 2>/dev/null; then
    echo "需要 sudo 权限来安装字体包"
    echo "请确保您有 sudo 权限"
fi

# 更新包列表
echo "1. 更新包列表..."
sudo apt update

# 安装基础中文字体
echo "2. 安装基础中文字体..."
sudo apt install -y fonts-wqy-microhei fonts-wqy-zenhei

# 安装 Noto 字体
echo "3. 安装 Noto 字体..."
sudo apt install -y fonts-noto-cjk fonts-noto-cjk-extra

# 安装思源字体
echo "4. 安装思源字体..."
sudo apt install -y fonts-source-han-sans fonts-source-han-serif || echo "思源字体安装失败，继续..."

# 安装文鼎字体
echo "5. 安装文鼎字体..."
sudo apt install -y fonts-arphic-ukai fonts-arphic-uming || echo "文鼎字体安装失败，继续..."

# 安装其他中文字体
echo "6. 安装其他中文字体..."
sudo apt install -y fonts-droid-fallback || echo "Droid 字体安装失败，继续..."

# 刷新字体缓存
echo "7. 刷新字体缓存..."
sudo fc-cache -fv

# 显示已安装的中文字体
echo "8. 检查已安装的中文字体..."
echo "已安装的中文字体："
fc-list :lang=zh | head -10

# 检查 matplotlib 缓存
echo "9. 清除 matplotlib 缓存..."
if [ -d "$HOME/.matplotlib" ]; then
    rm -rf "$HOME/.matplotlib"
    echo "✓ 已清除 matplotlib 缓存"
else
    echo "matplotlib 缓存目录不存在"
fi

echo ""
echo "=== 字体安装完成！ ==="
echo ""
echo "测试命令："
echo "  python fix_chinese_font.py"
echo "  python test/font_diagnosis.py"
echo "  python test/test_font.py"
echo ""
echo "如果仍有问题，请尝试："
echo "1. 重启 Python 程序"
echo "2. 重启系统"
echo "3. 检查系统语言设置"
