def get_max_profit(stock_prices):
	try:
		no_stock_prices=len(stock_prices)
		if  no_stock_prices < 2:
			if (no_stock_prices==1):
				raise ValueError('Need Atleast Two stock values for prediction')
			raise ValueError('Empty Array of Stock Prices')
		
		min_price=stock_prices[0]
		max_profit=stock_prices[1]-stock_prices[0]

		for i in range(1, no_stock_prices):
			current_price=stock_prices[i]
			temp=current_price-min_price
			max_profit=max(max_profit, temp)
			min_price=min(min_price, current_price)
		return max_profit
	except Exception as e:
		print(str(e))

stock_prices=[10,7,5,8,11,9]
print("Stock_prices",stock_prices)
print(get_max_profit(stock_prices))
print("###########################")

stock_prices=[7,1,2,8]
print("Stock_prices",stock_prices)
print(get_max_profit(stock_prices))
print("###########################")

stock_prices=[7,7,7,7]
print("Stock_prices",stock_prices)
print(get_max_profit(stock_prices))
print("###########################")

stock_prices=[7,6,5,4]
print("Stock_prices",stock_prices)
print(get_max_profit(stock_prices))
print("###########################")

stock_prices=[]
print("Stock_prices",stock_prices)
print(get_max_profit(stock_prices))
print("###########################")

stock_prices=[7]
print("Stock_prices",stock_prices)
print(get_max_profit(stock_prices))
print("###########################")
