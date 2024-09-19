from db.models import Category, Product


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


