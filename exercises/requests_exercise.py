import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import HTTPError, Timeout
from requests.auth import AuthBase
from getpass import getpass


response = requests.get(url='https://api.github.com')
# [200] response code = everything OK
print(response)
print(response.status_code)

# response is falsy so `if response` is a valid condition
if response.status_code == 200:
    print('Success!\n')
elif response.status_code == 404:
    print('Not found.\n')

# Here the response can be checked with `raise_for_status`.
for url in ['https://api.github.com', 'https://api.github.com//invalid']:
    try:
        response = requests.get(url)

        # If the response was successful, no error is raised.
        response.raise_for_status()
    except HTTPError as error:
        print(f'HTTP error occured: {error}.\n')
    except Exception as exception:
        print(f'Other exception occured: {exception}.\n')
    else:
        print('Success\n')

# Actual response content.
response = requests.get('https://api.github.com')
# in bytes
response.encoding = 'utf-8'  # This is optional in most cases.
print(response.content, '\n')
# in string format (utf-8)
print(response.text)
# in json
print(response.json(), '\n')
# The .json() method returns a dictionary => access by key is possible.

# Access the headers of the content.
print(response.headers, '\n')
print(f"Content type: {response.headers['Content-Type']}")

# Query string searching.
# Search github's repository for the requests module.
response = requests.get(
    url='https://api.github.com/search/repositories',
    # `q` comes from query string
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'},
)

json_response = response.json()
repository = json_response['items'][0]
print(f"Repository name: {repository['name']}.")
print(f"Repository description: {repository['description']}.")
print(f"Text matches: {repository['text_matches']}\n")

response = requests.post('https://httpbin.org/post', json={'key': 'value'})
json_response = response.json()
print(json_response['data'])
print(json_response['headers']['Content-Type'], '\n')

# Visualise the request made through the response.
print(response.request.url)
print(response.request.body)

# Borked -> inf loop if username or password invalid
# response = requests.get('https://api.github.com/user', auth=('username', getpass('0000')))
# print(response.status_code)


class TokenAuth(AuthBase):
    """Implements a custom authentication scheme."""

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        """Attach an API token to a custom auth header."""
        r.headers['X-TokenAuth'] = f'{self.token}'  # Python 3.6+
        return r


print(requests.get('https://httpbin.org/get', auth=TokenAuth('12345abcde-token')))

# GET request without SSL verification (not secure)
print(requests.get('https://api.github.com', verify=False))

# Requests with timeouts
# Passing a tuple to timeout specifies that the first value is time reserved to
# connect and the second to receive.
print(requests.get('https://api.github.com', timeout=1))
print(requests.get('https://api.github.com', timeout=3.3))

# Timeout exceptions
try:
    response = requests.get('https://api.github.com', timeout=1)
except Timeout:
    print('The request was timed out')
else:
    print('The request did not time out')

# Using sessions
with requests.Session() as session:
    session.auth = ('username', getpass())

    response = session.get('https://api.github.com/user')

print(response.headers)
print(response.json())

github_adapter = HTTPAdapter(max_retries=3)
session = requests.Session()

session.mount('https://api.github.com', github_adapter)

try:
    print(session.get('https://api.github.com'))
except ConnectionError as ce:
    print(ce)
