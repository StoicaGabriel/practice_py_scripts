import pytest
from exercises.joke_api import get_joke_types
from exercises.joke_api import get_a_random_joke, get_ten_random_jokes
from exercises.joke_api import get_a_random_joke_by_type, get_ten_random_jokes_by_type


def test_get_joke_type_basic():
    joke_types = ''
    with open('joke_types.txt', 'r') as f:
        for line in f:
            joke_types += line
    # Note: there is always a blank at the end of the file so no `.split(' ')`.
    expected = joke_types.split()
    joke_types_lst = get_joke_types(10)
    # There are definitely jokes registered so the list is expected to have at
    # least one element.
    assert joke_types_lst != []
    assert expected == joke_types_lst


def test_get_joke_type_too_low_int():
    with pytest.raises(ValueError):
        get_joke_types(tries=0)


def test_get_joke_type_too_high_int():
    with pytest.raises(ValueError):
        get_joke_types(tries=11)


def test_get_joke_type_not_int():
    invalid_params = [None, '', 2.2, [], {}, ()]
    for param in invalid_params:
        with pytest.raises(TypeError):
            get_joke_types(param)


def test_get_a_random_joke_basic():
    res = get_a_random_joke()
    assert res.status_code == 200
    assert isinstance(res.json(), dict)


def test_get_ten_random_jokes_basic():
    res = get_ten_random_jokes()
    assert res.status_code == 200
    assert isinstance(res.json(), list)
    for item in res.json():
        assert isinstance(item, dict)


def test_get_a_random_joke_by_type_basic():
    joke_type = 'general'
    res = get_a_random_joke_by_type(joke_type=joke_type)
    assert res.status_code == 200
    assert isinstance(res.json(), dict)
    assert res.json()['type'] == joke_type


def test_get_a_random_joke_by_type_empty_string():
    joke_type = ''
    res = get_a_random_joke_by_type(joke_type=joke_type)
    assert res.status_code == 404


def test_get_a_random_joke_by_type_invalid_data():
    invalid_joke_types = [None, 22, 3.4, tuple(), dict(), list(), set()]
    for joke_type in invalid_joke_types:
        with pytest.raises(TypeError):
            res = get_a_random_joke_by_type(joke_type=joke_type)


def test_get_ten_random_jokes_by_type_basic():
    joke_type = 'general'
    res = get_ten_random_jokes_by_type(joke_type=joke_type)
    assert res.status_code == 200
    assert isinstance(res.json(), list)
    for item in res.json():
        assert item['type'] == joke_type


def test_get_ten_random_jokes_by_type_empty_string():
    joke_type = ''
    res = get_ten_random_jokes_by_type(joke_type=joke_type)
    assert res.status_code == 404
