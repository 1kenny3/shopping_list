import sqlite3
from config import path_db
from db import queries


def init_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.create_table)
    print("ДБ подключена")
    conn.commit()
    conn.close()


def add_product_db(product):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.insert_task, (product,))
    conn.commit()
    product_id = cursor.lastrowid
    conn.close()
    return product_id


def delete_product_db(product_id):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.delete_task, (product_id,))
    conn.commit()
    conn.close()


def toggle_product_db(product_id, completed):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.update_task, (completed, product_id))
    conn.commit()
    conn.close()


def get_products(filter_type="all"):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    if filter_type == "completed":
        cursor.execute(queries.select_tasks_completed)
    elif filter_type == "uncompleted":
        cursor.execute(queries.select_tasks_uncompleted)
    else:
        cursor.execute(queries.select_task)
    products = cursor.fetchall()
    conn.close()
    return products
