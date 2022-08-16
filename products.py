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