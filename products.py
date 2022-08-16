products = []
while True:
    name = input('Enter your product name: ')
    if name == 'q':
        break
    price = input('Enter the product price: ') 
    products.append([name, price])
print(products)

for product in products:
    print(product)

with open('products.csv', 'w', encoding = 'utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')