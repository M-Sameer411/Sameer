from app import app, Products
from flask_mysqldb import MySQL
from flask import request, jsonify
import MySQLdb.cursors
from flask_migrate import Migrate


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'SuperMarket'

migrate = Migrate(app) 
mysql = MySQL(app)

@app.route('/users/products', methods = ["GET"])
def items():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM products")
    info = cursor.fetchall()
    return jsonify(info)


@app.route('/admin/products', methods = ["POST"])
def add_items():
    if request.method == 'POST' and 'ID' in request.form and 'Product_Name' in request.form and 'Description' in request.form and 'Price' in request.form:
        ID = request.form["ID"]
        Product_Name = request.form["Product_Name"]
        Description = request.form["Description"]
        Price = request.form["Price"]
        print(ID, Product_Name, Description, Price)

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO products VALUES (%s, %s, %s, %s)', (ID, Product_Name, Description, Price))
        mysql.connection.commit()
        cursor.close()
    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(debug=True)