from optparse import Values
import psycopg2

conn = psycopg2.connect(host='localhost',port='5432',user='postgres',password='1234',dbname='myduka_db')

cur = conn.cursor()



def products():
    cur.execute("select * from products")
    products = cur.fetchall()
    return products



def insert_products():
    cur.execute(f"insert into products(name, buying_price, selling_price) values{Values}")
    conn.commit()

values = ('Goat',60000,7000)
products = insert_products

print(products)
