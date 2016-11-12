import sys
import hug
import pkgutil
from djudge.db import *

@hug.get('/', output=hug.output_format.html)
def index_get():
    return pkgutil.get_data(__package__, 'templates/index.html').decode()


@hug.get('/submit', output=hug.output_format.html)
def submit_get():
    return pkgutil.get_data(__package__, 'templates/submit.html').decode()

@hug.post('/submit', output=hug.output_format.json)
def submit_post(problem: int, compiler: int, code: hug.types.text):
    print(problem, compiler, code)
    p= Problem(problem, compiler, code)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(p)
    session.commit()
    return{
    'problem': problem,
    'compiler': compiler,
    'code': code
    }

@hug.get('/contribute', output=hug.output_format.html)
def contribute():
    return pkgutil.get_data(__package__, 'templates/contribute.html').decode()


@hug.post('/contribute', output=hug.output_format.json)
def contribute(problem, compiler, code):
    print(problem, compiler, code)
    p= Problem(problem, compiler, code)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(p)
    session.commit()
    return{
    'problem': problem,
    'compiler': compiler,
    'code': code
    }


if __name__ == '__main__':
    print('Please run \'hug -m djudge.app\' instead.', file=sys.stderr)
