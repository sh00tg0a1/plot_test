"""
测试数据生成功能
"""

from src.data import (
    generate_customer_data,
    generate_sales_data,
    generate_time_series_data,
    save_dataframe,
)


def test_time_series():
    """测试时间序列数据生成"""
    print("测试时间序列数据生成...")
    df = generate_time_series_data(days=30)
    print(f"时间序列数据形状: {df.shape}")
    print("前5行数据:")
    print(df.head())
    return df


def test_sales_data():
    """测试销售数据生成"""
    print("\n测试销售数据生成...")
    df = generate_sales_data(products=10, months=6)
    print(f"销售数据形状: {df.shape}")
    print("前5行数据:")
    print(df.head())
    return df


def test_customer_data():
    """测试客户数据生成"""
    print("\n测试客户数据生成...")
    df = generate_customer_data(customers=100)
    print(f"客户数据形状: {df.shape}")
    print("前5行数据:")
    print(df.head())
    return df


def test_save_functionality():
    """测试保存功能"""
    print("\n测试数据保存功能...")

    # 生成小量测试数据
    ts_data = generate_time_series_data(days=10)
    sales_data = generate_sales_data(products=5, months=3)

    # 测试不同格式保存
    save_dataframe(ts_data, "test_time_series", "csv")
    save_dataframe(sales_data, "test_sales", "csv")

    print("测试数据保存完成！")


if __name__ == "__main__":
    print("开始测试数据生成功能...")

    # 测试各种数据生成
    test_time_series()
    test_sales_data()
    test_customer_data()

    # 测试保存功能
    test_save_functionality()

    print("\n所有测试完成！")
