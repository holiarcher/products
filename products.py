#读取挡案
products = []
with open('product.csv','r', encoding = 'utf-8') as f:
	for line in f:
		if '商品,价格' in line:
			continue
			
		s = line.strip().split(',')
		products.append(s)
		print(s)

products = (products)

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

with open('product.csv','w', encoding = 'utf-8') as f:
	f.write('商品,价格\n')
	for p in products:
		f.write(p[0]+','+p[1]+'\n')
