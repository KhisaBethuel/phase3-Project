from helpers import (
    list_all_categories, list_all_products,
    search_category_by_name, search_product_by_name,
    search_product_by_category, count_products_in_category,
    add_category, add_product, update_category, update_product,
    delete_category, delete_product, list_products_by_category
)

if __name__ == '__main__':
    print('Welcome to The CLI Products Store!')

    while True:
        print("\nOptions:")
        print("1. List all categories")
        print("2. List all products")
        print("3. Search category by name")
        print("4. Search product by name")
        print("5. Search product by category")
        print("6. Check amount of products in a category")
        print("7. Add new category")
        print("8. Add new product")
        print("9. Update a category")
        print("10. Update a product")
        print("11. Delete a category")
        print("12. Delete a product")
        print("13. List products by category")
        print("14. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_all_categories()
        elif choice == '2':
            list_all_products()
        elif choice == '3':
            name = input("Enter the category name: ")
            categories = search_category_by_name(name)
            for category in categories:
                print(f"ID: {category.id}, Name: {category.name}")
        elif choice == '4':
            name = input("Enter the product name: ")
            products = search_product_by_name(name)
            for product in products:
                print(f"ID: {product.id}, Name: {product.name}, Category ID: {product.category_id}, Price: {product.price}, Quantity: {product.quantity}")
        elif choice == '5':
            category_id = int(input("Enter the category ID: "))
            products = search_product_by_category(category_id)
            for product in products:
                print(f"ID: {product.id}, Name: {product.name}, Category ID: {product.category_id}, Price: {product.price}, Quantity: {product.quantity}")
        elif choice == '6':
            category_id = int(input("Enter the category ID: "))
            count = count_products_in_category(category_id)
            print(f"There are {count} products in category ID {category_id}")
        elif choice == '7':
            name = input("Enter the new category name: ")
            add_category(name)
        elif choice == '8':
            name = input("Enter the new product name: ")
            category_id = int(input("Enter the category ID: "))
            price = float(input("Enter the product price: "))
            quantity = int(input("Enter the product quantity: "))
            add_product(name, category_id, price, quantity)
        elif choice == '9':
            id = int(input("Enter the category ID to update: "))
            name = input("Enter the new category name: ")
            update_category(id, name)
        elif choice == '10':
            id = int(input("Enter the product ID to update: "))
            name = input("Enter the new product name: ")
            category_id = int(input("Enter the new category ID: "))
            price = float(input("Enter the new product price: "))
            quantity = int(input("Enter the new product quantity: "))
            update_product(id, name, category_id, price, quantity)
        elif choice == '11':
            id = int(input("Enter the category ID to delete: "))
            delete_category(id)
        elif choice == '12':
            id = int(input("Enter the product ID to delete: "))
            delete_product(id)
        elif choice == '13':
            category_id = int(input("Enter the category ID: "))
            list_products_by_category(category_id)
        elif choice == '14':
            print("Exiting...Adios")
            break
        else:
            print("Invalid choice. Please try again.")
