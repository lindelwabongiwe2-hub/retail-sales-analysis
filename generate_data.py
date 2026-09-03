import pandas as pd
import numpy as np

np.random.seed(42)

n = 6000

provinces = [
    "Gauteng",
    "KwaZulu-Natal",
    "Western Cape",
    "Eastern Cape",
    "Free State",
    "Limpopo",
    "Mpumalanga",
    "North West",
    "Northern Cape"
]

stores = {
    "Gauteng": ["Johannesburg", "Pretoria", "Soweto"],
    "KwaZulu-Natal": ["Durban", "Pietermaritzburg"],
    "Western Cape": ["Cape Town", "Stellenbosch"],
    "Eastern Cape": ["Gqeberha", "East London"],
    "Free State": ["Bloemfontein"],
    "Limpopo": ["Polokwane"],
    "Mpumalanga": ["Mbombela"],
    "North West": ["Rustenburg"],
    "Northern Cape": ["Kimberley"]
}

products = [
    ("Smartphone", "Electronics", 6500, 5000),
    ("Laptop", "Electronics", 12500, 9500),
    ("Headphones", "Electronics", 1800, 1100),
    ("Sneakers", "Clothing", 1600, 850),
    ("Jacket", "Clothing", 1200, 600),
    ("Jeans", "Clothing", 850, 420),
    ("Microwave", "Appliances", 2200, 1500),
    ("Kettle", "Appliances", 650, 350),
    ("Blender", "Appliances", 950, 500),
    ("Office Chair", "Furniture", 2400, 1500),
    ("Desk", "Furniture", 3200, 2050),
    ("Bookshelf", "Furniture", 1800, 1050),
    ("Face Cream", "Beauty", 420, 180),
    ("Perfume", "Beauty", 950, 420),
    ("Shampoo", "Beauty", 180, 80),
    ("Rice 5kg", "Groceries", 110, 70),
    ("Cooking Oil", "Groceries", 140, 90),
    ("Cereal", "Groceries", 75, 42)
]

dates = pd.date_range("2025-01-01", "2025-12-31")

province_weights = [
    0.32, 0.15, 0.14, 0.09, 0.08,
    0.07, 0.06, 0.06, 0.03
]

product_weights = np.array([
    8, 4, 10,
    8, 7, 10,
    5, 9, 7,
    4, 3, 5,
    7, 4, 10,
    10, 9, 9
], dtype=float)

product_weights /= product_weights.sum()

rows = []

for i in range(n):

    province = np.random.choice(
        provinces,
        p=province_weights
    )

    store = np.random.choice(
        stores[province]
    )

    product_index = np.random.choice(
        len(products),
        p=product_weights
    )

    product, category, price, cost = products[product_index]

    quantity = np.random.choice(
        [1, 2, 3, 4, 5, 6],
        p=[0.40, 0.27, 0.15, 0.09, 0.06, 0.03]
    )

    discount = np.random.choice(
        [0, 0.05, 0.10, 0.15],
        p=[0.55, 0.25, 0.15, 0.05]
    )

    sales = round(
        price * quantity * (1 - discount),
        2
    )

    total_cost = round(
        cost * quantity,
        2
    )

    profit = round(
        sales - total_cost,
        2
    )

    customer_type = np.random.choice(
        ["New", "Returning"],
        p=[0.35, 0.65]
    )

    payment_method = np.random.choice(
        ["Card", "Cash", "EFT", "Mobile"],
        p=[0.48, 0.18, 0.17, 0.17]
    )

    rows.append([
        f"MR-{100001 + i}",
        np.random.choice(dates),
        province,
        store,
        product,
        category,
        quantity,
        discount,
        sales,
        total_cost,
        profit,
        customer_type,
        payment_method
    ])

df = pd.DataFrame(rows, columns=[
    "Order_ID",
    "Date",
    "Province",
    "Store",
    "Product",
    "Category",
    "Quantity",
    "Discount",
    "Sales",
    "Cost",
    "Profit",
    "Customer_Type",
    "Payment_Method"
])

df = df.sort_values("Date")

df.to_csv(
    "retail_sales_data.csv",
    index=False
)

print("Dataset created successfully!")
print(f"Rows: {len(df)}")
