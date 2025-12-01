# Processing an API Response

# Now we’ll write a program to automatically issue an API call and process the results:

import requests

# Make an API call and check the response.
url = "https://api.github.com/search/repositories"  # 1
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}  # 2
r = requests.get(url, headers=headers)  # 3
print(f"Status code: {r.status_code}")  # 4

# Convert the response object to a dictionary.
response_dict = r.json()  # 5

# Process results.
print(response_dict.keys())

# We first import the requests module. Then we assign the URL of the API call to the url variable ❶. This is a long URL, so we break it into two lines. The first line is the main part of the URL, and the second line is the query string. We’ve included one more condition to the original query string: stars:>10000, which tells GitHub to only look for Python repositories that have more than 10,000 stars. This should allow GitHub to return a complete, consistent set of results.

# GitHub is currently on the third version of its API, so we define headers for the API call that ask explicitly to use this version of the API, and return the results in the JSON format ❷. Then we use requests to make the call to the API ❸. We call get() and pass it the URL and the header that we defined, and we assign the response object to the variable r.

# The response object has an attribute called status_code, which tells us whether the request was successful. (A status code of 200 indicates a successful response.) We print the value of status_code so we can make sure the call went through successfully ❹. We asked the API to return the information in JSON format, so we use the json() method to convert the information to a Python dictionary ❺. We assign the resulting dictionary to response_dict.

# Finally, we print the keys from response_dict and see the following output:
#    Status code: 200
#    dict_keys(['total_count', 'incomplete_results', 'items'])

# Because the status code is 200, we know that the request was successful. The response dictionary contains only three keys: 'total_count', 'incomplete_results', and 'items'. Let’s take a look inside the response dictionary.
