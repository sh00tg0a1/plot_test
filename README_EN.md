# Plot Test Project

[![CI](https://github.com/sh00tg0a1/plot_test/workflows/CI/badge.svg)](https://github.com/sh00tg0a1/plot_test/actions)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

[中文](README.md) | English

A Python data generation and plotting test project managed with uv, supporting multiple chart types and Chinese font display.

## Project Structure

```text
plot_test/
├── src/                       # Core modules
│   ├── __init__.py
│   ├── data.py                # Data generation module
│   └── plot.py                # Plotting module
├── test/                      # Test modules
│   ├── __init__.py
│   ├── test_data_generation.py # Data generation tests
│   ├── test_plot.py           # Plotting function tests
│   ├── test_font.py           # Font tests
│   └── test_ubuntu_fonts.py   # Ubuntu font tests
├── data/                      # Generated data files directory
├── output/                    # Generated image files directory
├── .github/workflows/         # CI/CD configuration
├── pyproject.toml            # Project configuration file
├── uv.lock                   # Dependency lock file
├── LICENSE                   # MIT License
├── CONTRIBUTING.md           # Contribution guide
└── README.md                 # Project documentation
```

## Features

### Data Generation

- **Time Series Data**
  - Customizable start date and duration
  - Built-in trend, seasonality, and noise
  - Support for daily, weekly, monthly frequencies

- **Sales Data**
  - Customizable product quantity and time period
  - Automatic seasonal adjustments
  - Includes sales, price, revenue, category, region

- **Customer Data**
  - Random age, income, purchase frequency
  - Gender, city, registration date
  - Supports large-scale data generation

- **Multiple Export Formats**
  - CSV (default format)
  - Excel (.xlsx)
  - Parquet (columnar storage)
  - JSON (structured data)

### Plotting Features

`plot.py` module provides the following plotting capabilities:

1. **Donut Chart** (`donut_chart`)
   - Support for data dictionaries and pandas Series
   - Automatic color assignment
   - Percentage display
   - Clean white background design

2. **Line Chart** (`line_chart`)
   - Multiple line comparison support
   - Custom line styles and colors
   - **Large-scale data optimization**: Support 100+ series × 100+ points
   - Smart legend: Auto-sampling when series > 10
   - Adaptive rendering: Auto-simplify markers and line width for many series
   - Clean grid-free design

3. **Bar Chart** (`bar_chart`)
   - **Grouped Bar Chart**: Side-by-side display of multiple series
   - **Stacked Bar Chart**: Stacked display with auto-alignment
   - Custom color support
   - Smart legend display
   - Clean white background design

4. **Image Export**
   - **Base64 Encoding**: `figure_to_base64()` method
   - **File Save**: PNG, JPG, SVG format support
   - **High Resolution**: Default 300 DPI

5. **Dashboard** (`create_dashboard`)
   - Multi-chart combination display
   - Automatic layout
   - Unified title and style

6. **Professional Design**
   - **Color Palette**: Predefined 9 professional colors
   - **Clean Style**: White background, no grid, minimal legend
   - **Chinese Font Support**: Auto-detect system fonts (Windows/Linux/macOS)
   - **Color Scheme**: `#5470c6, #91cc75, #fac858, #ee6666, #73c0de, #3ba272, #fc8452, #9a60b4, #ea7ccc`

## Installation and Setup

### 1. Install uv Package Manager

**Windows PowerShell:**

```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

**Ubuntu/Linux:**

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Or use pip:**

```bash
pip install uv
```

### 2. Chinese Font Setup (Optional)

Built-in auto-detection for Windows, Linux, and macOS systems.

#### Ubuntu/Linux System

**Automatic Installation (Recommended):**

```bash
chmod +x install_ubuntu_fonts.sh
./install_ubuntu_fonts.sh
```

**Manual Installation:**

```bash
sudo apt install fonts-wqy-microhei fonts-noto-cjk
sudo fc-cache -fv
```

#### Windows System

System fonts (Microsoft YaHei, SimHei, etc.) are pre-installed.

If font issues occur, run:

```bash
python fix_windows_font.py
```

#### Font Testing

```bash
# General test
python test/test_font.py

# Ubuntu specific test
python test/test_ubuntu_fonts.py

# Windows specific test
python test_windows_font.py

# Quick test
python quick_font_test.py
```

### 3. Install Project Dependencies

```bash
uv sync
```

### 4. Activate Virtual Environment

```bash
uv shell
```

## Project Dependencies

- **pandas**: Data processing and analysis
- **numpy**: Numerical computing
- **matplotlib**: Data visualization
- **seaborn**: Statistical visualization
- **openpyxl**: Excel file processing
- **pyarrow**: Parquet format support

### Development Dependencies

- **pytest**: Testing framework
- **black**: Code formatting
- **ruff**: Fast code linting and auto-fixing

## Usage

### Generate Data

```bash
# Generate all data files
uv run python src/data.py

# Or run directly
python src/data.py
```

### Test Plotting Functions

```bash
# Test mode (generate and save all charts)
uv run python test/test_plot.py

# Interactive display mode (show charts one by one)
uv run python test/test_plot.py show

# Demo with 100 series large-scale data example
uv run python src/plot.py
```

### Use Plotting Module

```python
from src.plot import PlotGenerator
from src.data import generate_time_series_data

# Create plotter (auto-detect and set Chinese fonts)
plotter = PlotGenerator()

# Generate data
data = generate_time_series_data(days=30)

# Create line chart
fig = plotter.line_chart(data, 'date', ['value'], "Time Series Trend")

# Save image
plotter.save_figure(fig, "my_chart", "png")

# Convert to base64
base64_str = plotter.figure_to_base64(fig)
```

## Examples

### 1. Donut Chart

```python
data = {
    'Category A': 30,
    'Category B': 25,
    'Category C': 20,
    'Category D': 15,
    'Category E': 10
}

fig = plotter.donut_chart(data, "Sales Distribution")
plotter.save_figure(fig, "donut_example")
```

### 2. Line Chart

```python
import pandas as pd

data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [100, 120, 115, 130, 140],
    'Profit': [30, 35, 32, 40, 45]
})

