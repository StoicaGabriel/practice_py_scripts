import re
from typing import Optional, List, Any


# Any function with no return actually returns None
def no_return_function():
    """This function does nothing and returns None.

    :return: None
    """
    pass


print(no_return_function())
print(no_return_function.__doc__)


def sort_key_func(value):
    return len(value)


lst = ['asdf', 'x', 'ytsda', 'yy', 'bb', 'TTT']
lst.sort(key=sort_key_func)
print(lst)

match = re.match('Hello', 'Hello world')
if match:
    print('Match')
    # With the .string attribute get the value of the match
    print(match.string)
else:
    print('Not a match')

match = re.match('Goodbye', 'Hello world')
if match is None:
    print('Not a match', '\n')


# Variable remembering
def bad_function(value, starter_list=[]):
    starter_list.append(value)
    return starter_list


# starter_list is initialised with the first call and is kept in memory.
print(bad_function('a'))
print(bad_function('b'))
print(bad_function('c'))
print(bad_function('d'), '\n')


class DontAppend:
    # Class used to discriminate values to append (replaces None)
    pass


# Better function declaration using None as a default value for starter_list.
def good_function(value=DontAppend, starter_list=None):
    # Note: `value=DontAppend` is pretty bad on the linter
    if starter_list is None:
        starter_list = list()
    if value is not DontAppend:
        starter_list.append(value)
    return starter_list


print(good_function('a'))
print(good_function('b'))
print(good_function('c'))
print(good_function('d'))
print(good_function(None))
lst_to_pass = ['a', 'b', 'c', 'd']
print(good_function(None, lst_to_pass))


# A take on None type hinting
def good_func_none(value: Any, starter_list: Optional[List] = None) -> List:
    if starter_list is None:
        starter_list = list()
    if value is not DontAppend:
        starter_list.append(value)
    return starter_list


print(good_func_none('a'))
