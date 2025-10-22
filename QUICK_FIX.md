# 中文字体快速修复指南

## 问题描述

matplotlib 中文显示为方块或乱码。

## 快速解决方案

### 方法一：一键修复（推荐）

```bash
# 运行自动修复脚本
python fix_chinese_font.py
```

### 方法二：Ubuntu 系统专用

```bash
# 给脚本执行权限
chmod +x install_ubuntu_fonts.sh

# 运行安装脚本
./install_ubuntu_fonts.sh
```

### 方法三：手动修复

#### 1. 清除缓存

```bash
# 清除 matplotlib 缓存
rm -rf ~/.matplotlib

# 或者使用 Python
python -c "import matplotlib; print(matplotlib.get_cachedir())"
```

#### 2. 安装字体（Ubuntu）

```bash
# 安装中文字体
sudo apt install fonts-wqy-microhei fonts-noto-cjk

# 刷新字体缓存
sudo fc-cache -fv
```

#### 3. 重启 Python 程序

```bash
# 重新运行测试
python test/test_font.py
```

## 诊断工具

如果问题仍然存在，运行诊断工具：

```bash
# 详细诊断
python test/font_diagnosis.py

# 测试字体显示
python test/test_font.py
```

## 常见问题

### 问题1：字体安装后仍显示方块

**解决方案**：
1. 清除 matplotlib 缓存：`rm -rf ~/.matplotlib`
2. 重启 Python 程序
3. 检查字体是否正确安装：`fc-list :lang=zh`

### 问题2：权限问题

**解决方案**：
```bash
# 使用用户字体目录
mkdir -p ~/.fonts
# 将字体文件复制到用户目录
```

### 问题3：字体设置不生效

**解决方案**：
```python
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 强制重建字体管理器
fm._rebuild()

# 设置字体
plt.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei']
plt.rcParams['axes.unicode_minus'] = False
```

## 验证修复

运行以下命令验证修复是否成功：

```bash
# 测试中文显示
python -c "
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei']
plt.rcParams['axes.unicode_minus'] = False
fig, ax = plt.subplots()
ax.text(0.5, 0.5, '中文字体测试', fontsize=16, ha='center')
ax.set_title('测试标题')
plt.savefig('test.png')
plt.close()
print('测试图片已保存为 test.png')
"
```

如果生成的图片中中文显示正常，说明修复成功！

## 系统特定解决方案

### Ubuntu/Debian

```bash
sudo apt install fonts-wqy-microhei fonts-noto-cjk fonts-source-han-sans
sudo fc-cache -fv
```

### CentOS/RHEL

```bash
sudo yum install wqy-microhei-fonts google-noto-sans-cjk-fonts
sudo fc-cache -fv
```

### Windows

Windows 系统通常自带中文字体，如果仍有问题：
1. 检查系统语言设置
2. 安装中文字体包
3. 重启 Python 程序

### macOS

macOS 系统通常自带中文字体，如果仍有问题：
1. 检查系统语言设置
2. 安装 Xcode Command Line Tools
3. 重启 Python 程序

## 联系支持

如果以上方法都无法解决问题，请：

1. 运行诊断工具：`python test/font_diagnosis.py`
2. 收集诊断信息
3. 提交 issue 到项目仓库
