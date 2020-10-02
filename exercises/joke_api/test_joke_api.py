import pytest
from exercises.joke_api import get_popular_joke_types
from exercises.joke_api import get_a_random_joke, get_ten_random_jokes
from exercises.joke_api import get_a_random_joke_by_type, get_ten_random_jokes_by_type


def test_get_popular_joke_types_basic():
    """Basic functionality test for the `get_joke_type` function. This test
    assumes that the joke_types.txt document has been recently updated. There is
    a slight chance that there are categories which appear very few times and
    have not been registered via the `get_popular_joke_types()` method, which
    will cause the test to fail."""
    joke_types = ''
    with open('joke_types.txt', 'r') as f:
        for line in f:
            joke_types += line
    # Note: there is always a blank at the end of the file, so no `.split(' ')`.
    expected = joke_types.split()
    joke_types_lst = get_popular_joke_types(update_file=False)
    # There are definitely jokes registered, so the list is expected to have at
    # least one element.
    assert joke_types_lst != []
    assert expected == joke_types_lst


def test_get_popular_joke_types_too_low_int():
    """joke_type lower than 1 should raise a ValueError."""
    with pytest.raises(ValueError):
        get_popular_joke_types(tries=0)


def test_get_popular_joke_types_too_high_int():
    """joke_type higher than 10 should also raise a ValueError."""
    with pytest.raises(ValueError):
        get_popular_joke_types(tries=11)


@pytest.mark.parametrize(
    'tries',
    [None, '', 3.4, tuple(), dict(), list(), set(), False],
)
def test_get_popular_joke_types_tries_invalid_data(tries):
    """Anything else than int passed to tries should raise a TypeError."""
    with pytest.raises(TypeError):
        get_popular_joke_types(tries=tries)


@pytest.mark.parametrize(
    'update_file',
    [None, '', 22, 3.4, tuple(), dict(), list(), set()],
)
def test_get_popular_joke_types_update_file_invalid_data(update_file):
    """Anything else than bool passed to update_file should raise a TypeError."""
    with pytest.raises(TypeError):
        get_popular_joke_types(update_file=update_file)


def test_get_a_random_joke_basic():
    """Basic functionality test for the `get_a_random_joke` function."""
    res = get_a_random_joke()
    assert res.status_code == 200
    assert isinstance(res.json(), dict)


def test_get_ten_random_jokes_basic():
    """Basic functionality test for the `get_ten_random_jokes` function."""
    res = get_ten_random_jokes()
    assert res.status_code == 200
    assert isinstance(res.json(), list)
    for item in res.json():
        assert isinstance(item, dict)


def test_get_a_random_joke_by_type_basic():
    """Basic functionality test for the `get_a_random_joke_by_type` function."""
    joke_type = 'general'
    res = get_a_random_joke_by_type(joke_type=joke_type)
    assert res.status_code == 200
    # For some reason, requesting a single joke through the /jokes endpoint
    # will return a list of a single dict element containing the joke.
    assert isinstance(res.json(), list)
    assert res.json()[0]['type'] == joke_type


def test_get_a_random_joke_by_type_empty_string():
    """Passing an empty string as joke_type should result in 404 status code."""
    joke_type = ''
    res = get_a_random_joke_by_type(joke_type=joke_type)
    assert res.status_code == 404


@pytest.mark.parametrize(
    'joke_type',
    [None, 22, 3.4, tuple(), dict(), list(), set(), False],
)
def test_get_a_random_joke_by_type_invalid_data(joke_type):
    """Passing anything else other than string as joke_type should raise a TypeError."""
    with pytest.raises(TypeError):
        res = get_a_random_joke_by_type(joke_type=joke_type)


def test_get_a_random_joke_by_type_nonexistent_type():
    """Passing a joke_type that does not exist results in empty list."""
    # Note: if the joke type does not exist in the api's data, an empty list is
    # returned instead of return code 404.
    joke_type = 'nonexistent_joke_type'
    res = get_a_random_joke_by_type(joke_type=joke_type)
    assert res.json() == []


def test_get_ten_random_jokes_by_type_basic():
    """Basic functionality test for the `get_ten_random_jokes_by_type` function."""
    joke_type = 'general'
    res = get_ten_random_jokes_by_type(joke_type=joke_type)
    assert res.status_code == 200
    assert isinstance(res.json(), list)
    for item in res.json():
        assert item['type'] == joke_type


def test_get_ten_random_jokes_by_type_empty_string():
    """Passing an empty string as joke_type should result in 404 status code."""
    joke_type = ''
    res = get_ten_random_jokes_by_type(joke_type=joke_type)
    assert res.status_code == 404


@pytest.mark.parametrize(
    'joke_type',
    [None, 22, 3.4, tuple(), dict(), list(), set(), False],
)
def test_get_ten_random_jokes_by_type_invalid_data(joke_type):
    """Passing anything else other than string as joke_type should raise a TypeError."""
    with pytest.raises(TypeError):
        res = get_ten_random_jokes_by_type(joke_type=joke_type)


def test_get_ten_random_jokes_by_type_nonexistent_type():
    """Passing a joke_type that does not exist results in empty list."""
    # Note: if the joke type does not exist in the api's data, an empty list is
    # returned instead of return code 404.
    joke_type = 'nonexistent_joke_type'
    res = get_ten_random_jokes_by_type(joke_type=joke_type)
    assert res.json() == []
