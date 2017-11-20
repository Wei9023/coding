import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, INTEGER, String, func, DATE,Enum
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:tonys-air@192.168.0.6/vvtestdb")

Base =declarative_base()
class user(Base):
    __tablename__='user'
    id = Column(INTEGER,primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return "<%s name:%s>" %(self.id,self.name)

class Student(Base):
    __tablename__ ="student"
    id = Column(INTEGER, primary_key= True)
    name = Column(String(32),nullable=False)
    age = Column(INTEGER,nullable=False)
    register_date = Column(DATE, nullable=False)
    gender = Column(Enum("M","F"),nullable=False)

Base.metadata.create_all(engine)


Session_class = sessionmaker(bind=engine)
Session = Session_class()

#user_obj = user(name = "valentina", password = "123456")
#user_obj2 = user(name = "tonysun", password = "123456")
#Session.add(user_obj)
#Session.add(user_obj2)

#data = Session.query(user).filter(user.id>0).filter(user.id<2).first()
#data.name = "vv"

#fake_user = user(name='pizza', password='123456')
#Session.add(fake_user)

#print (Session.query(user).filter(user.name.in_(['vv','pizza'])).all())

#print (Session.query(user).filter(id>0).count())

#print (Session.query(func.count(user.name),user.name).group_by(user.name).all())

#s1 = Student(name="tonysun",age=33,register_date="1985-06-15",gender="M")
#Session.add(s1)

#print(Session.query(user,Student).filter(user.name==Student.name).all())

Session.commit()

