import Ormforeignkey_many
from sqlalchemy.orm import sessionmaker, relationship, backref

Session_class = sessionmaker(bind=Ormforeignkey_many.engine)
session = Session_class()

addr1 = Ormforeignkey_many.Address(street="Rooseveltway", city ="Seattle", state= "Washington")
addr2 = Ormforeignkey_many.Address(street="Fifthavenue", city ="Newyork", state= "Newjesersy")
addr3 = Ormforeignkey_many.Address(street="Canonbay", city ="Portland", state= "Oregon")

session.add_all([addr1,addr2,addr3])

c1 = Ormforeignkey_many.Customer(name='valentina', billing_address = addr1, shipping_address = addr2)
c2 = Ormforeignkey_many.Customer(name='tony', billing_address = addr3, shipping_address = addr3)

session.add_all([c1,c2])

session.commit()
session.close()

print("hi")