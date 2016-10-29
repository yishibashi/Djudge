import sys
import hug
import pkgutil


@hug.get('/', output=hug.output_format.html)
def index_get():
    return pkgutil.get_data(__package__, 'templates/index.html').decode()


@hug.post('/', output=hug.output_format.json)
def index_post(problem: int, compiler: int, code: hug.types.text):
    return {
        'problem': problem,
        'compiler': compiler,
        'code': code
    }

if __name__ == '__main__':
    print('Please run \'hug -m djudge.app\' instead.', file=sys.stderr)
