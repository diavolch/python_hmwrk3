# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.

my_list = {'кружка': 0.1, 'одеяло': 0.5, 'чайник': 0.5, 'вода': 1, 'спальник': 1, 'картошка': 3, 'толстовка': 0.5,
           'носки': 0.1, 'консервы': 1, 'панама': 0.1, 'спички': 0.05}

MAX_WEIGHT = 3
list = []
count = 0

for key, val in my_list.items():
    if count <= MAX_WEIGHT and (count + val) <= MAX_WEIGHT:
        list.append(key)
        count = count + val

print(count)
print(list)
