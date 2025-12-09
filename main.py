from flask import Flask, render_template, request, redirect, url_for
from Database import get_products, get_sales, insert_products, insert_sales

# Flask instance
app = Flask(__name__)

# index route
@app.route('/')
def home():
        return render_template("index.html", current_year=2025)
    
# Products route
@app.route('/products')
def fetch_products():
        products = get_products()
        return render_template("products.html",products = products)

@app.route('/add_products',methods=['GET','POST'])
def products():
        product_name = request.form["product_name"]
        buying_price = request.form["buying_price"]
        selling_price = request.form["selling_price"]
        new_product = (product_name, buying_price, selling_price)
        insert_products(new_product)
        return redirect(url_for('fetch_products'))

# Sales route
@app.route('/sales')
def fetch_sales():
        sales = get_sales()
        return render_template("sales.html",sales = sales)
    
@app.route('/add_sales',methods=['GET','POST'])
def sales():
        product_id = request.form['product_id']
        quantity = request.form['quantity']
        new_sale = (product_id,quantity)
        insert_sales(new_sale)
        return redirect(url_for('fetch_sales'))

# dashboard route
@app.route('/dashboard')
def dashboard():
        return render_template("dashboard.html")
    

# login route
@app.route('/login')
def login():
        return render_template("login.html")
    

# Register route
@app.route('/register')
def register():
        return render_template("register.html")




# app run 
app.run(debug=True)