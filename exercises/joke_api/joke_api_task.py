import requests
import random
import pprint

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
A `.json()` call on the response variable will return either a dict item or a
list of dict items, depending of the endpoint. `/jokes/...` will always return
a list type, no matter how many jokes are requested. `/random_joke` endpoint
will always return a dict object containing one joke.
"""

# Global vars
base_url = 'https://official-joke-api.appspot.com'
joke_types = []


class ResponseError(Exception):
    # Custom exception for bad response. Currently not affecting any tests.
    pass


def get_popular_joke_types(tries: int, update_file: bool = False) -> list:
    """Attempt to find all the possible joke types by getting 10 random jokes
    for `tries` number of times from the api and recording the newly encountered
    tags. The tries must be at least 1 and not greater than 10 (10 tries are
    enough to obtain the most popular tags).
    If `only_read` is True, then it updates the `joke_type_lst` global var with
    what it currently finds in the file.
    """
    global joke_types

    if tries < 1 or tries > 10:
        raise ValueError('number of tries must be between 1 and 10')
    if not isinstance(tries, int):
        raise TypeError('number of tries must be of type int')
    if not isinstance(update_file, bool):
        raise TypeError('`only_read` parameter can be either `True` or `False`')

    with open('joke_types.txt', 'r+') as f:
        joke_types = ''
        for line in f:
            joke_types += line
        # Naming is bad, but making another list via `.copy()` is not efficient.
        current_joke_types_lst = joke_types.split()
        if not update_file:
            # Just change the global with what was in the file and exit.
            joke_types = [joke for joke in current_joke_types_lst]
            # Will actually "optionally" return the list in case it's needed
            # outside of module (e.g. tests).
            return joke_types
        # Otherwise continue with actually updating the file AND changing the global.

        for i in range(tries):
            random_ten = requests.get(url=f'{base_url}/random_ten')
            jokes = random_ten.json()
            for joke in jokes:
                if joke['type'] not in current_joke_types_lst:
                    f.write(joke['type'] + ' ')
                    current_joke_types_lst.append(joke['type'])

    joke_types = [joke for joke in current_joke_types_lst]
    return joke_types


# Task 1:
def get_a_random_joke() -> requests.models.Response:
    """Request a random joke from the joke_api."""
    url = f'{base_url}/random_joke'
    response = requests.get(url=url)

    return response


# Task 1:
def get_ten_random_jokes() -> requests.models.Response:
    """Request ten random jokes from the joke_api."""
    url = f'{base_url}/random_ten'
    response = requests.get(url=url)

    return response


# Task 1:
def get_a_random_joke_by_type(joke_type: str) -> requests.models.Response:
    """Request a random joke of a certain category from the joke_api."""
    if not isinstance(joke_type, str):
        raise TypeError('joke_type must be a string')
    url = f'{base_url}/jokes/{joke_type}/random'
    response = requests.get(url=url)

    return response


# Task 1:
def get_ten_random_jokes_by_type(joke_type: str) -> requests.models.Response:
    """Request ten random jokes of a certain category from the joke_api."""
    if not isinstance(joke_type, str):
        raise TypeError('joke_type must be a string')
    url = f'{base_url}/jokes/{joke_type}/ten'
    response = requests.get(url=url)

    return response


def do_everything(all_joke_types: list):
    """Function which does everything task-related, except the better printing.
    """
    endpoints = ['random_joke', 'random_ten', 'jokes']

    # Task 1:
    print('')
    for endpoint in endpoints:
        url = f'{base_url}/{endpoint}'
        if endpoint == 'jokes':
            url += '/programming'
            url_one = f'{url}/random'
            url_ten = f'{url}/ten'

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
    chosen_joke_type = random.randint(0, len(all_joke_types) - 1)

    url = f'{base_url}/jokes/{all_joke_types[chosen_joke_type]}/ten'
    response = requests.get(url=url)

    for joke in response.json():
        if joke['type'] != all_joke_types[chosen_joke_type]:
            raise ResponseError('joke type received differs from the one requested')

    # Task 4 (matter of choice: print only even id jokes):
    url = f'{base_url}/{endpoints[1]}'
    response = requests.get(url=url)

    for joke in response.json():
        if int(joke['id']) % 2 == 0:
            print_response(joke)


# Task 2:
# This is the standard pretty_print function, but with some parameter checking.
def pretty_print_response(content):
    """Print the responses of get requests with pprint."""
    if isinstance(content, list):
        for item in content:
            pprint.pprint(item)
    elif isinstance(content, dict):
        pprint.pprint(content)
    else:
        raise TypeError('content must be either a dict or a list of dicts')


# This is the customised printing function.
def print_response(content):
    """Print the content of a response to a joke_api request in a more human-
    readable form. It is advised to supply the response in response.json() form.
    """
    if isinstance(content, list):
        for item in content:
            # Note: knock-knock jokes are only 5.
            if item['setup'][-1] == '?' and item['type'] != 'knock-knock':
                print(f'Q: {item["setup"]}')
                print(f'A: {item["punchline"]}\n')
            else:
                print(f'{item["setup"]} {item["punchline"]} \n')
    elif isinstance(content, dict) and content['type'] != 'knock-knock':
        if content['setup'][-1] == '?':
            print(f'Q: {content["setup"]}')
            print(f'A: {content["punchline"]}\n')
        else:
            print(f'{content["setup"]} {content["punchline"]}\n')
    else:
        raise TypeError('content must be either a dict or a list of dicts')


if __name__ == '__main__':
    # Standard setup in case the file is empty or it's nonexistent.
    # Only use update_file=True when actually needed. It takes a while to update
    # the file.
    get_popular_joke_types(tries=1, update_file=False)
    chosen_type = random.randint(0, len(joke_types) - 1)

    # Task 1 & 2:
    print('Getting a random joke.')
    res = get_a_random_joke()
    print_response(res.json())
    print('-' * 20)
    print('Getting ten random jokes.')
    res = get_ten_random_jokes()
    print_response(res.json())
    print('-' * 20)
    print(f'Getting a {joke_types[chosen_type]} random joke.')
    res = get_a_random_joke_by_type(joke_type=joke_types[chosen_type])
    print_response(res.json())
    print('-' * 20)
    print(f'Getting ten {joke_types[chosen_type]} random jokes.')
    res = get_ten_random_jokes_by_type(joke_type=joke_types[chosen_type])
    print_response(res.json())
    print('-' * 20)

    # Task 3:
    res = get_ten_random_jokes_by_type(joke_type=joke_types[chosen_type])
    for jk in res.json():
        if jk['type'] != joke_types[chosen_type]:
            raise ResponseError('joke type received differs from the one requested')

    # Task 4 (matter of choice: print only even id jokes):
    res = get_ten_random_jokes()
    for jk in res.json():
        if int(jk['id']) % 2 == 0:
            print(f'Joke\'s id: {jk["id"]}')
            print_response(jk)
