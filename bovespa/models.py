from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String


engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()


class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)

    name = Column(String(50))
    cnpj = Column(String(50))
    sector = Column(String(12))

    def __repr__(self):
    	return "<User(name='%s', fullname='%s', password='%s')>" % (
                             self.name, self.fullname, self.password)



