number_product = int(input('Введите количество товаров'))
products = []
title_analytics = []
price_analytics = []
quantity_analytics = []
measurement_analytics = []
for i in range(0,number_product):
    title = input('Введите название продукта')
    price = input('Введите цену продукта')
    quantity = input('Введите количество продукта')
    measurement = input('Введите единицу измерения')
    products.insert(i,(i+1,{'название': title, 'цена': price, 'количество': quantity, 'ед.':measurement}))
    title_analytics.insert(i, title)
    price_analytics.insert(i, price)
    quantity_analytics.insert(i, quantity)
    measurement_analytics.insert(i, measurement)
print(products)
analytics = {
    'название': title_analytics,
    'цена': price_analytics,
    'количество': quantity_analytics,
    'ед.': measurement_analytics
}
print(analytics)