import sys
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


def attempt_stderr(error: str):
    """Force-print a sys.stderr to be captured by capsys."""
    print('There was an error while printing: {}'.format(error), file=sys.stderr)


def test_attempt_stderr(capsys):
    """Capture the sys.stderr which appears during test."""
    attempt_stderr('User-created Error')
    out, err = capsys.readouterr()

    assert out == ''
    assert 'User-created Error' in err
