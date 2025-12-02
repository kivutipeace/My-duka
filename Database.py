import psycopg2

# Establish connection to PostgresSQL
conn = psycopg2.connect(
    host = 'localhost',
    port = '5432',
    user = 'postgres',
    password = '1234',
    dbname = 'myduka_db'
)

cur = conn.cursor()

# ---------------------
#FUNCTION: Insert products products
# ----------------------
def insert_products(values):
    cur.execute(
        "INSERT INTO products(name, buying_price, selling_price) VALUES(%s, %s, %s)",
        (values)
        )
    conn.commit()

#-------------------------
# FUNCTION: Fetch all products
# ------------------------
def get_products():
    cur.execute("SELECT * From products")
    products = cur.fetchall
    return products

#----------------------------
# Getting the values
# ---------------------------
product_1 = ("Iphone 17",200000,300000)
insert_products(product_1)
products = get_products()
print(products)
    
# -----------------------
# FUNCTION: Inserting sales
# ------------------------
def insert_sales(values):
    cur.execute(
        "INSERT INTO sales(pid,quantity) VALUES(%s,%s)",
        (values)
    )
    conn.commit()
    
#------------------------
# FUNCTION: Fetch all sales
# --------------------------  
def get_sales():
    cur.execute("select * from sales")
    sales = cur.fetchall()
    return sales

# ------------------------
# Getting the values
#--------------------------
sale_1 = (2,2000)
insert_sales(sale_1)
sales = get_sales()
print(sales)
    
 





    
    