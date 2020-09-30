import pytest


@pytest.fixture()
def fruits_basket_dict() -> dict:
    """Dummy fixture"""
    basket_dict = {
        'fruits': 'apples',
        'quantity': 10,
        'weight': 2.5,
    }
    return basket_dict


@pytest.fixture()
def car_dict() -> dict:
    """Dummy fixture"""
    car_dict = {
        'color': 'red',
        'km': 1000,
        'fabrication-date': '22.10.2019',
    }
    return car_dict


# Note: 'module' scope causes the fixture to initialise only once per module run.
@pytest.fixture(scope='module')
def names_list():
    """Dummy fixture"""
    names_list = ['Andrew', 'John', 'Mike', 'Sally', 'Tyrone']
    print('Yield, tests start.')
    yield names_list
    print('Tests ended')


def test_fruits_basket(fruits_basket_dict):
    """Dummy test"""
    assert fruits_basket_dict['fruits'] == 'apples'


def test_car(car_dict):
    """Dummy test"""
    assert car_dict['km'] < 10_000


def test_names_lst(names_list):
    """Dummy test"""
    assert names_list[1] == 'John'


# This test also uses the names_list fixture.
def test_names_lst_len(names_list):
    """Dummy test"""
    assert len(names_list) == 5
