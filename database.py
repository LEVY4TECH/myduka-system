import psycopg2
from datetime import datetime
# create connection to the database
conn=psycopg2.connect(user='postgres', password='leshan1234', host='localhost', port='5432', database='w3schoolsdb')

# execute database operations
cur=conn.cursor()

# query 1
def fetching_products():
    cur.execute('select * from products;')

    products=cur.fetchall()
    return products
   
fetching_products()


# # query 2
def fetching_categories():
    cur.execute('select * from categories;')

    categories=cur.fetchall()
    for category in categories:
         print(category)

fetching_categories()


# inserting into products
# def insert_products():
#     cur.execute("insert into products(supplierid,categoryid,productname,unit,price)values(2,2,'juice','2 litres','2k')")
#     cur.execute("insert into products(supplierid,categoryid,productname,unit,price)values(3,4,'biscuit','2 packets','300')")
#     cur.execute("insert into products(supplierid,categoryid,productname,unit,price)values(3,4,'blueband','2 containers','500')")
#     cur.execute("insert into products(supplierid,categoryid,productname,unit,price)values(3,4,'tomato sauce','2 bottles','400')")
#     conn.commit()
    


# insert into categories
def insert_categories():
    cur.execute("insert into categories(categoryname,description)values('beef products','sausages and burgers')")
    cur.execute("insert into categories(categoryname,description)values('agriculture products','flowers and fruits')")
    cur.execute("insert into categories(categoryname,description)values('animal products','skin and bones')")
    conn.commit()

# insert_products()
insert_categories()
fetching_products()
fetching_categories()

time=datetime.now()
print(time)


# def select_data(conn,, ['supplierid','categoryid','productname','unit','price']):
#     cursor = conn.cursor()
#     col_names = ', '.join(columns) if isinstance(columns, list) else columns
#     sql = f"SELECT {col_names} FROM {table}"
#     cursor.execute(sql)
#     results = cursor.fetchall()
#     cursor.close()
#     return results


# re-usable code of fetching data from any table
def fetch_data(table):
    cur.execute(f"select * from {table};")
    data=cur.fetchall()
    return data

products=fetch_data('products')
categories=fetch_data('categories')
print("products from fetch data func:\n",products)
print("categories from fetch data func:\n",categories)


# INSERTING 1: TAKE VALUES AS PARAMETERS
def insert_products(values):
    # use placeholders
    insert="insert into products(supplierid,categoryid,productname,unit,price)values(%s,%s,%s,%s,%s)"
    cur.execute(insert,values)
    conn.commit()

product_values=(5,89,'changaa','4 jericans','20000')
product_values2=(3,56,'water','3 bottles','4500')
# insert_products(product_values)
# insert_products(product_values2)
# products=fetch_data('products')
# print("fetching data after modified func.\n",products)


# INSERTING METHOD 2: STILL TAKES VALUES AS PARAMETERES BUT DOES NOT USE PLACEHOLDERS
# Intead we replace placeholders with {value} parameters in a formatted string
def insert_products_method_two(values):
    insert=f"insert into products(supplierid,categoryid,productname,unit,price)values{values}"
    cur.execute(insert)
    conn.commit()

product_values=(4,34,'juiss','6 litres','5600')
product_values2=(2,78,'sugar','7 kilos','970')
product_values3=(1,67,'mchele','8 kilos','1080')
# insert_products_method_two(product_values)
# insert_products_method_two(product_values2)
# insert_products_method_two(product_values3)
# products=fetch_data('products')
# print("fetching prods method 2:\n",products)


# METHOD 3: INSERTING DATA INTO MULTIPLE TABLES WITH VARYING NUMBER OF COLUMNS

# insert into <
def insert_data(table,columns,values):
    cur.execute(f"insert into {table}({columns})values{values}")
    conn.commit()

# repeatable method when one wants to insert data in another table or insert different values
table='products'
columns="supplierid,categoryid,productname,unit,price"
values=(3,2,'milo','2 tins','789')
insert_data(table,columns,values)
products=fetch_data('products')
print("data from last method:\n",products)

table='categories'
columns='categoryname,description'
values=('alcoholic drinks','smirn off, hennesy, vodka')
insert_data(table,columns,values)
categories=fetch_data('categories')
print("practising my method:\n",categories)




