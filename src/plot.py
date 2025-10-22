"""
绘图模块
支持环形图、折线图、柱状图，以及图片转 base64 功能
"""

# flake8: noqa: E501
# pylint: disable=line-too-long

import base64
import io
import platform
from typing import Dict, List, Optional, Union

import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.lines import Line2D

# import platform  # 暂时未使用
# import matplotlib
# matplotlib.use("QtAgg")

DEFAULT_STYLE = "default"

# 预定义颜色序列
COLOR_PALETTE = [
    "#5470c6",
    "#91cc75",
    "#fac858",
    "#ee6666",
    "#73c0de",
    "#3ba272",
    "#fc8452",
    "#9a60b4",
    "#ea7ccc",
]

plt.style.use(DEFAULT_STYLE)


class PlotGenerator:
    """绘图生成器类"""

    def __init__(self, figsize=(10, 6), color_palette=COLOR_PALETTE):
        """
        初始化绘图生成器

        Args:
            style: matplotlib 样式
            figsize: 图片尺寸
        """
        # 设置中文字体
        self._setup_chinese_font()

        self.figsize = figsize
        self.current_fig = None
        self.current_ax = None
        self.color_palette = color_palette

    def _setup_chinese_font(self):
        """设置中文字体"""

        # 根据系统选择字体
        system = platform.system().lower()

        if system == "linux":
            chinese_fonts = [
                "WenQuanYi Micro Hei",
                "WenQuanYi Zen Hei",
                "Noto Sans CJK SC",
                "Source Han Sans SC",
                "Droid Sans Fallback",
                "AR PL UMing CN",
                "AR PL UKai CN",
            ]
        elif system == "windows":
            print("正在为 Windows 系统设置字体...")
            chinese_fonts = ["Microsoft YaHei", "SimHei", "SimSun"]
        elif system == "darwin":  # macOS
            chinese_fonts = [
                "PingFang SC",
                "Hiragino Sans GB",
                "STHeiti",
                "Arial Unicode MS",
            ]
        else:
            chinese_fonts = [
                "WenQuanYi Micro Hei",
                "Noto Sans CJK SC",
                "Source Han Sans SC",
                "DejaVu Sans",
            ]

        # 获取所有可用字体
        available_fonts = [f.name for f in fm.fontManager.ttflist]
        print(f"系统中共有 {len(available_fonts)} 个字体")

        # 尝试设置字体
        for font in chinese_fonts:
            if font in available_fonts:
                try:
                    plt.rcParams["font.sans-serif"] = [font]
                    plt.rcParams["axes.unicode_minus"] = False
                    print(f"✓ 使用中文字体: {font}")
                    break
                except Exception as e:
                    print(f"✗ 字体设置失败: {font}, 错误: {e}")
                    continue

    def _setup_figure(self, figsize: Optional[tuple] = None):
        """设置图形"""
        if figsize is None:
            figsize = self.figsize
        self.current_fig, self.current_ax = plt.subplots(figsize=figsize)
        # 统一白底
        self.current_fig.patch.set_facecolor("white")
        self.current_ax.set_facecolor("white")

        return self.current_fig, self.current_ax

    def _get_colors(self, n_colors: int) -> List[str]:
        """获取指定数量的颜色"""
        if n_colors <= len(self.color_palette):
            return self.color_palette[:n_colors]
        else:
            # 如果需要的颜色超过预定义的数量，循环使用
            colors = []
            for i in range(n_colors):
                colors.append(self.color_palette[i % len(self.color_palette)])
            return colors

    def donut_chart(
        self,
        data: Union[Dict, pd.Series, pd.DataFrame],
        title: str = "环形图",
        figsize: Optional[tuple] = None,
        colors: Optional[List[str]] = None,
        label_col: str = None,  # 标签字段名
        value_col: str = None,  # 数值字段名
    ) -> plt.Figure:
        """
        绘制环形图

        Args:
            data: 数据字典、pandas Series 或 DataFrame
            title: 图表标题
            figsize: 图片尺寸
            colors: 颜色列表
            label_col: 标签字段名（当 data 为 DataFrame 时使用）
            value_col: 数值字段名（当 data 为 DataFrame 时使用）

        Returns:
            matplotlib Figure 对象
        """
        fig, ax = self._setup_figure(figsize)

        # 处理数据
        if isinstance(data, dict):
            labels = list(data.keys())
            values = list(data.values())
        elif isinstance(data, pd.Series):
            labels = data.index.tolist()
            values = data.values.tolist()
        elif isinstance(data, pd.DataFrame):
            if label_col is None or value_col is None:
                raise ValueError("当 data 为 DataFrame 时，必须指定 " "label_col 和 value_col")
            labels = data[label_col].tolist()
            values = data[value_col].tolist()
        else:
            raise ValueError("数据必须是字典、pandas Series 或 DataFrame")

        # 设置颜色
        if colors is None:
            colors = self._get_colors(len(labels))

        # 根据扇形宽度调整显示参数
        n_items = len(labels)
        total_value = sum(values)

        # 计算最小扇形角度（以度为单位）
        min_angle = min(values) / total_value * 360

        # 根据最小扇形角度决定显示策略
        if min_angle < 5:  # 扇形角度小于5度时，不显示标签和百分比
            show_labels = False
            show_percent = False
            label_distance = 1.1
        elif min_angle < 10:  # 扇形角度5-10度时，只显示百分比
            show_labels = False
            show_percent = True
            label_distance = 1.1
        elif min_angle < 15:  # 扇形角度10-15度时，显示标签和百分比
            show_labels = True
            show_percent = True
            label_distance = 1.1
        else:  # 扇形角度大于15度时，正常显示
            show_labels = True
            show_percent = True
            label_distance = 1.1

        # 绘制外圆
        pie_result = ax.pie(
            values,
            labels=labels if show_labels else None,
            colors=colors,
            autopct="%1.1f%%" if show_percent else None,
            startangle=90,
            pctdistance=0.85,
            labeldistance=label_distance,
        )

        # 处理返回值
        wedges = pie_result[0]
        autotexts = pie_result[2] if len(pie_result) > 2 else []

        # 绘制内圆（创建环形效果）
        centre_circle = plt.Circle((0, 0), 0.50, fc="white")
        ax.add_artist(centre_circle)

        # 设置标题
        ax.set_title(title, fontsize=16, fontweight="bold", pad=20)

        # 美化文本
        for autotext in autotexts:
            autotext.set_color("white")
            autotext.set_fontweight("bold")

        # 当扇形较窄且不显示标签时，添加图例
        if min_angle < 10 and not show_labels:
            # 限制图例显示数量，避免图例过长
            max_legend_items = 15
            if n_items <= max_legend_items:
                ax.legend(wedges, labels, loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
            else:
                # 只显示前15个图例项
                legend_wedges = wedges[:max_legend_items]
                legend_labels = labels[:max_legend_items]
                legend_labels.append("...")
                ax.legend(
                    legend_wedges,
                    legend_labels,
                    loc="center left",
                    bbox_to_anchor=(1, 0, 0.5, 1),
                )

        return fig

    def line_chart(
        self,
        data: Union[pd.DataFrame, Dict],
        x_col: str = None,
        y_cols: List[str] = None,
        title: str = "折线图",
        xlabel: str = None,
        ylabel: str = None,
        figsize: Optional[tuple] = None,
        colors: Optional[List[str]] = None,
        line_styles: Optional[List[str]] = None,
        show_values: bool = False,  # 是否显示数值标签
    ) -> plt.Figure:
        """
        绘制折线图

        Args:
            data: 数据 DataFrame 或字典
            x_col: X 轴列名
            y_cols: Y 轴列名列表
            title: 图表标题
            xlabel: X 轴标签（默认使用 x_col）
            ylabel: Y 轴标签（默认为 "数值"）
            figsize: 图片尺寸
            colors: 颜色列表
            line_styles: 线型列表
            show_values: 是否在数据点上显示数值标签

        Returns:
            matplotlib Figure 对象
        """
        fig, ax = self._setup_figure(figsize)

        # 处理数据
        if isinstance(data, dict):
            df = pd.DataFrame(data)
        else:
            df = data.copy()

        # 设置默认值
        if x_col is None:
            x_col = df.columns[0]
        if y_cols is None:
            y_cols = [col for col in df.columns if col != x_col]

        # 设置颜色和线型
        if colors is None:
            colors = self._get_colors(len(y_cols))
        if line_styles is None:
            # 大量系列时统一使用实线，减少渲染负担
            if len(y_cols) > 20:
                line_styles = ["-"] * len(y_cols)
            else:
                line_styles = ["-", "--", "-.", ":"] * ((len(y_cols) // 4) + 1)
                line_styles = line_styles[: len(y_cols)]

        # 绘制折线
        use_markers = len(y_cols) <= 20
        for i, y_col in enumerate(y_cols):
            ax.plot(
                df[x_col],
                df[y_col],
                color=colors[i],
                linestyle=line_styles[i],
                linewidth=1.5 if len(y_cols) > 20 else 2.5,
                marker="o" if use_markers else None,
                markersize=4 if use_markers else 0,
                label=y_col,
            )

            # 添加数值标签（数据点过多时自动隐藏）
            if show_values and len(df) <= 20:  # 最多显示20个数据点
                x_data = df[x_col].values
                y_data = df[y_col].values
                for j, (x_val, y_val) in enumerate(zip(x_data, y_data)):
                    if not pd.isna(y_val):  # 只显示非空值
                        # 格式化数值，避免科学计数法
                        if y_val >= 1000000:
                            value_str = f"{y_val/1000000:.1f}M"
                        elif y_val >= 1000:
                            value_str = f"{y_val/1000:.1f}K"
                        else:
                            value_str = f"{y_val:.1f}"
                        ax.text(
                            x_val,
                            y_val,
                            value_str,
                            ha="center",
                            va="bottom",
                            fontsize=8,
                            color=colors[i],
                            alpha=0.8,
                        )

        # 设置标题和标签
        ax.set_title(title, fontsize=16, fontweight="bold", pad=20)
        if xlabel is not None:
            ax.set_xlabel(xlabel, fontsize=12)
        else:
            ax.set_xlabel(x_col, fontsize=12)
        if ylabel is not None:
            ax.set_ylabel(ylabel, fontsize=12)
        else:
            ax.set_ylabel("数值", fontsize=12)

        # 设置X轴标签旋转（根据标签长度自动调整）
        x_labels = df[x_col].astype(str).tolist()
        max_label_length = max(len(str(label)) for label in x_labels)
        if max_label_length > 8:  # 标签较长时旋转
            rotation_angle = 45 if max_label_length > 15 else 30
            ax.tick_params(axis="x", rotation=rotation_angle)
        else:
            ax.tick_params(axis="x", rotation=0)

        # 添加图例（简洁样式；系列很多时仅抽样展示）
        if len(y_cols) <= 10:
            ax.legend(loc="best", frameon=False)
        else:
            # 抽样展示最多 10 条图例项，均匀抽样
            max_items = 10
            idx = np.linspace(0, len(y_cols) - 1, max_items, dtype=int)
            handles = [Line2D([0], [0], color=colors[i], lw=2) for i in idx]
            labels = [y_cols[i] for i in idx]
            ax.legend(handles, labels, loc="best", frameon=False, ncol=2)

        # 不显示网格
        ax.grid(False)

        return fig

    def bar_chart(
        self,
        data: Union[pd.DataFrame, Dict],
        x_col: str = None,
        y_col: str = None,  # 数值列名
        group_col: str = None,  # 分组列名
        stack_col: str = None,  # 堆叠列名
        title: str = "柱状图",
        xlabel: str = None,
        ylabel: str = None,
        figsize: Optional[tuple] = None,
        colors: Optional[List[str]] = None,
        show_values: bool = False,  # 是否显示数值标签
    ) -> plt.Figure:
        """
        绘制柱状图（支持分组、堆叠和分组+堆叠组合）

        Args:
            data: 数据 DataFrame 或字典
            x_col: X 轴列名
            y_col: 数值列名
            group_col: 分组列名（用于分组显示）
            stack_col: 堆叠列名（用于堆叠显示）
            title: 图表标题
            xlabel: X 轴标签（默认使用 x_col）
            ylabel: Y 轴标签（默认为 "数值"）
            figsize: 图片尺寸
            colors: 颜色列表
            show_values: 是否在柱子上显示数值标签

        Returns:
            matplotlib Figure 对象
        """
        fig, ax = self._setup_figure(figsize)

        # 处理数据
        if isinstance(data, dict):
            df = pd.DataFrame(data)
        else:
            df = data.copy()

        # 设置默认值
        if x_col is None:
            x_col = df.columns[0]
        if y_col is None:
            y_col = df.columns[1]  # 假设第二列是数值列

        # 获取唯一值用于分组和堆叠
        x_values = df[x_col].unique()
        group_values = df[group_col].unique() if group_col else [None]
        stack_values = df[stack_col].unique() if stack_col else [None]

        # 设置颜色
        if group_col and stack_col:
            n_colors = len(group_values) * len(stack_values)
        else:
            n_colors = max(len(group_values), len(stack_values))
        if colors is None:
            colors = self._get_colors(n_colors)

        # 设置 x 轴位置
        x_pos = np.arange(len(x_values))

        # 绘制柱状图 - 根据参数自动判断类型
        if group_col and stack_col:
            # 分组+堆叠组合
            # 根据系列数量动态调整宽度
            total_series = len(group_values) * len(stack_values)
            if total_series <= 2:
                base_width = 0.6  # 系列少时使用较窄的宽度
            elif total_series <= 4:
                base_width = 0.7
            else:
                base_width = 0.8
            group_width = base_width / len(group_values)
            color_idx = 0

            for group_idx, group_val in enumerate(group_values):
                offset = (group_idx - len(group_values) / 2 + 0.5) * group_width
                bottom = np.zeros(len(x_values))

                for stack_val in stack_values:
                    # 获取特定分组和堆叠组合的数据
                    subset = df[(df[group_col] == group_val) & (df[stack_col] == stack_val)]
                    aggregated = subset.groupby(x_col)[y_col].sum()
                    values = [aggregated.get(x_val, 0) for x_val in x_values]

                    bars = ax.bar(
                        x_pos + offset,
                        values,
                        group_width,
                        bottom=bottom,
                        label=f"{group_val}-{stack_val}",
                        color=colors[color_idx % len(colors)],
                        alpha=0.8,
                    )

                    # 添加数值标签（数据点过多时自动隐藏）
                    if show_values and len(x_values) <= 15:  # 最多显示15个X轴值
                        for i, (bar, value) in enumerate(zip(bars, values)):
                            if value > 0:
                                height = bar.get_height()
                                y_pos = bar.get_y() + height / 2
                                # 格式化数值，避免科学计数法
                                if value >= 1000000:
                                    value_str = f"{value/1000000:.1f}M"
                                elif value >= 1000:
                                    value_str = f"{value/1000:.1f}K"
                                else:
                                    value_str = f"{value:.0f}"
                                ax.text(
                                    bar.get_x() + bar.get_width() / 2,
                                    y_pos,
                                    value_str,
                                    ha="center",
                                    va="center",
                                    fontsize=8,
                                )
                    bottom = bottom + values
                    color_idx += 1
        elif group_col:
            # 分组柱状图
            # 根据系列数量动态调整宽度
            if len(group_values) <= 2:
                base_width = 0.6  # 系列少时使用较窄的宽度
            elif len(group_values) <= 4:
                base_width = 0.7
            else:
                base_width = 0.8
            width = base_width / len(group_values)
            color_idx = 0
            for group_val in group_values:
                group_data = df[df[group_col] == group_val]
                # 按 x 轴值聚合数据
                aggregated = group_data.groupby(x_col)[y_col].sum()
                values = [aggregated.get(x_val, 0) for x_val in x_values]

                offset = (color_idx - len(group_values) / 2 + 0.5) * width
                bars = ax.bar(
                    x_pos + offset,
                    values,
                    width,
                    label=group_val,
                    color=colors[color_idx],
                    alpha=0.8,
                )

                # 添加数值标签（数据点过多时自动隐藏）
                if show_values and len(x_values) <= 15:  # 最多显示15个X轴值
                    for i, (bar, value) in enumerate(zip(bars, values)):
                        if value > 0:
                            height = bar.get_height()
                            y_pos = bar.get_y() + height / 2
                            # 格式化数值，避免科学计数法
                            if value >= 1000000:
                                value_str = f"{value/1000000:.1f}M"
                            elif value >= 1000:
                                value_str = f"{value/1000:.1f}K"
                            else:
                                value_str = f"{value:.0f}"
                            ax.text(
                                bar.get_x() + bar.get_width() / 2,
                                y_pos,
                                value_str,
                                ha="center",
                                va="center",
                                fontsize=8,
                            )

                color_idx += 1
        elif stack_col:
            # 堆叠柱状图
            # 根据系列数量动态调整宽度
            if len(stack_values) <= 2:
                width = 0.6  # 系列少时使用较窄的宽度
            elif len(stack_values) <= 4:
                width = 0.7
            else:
                width = 0.8
            bottom = np.zeros(len(x_values))
            color_idx = 0
            for stack_val in stack_values:
                stack_data = df[df[stack_col] == stack_val]
                aggregated = stack_data.groupby(x_col)[y_col].sum()
                values = [aggregated.get(x_val, 0) for x_val in x_values]

                bars = ax.bar(
                    x_pos,
                    values,
                    width,
                    bottom=bottom,
                    label=stack_val,
                    color=colors[color_idx],
                    alpha=0.8,
                )

                # 添加数值标签（数据点过多时自动隐藏）
                if show_values and len(x_values) <= 15:  # 最多显示15个X轴值
                    for i, (bar, value) in enumerate(zip(bars, values)):
                        if value > 0:
                            height = bar.get_height()
                            y_pos = bar.get_y() + height / 2
                            # 格式化数值，避免科学计数法
                            if value >= 1000000:
                                value_str = f"{value/1000000:.1f}M"
                            elif value >= 1000:
                                value_str = f"{value/1000:.1f}K"
                            else:
                                value_str = f"{value:.0f}"
                            ax.text(
                                bar.get_x() + bar.get_width() / 2,
                                y_pos,
                                value_str,
                                ha="center",
                                va="center",
                                fontsize=8,
                            )

                bottom = bottom + values
                color_idx += 1
        else:
            # 简单柱状图
            # 根据数据点数量动态调整宽度
            if len(x_values) <= 5:
                width = 0.6  # 数据点少时使用较窄的宽度
            elif len(x_values) <= 10:
                width = 0.7
            else:
                width = 0.8
            aggregated = df.groupby(x_col)[y_col].sum()
            values = [aggregated.get(x_val, 0) for x_val in x_values]
            bars = ax.bar(x_pos, values, width, color=colors[0], alpha=0.8)

            # 添加数值标签（数据点过多时自动隐藏）
            if show_values and len(x_values) <= 15:  # 最多显示15个X轴值
                for i, (bar, value) in enumerate(zip(bars, values)):
                    if value > 0:
                        height = bar.get_height()
                        y_pos = bar.get_y() + height / 2
                        # 格式化数值，避免科学计数法
                        if value >= 1000000:
                            value_str = f"{value/1000000:.1f}M"
                        elif value >= 1000:
                            value_str = f"{value/1000:.1f}K"
                        else:
                            value_str = f"{value:.0f}"
                        ax.text(
                            bar.get_x() + bar.get_width() / 2,
                            y_pos,
                            value_str,
                            ha="center",
                            va="center",
                            fontsize=8,
                        )

        # 设置标题和标签
        ax.set_title(title, fontsize=16, fontweight="bold", pad=20)
        if xlabel is not None:
            ax.set_xlabel(xlabel, fontsize=12)
        else:
            ax.set_xlabel(x_col, fontsize=12)
        if ylabel is not None:
            ax.set_ylabel(ylabel, fontsize=12)
        else:
            ax.set_ylabel("数值", fontsize=12)
        # 设置X轴标签旋转（根据标签长度自动调整）
        max_label_length = max(len(str(label)) for label in x_values)
        if max_label_length > 8:  # 标签较长时旋转
            rotation_angle = 45 if max_label_length > 15 else 30
            ax.set_xticks(x_pos)
            ax.set_xticklabels(x_values, rotation=rotation_angle, ha="right")
        else:
            ax.set_xticks(x_pos)
            ax.set_xticklabels(x_values, rotation=0, ha="center")

        # 添加图例（限制最大显示10个）
        handles, labels = ax.get_legend_handles_labels()
        if len(labels) > 10:
            # 只显示前10个图例项
            handles = handles[:10]
            labels = labels[:10]
            # 添加省略号提示
            labels.append("...")
            handles.append(plt.Rectangle((0, 0), 1, 1, color="white", alpha=0))
        ax.legend(handles, labels, loc="best", frameon=False)

        # 不显示网格
        ax.grid(False)

        return fig

    def figure_to_base64(
        self,
        fig: plt.Figure,
        format: str = "png",
        dpi: int = 300,
        bbox_inches: str = "tight",
    ) -> str:
        """
        将 matplotlib Figure 转换为 base64 字符串

        Args:
            fig: matplotlib Figure 对象
            format: 图片格式 ('png', 'jpg', 'svg')
            dpi: 图片分辨率
            bbox_inches: 边界框设置

        Returns:
            base64 编码的图片字符串
        """
        # 创建内存缓冲区
        buffer = io.BytesIO()

        # 保存图片到缓冲区
        fig.savefig(buffer, format=format, dpi=dpi, bbox_inches=bbox_inches)
        buffer.seek(0)

        # 转换为 base64
        image_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

        # 关闭缓冲区
        buffer.close()

        return image_base64

    def save_figure(self, fig: plt.Figure, filename: str, format: str = "png", dpi: int = 300) -> str:
        """
        保存图片到文件

        Args:
            fig: matplotlib Figure 对象
            filename: 文件名（不含扩展名）
            format: 图片格式
            dpi: 图片分辨率

        Returns:
            保存的文件路径
        """
        import os

        os.makedirs("output", exist_ok=True)
        filepath = f"output/{filename}.{format}"
        fig.savefig(filepath, format=format, dpi=dpi, bbox_inches="tight")
        return filepath


def demo():
    """演示函数"""
    # 创建示例数据
    np.random.seed(42)

    # 时间序列数据
    dates = pd.date_range("2024-01-01", periods=12, freq="M")
    sales_data = pd.DataFrame(
        {
            "月份": [d.strftime("%Y-%m") for d in dates],
            "销售额": np.random.randint(100, 500, 12),
            "利润": np.random.randint(50, 200, 12),
            "成本": np.random.randint(30, 150, 12),
        }
    )

    # 分类数据
    category_data = {"电子产品": 35, "服装": 25, "食品": 20, "图书": 15, "其他": 5}

    # 创建绘图器
    plotter = PlotGenerator()

    print("生成各种图表...")

    # 1. 环形图
    fig1 = plotter.donut_chart(category_data, "产品销售占比")
    plotter.save_figure(fig1, "donut_chart")
    base64_1 = plotter.figure_to_base64(fig1)
    print(f"环形图 base64 长度: {len(base64_1)}")

    # 2. 折线图
    fig2 = plotter.line_chart(sales_data, "月份", ["销售额", "利润"], "销售趋势")
    plotter.save_figure(fig2, "line_chart")
    base64_2 = plotter.figure_to_base64(fig2)
    print(f"折线图 base64 长度: {len(base64_2)}")

    # 3. 分组柱状图
    # 转换为二维表数据格式
    sales_data_long = sales_data.melt(
        id_vars=["月份"],
        value_vars=["销售额", "利润"],
        var_name="指标",
        value_name="数值",
    )
    fig3 = plotter.bar_chart(
        sales_data_long,
        x_col="月份",
        y_col="数值",
        group_col="指标",
        title="月度销售对比",
    )
    plotter.save_figure(fig3, "grouped_bar_chart")
    base64_3 = plotter.figure_to_base64(fig3)
    print(f"分组柱状图 base64 长度: {len(base64_3)}")

    # 4. 堆叠柱状图
    # 转换为二维表数据格式
    finance_data_long = sales_data.melt(
        id_vars=["月份"],
        value_vars=["销售额", "利润", "成本"],
        var_name="类型",
        value_name="数值",
    )
    fig4 = plotter.bar_chart(
        finance_data_long,
        x_col="月份",
        y_col="数值",
        stack_col="类型",
        title="月度财务数据",
    )
    plotter.save_figure(fig4, "stacked_bar_chart")
    base64_4 = plotter.figure_to_base64(fig4)
    print(f"堆叠柱状图 base64 长度: {len(base64_4)}")

    print("\n所有图表已生成并保存到 output/ 目录")
    print("Base64 编码已生成，可用于网页显示或数据传输")


if __name__ == "__main__":
    demo()
