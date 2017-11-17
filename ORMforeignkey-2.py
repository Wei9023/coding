import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, INTEGER, String, func, DATE,Enum, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("mysql+pymysql://root:tonys-air@192.168.0.6/vvtestdb")

Base =declarative_base()

class Student(Base):
    __tablename__ ="student"
    id = Column(INTEGER, primary_key= True)
    name = Column(String(32),nullable=False)
    register_date = Column(DATE, nullable=False)

    def __repr__(self):
        return "<%s name:%s>" %(self.id,self.name)

#abc
class StudyRecord(Base):
    __tablename__="study_record"
    id = Column(INTEGER, primary_key=True)
    day = Column(INTEGER,nullable=False)
    status = Column(String(32),nullable=False)
    stu_id = Column(INTEGER,ForeignKey('student.id'))

    student = relationship("Student", backref="study_record")

    def __repr__(self):
        return "<%s day:%s status:%s>" %(self.student.name,self.day,self.status)

Base.metadata.create_all(engine)

Session_class = sessionmaker(bind=engine)
Session = Session_class()

'''
s1= Student(name="vv",register_date="2010-09-23")
s2= Student(name="tt",register_date="2010-06-15")
s3= Student(name="bb",register_date="2010-08-21")
s4= Student(name="pp",register_date="2010-03-30")

study_obj1 = StudyRecord(day = 1, status ="YES",stu_id = 1)
study_obj2 = StudyRecord(day = 2, status ="NO",stu_id = 1)
study_obj3 = StudyRecord(day = 3, status ="YES",stu_id = 1)
study_obj4 = StudyRecord(day = 1, status ="YES",stu_id = 2)

Session.add_all([s1,s2,s3,s4,study_obj1,study_obj2,study_obj3,study_obj4])
'''

stu_obj = Session.query(Student).filter(Student.name == "vv").first()



Session.commit()