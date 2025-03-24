from typing import List

with open('products.txt', 'w') as output:
    print("""Apple, 1.50, 10
Banana, 0.75, 15
Orange, 2.0, 17
Carrot, 1.25, 25
Tomato, 2.5, 14""", file=output)


def calculate_total_price(table: List[dict]) -> float:
    total = 0
    for d in table:
        total += d['price'] * d['amount']
    return total


with open('products.txt', 'r') as file:
    products = []
    for line in file:
        name, price, amount = line.strip().split(', ')
        products.append({'name': name, 'price': float(price), 'amount': int(amount)})
    print(calculate_total_price(products))
