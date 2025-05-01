# importinf flask to use it
from flask import Flask, render_template, request, redirect, url_for
from database import fetching_products,fetching_categories,insert_products,insert_categories

# instantiate your application - initialization 
# flask instance
app= Flask(__name__)

# __name__ - informs pyhton that this is the main application
# __name__ - special inbuilt variable 
# represents the name of the current file where your application is built 
# informs flask where your project starts

@app.route('/')
def home():
    user={'name':'Levy','location':'nairobi'}
    numbers=[1,2,3,4,5]
    return render_template ('index.html',data=user,numbers=numbers)

@app.route('/products')
def products():
    products=fetching_products()
    return render_template ('products.html',products=products)

@app.route('/add_products',methods=['GET','POST'])
def add_products():
    if request.method=='POST':
        supplierID=request.form['SID']
        categoryID=request.form['CID']
        productName=request.form['ProductName']
        unit=request.form['Unit']
        price=request.form['Price']
        new_product=(supplierID,categoryID,productName,unit,price)
        insert_products(new_product)
        return redirect(url_for('home'))



@app.route('/categories')
def categories():
    categories=fetching_categories()
    # print ("Categories in main\n",categories)
    return render_template ('categories.html',categories=categories)

@app.route('/add_categories',methods=['GET','POST'])
def add_categories():
    if request.method=='POST':
        categoryID=request.form['CID']
        categoryname=request.form['CN']
        description=request.form['Desc']
        new_category=(categoryname,description)
        insert_categories(new_category)
        return redirect(url_for('categories'))

    

@app.route('/task')
def task():
    fruits=['pineapple','apple','mango','orange']
    return render_template('task.html',fruits=fruits)

app.run(debug=True)