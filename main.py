from flask import Flask, render_template, request, redirect, url_for,flash,session
from Database import get_products, get_sales, get_users, insert_products, insert_sales, insert_users, insert_stock, available_stock, get_stock, check_user_exists, insert_users, sales_per_product, sales_per_day, profit_per_day, profit_per_product
from flask_bcrypt import Bcrypt
from functools import wraps

# Flask instance
app = Flask(__name__)


# Creating bcrypt object
bcrypt = Bcrypt(app)

# Secret key - sign session data
app.secret_key = 'liverpool20eplsoewok'

# index route
@app.route('/')
def home():
        return render_template("index.html", current_year=2025)
    
def login_required(f):
        @wraps(f)
        def protected(*args,**kwargs):
                if 'email' not in session:
                        return redirect(url_for('login'))
                return f(*args,**kwargs)
        return protected


# Products route
@app.route('/products')
@login_required
def fetch_products():
        products = get_products()
        # Rendering products in product html file
        return render_template("products.html",products = products)

# Adding products by getting('GET') products and posting('POST') products
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
@login_required
def fetch_sales():
        sales = get_sales()
        products = get_products()
        return render_template("sales.html",sales = sales, products = products)

#Adding sales by getting ('GET') sales and posting ('POST') sales
@app.route('/add_sales',methods=['GET','POST'])
def sales():
        product_id = request.form['product_id']
        quantity = request.form['quantity']
        new_sale = (product_id,quantity)
        check_stock = available_stock(product_id)
        if check_stock < float(quantity):
                flash("insufficient srock",'danger')
                return redirect(url_for('fetch_sales'))
        insert_sales(new_sale)
        flash("Sale made successully",'success')
        return redirect(url_for('fetch_sales'))

# Routing stocks
@app.route('/stock')
def fetch_stock():
        stock = get_stock()
        products = get_products()
        return render_template("stock.html", stock = stock, products = products)

# Write a function to insert stock
@app.route('/add_stock', methods=['GET','POST'])
def stock():
        product_id = request.form['product_id']
        stock_quantity = request.form['stock_quantity']
        new_stock = (product_id, stock_quantity)
        insert_stock(new_stock)
        return redirect(url_for('fetch_stock')) 

       

       
                
# dashboard route
@app.route('/dashboard')
@login_required
def dashboard():
        product_sales = sales_per_product()
        daily_sales = sales_per_day()
        product_profit = profit_per_product()
        daily_profit = profit_per_day()
        
        product_names = [ i[0] for i in product_sales ]
        sales_per_p = [ float(i[1]) for i in product_sales ]
        profit_per_p = [ float(i[1]) for i in product_profit ]
        
        date = [ str(i[0]) for i in daily_profit]
        sales_per_d = [ float(i[1]) for i in daily_sales]
        profit_per_d = [ float(i[1]) for i in daily_profit]
        
        return render_template("dashboard.html",
        product_names=product_names, sales_per_p=sales_per_p,profit_per_p=profit_per_p,
        date= date, sales_per_d=sales_per_d,profit_per_d=profit_per_d           
                           ) 
    

# login route
@app.route('/login', methods=['GET','POST'])
def login():
        if request.method == 'POST':
                email = request.form['email']
                password = request.form['password']
                registered_user = check_user_exists(email)
                if not registered_user:
                    flash("User with this email does not exist, register",'danger')
                else:
                    if bcrypt.check_password_hash(registered_user[-1],password):
                        flash("Login sucessful",'success')
                        session['email'] = email
                        return redirect(url_for('dashboard'))
                    else:
                        flash("Passorwd incorrect",'danger')
        return render_template("login.html")

    

# Register route
@app.route('/register', methods=['GET','POST'])
def register():
        if request.method == 'POST':
                full_name = request.form["name"]
                email = request.form["email"]
                phone_number = request.form["phone"]
                password = request.form["password"]
                existing_user = check_user_exists(email)
                if not existing_user:
                        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
                        new_user = (full_name,email,phone_number,hashed_password)
                        insert_users(new_user)
                        flash("User registered sucessfully",'succes')
                        return redirect(url_for('login'))
                else:
                        flash("User with this email already exists,login instead",'danger')
        return render_template("register.html")
        
@app.route('/logout')
def logout():
        session.pop('email',None)
        flash("Logged out successfully",'success')
        return redirect(url_for('login'))

# app run 
app.run(debug=True)