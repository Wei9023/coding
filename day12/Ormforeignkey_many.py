from sqlalchemy import create_engine
from sqlalchemy import INTEGER,ForeignKey,String,Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine("mysql+pymysql://root:tonys-air@192.168.0.6/vvtestdb")

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(INTEGER, primary_key=True)
    name = Column(String(64))

    billing_address_id =Column(INTEGER, ForeignKey("address.id"))
    shipping_address_id = Column(INTEGER, ForeignKey("address.id"))

    billing_address = relationship("Address", foreign_keys=[billing_address_id])
    shipping_address = relationship("Address", foreign_keys=[billing_address_id])

class Address(Base):
    __tablename__ = 'address'
    id = Column(INTEGER, primary_key=True)
    street = Column(String(64))
    city = Column(String(64))
    state = Column(String(64))

#Base.metadata.create_all(engine)



