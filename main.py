from flask import Flask
from Database import get_products
from Database import get_sales

# Flask instance
app = Flask(__name__)

# index
@app.route('/')
def home():
        return "This is the index route"
    

@app.route('/products')
def fetch_products():
        products = get_products()
        return products

@app.route('/sales')
def fetch_sales():
        sales = get_sales()
        return sales
    

# dashboard
@app.route('/dashboard')
def dashboard():
        return "This is a dashboard route"
    

# login
@app.route('/login')
def login():
        return "This is a login route"
    

# Register
@app.route('/register')
def register():
        return "This is a register route"

app.run()