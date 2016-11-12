from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///db.sqlite3', echo=True)
metadata = MetaData()
metadata.bind = engine

Base = declarative_base() #cls=ReprBase)


class Problem(Base):
    __tablename__ = 'problem'

    id = Column(Integer, primary_key=True)
    contest_name = Column(String(32), nullable=False)
    problem_type = Column(String(32), nullable=False)
    problem_body = Column(Text, nullable=False) # Text? String?

    def __init__(self, contest_name, problem_type, problem_body):
        self.contest_name = contest_name
        self.problem_type = problem_type
        self.problem_body = problem_body

class Submit(Base):
    __tablename__ = 'submit'

    id = Column(Integer, primary_key=True)
    problem = Column(String(32), nullable=False)
    compiler = Column(String(32), nullable=False)
    code = Column(Text, nullable=False)

    def __init__(self, problem, compiler, code):
        self.problem = problem
        self.compiler = compiler
        self.code = code

if __name__ == '__main__':
    Base.metadata.create_all(engine)
