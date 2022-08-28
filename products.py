import os # operating system

# read file
def read_file(filename):
    products = []
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                     continue
            name, price = line.strip().split(',')
            products.append([name, price])
    return products
    
# user enter the information
def user_input(products):
    while True:
        name = input('Enter your product name: ')
        if name == 'q':
            break
        price = input('Enter the product price: ') 
        products.append([name, price])
    print(products)
    return products

# print all information
def print_products(products):
    for p in products:
        print(p[0], 'is $', p[1])

# write file
def write_file(filename, products):
    with open(filename, 'w', encoding = 'utf-8') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')

def main():
    # file check
    filename = 'products.csv'
    if os.path.isfile(filename):
        print('Yes, you find the file.')
        products = read_file(filename)
    else:
        print('Error, your file is not exist.')

    products = user_input(products)
    print_products(products)
    write_file(filename, products)

main()
