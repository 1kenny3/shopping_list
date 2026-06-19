create_table = """CREATE TABLE IF NOT EXISTS products(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product TEXT NOT NULL,
        completed INTEGER DEFAULT 0
    )"""

insert_task = "INSERT INTO products (product) VALUES (?)"

select_task = "SELECT id, product, completed FROM products"

select_tasks_completed = "SELECT id, product, completed FROM products WHERE completed = 1"

select_tasks_uncompleted = "SELECT id, product, completed FROM products WHERE completed = 0"

update_task = "UPDATE products SET completed = ? WHERE id = ?"

delete_task = "DELETE FROM products WHERE id = ?"
