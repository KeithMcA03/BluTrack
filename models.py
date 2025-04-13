from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Customer table
class Customer(db.Model):
    Customer_ID = db.Column(db.Integer, primary_key=True)
    First_Name = db.Column(db.String(50))
    Last_Name = db.Column(db.String(50))
    Email = db.Column(db.String(100), unique=True)
    Phone_Number = db.Column(db.String(20))

# Admin table
class Admin(db.Model):
    Admin_ID = db.Column(db.Integer, primary_key=True)
    First_Name = db.Column(db.String(50))
    Last_Name = db.Column(db.String(50))
    Email = db.Column(db.String(100), unique=True)
    Password = db.Column(db.String(255)) 

# Dumpster table
class Dumpster(db.Model):
    Dumpster_ID = db.Column(db.Integer, primary_key=True)
    Size = db.Column(db.String(20))
    Status = db.Column(db.String(20))  # Available, In Use, etc.

# Order table
class Order(db.Model):
    Order_ID = db.Column(db.Integer, primary_key=True)
    Customer_ID = db.Column(db.Integer, db.ForeignKey('customer.Customer_ID'))
    Admin_ID = db.Column(db.Integer, db.ForeignKey('admin.Admin_ID'))
    Dumpster_ID = db.Column(db.Integer, db.ForeignKey('dumpster.Dumpster_ID'))
    Street1 = db.Column(db.String(100))
    Street2 = db.Column(db.String(100))
    City = db.Column(db.String(50))
    ZIP_Code = db.Column(db.String(10))
    Status = db.Column(db.String(30))
    Delivery_Date = db.Column(db.Date)
    Pickup_Date = db.Column(db.Date)

# Status History table
class StatusHistory(db.Model):
    Status_ID = db.Column(db.Integer, primary_key=True)
    Order_ID = db.Column(db.Integer, db.ForeignKey('order.Order_ID'))
    Status = db.Column(db.String(30))
    TimeStamp = db.Column(db.DateTime)
