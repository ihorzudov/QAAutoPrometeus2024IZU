import pytest
from modules.common.database import Database

@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()


@pytest.mark.database

def test_check_all_users():
    db= Database()
    users = db.get_all_users()
    print(users)

@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    user = db.get_user_adress_by_name("Sergii")

    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"


@pytest.mark.database
def test_product_qnt_update():
    db=Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_id(1)
    assert water_qnt[0][0] == 25

@pytest.mark.database
def test_product_insert():
    db= Database()
    db.insert_product(4, "cakes", "sweet", 30)
    water_qnt = db.select_product_qnt_id(4)
    assert  water_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, "testovi", "dani", 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_id(99)
    assert len(qnt) == 0

@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Zamovlenia", orders)
    assert len(orders) == 1

    # Check structure of data
    assert orders[0][0] == 1
    assert orders[0][1] == "Sergii"
    assert orders[0][2] == "cakes"
    assert orders[0][3] == "sweet"
    assert type(orders[0][1]) == str
    print(type(orders[0][4]))

    print(orders)

@pytest.mark.database
def test_product_insert1():
    db= Database()
    db.insert_product(True, "cakes", "sweet", 30)
    water_qnt = db.select_product_qnt_id(4)
    assert  water_qnt[0][0] == 30
    assert (type(water_qnt[0][0])) == int

