goods_count = int(input('Введите количество товаров: '))
goods = []

for index in range(goods_count):
    number = index + 1
    title = input(f'Введите название товара №{number}: ')
    price = int(input(f'Введите цену товара "{title}": '))
    count = int(input(f'Введите количество товара "{title}": '))
    unit = input(f'Введите единицу измерения товара "{title}": ')
    goods.append((number, {
        'название': title,
        'цена': price,
        'количество': count,
        'ед': unit
    }))

analytic = {}

for good in goods:
    for key, value in good[1].items():
        if key not in analytic:
            analytic[key] = []

        if value not in analytic[key]:
            analytic[key].append(value)

print(analytic)
