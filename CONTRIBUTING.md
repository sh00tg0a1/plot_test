# 贡献指南

感谢您对 plot_test 项目的关注！我们欢迎各种形式的贡献。

## 如何贡献

### 1. Fork 项目

1. 点击项目页面右上角的 "Fork" 按钮
2. 将 fork 的仓库克隆到本地：

   ```bash
   git clone https://github.com/your-username/plot_test.git
   cd plot_test
   ```

### 2. 创建开发环境

```bash
# 安装 uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# 安装依赖
uv sync

# 激活虚拟环境
uv shell
```

### 3. 创建功能分支

```bash
git checkout -b feature/your-feature-name
```

### 4. 进行开发

- 在 `src/` 目录下添加新功能
- 在 `test/` 目录下添加测试
- 更新文档

### 5. 运行测试

```bash
# 运行所有测试
uv run python test/test_data_generation.py
uv run python test/test_plot.py
uv run python test/test_font.py

# 运行代码检查
uv run flake8 src/ test/
uv run black src/ test/
```

### 6. 提交更改

```bash
git add .
git commit -m "Add: 描述您的更改"
git push origin feature/your-feature-name
```

### 7. 创建 Pull Request

1. 在 GitHub 上创建 Pull Request
2. 详细描述您的更改
3. 等待代码审查

## 开发规范

### 代码风格

- 使用 Black 进行代码格式化
- 使用 Flake8 进行代码检查
- 遵循 PEP 8 规范

### 提交信息

使用以下格式：
- `Add: 新功能`
- `Fix: 修复问题`
- `Update: 更新功能`
- `Docs: 文档更新`
- `Test: 测试相关`

### 测试要求

- 新功能必须包含测试
- 测试覆盖率应保持或提高
- 所有测试必须通过

## 项目结构

```
plot_test/
├── src/                    # 核心模块
│   ├── __init__.py
│   ├── data.py            # 数据生成
│   └── plot.py            # 绘图功能
├── test/                   # 测试模块
│   ├── __init__.py
│   ├── test_data_generation.py
│   ├── test_plot.py
│   ├── test_font.py
│   └── test_ubuntu_fonts.py
├── data/                   # 数据文件
├── output/                 # 输出文件
├── .github/workflows/      # CI/CD
├── pyproject.toml         # 项目配置
└── README.md              # 项目说明
```

## 功能开发

### 添加新的图表类型

1. 在 `src/plot.py` 中添加新方法
2. 在 `test/test_plot.py` 中添加测试
3. 更新文档

### 添加新的数据生成功能

1. 在 `src/data.py` 中添加新函数
2. 在 `test/test_data_generation.py` 中添加测试
3. 更新文档

## 问题报告

如果您发现了 bug 或有功能建议，请：

1. 检查是否已有相关 issue
2. 创建新的 issue，详细描述问题
3. 提供复现步骤（如果是 bug）

## 文档贡献

- 更新 README.md
- 添加使用示例
- 改进代码注释
- 创建教程文档

## 许可证

本项目采用 MIT 许可证。贡献代码即表示您同意将代码在 MIT 许可证下发布。

## 联系方式

- 项目主页：https://github.com/your-username/plot_test
- 问题反馈：https://github.com/your-username/plot_test/issues

感谢您的贡献！



