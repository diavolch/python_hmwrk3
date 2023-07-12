# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

my_list = [2, 3, 4, 4, 2, 5, 4, 7, 6, 7, 8, 9, 6, 9]
i = 0
dublicate = []
while i < len(my_list):
    if my_list.count(my_list[i]) > 1:
        if my_list[i] not in dublicate:
            dublicate.append(my_list[i])
    i += 1

print(f"Изначальный список: {my_list}")
print(f"Дублирующиеся элементы: {dublicate}")
