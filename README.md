# Plot Test 项目

[![CI](https://github.com/sh00tg0a1/plot_test/workflows/CI/badge.svg)](https://github.com/sh00tg0a1/plot_test/actions)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

中文 | [English](README_EN.md)

这是一个使用 uv 管理的 Python 数据生成和绘图测试项目，支持多种图表类型和中文字体显示。

## 项目结构

```text
plot_test/
├── src/                       # 核心模块
│   ├── __init__.py
│   ├── data.py                # 数据生成模块
│   └── plot.py                # 绘图模块
├── test/                      # 测试模块
│   ├── __init__.py
│   ├── test_data_generation.py # 数据生成测试
│   ├── test_plot.py           # 绘图功能测试
│   ├── test_font.py           # 字体测试
│   └── test_ubuntu_fonts.py   # Ubuntu 字体测试
├── data/                      # 生成的数据文件目录
├── output/                    # 生成的图片文件目录
├── .github/workflows/         # CI/CD 配置
├── pyproject.toml            # 项目配置文件
├── uv.lock                   # 依赖锁定文件
├── LICENSE                   # MIT 许可证
├── CONTRIBUTING.md           # 贡献指南
└── README.md                 # 项目说明
```

## 功能特性

### 数据生成功能

`data.py` 模块提供以下数据生成功能：

1. **时间序列数据** (`generate_time_series_data`)
   - 生成带趋势和季节性的时间序列数据
   - 支持自定义时间范围和频率
   - 包含分类和地区信息

2. **销售数据** (`generate_sales_data`)
   - 生成产品销售数据
   - 包含销量、价格、收入等信息
   - 支持季节性调整和随机波动

3. **客户数据** (`generate_customer_data`)
   - 生成客户基本信息
   - 包含年龄、收入、购买次数等字段
   - 支持多个城市和性别分布

4. **数据保存** (`save_dataframe`)
   - 支持多种格式：CSV、Excel、Parquet、JSON
   - 自动创建数据目录
   - 提供保存进度反馈

### 绘图功能

`plot.py` 模块提供以下绘图功能：

1. **环形图** (`donut_chart`)
   - 支持数据字典和 pandas Series
   - 自动颜色分配
   - 百分比显示
   - 简洁白底设计

2. **折线图** (`line_chart`)
   - 支持多条线对比
   - 自定义线型和颜色
   - **大规模数据优化**：支持 100+ 系列 × 100+ 点
   - 智能图例：系列数量超过 10 时，自动抽样显示
   - 自适应渲染：大量系列时自动简化标记和线宽
   - 简洁无网格设计

3. **柱状图** (`bar_chart`)
   - **分组柱状图**：并排显示多个系列
   - **堆叠柱状图**：叠加显示多个系列（自动数据对齐）
   - 支持自定义颜色
   - 智能图例显示
   - 简洁白底设计

4. **图片导出功能**
   - **Base64 编码**：`figure_to_base64()` 方法
   - **文件保存**：支持 PNG、JPG、SVG 格式
   - **高分辨率**：默认 300 DPI

5. **仪表板功能** (`create_dashboard`)
   - 多图表组合显示
   - 自动布局
   - 统一标题和样式

6. **专业设计风格**
   - **颜色序列**：预定义 9 种专业配色
   - **简洁样式**：白色背景，无网格，简洁图例
   - **中文字体支持**：自动检测系统字体（Windows/Linux/macOS）
   - **配色方案**：`#5470c6, #91cc75, #fac858, #ee6666, #73c0de, #3ba272, #fc8452, #9a60b4, #ea7ccc`

## 安装和设置

### 1. 安装 uv 包管理器

**Windows PowerShell:**

```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

**Ubuntu/Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**或者使用 pip:**

```bash
pip install uv
```

### 2. 中文字体设置（可选）

项目已内置自动字体检测功能，支持 Windows、Linux、macOS 系统。

#### Ubuntu/Linux 系统

**自动安装（推荐）：**

```bash
chmod +x install_ubuntu_fonts.sh
./install_ubuntu_fonts.sh
```

**手动安装：**

```bash
sudo apt install fonts-wqy-microhei fonts-noto-cjk
sudo fc-cache -fv
```

#### Windows 系统

系统自带中文字体（微软雅黑、SimHei 等），无需额外安装。

如遇字体问题，运行：

```bash
python fix_windows_font.py
```

#### 字体测试

```bash
# 通用测试
python test/test_font.py

# Ubuntu 专用测试
python test/test_ubuntu_fonts.py

# Windows 专用测试
python test_windows_font.py

# 快速测试
python quick_font_test.py
```

### 3. 安装项目依赖

```bash
uv sync
```

### 4. 激活虚拟环境

```bash
uv shell
```

## 项目依赖

- **pandas**: 数据处理和分析
- **numpy**: 数值计算
- **matplotlib**: 绘图库
- **openpyxl**: Excel 文件支持
- **pyarrow**: Parquet 文件支持

## 开发依赖

- **pytest**: 测试框架
- **black**: 代码格式化
- **ruff**: 快速代码检查和自动修复

## 使用方法

### 生成数据文件

```bash
# 运行主程序生成所有数据文件
uv run python data.py

# 运行测试脚本
uv run python test_data_generation.py
```

### 绘图功能

```bash
# 运行绘图测试（生成所有图表）
uv run python test/test_plot.py

# 交互式展示图表
uv run python test/test_plot.py show

# 运行绘图演示（包含 100 系列大规模数据示例）
uv run python src/plot.py
```

### 生成的数据文件

运行 `data.py` 后，会在 `data/` 目录下生成以下文件：

- `time_series_data.csv` - 时间序列数据
- `sales_data.csv` - 销售数据
- `customer_data.csv` - 客户数据
- `sales_data.xlsx` - Excel 格式的销售数据

### 自定义数据生成

```python
from src.data import generate_time_series_data, save_dataframe

# 生成自定义时间序列数据
df = generate_time_series_data(start_date='2023-01-01', days=180, freq='W')

# 保存为不同格式
save_dataframe(df, 'my_data', 'csv')
save_dataframe(df, 'my_data', 'excel')
```

### 绘图使用示例

```python
from src.plot import PlotGenerator
from src.data import generate_sales_data
import pandas as pd

# 创建绘图器（自动检测并设置中文字体）
plotter = PlotGenerator()

# 示例数据
data = pd.DataFrame({
    '月份': ['1月', '2月', '3月', '4月'],
    '销售额': [100, 150, 200, 180],
    '利润': [20, 30, 40, 35]
})

# 1. 环形图
category_data = {'电子产品': 40, '服装': 30, '食品': 20, '其他': 10}
fig1 = plotter.donut_chart(category_data, "产品销售占比")
plotter.save_figure(fig1, "my_donut")  # 保存图片
base64_1 = plotter.figure_to_base64(fig1)  # 转换为 base64

# 2. 折线图
fig2 = plotter.line_chart(data, '月份', ['销售额', '利润'], "销售趋势")

# 3. 分组柱状图
fig3 = plotter.bar_chart(data, '月份', ['销售额', '利润'], 
                        "月度对比", chart_type='grouped')

# 4. 堆叠柱状图
fig4 = plotter.bar_chart(data, '月份', ['销售额', '利润'], 
                        "财务数据", chart_type='stacked')

# 5. 保存图片
plotter.save_figure(fig1, "my_donut_chart", "png")
```

## 常用命令

```bash
# 安装依赖
uv sync

# 添加新依赖
uv add package-name

# 添加开发依赖
uv add --dev package-name

# 运行 Python 脚本
uv run python data.py

# 激活虚拟环境
uv shell

# 运行测试
uv run python test_data_generation.py
```

## 开发工作流

1. 激活虚拟环境：`uv shell`
2. 编辑代码
3. 运行测试：`uv run python test/test_data_generation.py`
4. 生成数据：`uv run python test/test_plot.py`
5. 格式化代码：`uv run black .`
6. 检查代码：`uv run ruff check .`
7. 自动修复：`uv run ruff check --fix .`

## 贡献

我们欢迎各种形式的贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何参与项目开发。

### 快速开始

1. Fork 本项目
2. 创建功能分支：`git checkout -b feature/your-feature`
3. 提交更改：`git commit -m 'Add some feature'`
4. 推送分支：`git push origin feature/your-feature`
5. 创建 Pull Request

## 许可证

本项目采用 [MIT 许可证](LICENSE)。

## 相关链接

- [项目主页](https://github.com/sh00tg0a1/plot_test)
- [问题反馈](https://github.com/sh00tg0a1/plot_test/issues)
- [Ubuntu 字体设置指南](ubuntu_font_guide.md)
- [快速修复指南](QUICK_FIX.md)
