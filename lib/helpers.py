from db.models import Category, Product

# most of the functions here are have names explaining what they do


def add_category(name):
    category = Category(name=name)
    category.save()
    print(f"Category '{name}' added with ID {category.id}")
    
    
def add_product(name, category_id, price, quantity):
    product = Product(name=name, category_id=category_id, price=price, quantity=quantity)
    product.save()
    print(f"Product '{name}' added with ID {product.id} in Category ID {category_id}")


def list_all_categories():
    categories = Category.all()
    for category in categories:
        print(f"ID: {category.id}, Category Name: {category.name}")
        
        
def list_all_products():
    products = Product.all()
    for product in products:
        print(f"ID: {product.id}, Name: {product.name}, Category ID: {product.category_id}, Price: {product.price}, Quantity: {product.quantity}")

def search_category_by_name(name):
    categories = Category.all()
    return [cat for cat in categories if cat.name.lower() == name.lower()]

def search_product_by_name(name):
    products = Product.all()
    return [prod for prod in products if prod.name.lower() == name.lower()]

def search_product_by_category(category_id):
    products = Product.all()
    return [prod for prod in products if prod.category_id == category_id]

def count_products_in_category(category_id):
    products = search_product_by_category(category_id)
    return len(products)

def update_category(id, name):
    category = Category.get(id)
    if category:
        category.name = name
        category.save()
        print(f"Category ID {id} updated to name '{name}'")
    else:
        print(f"Category ID {id} not found")

def update_product(id, name, category_id, price, quantity):
    product = Product.get(id)
    if product:
        product.name = name
        product.category_id = category_id
        product.price = price
        product.quantity = quantity
        product.save()
        print(f"Product ID {id} updated with name '{name}', category ID {category_id}, price {price}, and quantity {quantity}")
    else:
        print(f"Product ID {id} not found")
