"""
绘图模块
支持环形图、折线图、柱状图，以及图片转 base64 功能
"""

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import pandas as pd
import base64
import io
from typing import List, Dict, Optional, Union
# import platform  # 暂时未使用


class PlotGenerator:
    """绘图生成器类"""

    # 预定义颜色序列
    COLOR_PALETTE = [
        '#5470c6', '#91cc75', '#fac858', '#ee6666', '#73c0de',
        '#3ba272', '#fc8452', '#9a60b4', '#ea7ccc'
    ]

    def __init__(self, style='seaborn-v0_8', figsize=(10, 6)):
        """
        初始化绘图生成器

        Args:
            style: matplotlib 样式
            figsize: 图片尺寸
        """
        # 设置中文字体
        self._setup_chinese_font()
        
        plt.style.use(style)
        self.figsize = figsize
        self.current_fig = None
        self.current_ax = None

    def _setup_chinese_font(self):
        """设置中文字体"""
        import platform
        import os
        
        # 清除 matplotlib 字体缓存
        try:
            import matplotlib
            cache_dir = matplotlib.get_cachedir()
            if os.path.exists(cache_dir):
                import shutil
                shutil.rmtree(cache_dir, ignore_errors=True)
        except:
            pass
        
        # 重新构建字体管理器
        try:
            fm._rebuild()
        except:
            pass
        
        # 根据系统选择字体
        system = platform.system().lower()
        
        if system == 'linux':
            chinese_fonts = [
                'WenQuanYi Micro Hei',
                'WenQuanYi Zen Hei',
                'Noto Sans CJK SC',
                'Source Han Sans SC',
                'Droid Sans Fallback',
                'AR PL UMing CN',
                'AR PL UKai CN'
            ]
        elif system == 'windows':
            chinese_fonts = [
                'Microsoft YaHei',
                'SimHei',
                'KaiTi',
                'FangSong',
                'SimSun'
            ]
        elif system == 'darwin':  # macOS
            chinese_fonts = [
                'PingFang SC',
                'Hiragino Sans GB',
                'STHeiti',
                'Arial Unicode MS'
            ]
        else:
            chinese_fonts = [
                'WenQuanYi Micro Hei',
                'Noto Sans CJK SC',
                'Source Han Sans SC',
                'DejaVu Sans'
            ]
        
        # 获取所有可用字体
        available_fonts = [f.name for f in fm.fontManager.ttflist]
        
        # 尝试设置字体
        font_set = False
        for font in chinese_fonts:
            if font in available_fonts:
                try:
                    plt.rcParams['font.sans-serif'] = [font]
                    plt.rcParams['axes.unicode_minus'] = False
                    font_set = True
                    print(f"✓ 使用中文字体: {font}")
                    break
                except Exception as e:
                    print(f"✗ 字体设置失败: {font}, 错误: {e}")
                    continue
        
        # 如果仍然没有设置成功，尝试强制设置
        if not font_set:
            try:
                # 尝试使用系统默认字体
                plt.rcParams['font.family'] = 'sans-serif'
                plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Liberation Sans']
                plt.rcParams['axes.unicode_minus'] = False
                print("⚠ 使用默认字体，中文可能显示为方块")
            except Exception as e:
                print(f"✗ 字体设置完全失败: {e}")
        
        # 测试中文显示
        try:
            import matplotlib.pyplot as plt
            fig, ax = plt.subplots(figsize=(1, 1))
            ax.text(0.5, 0.5, '测试', fontsize=12, ha='center')
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.axis('off')
            plt.close(fig)
            print("✓ 中文字体测试通过")
        except Exception as e:
            print(f"✗ 中文字体测试失败: {e}")

    def _setup_figure(self, figsize: Optional[tuple] = None):
        """设置图形"""
        if figsize is None:
            figsize = self.figsize
        self.current_fig, self.current_ax = plt.subplots(figsize=figsize)
        return self.current_fig, self.current_ax

    def _get_colors(self, n_colors: int) -> List[str]:
        """获取指定数量的颜色"""
        if n_colors <= len(self.COLOR_PALETTE):
            return self.COLOR_PALETTE[:n_colors]
        else:
            # 如果需要的颜色超过预定义的数量，循环使用
            colors = []
            for i in range(n_colors):
                colors.append(self.COLOR_PALETTE[i % len(self.COLOR_PALETTE)])
            return colors

    def donut_chart(self, data: Union[Dict, pd.Series],
                    title: str = "环形图",
                    figsize: Optional[tuple] = None,
                    colors: Optional[List[str]] = None) -> plt.Figure:
        """
        绘制环形图

        Args:
            data: 数据字典或 pandas Series
            title: 图表标题
            figsize: 图片尺寸
            colors: 颜色列表

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
        else:
            raise ValueError("数据必须是字典或 pandas Series")

        # 设置颜色
        if colors is None:
            colors = self._get_colors(len(labels))

        # 绘制外圆
        wedges, texts, autotexts = ax.pie(
            values, labels=labels,
            colors=colors,
            autopct='%1.1f%%', startangle=90,
            pctdistance=0.85
        )

        # 绘制内圆（创建环形效果）
        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        ax.add_artist(centre_circle)

        # 设置标题
        ax.set_title(title, fontsize=16, fontweight='bold', pad=20)

        # 美化文本
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')

        return fig

    def line_chart(self, data: Union[pd.DataFrame, Dict],
                   x_col: str = None, y_cols: List[str] = None,
                   title: str = "折线图",
                   figsize: Optional[tuple] = None,
                   colors: Optional[List[str]] = None,
                   line_styles: Optional[List[str]] = None) -> plt.Figure:
        """
        绘制折线图

        Args:
            data: 数据 DataFrame 或字典
            x_col: X 轴列名
            y_cols: Y 轴列名列表
            title: 图表标题
            figsize: 图片尺寸
            colors: 颜色列表
            line_styles: 线型列表

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
            line_styles = ['-', '--', '-.', ':'][:len(y_cols)]

        # 绘制折线
        for i, y_col in enumerate(y_cols):
            ax.plot(
                df[x_col], df[y_col],
                color=colors[i],
                linestyle=line_styles[i],
                linewidth=2.5,
                marker='o',
                markersize=6,
                label=y_col
            )

        # 设置标题和标签
        ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
        ax.set_xlabel(x_col, fontsize=12)
        ax.set_ylabel('数值', fontsize=12)

        # 添加图例
        ax.legend(loc='best', frameon=True, fancybox=True, shadow=True)

        # 添加网格
        ax.grid(True, alpha=0.3, linestyle='--')

        return fig

    def bar_chart(self, data: Union[pd.DataFrame, Dict],
                  x_col: str = None, y_cols: List[str] = None,
                  title: str = "柱状图",
                  chart_type: str = 'grouped',  # 'grouped' 或 'stacked'
                  figsize: Optional[tuple] = None,
                  colors: Optional[List[str]] = None) -> plt.Figure:
        """
        绘制柱状图（支持分组和堆叠）

        Args:
            data: 数据 DataFrame 或字典
            x_col: X 轴列名
            y_cols: Y 轴列名列表
            title: 图表标题
            chart_type: 图表类型 ('grouped' 或 'stacked')
            figsize: 图片尺寸
            colors: 颜色列表

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

        # 设置颜色
        if colors is None:
            colors = self._get_colors(len(y_cols))

        # 设置 x 轴位置
        x_pos = np.arange(len(df[x_col]))
        width = 0.8 / len(y_cols) if chart_type == 'grouped' else 0.8

        # 绘制柱状图
        if chart_type == 'grouped':
            for i, y_col in enumerate(y_cols):
                offset = (i - len(y_cols)/2 + 0.5) * width
                ax.bar(
                    x_pos + offset, df[y_col],
                    width, label=y_col, color=colors[i], alpha=0.8
                )
        elif chart_type == 'stacked':
            bottom = np.zeros(len(df))
            for i, y_col in enumerate(y_cols):
                ax.bar(
                    x_pos, df[y_col], width,
                    bottom=bottom, label=y_col,
                    color=colors[i], alpha=0.8
                )
                bottom += df[y_col]

        # 设置标题和标签
        ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
        ax.set_xlabel(x_col, fontsize=12)
        ax.set_ylabel('数值', fontsize=12)
        ax.set_xticks(x_pos)
        ax.set_xticklabels(df[x_col], rotation=45, ha='right')

        # 添加图例
        ax.legend(loc='best', frameon=True, fancybox=True, shadow=True)

        # 添加网格
        ax.grid(True, alpha=0.3, linestyle='--', axis='y')

        return fig

    def figure_to_base64(self, fig: plt.Figure, format: str = 'png',
                         dpi: int = 300, bbox_inches: str = 'tight') -> str:
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
        image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

        # 关闭缓冲区
        buffer.close()

        return image_base64

    def save_figure(self, fig: plt.Figure, filename: str,
                    format: str = 'png', dpi: int = 300) -> str:
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
        os.makedirs('output', exist_ok=True)
        filepath = f'output/{filename}.{format}'
        fig.savefig(filepath, format=format, dpi=dpi, bbox_inches='tight')
        return filepath

    def create_dashboard(self, charts: List[Dict],
                         title: str = "数据仪表板",
                         figsize: tuple = (15, 10)) -> plt.Figure:
        """
        创建多图表仪表板

        Args:
            charts: 图表配置列表
            title: 仪表板标题
            figsize: 图片尺寸

        Returns:
            matplotlib Figure 对象
        """
        n_charts = len(charts)
        rows = (n_charts + 1) // 2
        cols = 2 if n_charts > 1 else 1

        fig, axes = plt.subplots(rows, cols, figsize=figsize)
        if n_charts == 1:
            axes = [axes]
        elif rows == 1:
            axes = axes
        else:
            axes = axes.flatten()

        for i, chart_config in enumerate(charts):
            ax = axes[i] if n_charts > 1 else axes[0]

            chart_type = chart_config.get('type', 'line')
            data = chart_config.get('data')
            chart_title = chart_config.get('title', f'图表 {i+1}')

            if chart_type == 'donut':
                # 环形图需要特殊处理
                if isinstance(data, dict):
                    labels = list(data.keys())
                    values = list(data.values())
                else:
                    labels = data.index.tolist()
                    values = data.values.tolist()

                colors = self._get_colors(len(labels))
                wedges, texts, autotexts = ax.pie(
                    values, labels=labels,
                    colors=colors,
                    autopct='%1.1f%%'
                )
                centre_circle = plt.Circle((0, 0), 0.70, fc='white')
                ax.add_artist(centre_circle)

            elif chart_type == 'line':
                x_col = chart_config.get('x_col')
                y_cols = chart_config.get('y_cols')
                if x_col and y_cols:
                    colors = self._get_colors(len(y_cols))
                    for j, y_col in enumerate(y_cols):
                        ax.plot(
                            data[x_col], data[y_col],
                            color=colors[j], linewidth=2, label=y_col
                        )
                    ax.legend()

            elif chart_type == 'bar':
                x_col = chart_config.get('x_col')
                y_cols = chart_config.get('y_cols')
                chart_subtype = chart_config.get('subtype', 'grouped')

                if x_col and y_cols:
                    colors = self._get_colors(len(y_cols))
                    x_pos = np.arange(len(data[x_col]))
                    width = (0.8 / len(y_cols) if chart_subtype == 'grouped'
                             else 0.8)

                    if chart_subtype == 'grouped':
                        for j, y_col in enumerate(y_cols):
                            offset = (j - len(y_cols)/2 + 0.5) * width
                            ax.bar(
                                x_pos + offset, data[y_col],
                                width, label=y_col, color=colors[j]
                            )
                    else:  # stacked
                        bottom = np.zeros(len(data))
                        for j, y_col in enumerate(y_cols):
                            ax.bar(
                                x_pos, data[y_col], width,
                                bottom=bottom, label=y_col,
                                color=colors[j]
                            )
                            bottom += data[y_col]

                    ax.set_xticks(x_pos)
                    ax.set_xticklabels(data[x_col], rotation=45)
                    ax.legend()

            ax.set_title(chart_title, fontsize=12, fontweight='bold')
            ax.grid(True, alpha=0.3)

        # 隐藏多余的子图
        for i in range(n_charts, len(axes)):
            axes[i].set_visible(False)

        fig.suptitle(title, fontsize=18, fontweight='bold', y=0.98)
        plt.tight_layout()

        return fig


def demo():
    """演示函数"""
    # 创建示例数据
    np.random.seed(42)

    # 时间序列数据
    dates = pd.date_range('2024-01-01', periods=12, freq='M')
    sales_data = pd.DataFrame({
        '月份': [d.strftime('%Y-%m') for d in dates],
        '销售额': np.random.randint(100, 500, 12),
        '利润': np.random.randint(50, 200, 12),
        '成本': np.random.randint(30, 150, 12)
    })

    # 分类数据
    category_data = {
        '电子产品': 35,
        '服装': 25,
        '食品': 20,
        '图书': 15,
        '其他': 5
    }

    # 创建绘图器
    plotter = PlotGenerator()

    print("生成各种图表...")

    # 1. 环形图
    fig1 = plotter.donut_chart(category_data, "产品销售占比")
    plotter.save_figure(fig1, "donut_chart")
    base64_1 = plotter.figure_to_base64(fig1)
    print(f"环形图 base64 长度: {len(base64_1)}")

    # 2. 折线图
    fig2 = plotter.line_chart(sales_data, '月份', ['销售额', '利润'], "销售趋势")
    plotter.save_figure(fig2, "line_chart")
    base64_2 = plotter.figure_to_base64(fig2)
    print(f"折线图 base64 长度: {len(base64_2)}")

    # 3. 分组柱状图
    fig3 = plotter.bar_chart(
        sales_data, '月份', ['销售额', '利润'],
        "月度销售对比", chart_type='grouped'
    )
    plotter.save_figure(fig3, "grouped_bar_chart")
    base64_3 = plotter.figure_to_base64(fig3)
    print(f"分组柱状图 base64 长度: {len(base64_3)}")

    # 4. 堆叠柱状图
    fig4 = plotter.bar_chart(
        sales_data, '月份', ['销售额', '利润', '成本'],
        "月度财务数据", chart_type='stacked'
    )
    plotter.save_figure(fig4, "stacked_bar_chart")
    base64_4 = plotter.figure_to_base64(fig4)
    print(f"堆叠柱状图 base64 长度: {len(base64_4)}")

    # 5. 仪表板
    dashboard_config = [
        {'type': 'donut', 'data': category_data, 'title': '产品分类'},
        {'type': 'line', 'data': sales_data, 'x_col': '月份',
         'y_cols': ['销售额'], 'title': '销售趋势'},
        {'type': 'bar', 'data': sales_data, 'x_col': '月份',
         'y_cols': ['销售额', '利润'], 'subtype': 'grouped',
         'title': '月度对比'},
        {'type': 'bar', 'data': sales_data, 'x_col': '月份',
         'y_cols': ['销售额', '利润', '成本'], 'subtype': 'stacked',
         'title': '财务数据'}
    ]

    fig5 = plotter.create_dashboard(dashboard_config, "综合数据仪表板")
    plotter.save_figure(fig5, "dashboard")
    base64_5 = plotter.figure_to_base64(fig5)
    print(f"仪表板 base64 长度: {len(base64_5)}")

    print("\n所有图表已生成并保存到 output/ 目录")
    print("Base64 编码已生成，可用于网页显示或数据传输")

    # 显示图表
    plt.show()


if __name__ == "__main__":
    demo()
