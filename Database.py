import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    port = '5432',
    user = 'postgres',
    password = '1234',
    dbname = 'myduka_db'
)


cur = conn.cursor()

def products():
    cur.execute("SELECT * FROM products")
    return cur.fetchall()

def insert_products(name,buying_price,selling_price):
    cur.execute(
        "INSERT INTO products(name,buying_price,selling_price) VALUES(%s,%s,%s)",
        (name,buying_price,selling_price)
    )
    conn.commit()
    return "Producta added successfully"

# insert product
result = insert_products("Goat",60000,70000) 

# fetch all products
print(products())