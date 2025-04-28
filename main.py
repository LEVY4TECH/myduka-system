# importinf flask to use it
from flask import Flask, render_template

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
    return render_template ('products.html')

@app.route('/categories')
def categories():
    return render_template ('categories.html')

app.run(debug=True)