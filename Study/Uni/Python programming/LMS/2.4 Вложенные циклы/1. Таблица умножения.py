dim = int(input())

# Проходим по строкам таблицы
for i in range(dim):
    # Проходим по столбцам таблицы
    for j in range(dim):
        # Выводим произведение текущих индексов, увеличенных на 1
        print((i + 1) * (j + 1), end=' ')
    # Переход на новую строку после завершения строки таблицы
    print()