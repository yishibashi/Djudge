from setuptools import setup

setup(
    name='djudge',
    version='0.1',
    packages=['djudge'],
    install_requires=[
        'hug',
        'SQLAlchemy',
        'PyMySQL'
    ],
    package_data={
        'djudge': ['templates/*']
    },
    author='yishibashi',
    author_email='yishibashi101@gmail.com',
    description='C++ Online Judge in D.......',
    license='MIT',
    keywords='programming compile',
    url='https://github.com/yishibashi/DJudge',
)
