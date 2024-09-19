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
    pass