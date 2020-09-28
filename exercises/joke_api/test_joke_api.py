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
    assert expected == joke_types_lst


def test_get_joke_type_too_low_int():
    with pytest.raises(ValueError):
        get_joke_types(0)


def test_get_joke_type_too_high_int():
    with pytest.raises(ValueError):
        get_joke_types(11)


def test_get_joke_type_not_int():
    invalid_params = [None, '', 2.2, [], {}, ()]
    for param in invalid_params:
        with pytest.raises(TypeError):
            get_joke_types(param)


def test_get_a_random_joke_basic():
    res = get_a_random_joke()
    assert res.status_code == 200
    assert isinstance(res.json(), dict)
