import pytest
from src.db import Db


def test_1(db1_name, db2_name):
    db1 = Db(name=db1_name)
    db2 = Db(name=db2_name)
    assert id(db1.connection) == id(db2.connection)
    assert id(db1.cursor) == id(db2.cursor)


def test_2(db1_name, db3_name):
    db1 = Db(name=db1_name)
    db3 = Db(name=db3_name)
    assert db3._shared_data.get(db3_name, None) is not None
    del db1
    assert db3._shared_data.get(db1_name, None) is None
