from db.seed import get_connection


# class Category for the categories table
class Category:
    def __init__(self, id = None, name = None):
        self.id = id
        self.name = name

    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Category name cannot be empty.")
        self._name = value

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute('INSERT INTO categories (name) VALUES (?)', (self.name,))
            self.id = cursor.lastrowid
        else:
            cursor.execute('UPDATE categories SET name = ? WHERE id = ?', (self.name, self.id))
        conn.commit()
        conn.close()

#class product for products table
class Product:
    def __init__(self, id=None, name=None, category_id=None, price=None, quantity=None):
        self.id = id
        self.name = name
        self.category_id = category_id
        self.price = price
        self.quantity = quantity

    # Validations of the instance attributes
    
    #name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Product name cannot be empty.")
        self._name = value

    # price
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value is None or value < 0:
            raise ValueError("Price must be a non-negative number.")
        self._price = value

    #pquantity
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value is None or value < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        self._quantity = value


    #saving to the database
    def save(self):
        conn = get_connection()
        cursor = conn.cursor()

        # Check if the category_id exists
        if self.category_id:
            cursor.execute('SELECT 1 FROM categories WHERE id = ?', (self.category_id,))
            if not cursor.fetchone():
                raise ValueError("Category ID does not exist.")

        if self.id is None:
            cursor.execute('INSERT INTO products (name, category_id, price, quantity) VALUES (?, ?, ?, ?)', 
                        (self.name, self.category_id, self.price, self.quantity))
            self.id = cursor.lastrowid
        else:
            cursor.execute('UPDATE products SET name = ?, category_id = ?, price = ?, quantity = ? WHERE id = ?', 
                        (self.name, self.category_id, self.price, self.quantity, self.id))
        conn.commit()
        conn.close()