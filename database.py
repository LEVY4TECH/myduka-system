import psycopg2
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