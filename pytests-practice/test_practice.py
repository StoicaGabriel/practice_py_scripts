import pytest
from collections import namedtuple


Task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)


# Note to self: pytest run messages are more descriptive in command line than in
# the editor.
def test_pass():
    assert (1, 2, 3) == (1, 2, 3)


def test_fail():
    # Using `with pytest.raises` in desired fail-scenarios makes the test pass.
    with pytest.raises(AssertionError):
        assert (1, 2, 3) == (2, 3, 4)


def test_defaults():
    """Passing no parameters should invoke defaults."""
    t1 = Task()
    t2 = Task(None, None, False, None)
    assert t1 == t2


def test_member_access():
    """Check .field functionality of namedtuple."""
    t = Task('buy milk', 'brian')
    assert t.summary == 'buy milk'
    assert t.owner == 'brian'
    assert (t.done, t.id) == (False, None)


def test_asdict():
    """_asdict() should return a dictionary."""
    t = Task('do something', 'okken', True, 21)
    t_dct = t._asdict()
    expected = {
        'summary': 'do something',
        'owner': 'okken',
        'done': True,
        'id': 21,
    }
    assert t_dct == expected


def test_replace():
    """replace() should change passed fields."""
    t = Task('finish book', 'brian', False)
    t_updated = t._replace(id=10, done=True)
    expected = Task('finish book', 'brian', True, 10)
    assert expected == t_updated
