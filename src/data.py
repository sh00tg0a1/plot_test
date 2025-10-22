"""
数据生成模块
专门用于生成和保存 DataFrame 数据文件
"""

import pandas as pd
import numpy as np
import os


def generate_time_series_data(start_date="2024-01-01", days=365, freq="D"):
    """
    生成时间序列数据

    Args:
        start_date: 开始日期
        days: 数据天数
        freq: 频率 ('D'=日, 'H'=小时, 'W'=周)

    Returns:
        pd.DataFrame: 包含时间序列的 DataFrame
    """
    # 创建时间索引
    date_range = pd.date_range(start=start_date, periods=days, freq=freq)

    # 生成模拟数据
    np.random.seed(42)
    n_points = len(date_range)

    # 基础趋势
    trend = np.linspace(100, 200, n_points)

    # 季节性模式
    seasonal = 20 * np.sin(2 * np.pi * np.arange(n_points) / 365.25)

    # 随机噪声
    noise = np.random.normal(0, 10, n_points)

    # 组合数据
    values = trend + seasonal + noise

    # 创建 DataFrame
    df = pd.DataFrame(
        {
            "date": date_range,
            "value": values,
            "category": np.random.choice(["A", "B", "C"], n_points),
            "region": np.random.choice(["North", "South", "East", "West"], n_points),
        }
    )

    return df


def generate_sales_data(products=50, months=12):
    """
    生成销售数据

    Args:
        products: 产品数量
        months: 月份数量

    Returns:
        pd.DataFrame: 销售数据 DataFrame
    """
    np.random.seed(42)

    # 生成产品列表
    products_list = [f"Product_{i:03d}" for i in range(1, products + 1)]

    # 生成月份列表
    months_list = pd.date_range("2024-01-01", periods=months, freq="M")

    data = []
    for product in products_list:
        for month in months_list:
            # 基础销量（不同产品有不同的基础销量）
            base_sales = np.random.randint(50, 500)

            # 季节性调整
            seasonal_factor = 1 + 0.3 * np.sin(2 * np.pi * month.month / 12)

            # 随机波动
            random_factor = np.random.uniform(0.7, 1.3)

            sales = int(base_sales * seasonal_factor * random_factor)
            price = np.random.uniform(10, 100)
            revenue = sales * price

            data.append(
                {
                    "product": product,
                    "month": month,
                    "sales": sales,
                    "price": round(price, 2),
                    "revenue": round(revenue, 2),
                    "category": np.random.choice(
                        ["Electronics", "Clothing", "Books", "Home"]
                    ),
                    "region": np.random.choice(["North", "South", "East", "West"]),
                }
            )

    return pd.DataFrame(data)


def generate_customer_data(customers=1000):
    """
    生成客户数据

    Args:
        customers: 客户数量

    Returns:
        pd.DataFrame: 客户数据 DataFrame
    """
    np.random.seed(42)

    # 生成客户ID
    customer_ids = [f"CUST_{i:06d}" for i in range(1, customers + 1)]

    # 生成随机数据
    ages = np.random.randint(18, 80, customers)
    incomes = np.random.lognormal(10, 0.5, customers)
    purchase_counts = np.random.poisson(5, customers)

    # 创建 DataFrame
    df = pd.DataFrame(
        {
            "customer_id": customer_ids,
            "age": ages,
            "income": np.round(incomes, 2),
            "purchase_count": purchase_counts,
            "gender": np.random.choice(["M", "F"], customers),
            "city": np.random.choice(
                ["Beijing", "Shanghai", "Guangzhou", "Shenzhen", "Hangzhou"], customers
            ),
            "registration_date": pd.date_range(
                "2020-01-01", periods=customers, freq="D"
            )[:customers],
        }
    )

    return df


def save_dataframe(df, filename, format="csv"):
    """
    保存 DataFrame 到文件

    Args:
        df: 要保存的 DataFrame
        filename: 文件名（不含扩展名）
        format: 保存格式 ('csv', 'excel', 'parquet', 'json')
    """
    # 确保 data 目录存在
    os.makedirs("data", exist_ok=True)

    filepath = f"data/{filename}.{format}"

    if format == "csv":
        df.to_csv(filepath, index=False, encoding="utf-8-sig")
    elif format == "excel":
        df.to_excel(filepath, index=False)
    elif format == "parquet":
        df.to_parquet(filepath, index=False)
    elif format == "json":
        df.to_json(filepath, orient="records", date_format="iso")
    else:
        raise ValueError(f"不支持的格式: {format}")

    print(f"数据已保存到: {filepath}")
    print(f"数据形状: {df.shape}")


def main():
    """主函数 - 生成所有数据文件"""
    print("开始生成数据文件...")

    # 1. 生成时间序列数据
    print("\n1. 生成时间序列数据...")
    ts_data = generate_time_series_data()
    save_dataframe(ts_data, "time_series_data", "csv")

    # 2. 生成销售数据
    print("\n2. 生成销售数据...")
    sales_data = generate_sales_data()
    save_dataframe(sales_data, "sales_data", "csv")

    # 3. 生成客户数据
    print("\n3. 生成客户数据...")
    customer_data = generate_customer_data()
    save_dataframe(customer_data, "customer_data", "csv")

    # 4. 生成 Excel 格式的销售数据
    print("\n4. 生成 Excel 格式的销售数据...")
    save_dataframe(sales_data, "sales_data", "excel")

    print("\n所有数据文件生成完成！")
    print("生成的文件:")
    print("- data/time_series_data.csv")
    print("- data/sales_data.csv")
    print("- data/customer_data.csv")
    print("- data/sales_data.xlsx")


if __name__ == "__main__":
    main()
