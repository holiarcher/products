products = []

while True:
	name = input('请输入商品名称:')
	if name == 'q':
		break

	products.append(name)

print(products)

