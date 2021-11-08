
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restx import Api

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Newpassword@localhost/lab6'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(
    app,
    version="1.0.0",
    title="Travel Agency API",
    description="Swagger documentation of Travel Agency API",
)






USERNAME = 'root'
PASSWORD = 'Newpassword'
SERVER = '127.0.0.1:3306'
DB = "mydb"
# alembic downgrade -1
#alembic upgrade +1
# mysql+pymysql://root:Newpassword@127.0.0.1:3306/mydb