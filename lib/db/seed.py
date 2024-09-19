import sqlite3


# Function to create the database and fill it with tables from the create table file
def setup_database():
    conn = sqlite3.connect('store.db')
    
    with open('lib/migrations/create_tables.sql', 'r') as f:
        conn.executescript(f.read())
        
    conn.close()
    print("Database setup complete!")

#function that I will use to connect to the database in my models instead of using conn = sqlite3.connect() repetedly
def get_connection():
    return sqlite3.connect('store.db')

if __name__ == "__main__":
    setup_database()