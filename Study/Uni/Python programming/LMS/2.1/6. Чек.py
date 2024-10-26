# Input from the user
product_name = input("Введите название товара: ")
price_per_kg = float(input("Введите цену товара (руб/кг): "))
weight = float(input("Введите вес товара (кг): "))
money_given = float(input("Введите количество денег у пользователя (руб): "))

# Calculating total cost and change
total_cost = price_per_kg * weight
change = money_given - total_cost

# Printing the receipt
print("Чек")
print(f"{product_name} - {weight}кг - {price_per_kg}руб/кг")
print(f"Итого: {total_cost}руб")
print(f"Внесено: {money_given}руб")
print(f"Сдача: {change}руб")