# Working with the Response Dictionary
#
# With the information from the API call represented as a dictionary, we can work with the data stored there. Let’s generate some output that summarizes the information. This is a good way to make sure we received the information we expected, and to start examining the information we’re interested in:

import requests

# Make an API call and check the response.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Convert the response object to a dictionary.
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")  # 1
print(f"Complete results: {not response_dict['incomplete_results']}")

# Explore information about the repositories.
repo_dicts = response_dict["items"]  # 2
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository.
repo_dict = repo_dicts[0]  # 3
print(f"\nKeys: {len(repo_dict)}")  # 4
for key in sorted(repo_dict.keys()):  # 5
    print(key)

# We start exploring the response dictionary by printing the value associated with 'total_count', which represents the total number of Python repositories returned by this API call ❶. We also use the value associated with 'incomplete_results', so we'll know if GitHub was able to fully process the query. Rather than printing this value directly, we print its opposite: a value of True will indicate that we received a complete set of results.
# The value associated with 'items' is a list containing a number of dictionaries, each of which contains data about an individual Python repository. We assign this list of dictionaries to repo_dicts ❷. We then print the length of repo_dicts to see how many repositories we have information for.
# To look closer at the information returned about each repository, we pull out the first item from repo_dicts and assign it to repo_dict ❸. We then print the number of keys in the dictionary to see how much information we have ❹. Finally, we print all the dictionary’s keys to see what kind of information is included ❺.

# The results give us a clearer picture of the actual data:

# Status code: 200
# Total repositories: 248 #1
# Complete results: True #2
# Repositories returned: 30

# Keys: 78 #3
# allow_forking
# archive_url

# archived
# --snip--
# url
# visiblity
# watchers
# watchers_count

# At the time of this writing, there are only 248 Python repositories with over 10,000 stars ❶. We can see that GitHub was able to fully process the API call ❷. In this response, GitHub returned information about the first 30 repositories that match the conditions of our query. If we want more repositories, we can request additional pages of data.

# GitHub’s API returns a lot of information about each repository: there are 78 keys in repo_dict ❸. When you look through these keys, you’ll get a sense of the kind of information you can extract about a project. (The only way to know what information is available through an API is to read the documentation or to examine the information through code, as we’re doing here.)

# Let’s pull out the values for some of the keys in repo_dict at the next folder:
