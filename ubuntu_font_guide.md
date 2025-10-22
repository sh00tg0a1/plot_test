# Ubuntu 系统中文字体设置指南

## 问题描述

在 Ubuntu 系统上使用 matplotlib 绘制中文图表时，可能出现中文显示为方块的问题。这是因为 Ubuntu 默认不包含中文字体。

## 解决方案

### 方法一：自动安装脚本（推荐）

运行项目中的自动安装脚本：

```bash
# 给脚本执行权限
chmod +x install_ubuntu_fonts.sh

# 运行安装脚本
./install_ubuntu_fonts.sh
```

### 方法二：手动安装

#### 1. 安装文泉驿字体（推荐）

```bash
# 安装文泉驿微米黑和正黑
sudo apt install fonts-wqy-microhei fonts-wqy-zenhei

# 刷新字体缓存
sudo fc-cache -fv
```

#### 2. 安装 Noto 字体（Google 开源）

```bash
# 安装 Noto Sans CJK
sudo apt install fonts-noto-cjk fonts-noto-cjk-extra

# 刷新字体缓存
sudo fc-cache -fv
```

#### 3. 安装思源字体（Adobe 开源）

```bash
# 安装思源黑体
sudo apt install fonts-source-han-sans fonts-source-han-serif

# 刷新字体缓存
sudo fc-cache -fv
```

#### 4. 安装其他中文字体

```bash
# 安装文鼎字体
sudo apt install fonts-arphic-ukai fonts-arphic-uming

# 安装 Android 字体
sudo apt install fonts-droid-fallback

# 刷新字体缓存
sudo fc-cache -fv
```

### 方法三：一键安装所有字体

```bash
# 安装所有推荐的中文字体
sudo apt install fonts-wqy-microhei fonts-wqy-zenhei fonts-noto-cjk fonts-source-han-sans fonts-arphic-ukai fonts-arphic-uming fonts-droid-fallback

# 刷新字体缓存
sudo fc-cache -fv
```

## 验证安装

### 1. 检查已安装的字体

```bash
# 查看所有中文字体
fc-list :lang=zh

# 查看特定字体
fc-list | grep -i "wenquanyi\|noto\|source"
```

### 2. 运行测试脚本

```bash
# 测试 Ubuntu 中文字体
python test_ubuntu_fonts.py

# 或运行通用测试
python test_font.py
```

### 3. 手动验证

```python
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 查看可用字体
fonts = [f.name for f in fm.fontManager.ttflist]
chinese_fonts = [f for f in fonts if any(x in f.lower() for x in ['wenquanyi', 'noto', 'source', 'ar pl'])]
print("可用的中文字体:", chinese_fonts)

# 测试中文显示
plt.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei', 'Noto Sans CJK SC', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots()
ax.text(0.5, 0.5, '中文字体测试', fontsize=20, ha='center')
ax.set_title('Ubuntu 中文显示测试')
plt.show()
```

## 常见问题解决

### 问题1：字体安装后仍显示方块

**解决方案**：
1. 清除 matplotlib 字体缓存：
   ```bash
   rm -rf ~/.matplotlib
   ```
2. 重启 Python 程序
3. 检查字体是否正确安装：
   ```bash
   fc-list | grep -i "wenquanyi"
   ```

### 问题2：字体设置不生效

**解决方案**：
1. 确认字体名称正确
2. 使用完整路径：
   ```python
   import matplotlib.font_manager as fm
   font_path = '/usr/share/fonts/truetype/wqy/wqy-microhei.ttc'
   plt.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei']
   ```

### 问题3：权限问题

**解决方案**：
1. 使用用户字体目录：
   ```bash
   mkdir -p ~/.fonts
   cp font_file.ttf ~/.fonts/
   fc-cache -fv
   ```

### 问题4：字体显示模糊

**解决方案**：
1. 调整 DPI 设置：
   ```python
   plt.rcParams['figure.dpi'] = 100
   plt.rcParams['savefig.dpi'] = 300
   ```

## 推荐字体组合

### 基础组合（最小安装）
```bash
sudo apt install fonts-wqy-microhei
```

### 完整组合（推荐）
```bash
sudo apt install fonts-wqy-microhei fonts-wqy-zenhei fonts-noto-cjk
```

### 专业组合（所有字体）
```bash
sudo apt install fonts-wqy-microhei fonts-wqy-zenhei fonts-noto-cjk fonts-source-han-sans fonts-arphic-ukai fonts-arphic-uming fonts-droid-fallback
```

## 字体特点

- **文泉驿微米黑**：Ubuntu 默认推荐，显示效果好
- **文泉驿正黑**：适合标题和重要文本
- **Noto Sans CJK**：Google 开源，支持多语言
- **思源黑体**：Adobe 开源，专业设计
- **文鼎字体**：传统中文字体

## 性能优化

### 1. 减少字体加载时间
```python
# 只加载需要的字体
plt.rcParams['font.sans-serif'] = ['WenQuanYi Micro Hei']
```

### 2. 缓存字体
```python
# 预加载字体
import matplotlib.font_manager as fm
fm._rebuild()
```

### 3. 使用系统字体
```python
# 使用系统默认字体
plt.rcParams['font.family'] = 'sans-serif'
```

## 测试命令

```bash
# 运行完整测试
python test_ubuntu_fonts.py

# 运行绘图测试
python test_plot.py

# 运行字体测试
python test_font.py
```

## 故障排除

如果遇到问题，请按以下顺序检查：

1. **检查字体是否安装**：
   ```bash
   fc-list :lang=zh
   ```

2. **清除缓存**：
   ```bash
   rm -rf ~/.matplotlib
   sudo fc-cache -fv
   ```

3. **重启程序**：
   ```bash
   python test_ubuntu_fonts.py
   ```

4. **检查权限**：
   ```bash
   ls -la /usr/share/fonts/
   ```

5. **查看错误日志**：
   ```bash
   python -c "import matplotlib; print(matplotlib.get_data_path())"
   ```

按照本指南操作后，Ubuntu 系统上的 matplotlib 应该能够正确显示中文了！
