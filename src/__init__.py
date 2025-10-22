"""
plot_test 核心模块

包含数据生成和绘图功能
"""

from .data import (
    generate_time_series_data,
    generate_sales_data,
    generate_customer_data,
    save_dataframe
)

from .plot import PlotGenerator

__version__ = "0.1.0"
__author__ = "plot_test team"

__all__ = [
    "generate_time_series_data",
    "generate_sales_data", 
    "generate_customer_data",
    "save_dataframe",
    "PlotGenerator"
]
