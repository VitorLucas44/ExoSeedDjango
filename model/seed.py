# from django_seed import Seed
# from .models import Product

# def run():
# 	seeder = Seed.seeder()
# 	datas = [
# 		{"name": "Nike", "price": 39.99, "stock": 19},
# 		{"name": "Adidas", "price": 12.99, "stock": 4},
# 		{"name": "Puma", "price": 59.99, "stock": 29},
# 		{"name": "Vans", "price": 29.99, "stock": 45},
# 		{"name": "Vans", "price": 339.99, "stock": 87},
# 	]
# 	for data in datas:
# 		seeder.add_entity(Product, 1, data)
# 	print(seeder.execute())

from django_seed import Seed
from faker import Faker
from .models import Product

def run():
    seeder = Seed.seeder()
    faker = Faker()
    for _ in range(5):
        name = faker.company()
        price = faker.pydecimal(min_value=10, max_value=100, right_digits=2)
        stock = faker.random_int(min=0, max=100)
        data = {"name": name, "price": price, "stock": stock}
        seeder.add_entity(Product, 1, data)
    print(seeder.execute())
