from setuptools import setup, find_packages

setup(
    name='djudge',
    version='0.1',
    packages=['djudge'],
    entry_points={
        'console_scripts': [
            'djudge = djudge.http_server:djudge',
        ]
    },

    author='yishibashi',
    author_email='yishibashi101@gmail.com',
    description='C++ Online Judge in D.......',
    license='MIT',
    keywords='programming compile',
    url='https://github.com/yishibashi/DJudge',
)
