# Rows represent products and columns represent monthly sales data
import numpy as np
sales = np.array([
		[100,300,250,200],
		[150,200,350,120],
		[230,180,320,100]
])
product_sales = sales.sum(axis=1)
print("Total sales per product =", product_sales)
monthly_sales = sales.sum(axis=0)
print("Total sales per month =", monthly_sales)
best_sell_product = product_sales.argmax()
print("Best selling product index =", best_sell_product)
best_month = monthly_sales.argmax()
print("Best selling month index =", best_month)
avg_sales = sales.mean()
print("Average sales =", np.round(avg_sales, 2))
highest_sale = sales.max()
print("Maximum Sale =", highest_sale)
lowest_sale = sales.min()
print("Minimum Sale =", lowest_sale)
