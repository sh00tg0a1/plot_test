# test_plot.py 使用说明

## 功能概述

`test_plot.py` 是一个测试和展示绘图功能的脚本，支持两种运行模式：

1. **测试模式**：生成并保存所有图表，显示测试结果
2. **展示模式**：逐个显示图表窗口

## 使用方法

### 1. 测试模式（默认）

```bash
# 运行完整测试
uv run python test_plot.py

# 或者
python test_plot.py
```

**功能：**
- 生成 5 种不同类型的图表
- 保存图片到 `output/` 目录
- 生成 base64 编码
- 最后显示所有图表

**生成的图片文件：**
- `output/test_donut_chart.png` - 环形图
- `output/test_line_chart.png` - 折线图
- `output/test_grouped_bar_chart.png` - 分组柱状图
- `output/test_stacked_bar_chart.png` - 堆叠柱状图
- `output/test_dashboard.png` - 综合仪表板

### 2. 展示模式

```bash
# 逐个展示图表
uv run python test_plot.py show

# 或者
python test_plot.py show
```

**功能：**
- 逐个显示图表窗口
- 每个图表单独展示
- 适合查看图表细节

## 图表类型

### 1. 环形图 (Donut Chart)
- **数据**：产品销售占比
- **特点**：环形设计，百分比显示
- **颜色**：自动分配美观颜色

### 2. 折线图 (Line Chart)
- **数据**：月度销售趋势
- **特点**：多条线对比，带标记点
- **功能**：显示销售额和利润趋势

### 3. 分组柱状图 (Grouped Bar Chart)
- **数据**：月度销售对比
- **特点**：并排显示多个系列
- **功能**：对比不同月份的销售额和利润

### 4. 堆叠柱状图 (Stacked Bar Chart)
- **数据**：月度财务数据
- **特点**：叠加显示多个系列
- **功能**：显示销售额、利润、成本的构成

### 5. 综合仪表板 (Dashboard)
- **内容**：包含上述所有图表类型
- **布局**：2x2 网格布局
- **功能**：一站式查看所有数据

## 输出说明

### 控制台输出
```
开始测试绘图功能...
1. 测试环形图...
   ✓ 环形图生成成功，base64 长度: 12345
   ✓ 环形图已保存到 output/test_donut_chart.png
...
所有测试完成！

生成的图片文件:
- output/test_donut_chart.png
- output/test_line_chart.png
- output/test_grouped_bar_chart.png
- output/test_stacked_bar_chart.png
- output/test_dashboard.png

正在显示图表...
```

### 文件输出
- 所有图片保存到 `output/` 目录
- PNG 格式，高分辨率（300 DPI）
- 自动创建目录（如果不存在）

## 技术特性

- **颜色序列**：使用预定义的 9 种专业配色
- **配色方案**：`#5470c6, #91cc75, #fac858, #ee6666, #73c0de, #3ba272, #fc8452, #9a60b4, #ea7ccc`
- **Base64 编码**：支持图片转 base64 字符串
- **高分辨率**：300 DPI 输出质量
- **自动布局**：智能调整图表布局
- **错误处理**：完整的异常捕获和提示

## 依赖要求

- matplotlib
- pandas
- numpy
- seaborn（用于样式）

## 注意事项

1. 确保已安装所有依赖包
2. 首次运行会自动创建 `output/` 目录
3. 图表窗口需要手动关闭才能继续
4. 在无图形界面的环境中，展示模式可能无法正常工作
