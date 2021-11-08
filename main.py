from flask import Blueprint, Response, request, jsonify, Flask
from marshmallow import ValidationError
from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SECRET_KEY'] = "Newpassword"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:Newpassword@localhost/lab6"

counter = 15
bcrypt = Bcrypt(app)
session = sessionmaker(bind=engine)
ss = session()
purses = 1
id_student = 19

@app.route('/user', methods=['POST'])
def create_user():
    global counter
    try:
        data = request.get_json(force=True)
        hashed_password = bcrypt.generate_password_hash(data["password"])
        new_user = User(counter, data["username"], data["first_name"],
                        data["last_name"], data["email"], hashed_password, data["phone"])
    except:
        return Response(status=400, response='Invalid user suplied')
    counter += 1
    ss.add(new_user)
    ss.commit()
    return Response(status=200, response='successful operation')
@app.route('/user/<id_user>', methods=['GET'])
def get_user_by_id(id_user):
    try:
        user = ss.query(User).filter(User.id_user == id_user).first()
    except:
        return Response(status=400, response='Invalid ID supplied')
    if not user:
        return Response(status=404, response='Purse not found')
    user_data = {"id_user": user.id_user, "username": user.username, "first_name": user.first_name, "last_name": user.last_name}
    return jsonify({"user": user_data}), 200

@app.route('/user/<id_user>', methods = ['PUT'])
def refresh_user(id_user):
    data = request.get_json(force=True)
    users = ss.query(User).filter(User.id_user == id_user).first()
    if not users:
        return Response(status=404, response='User not found')
    try:
        if("username" in list(data)):
            users.username = data['username']
        if("first_name" in list(data)):
            users.first_name = data['first_name']
        if('last_name' in list(data)):
            users.last_name = data['last_name']
        if('email' in list(data)):
            users.email = data['email']
        if('password' in list(data)):
           users.password = data['password']
        if('phone' in list(data)):
            users.phone = data['phone']
    except:
        return Response(status = 400, response = 'Invalid user suplied')
    ss.commit()
    state_data = {"username": users.username ,"first_name" : users.first_name, "last_name" : users.last_name,
                  "email" : users.email, "phone" : users.phone}
    return jsonify({"user": state_data}), 200
@app.route('/user/<id_user>', methods = ['DELETE'])
def delete_user(id_user):
    try:
        users = ss.query(User).filter(User.id_user == id_user).first()
    except:
        return Response(status = 400, response = 'Invalid userphone supplied')
    if not users:
        return Response(status = 404, response = 'User not found')
    ss.delete(users)
    ss.commit()
    return Response(status = '200',response = 'successful operation')

@app.route('/student', methods = ['POST'])
def create_student():
    global id_student
    try:
        data = request.get_json(force=True)
        new_student = Student(id_student, data["name_student"], data["last_name_student"], data["email"],
                        data["rating"], data["id_major"], data["id_user"])
    except:
        return Response(status=400, response='Invalid student suplied')
    id_student += 1
    ss.add(new_student)
    ss.commit()
    return Response(status=200, response='successful operation')
@app.route('/student/<id_student>', methods = ['PUT'])
def refresh_student(id_student):
    data = request.get_json(force=True)
    students = ss.query(Student).filter(Student.id_student == id_student).first()
    if not students:
        return Response(status=404, response='Student not found')
    try:
        if("name_student" in list(data)):
            students.name_student = data['name_student']
        if('last_name_student' in list(data)):
            students.last_name_student = data['last_name_student']
        if('email' in list(data)):
            students.email = data['email']
        if('rating' in list(data)):
           students.rating = data['rating']
        if('id_major' in list(data)):
            students.id_major = data['id_major']
        if('id_user' in list(data)):
            students.id_user = data['id_user']
    except:
        return Response(status = 400, response = 'Invalid student suplied')
    ss.commit()
    state_data = {"name_student": students.name_student ,"last_name_student" : students.last_name_student, "email" : students.email,
                  "rating" : students.rating, "id_major" : students.id_major, "is_user": students.id_user}
    return jsonify({"user": state_data}), 200

@app.route('/student/<id_student>', methods=['GET'])
def get_student_by_id(id_student):
    try:
        student = ss.query(Student).filter(Student.id_student == id_student).first()
    except:
        return Response(status=400, response='Invalid ID supplied')
    if not student:
        return Response(status=404, response='Student not found')
    user_data = {"id_student": student.id_student, "name_student": student.name_student, "last_name_student": student.last_name_student}
    return jsonify({"user": user_data}), 200

@app.route('/student/<id_student>', methods = ['DELETE'])
def delete_student(id_student):
    try:
        student = ss.query(Student).filter(Student.id_student == id_student).first()
    except:
        return Response(status=400, response='Invalid id_student supplied')
    if not student:
        return Response(status=404, response='Student not found')
    ss.delete(student)
    ss.commit()
    return Response(status='200', response='successful operation')

if __name__ == '__main__':
    app.run(debug=False)
