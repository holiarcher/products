products = []

while True:
	name = input('请输入商品名称:')
	if name == 'q':
		break
	price = input('请输入价格:')
	p = []
	p.append(name)
	p.append(price)
	products.append(p)

print(products)

with open('product.csv','w') as f:
	for p in products:
		f.write(p[0]+','+p[1]+'\n')
