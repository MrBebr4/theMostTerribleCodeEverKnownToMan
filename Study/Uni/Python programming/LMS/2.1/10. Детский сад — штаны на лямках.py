#запрашиваем данные у пользователя
name = input()
id = input()

#Разделяем строку на части
group = id[0]
bed = id[1]
locker = id
number = id[2]

#Выводим сформированную карточку в консоль
print(f'Группа №{group}.')
print(f'{number}. {name}.')
print(f'Шкафчик: {locker}.')
print(f'Кроватка: {bed}.')