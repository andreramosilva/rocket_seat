from _sqlite3 import Connection as SqliteConnection

class ProductsRepository:
    def __init__(self, sqlite_conn: SqliteConnection) -> None:
        self.sqlite_conn = sqlite_conn

    def find_product_by_name(self,product_name: str) -> tuple:
        cursor = self.sqlite_conn.cursor()
        cursor.execute("SELECT * FROM products WHERE name=?", (product_name,))
        product = cursor.fetchone()
        cursor.close()
        return product
    
    def insert_product(self, name: str, price: float, quantity: int) -> None:
        cursor = self.sqlite_conn.cursor()
        cursor.execute("INSERT INTO products (name, price, quantity) VALUES (?, ?,?)", (name, price, quantity))
        self.sqlite_conn.commit()
        cursor.close()