fig = plotter.line_chart(data, 'Month', ['Sales', 'Profit'], "Monthly Trend")
plotter.save_figure(fig, "line_example")
```

### 3. Bar Chart

```python
# Grouped bar chart
fig = plotter.bar_chart(
    data, 'Month', ['Sales', 'Profit'],
    "Monthly Comparison", chart_type='grouped'
)

# Stacked bar chart
fig = plotter.bar_chart(
    data, 'Month', ['Sales', 'Profit'],
    "Monthly Composition", chart_type='stacked'
)
```

## uv Common Commands

```bash
# Sync dependencies
uv sync

# Add new dependency
uv add package-name

# Add dev dependency
uv add --dev package-name

# Run Python script
uv run python data.py

# Activate virtual environment
uv shell

# Run tests
uv run python test_data_generation.py
```

## Development Workflow

1. Activate virtual environment: `uv shell`
2. Edit code
3. Run tests: `uv run python test/test_data_generation.py`
4. Generate data: `uv run python test/test_plot.py`
5. Format code: `uv run black .`
6. Lint code: `uv run ruff check .`
7. Auto-fix: `uv run ruff check --fix .`

## Contributing

We welcome all forms of contributions! Please check [CONTRIBUTING.md](CONTRIBUTING.md) to learn how to participate in project development.

### Quick Start

1. Fork this project
2. Create feature branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -m 'Add some feature'`
4. Push branch: `git push origin feature/your-feature`
5. Create Pull Request

## License

This project is licensed under the [MIT License](LICENSE).

## Related Links

- [Project Homepage](https://github.com/sh00tg0a1/plot_test)
- [Issue Tracker](https://github.com/sh00tg0a1/plot_test/issues)
- [Ubuntu Font Setup Guide](ubuntu_font_guide.md)
- [Quick Fix Guide](QUICK_FIX.md)
