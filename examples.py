from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Boolean, Integer, String, Date, ForeignKey

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from models import *

session = sessionmaker(bind=engine)
# user_1 = User(id_user=1, username ="teacher1", first_name ="Firstname1", last_name ="Lastname2", email ="email1", password ="abc1",
#                 phone ='1111')
# user_2 = User(id_user=2, username ="teacher2", first_name ="Firstname2", last_name ="Lastname2", email ="email2", password ="abc2",
#                phone ='2222')
subject_1 = Subject(id_subject = 1, name_subject ='Іноземна мова за професійним спрамюванням, частина 1')
subject_2 = Subject(id_subject = 2, name_subject ='Менеджмент')
subject_3 = Subject(id_subject = 3, name_subject ='Педагогіка')
subject_4 = Subject(id_subject = 4, name_subject ='Математичні методи в психології')
subject_5 = Subject(id_subject = 5, name_subject ='Теорія інформації')
# student_1 = Student(id_student =1, name_student ='Дольницька', last_name_student ='Вероніка',
#                     phone = '38(050)669-70-33', email ='quireumoppoinu-6188@yopmail.com', id_major =51, id_user =1)
# student_2 = Student(id_student =2, name_student ='Танська', last_name_student ='Уляна',
#                     rating = '38(050)756-89-63', email ='joicrocepeho-8197@yopmail.com', id_major =81, id_user =1)
# student_3 = Student(id_student =3, name_student ='Мацюра', last_name_student ='Альвіна',
#                     rating = '38(050)157-64-23', email ='croippequereupru-6665@yopmail.com', id_major =53, id_user =1)
# student_4 = Student(id_student =4, name_student ='Кусень', last_name_student ='Естер',
#                     rating = '38(050)231-28-58', email ='cressoibauxemu-8205@yopmail.com', id_major =122, id_user =1)
# student_5 = Student(id_student =5, name_student ='Гетьман', last_name_student ='Зоряна',
#                     rating = '38(050)273-21-67', email ='criyakifrezu-8177@yopmail.com', id_major =122, id_user =1)
# student_6 = Student(id_student =6, name_student ='Гуляк', last_name_student ='Грива',
#                     rating = '38(050)237-10-12', email ='tucetteippeubre-3395@yopmail.com', id_major =53, id_user =1)
# student_7 = Student(id_student =7, name_student ='Гайдукевич', last_name_student ='Корнелій',
#                     rating = '38(050)798-12-16', email ='neinneifoiffuneu-5125@yopmail.com', id_major =51, id_user =1)
# student_8 = Student(id_student =8, name_student ='Терещук', last_name_student ='Щастислав',
#                     rating = '38(050)588-43-69', email ='koucressazeca-2388@yopmail.com', id_major =122, id_user =1)
# student_9 = Student(id_student =9, name_student ='Трутовський', last_name_student ='Борис',
#                     rating = '38(050)429-59-64', email ='vuyuttiprouza-9514@yopmail.com', id_major =51, id_user =1)
# student_10 = Student(id_student =10, name_student ='Геровський', last_name_student ='Острозор',
#                      rating = '38(050)023-03-52', email ='labressasohi-3315@yopmail.com', id_major =122, id_user =1)
# mark_1 = Mark(id_mark =1, grade =2, id_subject =1, id_student =1,id_user =1)
# mark_2 = Mark(id_mark =2, grade =5, id_subject =2, id_student =2,id_user =1)
# mark_3 = Mark(id_mark =3, grade =3, id_subject =3, id_student =10,id_user =2)
major_51 = Major(id_major =51, name = 'Економіка')
major_53 = Major(id_major =53, name = 'Психологія')
major_81 = Major(id_major =81, name = 'Право')
major_122 = Major(id_major =122, name = 'Комп\'ютерні науки')

ss = session()

# ss.add(user_1)
# ss.add(user_2)
# ss.add(major_51)
# ss.add(major_53)
# ss.add(major_81)
# ss.add(major_122)
# ss.add(subject_1)
# ss.add(subject_2)
# ss.add(subject_3)
# ss.add(subject_4)
# ss.add(subject_5)
# ss.commit()
# ss.add(student_1)
# ss.add(student_2)
# ss.add(student_3)
# ss.add(student_4)
# ss.add(student_5)
# ss.add(student_6)
# ss.add(student_7)
# ss.add(student_8)
# ss.add(student_9)
# ss.add(student_10)
# ss.commit()
# ss.add(mark_1)
# ss.add(mark_2)
# ss.add(mark_3)
# ss.commit()
# ss.add(add_order)
# ss.add(add_order_2)
# ss.add(add_order_2)
# ss.commit()


# add_category = Category(id_category=57, name_category='ffff')
# add_category_53 = Category(id_category=53, name_category='ffff')
# add_category_81 = Category(id_category=81, name_category='ffff')
# add_user = User(id_user=0, username='люблячий_брат', first_name='ітачі', last_name='учіха',
#                 email='ilovemyfamilie@gmail.com', password='saske', phone=666)
# add_user_2 = User(id_user=2, username='7 хокаге', first_name='наруто', last_name='узумакі',
#                   email='saskegohome@gmail.com', password='saske2',  phone=111)
# add_medicine = Medicine(id_medicine=1, name_medicine='ношпа', manufacurer=1, price=20, id_stock=1, demand=False,
#                         id_stock_number=1, demand_number=2, category_id=51)
# add_medicine_2 = Medicine(id_medicine=2, name_medicine='спазмалгін', manufacurer=1, price=24, id_stock=1, demand=False,
#                           id_stock_number=1, demand_number=2, category_id=53)
# add_medicine_3 = Medicine(id_medicine=3, name_medicine='гофен', manufacurer=1, price=40, id_stock=1, demand=False,
#                           id_stock_number=1, demand_number=22, category_id=81)
# add_order = Order(id_order=0, shipDate='2020-11-05', status='to_do', complete=False, user_id=1, medicine_id=1)
# add_order_2 = Order(id_order=2, shipDate='2020-11-07', status='done', complete=True, user_id=2, medicine_id=2)
# add_order_3 = Order(id_order=3, shipDate='2020-12-05', status='to_do', complete=False, user_id=1, medicine_id=3)
# add_transfer3 = Transfer(transfer_id=3, quantity_funds= 100,  date='24.09.2021', purse_id_from=1,purse_id_to=2)
# ss = session()

# ss.add(add_user)
# ss.add(add_user_2)
# ss.add(add_category)
# ss.add(add_category_53)
# ss.add(add_category_81)
# ss.commit()
# ss.add(add_medicine)
# ss.add(add_medicine_2)
# ss.add(add_medicine_3)
# ss.commit()
# ss.add(add_order)
# ss.add(add_order_2)
# ss.add(add_order_2)
# ss.commit()
