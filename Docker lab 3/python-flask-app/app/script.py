import random
from faker import Faker
from app.models import db, Product  

fake = Faker()

categories = ['Electronics', 'Clothing', 'Home', 'Toys', 'Books', 'Food']

# Создаем список для хранения продуктов
products = []

for _ in range(100):
    category = random.choice(categories)  # Выбираем случайную категорию из списка
    name = fake.word().capitalize()  # Название продукта
    quantity_sold = random.randint(1, 50)  # Количество проданных товаров
    total_revenue = round(quantity_sold * random.uniform(5, 500), 2)  # Сумма выручки

    # Создаем объект Product с категорией
    product = Product(
        name=name, 
        quantity_sold=quantity_sold, 
        total_revenue=total_revenue,
        category=category  # Добавляем категорию
    )

    # Добавляем объект в список
    products.append(product)

# Массовая вставка объектов в базу данных
db.session.bulk_save_objects(products)  # Передаем список объектов
db.session.commit()

print("100 товаров добавлено в базу!")