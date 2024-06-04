import sqlite3



class Database():

    def __init__(self):
        self.connection = sqlite3.connect("/home/iz/QAAutoPrometeus2024IZU/become_qa_auto.db")
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_query= "Select sqlite_version();"
        self.cursor.execute(sqlite_select_query)
        record =self.cursor.fetchall()
        print(f"Connected is succcesfully. SQlite Database Version is: {record}")

    def get_all_users(self):
        query = "Select name, address, city from customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_user_adress_by_name(self, name):
        query = f"Select address, city, postalCode, country from customers where name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} where id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_id(self, product_id):
        query = f"Select quantity from products where id = {product_id} "
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def insert_product(self, product_id, name, description, qnt):
        query = (f" Insert or Replace Into products (id, name, description, quantity) \
                Values ({product_id}, '{name}', '{description}', '{qnt}')")
        self.cursor.execute(query)
        self.connection.commit()


    def delete_product_by_id(self, product_id):
        query = f"Delete from products where id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = ("Select orders.id, customers.name, products.name, \
                 products.description, orders.order_date \
                 from orders \
                 join customers on orders.customer_id = customers.id \
                 join products on orders.product_id = products.id")
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record