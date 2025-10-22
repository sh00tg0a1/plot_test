# 中文字体设置指南

## 问题描述

matplotlib 默认不支持中文字体显示，会出现中文显示为方块的问题。

## 解决方案

### 1. 自动字体检测

`plot.py` 已经集成了自动中文字体检测功能，会按以下优先级尝试设置字体：

1. **SimHei** (黑体) - Windows 系统
2. **Microsoft YaHei** (微软雅黑) - Windows 系统
3. **PingFang SC** (苹方) - macOS 系统
4. **Hiragino Sans GB** (冬青黑体) - macOS 系统
5. **Source Han Sans** (思源黑体) - 跨平台
6. **Noto Sans CJK SC** (Noto Sans 中文) - 跨平台
7. **WenQuanYi Micro Hei** (文泉驿微米黑) - Linux 系统
8. **DejaVu Sans** - 备选字体

### 2. 手动安装中文字体

#### Windows 系统

1. **使用系统自带字体**：
   - 系统通常已包含 SimHei 和 Microsoft YaHei
   - 无需额外安装

2. **安装开源字体**：
   - 下载思源黑体：https://github.com/adobe-fonts/source-han-sans
   - 下载 Noto Sans：https://fonts.google.com/noto/specimen/Noto+Sans+SC

#### macOS 系统

1. **使用系统自带字体**：
   - 系统通常已包含 PingFang SC 和 Hiragino Sans GB
   - 无需额外安装

2. **安装开源字体**：
   - 使用 Homebrew：`brew install font-source-han-sans`
   - 或手动下载安装

#### Linux 系统

1. **Ubuntu/Debian**：
   ```bash
   sudo apt-get install fonts-wqy-microhei
   sudo apt-get install fonts-noto-cjk
   ```

2. **CentOS/RHEL**：
   ```bash
   sudo yum install wqy-microhei-fonts
   sudo yum install google-noto-sans-cjk-fonts
   ```

3. **手动安装**：
   - 下载字体文件到 `~/.fonts/` 目录
   - 运行 `fc-cache -fv` 刷新字体缓存

### 3. 测试字体设置

运行字体测试脚本：

```bash
# 测试中文字体显示
uv run python test_font.py

# 或
python test_font.py
```

### 4. 验证字体设置

检查 matplotlib 可用的字体：

```python
import matplotlib.font_manager as fm

# 查看所有可用字体
fonts = [f.name for f in fm.fontManager.ttflist]
chinese_fonts = [f for f in fonts if 'SimHei' in f or 'YaHei' in f or 'PingFang' in f or 'Source' in f or 'Noto' in f]
print("可用的中文字体:", chinese_fonts)
```

### 5. 常见问题解决

#### 问题1：字体仍然显示为方块
**解决方案**：
1. 确认字体已正确安装
2. 清除 matplotlib 字体缓存：删除 `~/.matplotlib/fontlist-v*.json`
3. 重启 Python 程序

#### 问题2：字体设置不生效
**解决方案**：
1. 检查字体名称是否正确
2. 使用 `matplotlib.font_manager.findSystemFonts()` 查找字体路径
3. 手动指定字体路径

#### 问题3：负号显示异常
**解决方案**：
```python
plt.rcParams['axes.unicode_minus'] = False
```

### 6. 推荐字体

#### 开源字体（推荐）
- **思源黑体 (Source Han Sans)**：Adobe 开源，支持多语言
- **Noto Sans CJK**：Google 开源，支持中日韩文字
- **文泉驿微米黑**：Linux 系统常用

#### 商业字体
- **微软雅黑**：Windows 系统自带
- **苹方**：macOS 系统自带
- **黑体**：Windows 系统自带

### 7. 字体文件位置

#### Windows
- 系统字体：`C:\Windows\Fonts\`
- 用户字体：`C:\Users\[用户名]\AppData\Local\Microsoft\Windows\Fonts\`

#### macOS
- 系统字体：`/System/Library/Fonts/`
- 用户字体：`~/Library/Fonts/`

#### Linux
- 系统字体：`/usr/share/fonts/`
- 用户字体：`~/.fonts/`

### 8. 验证设置

运行以下代码验证字体设置：

```python
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 设置字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# 测试中文显示
fig, ax = plt.subplots()
ax.text(0.5, 0.5, '中文字体测试', fontsize=20, ha='center')
ax.set_title('中文标题测试')
plt.show()
```

如果显示正常，说明字体设置成功！
