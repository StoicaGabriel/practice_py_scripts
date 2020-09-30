import pytest


def greeting(name: str):
    """Print a greeting message, given the person's name."""
    print('Hi, {}'.format(name))


def test_greeting(capsys: pytest.fixture):
    """Test out the function by capturing its output with capsys."""
    greeting('Person')
    out, err = capsys.readouterr()
    assert out == 'Hi, Person\n'
    assert err == ''

    # Any previous outputs are captured, no matter how many print
    # calls there are.
    greeting('John')
    greeting('Mark')
    out, err = capsys.readouterr()
    assert out == 'Hi, John\nHi, Mark\n'
    assert err == ''
