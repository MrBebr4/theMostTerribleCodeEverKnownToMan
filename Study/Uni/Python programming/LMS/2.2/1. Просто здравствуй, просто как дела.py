#спрашиваем имя
name = input("Как вас зовут?\n")
print(f"Здравствуйте, {name}")

#В зависимости от ответа выводим результат
mood = input("Как дела?\n")
if mood == "Хорошо":
    print("Я за вас рада!")
elif mood == "Плохо":
    print("Все наладится!")
else:
    print("Нормальный ввод дай болван")