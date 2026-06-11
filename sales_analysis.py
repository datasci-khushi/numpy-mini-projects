# Rows represent products and columns represent monthly sales data
import numpy as np
sales = np.array([
		[100,300,250,200],
		[150,200,350,120],
		[230,180,320,100]
])
each_product_sale = sales.sum(axis=1)
print(each_product_sale)
each_month_sale = sales.sum(axis=0)
print(each_month_sale)
best_sell_product = each_product_sale.argmax()
print(best_sell_product)
best_month = each_month_sale.argmax()
print(best_month)
avg_sales = sales.mean()
print(np.round(avg_sales, 2))
highest_sale = sales.max()
print(highest_sale)
lowest_sale = sales.min()
print(lowest_sale)
