# models.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    founding_year = Column(Integer)
    freebies = relationship('Freebie', backref='company')
    devs = relationship('Dev', secondary='dev_freebies', back_populates='companies')

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    freebies = relationship('Freebie', back_populates='dev')
    companies = relationship('Company', secondary='dev_freebies', back_populates='devs')

class DevFreebie(Base):
    __tablename__ = 'dev_freebies'

    id = Column(Integer, primary_key=True)
    dev_id = Column(Integer, ForeignKey('devs.id'))
    freebie_id = Column(Integer, ForeignKey('freebies.id'))

class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer, primary_key=True)
    dev_id = Column(Integer, ForeignKey('devs.id'))
    company_id = Column(Integer, ForeignKey('companies.id'))
    item_name = Column(String)
    value = Column(Integer)
    dev = relationship('Dev', back_populates='freebies')
    company = relationship('Company', back_populates='freebies')

    def print_details(self):
        return f"{self.dev.name} owns a {self.item_name} from {self.company.name}"

