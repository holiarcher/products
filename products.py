import os #operating system

fil = input('请输入挡案名称:')

products = []
if os.path.isfile(fil):
	print('yes, there is')
	with open(fil,'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,价格' in line:
				continue

			s = line.strip().split(',')
			products.append(s)
	print(products)
else:
	print('no, there is not')



#读取挡案



products = (products)
#使用者输入价格
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

with open(fil,'w', encoding = 'utf-8') as f:
	f.write('商品,价格\n')
	for p in products:
		f.write(p[0]+','+p[1]+'\n')
