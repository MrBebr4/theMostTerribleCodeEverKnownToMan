# Ввод строки от пользователя
input_string = input("Введите строку: ")

# Преобразование строки в множество для удаления повторяющихся символов
unique_characters = set(input_string)

# Вывод уникальных символов
print("".join(unique_characters))