from pytest import fixture
from src.db import Db


@fixture(scope='session')
def db1_name():
    return '../dbs/test_db_1.db'


@fixture(scope='session')
def db2_name():
    return '../dbs/test_db_1.db'


@fixture(scope='session')
def db3_name():
    return '../dbs/test_db_3.db'


@fixture(scope='session')
def db4_name():
    return '../dbs/test_db_3.db'


@fixture(scope='function')
def db1(db1_name):
    return Db(name=db1_name)
