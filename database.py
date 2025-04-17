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
    for product in products:
        print(product)

fetching_products()


# query 2
def fetching_categories():
    cur.execute('select * from categories;')

    categories=cur.fetchall()
    for category in categories:
         print(category)

fetching_categories()


# inserting into products
def insert_products():
    cur.execute("insert into products(supplierid,categoryid,productname,unit,price)values(2,2,'juice','2 litres','2k')")
    cur.execute("insert into products(supplierid,categoryid,productname,unit,price)values(3,4,'biscuit','2 packets','300')")
    cur.execute("insert into products(supplierid,categoryid,productname,unit,price)values(3,4,'blueband','2 containers','500')")
    cur.execute("insert into products(supplierid,categoryid,productname,unit,price)values(3,4,'tomato sauce','2 bottles','400')")
    conn.comit()

# insert into categories
def insert_categories():
    cur.execute("insert into categories(categoryname,description)values('beef products','sausages and burgers')")
    cur.execute("insert into categories(categoryname,description)values('agriculture products','flowers and fruits')")
    cur.execute("insert into categories(categoryname,description)values('animal products','skin and bones')")
    conn.commit()

insert_products()
insert_categories()
fetching_products()
fetching_categories()

time=datetime.now()
print(time)