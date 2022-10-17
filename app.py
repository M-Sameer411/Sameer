from crypt import methods
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mysqldb import MySQL
import re


app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'SuperMarket'

#app.config['SQLALCHEMY_DATABASE_URI'] = ('mysql://root:''@localhost:3306/SuperMarket')
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate = Migrate(app, db)

mysql = MySQL(app)

class User(db.Model):
    Name = db.Column(db.String(50))
    Email = db.Column(db.String(50), primary_key = True)
    Password = db.Column(db.String(50))

    customer = db.relationship('Details', backref = 'User')
    receipt = db.relationship('Order', backref = 'User')

    def __repr__(self):
        return f'<User: {self.Email,self.Password}>'

class Products(db.Model):
    ID = db.Column(db.Integer(), primary_key = True)
    Product_Name = db.Column(db.String(50))
    Description = db.Column(db.String(50))
    Price = db.Column(db.Integer())
    Product_Image = db.Column(db.String(50))

    details = db.relationship('Details', backref = 'Products')
    def __repr__(self):
        return f'<Products: {self.ID, self.Product_Name, self.Price, self.Product_Image}>'

class Details(db.Model):
    Cart_ID = db.Column(db.Integer(), primary_key = True)
    Quantity = db.Column(db.Integer())
    Total_Price = db.Column(db.Integer())

    User_Email = db.Column(db.String(50), db.ForeignKey('user.Email'))
    Products_ID = db.Column(db.Integer(), db.ForeignKey('products.ID'))

    item = db.relationship('Order', backref = 'Details')


    def __repr__(self):
        return f'<Details: {self.User_Email,self.Products_ID, self.Cart_ID, self.Quantity, self.Total_Price}'

class Order(db.Model):
    Email = db.Column(db.String(50))
    Order_ID = db.Column(db.Integer(), primary_key = True)

    Purchasing_Date = db.Column(db.DateTime) 

    User_Email = db.Column(db.String(50), db.ForeignKey('user.Email'))
    Cart_ID = db.Column(db.Integer(), db.ForeignKey('details.Cart_ID')) 


    def __repr__(self):
        return f'<Order: {self.Email, self.Cart_ID, self.Cart_ID, self.Purchasing_Date}>'



@app.route('/')
def greeting():
    return "Welcome to the Super Market"

if __name__ == "__main__":
    app.run(debug=True)