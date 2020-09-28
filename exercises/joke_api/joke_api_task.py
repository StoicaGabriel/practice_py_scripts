import requests
import pprint
import random
from typing import Optional

"""How joke_api endpoints work
A GET request at "https://official-joke-api.appspot.com/random_joke" or at
"https://official-joke-api.appspot.com/random_ten" will return one random joke,
respectively ten random jokes. `/random_joke` and `random_ten` are assigned to
this.

A GET request at "https://official-joke-api.appspot.com/jokes" + any joke tag
such as "/programming" and followed by a method (random or ten) will do the same
thing as the other two, but filtered by the joke's tag (or, better said `type`). 

So, generally the format is "https://official-joke-api.appspot.com" with the
options:
 - /random_joke
 - /random_ten
 - /jokes/{type}/random
 - /jokes/{type}/ten
where {type} is to be replaced by the desired joke type (e.g. "programming",
"general" or "knock-knock".
"""


class ResponseError(Exception):
    pass


def get_joke_types(tries: int) -> list:
    """Attempt to find all the possible joke types by getting 10 random jokes
    for `tries` number of times from the api and recording the newly encountered
    tags. The tries must be at least 1 and not greater than 10 (there is no point
    in adding types only present for very few number of times).
    """
    if tries < 1 or tries > 10:
        raise ValueError('number of tries must be between 1 and 10')
    if not isinstance(tries, int):
        raise TypeError('number of tries must be of type int')

    with open('joke_types.txt', 'r+') as f:
        joke_types = ''
        for line in f:
            joke_types += line
        joke_types_lst = joke_types.split()

        random_ten = requests.get(url='https://official-joke-api.appspot.com/random_ten')
        jokes = random_ten.json()

        for i in range(tries):
            for joke in jokes:
                if joke['type'] not in joke_types_lst:
                    f.write(joke['type'] + ' ')
                    joke_types_lst.append(joke['type'])

    return joke_types_lst


# Task 1:
def get_a_random_joke():
    """Request a random joke from the joke_api."""
    url = 'https://official-joke-api.appspot.com/random_joke'
    response = requests.get(url=url)
    # print_response(response.json())

    return response


# Task 1:
def get_ten_random_jokes():
    """Request ten random jokes from the joke_api."""
    url = 'https://official-joke-api.appspot.com/random_ten'
    response = requests.get(url=url)
    # print_response(response.json())

    return response


# Task 1:
def get_a_random_joke_by_type(joke_type: str):
    """Request a random joke of a certain category from the joke_api."""
    if not isinstance(joke_type, str):
        raise TypeError('joke_type must be a string')
    url = 'https://official-joke-api.appspot.com/jokes' + '/' + joke_type + '/random'
    response = requests.get(url=url)
    # print_response(response.json())

    return response


# Task 1:
def get_ten_random_jokes_by_type(joke_type: str):
    """Request ten random jokes of a certain category from the joke_api."""
    if not isinstance(joke_type, str):
        raise TypeError('joke_type must be a string')
    url = 'https://official-joke-api.appspot.com/jokes' + '/' + joke_type + '/ten'
    response = requests.get(url=url)
    # print_response(response.json())

    return response


def do_everything(joke_types: list):
    """Function which does everything task-related, except the better printing.
    """
    base_url = 'https://official-joke-api.appspot.com'
    endpoints = ['random_joke', 'random_ten', 'jokes']

    # Task 1:
    print('')
    for endpoint in endpoints:
        url = base_url + '/' + endpoint
        if endpoint == 'jokes':
            url += '/programming'
            url_one = url + '/random'
            url_ten = url + '/ten'

            response_one = requests.get(url=url_one)
            response_ten = requests.get(url=url_ten)

            print_response(response_one.json())
            print('\n')
            print_response(response_ten.json())
        else:
            response = requests.get(url=url)
            print_response(response.json())
        print('\n')

    # Task 3:
    chosen_type = random.randint(0, len(joke_types) - 1)

    url = base_url + '/jokes' + '/' + joke_types[chosen_type] + '/ten'
    response = requests.get(url=url)

    for joke in response.json():
        if joke['type'] != joke_types[chosen_type]:
            raise ResponseError('joke type received differs from the one requested')

    # Task 4 (matter of choice: print only even id jokes):
    url = base_url + '/' + endpoints[1]
    response = requests.get(url=url)

    for joke in response.json():
        if int(joke['id']) % 2 == 0:
            print_response(joke)


# Task 2:
def pretty_print_response(content):
    """Print the responses of get requests with pprint."""
    if isinstance(content, list):
        for item in content:
            pprint.pprint(item)
    elif isinstance(content, dict):
        pprint.pprint(content)
    else:
        raise TypeError('content must be either a dict or a list of dicts')


def print_response(content):
    """Print the content of a response to a joke_api request in a more human-
    readable form. It is advised to supply the response in response.json() form.
    """
    if isinstance(content, list):
        for item in content:
            # Note: knock-knock jokes are only 5.
            if item['setup'][-1] == '?' and item['type'] != 'knock-knock':
                print('Q: ' + item['setup'])
                print('A: ' + item['punchline'], '\n')
            else:
                print(item['setup'] + ' ' + item['punchline'], '\n')
    elif isinstance(content, dict):
        if content['setup'][-1] == '?':
            print('Q: ' + content['setup'])
            print('A: ' + content['punchline'], '\n')
        else:
            print(content['setup'] + ' ' + content['punchline'], '\n')
    else:
        raise TypeError('content must be either a dict or a list of dicts')


if __name__ == '__main__':
    all_joke_types = get_joke_types(tries=10)
    chosen_type = random.randint(0, len(all_joke_types) - 1)

    # Task 1 & 2:
    print('Getting a random joke.')
    res = get_a_random_joke()
    print_response(res.json())
    print('-' * 20)
    print('Getting ten random jokes.')
    res = get_ten_random_jokes()
    print_response(res.json())
    print('-' * 20)
    print(f'Getting a {all_joke_types[chosen_type]} random joke.')
    res = get_a_random_joke_by_type(joke_type=all_joke_types[chosen_type])
    print_response(res.json())
    print('-' * 20)
    print(f'Getting ten {all_joke_types[chosen_type]} random jokes.')
    res = get_ten_random_jokes_by_type(joke_type=all_joke_types[chosen_type])
    print_response(res.json())
    print('-' * 20)

    # Task 3:
    res = get_ten_random_jokes_by_type(joke_type=all_joke_types[chosen_type])
    for jk in res.json():
        if jk['type'] != all_joke_types[chosen_type]:
            raise ResponseError('joke type received differs from the one requested')

    # Task 4 (matter of choice: print only even id jokes):
    res = get_ten_random_jokes()
    for jk in res.json():
        if int(jk['id']) % 2 == 0:
            print('Joke\'s id: ', jk['id'])
            print_response(jk)
