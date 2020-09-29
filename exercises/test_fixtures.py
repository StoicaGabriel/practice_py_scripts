import pytest


@pytest.fixture()
def fruits_basket_dict() -> dict:
    basket_dict = {
        'fruits': 'apples',
        'quantity': 10,
        'weight': 2.5,
    }
    return basket_dict


@pytest.fixture()
def car_dict() -> dict:
    car_dict = {
        'color': 'red',
        'km': 1000,
        'fabrication-date': '22.10.2019',
    }
    return car_dict


@pytest.fixture()
def names_list() -> list:
    names_list = ['Andrew', 'John', 'Mike', 'Sally', 'Tyrone']
    return names_list


def test_fruits_basket(fruits_basket_dict):
    assert fruits_basket_dict['fruits'] == 'apples'


def test_car(car_dict):
    assert car_dict['km'] < 10_000


def test_names_lst(names_list):
    assert names_list[1] == 'John'


def test_names_lst_len(names_list):
    assert len(names_list) == 5
