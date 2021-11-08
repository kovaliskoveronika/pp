from sqlalchemy import Column, BOOLEAN, Integer, VARCHAR, DATETIME, ForeignKey

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
engine = create_engine("mysql+mysqlconnector://root:Newpassword@localhost/lab6", echo=True)
Base = declarative_base()

metadata = Base.metadata

class User(Base):
    __tablename__ = 'user'
    id_user = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(VARCHAR(25), nullable=False)
    first_name = Column(VARCHAR(25), nullable=False)
    last_name = Column(VARCHAR(25), nullable=False)
    email = Column(VARCHAR(25), nullable=False)
    password = Column(VARCHAR(205), nullable=False)
    phone = Column(VARCHAR(25), nullable=False)

    def __init__(self, id_user, username, first_name, last_name, email, password, phone):
        self.id_user = id_user
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone = phone

    def __repr__(self):
        return 'User ' + str(self.id_user) + ' ' + self.username + ' ' + self.first_name + ' ' + self.last_name + ' ' + self.email + ' ' + self.password + ' ' + self.phone + '\n'



class Major(Base):
    __tablename__ = 'major'
    id_major = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(45), nullable=False)
    def __init__(self, id_major, name):
        self.id_major = id_major
        self.name = name

    def __repr__(self):
        return 'Major ' + str(self.id_major) + ' ' + self.name + '\n'




class Student(Base):
    __tablename__ = 'student'
    id_student = Column(Integer, primary_key=True, autoincrement=True)
    name_student = Column(VARCHAR(45), nullable=False)
    last_name_student = Column(VARCHAR(45), nullable=False)
    email = Column(VARCHAR(100), nullable=False)
    rating = Column(VARCHAR(45))
    id_major = Column(Integer, ForeignKey('major.id_major'), nullable=False)
    id_user = Column(Integer, ForeignKey('user.id_user'), nullable=False)

    def __init__(self, id_student, name_student, last_name_student, rating, email, id_major, id_user):
        self.id_student = id_student
        self.name_student = name_student
        self.last_name_student = last_name_student
        self.phone = rating
        self.email = email
        self.id_major = id_major
        self.id_user = id_user

    def __repr__(self):
        return 'Student ' + str(
            self.id_student) + ' ' + self.name_student + ' ' + self.last_name_student + ' ' + self.email + ' ' + str(
            self.id_major) + '\n'


class Subject(Base):
    __tablename__ = 'subject'
    id_subject = Column(Integer, primary_key=True, autoincrement=True)
    name_subject = Column(VARCHAR(100), nullable=False)
    def __init__(self, id_subject, name_subject):
        self.id_subject = id_subject
        self.name_subject = name_subject

    def __repr__(self):
        return 'Subject ' + str(self.id_subject) + ' ' + self.name_subject + '\n'




class Mark(Base):
    __tablename__ = 'mark'

    id_mark = Column(Integer, primary_key=True, autoincrement=True)
    grade = Column(Integer, nullable=False)
    id_subject = Column(Integer, ForeignKey('subject.id_subject'), nullable=False)
    id_student = Column(Integer, ForeignKey('student.id_student'), nullable=False)
    id_user = Column(Integer, ForeignKey('user.id_user'), nullable=False)
    def __init__(self, grade, id_subject, id_student, id_user):
        self.grade = grade
        self.id_subject = id_subject
        self.id_student = id_student
        self.id_user = id_user

    def __repr__(self):
        return 'Mark ' + str(self.grade) + ' ' + str(self.id_student) + ' ' + str(self.id_subject) + '\n'


#
# class User(Base):
#     __tablename__ = 'user'
#     id_user = Column(Integer, primary_key=True)
#     username = Column(VARCHAR(25), nullable=False)
#     first_name = Column(VARCHAR(25), nullable=False)
#     last_name = Column(VARCHAR(25), nullable=False)
#     email = Column(VARCHAR(25), nullable=False)
#     password = Column(VARCHAR(25), nullable=False)
#     phone = Column(VARCHAR(25), nullable=False)
#
#
# class Category(Base):
#     __tablename__ = 'category'
#     id_category = Column(Integer, primary_key=True)
#     name_category = Column(VARCHAR(45), nullable=True)
#
#
# class Medicine(Base):
#     __tablename__ = 'medicine'
#     id_medicine = Column(Integer, primary_key=True)
#     name_medicine = Column(VARCHAR(45), nullable=False)
#     manufacurer = Column(Integer, nullable=False)
#     price = Column(Integer, nullable=False)
#     id_stock = Column(BOOLEAN, nullable=False)
#     demand = Column(BOOLEAN, nullable=False)
#     id_stock_number = Column(Integer, nullable=False)
#     demand_number = Column(Integer, nullable=False)
#     category_id = Column(Integer, ForeignKey('category.id_category'), nullable=False)
#
# class Order(Base):
#     __tablename__ = 'order'
#     id_order = Column(Integer, primary_key=True, autoincrement=True)
#     shipDate = Column(DATETIME, nullable=False)
#     status = Column(VARCHAR(45), nullable=False)
#     complete = Column(BOOLEAN, nullable=False)
#     user_id = Column(Integer, ForeignKey('user.id_user'), nullable=False)
#     medicine_id = Column(Integer, ForeignKey('medicine.id_medicine'), nullable=False)
#     # medicine = relationship("Medicine", primaryjoin="Order.id_medicine==Medicine.id_medicine")
