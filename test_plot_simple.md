# test_plot.py 简化版使用说明

## 功能概述

`test_plot.py` 现在使用 `data.py` 生成的真实数据，创建单张图表，不再使用复杂的仪表板。

## 数据来源

- **时间序列数据**：`generate_time_series_data()` - 30天的时间序列
- **销售数据**：`generate_sales_data()` - 10个产品，6个月的销售数据
- **客户数据**：`generate_customer_data()` - 100个客户的基本信息

## 生成的图表

### 1. 环形图 - 客户年龄分布
- **数据来源**：客户数据中的年龄字段
- **处理方式**：按年龄分组（18-25, 26-35, 36-45, 46-55, 56-65, 65+）
- **输出文件**：`output/customer_age_distribution.png`

### 2. 折线图 - 时间序列趋势
- **数据来源**：时间序列数据
- **显示内容**：30天的数值趋势
- **输出文件**：`output/time_series_trend.png`

### 3. 分组柱状图 - 产品销售对比
- **数据来源**：销售数据按产品汇总
- **显示内容**：各产品的销量和收入对比
- **输出文件**：`output/product_sales_comparison.png`

### 4. 堆叠柱状图 - 月度销售构成
- **数据来源**：销售数据按月份汇总
- **显示内容**：各月的销量和收入构成
- **输出文件**：`output/monthly_sales_composition.png`

## 使用方法

### 测试模式（默认）
```bash
# 生成所有图表并保存
uv run python test_plot.py

# 或者
python test_plot.py
```

### 展示模式
```bash
# 逐个显示图表窗口
uv run python test_plot.py show

# 或者
python test_plot.py show
```

## 输出说明

### 控制台输出
```
开始测试绘图功能...
1. 生成时间序列数据...
   ✓ 时间序列数据生成完成，形状: (30, 4)
2. 生成销售数据...
   ✓ 销售数据生成完成，形状: (60, 7)
3. 生成客户数据...
   ✓ 客户数据生成完成，形状: (100, 7)

4. 生成环形图（客户年龄分布）...
   ✓ 环形图已保存到 output/customer_age_distribution.png
5. 生成折线图（时间序列趋势）...
   ✓ 折线图已保存到 output/time_series_trend.png
6. 生成分组柱状图（产品销售对比）...
   ✓ 分组柱状图已保存到 output/product_sales_comparison.png
7. 生成堆叠柱状图（月度销售构成）...
   ✓ 堆叠柱状图已保存到 output/monthly_sales_composition.png

所有测试完成！

生成的图片文件:
- output/customer_age_distribution.png
- output/time_series_trend.png
- output/product_sales_comparison.png
- output/monthly_sales_composition.png

正在显示图表...
```

### 文件输出
- 所有图片保存到 `output/` 目录
- PNG 格式，高分辨率（300 DPI）
- 使用新的专业配色方案

## 技术特性

- **真实数据**：使用 `data.py` 生成的数据，不是模拟数据
- **单张图表**：每个图表独立显示，不包含复杂的仪表板
- **专业配色**：使用 9 种专业配色方案
- **数据聚合**：自动对数据进行分组和汇总
- **错误处理**：完整的异常捕获和提示

## 数据特点

- **时间序列数据**：包含趋势和季节性
- **销售数据**：包含产品、月份、销量、价格、收入等信息
- **客户数据**：包含年龄、收入、购买次数、性别、城市等信息

## 注意事项

1. 确保 `data.py` 模块可用
2. 首次运行会自动创建 `output/` 目录
3. 图表窗口需要手动关闭才能继续
4. 数据每次运行都会重新生成（使用随机种子确保一致性）
