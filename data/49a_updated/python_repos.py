import requests

# Make an API call and check the response.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Convert the response object to a dictionary.
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

# Explore information about the repositories.
repo_dicts = response_dict["items"]
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository.
repo_dict = repo_dicts[0]

print("\nSelected information about first repository:")
print(f"Name: {repo_dict['name']}")  # 1
print(f"Owner: {repo_dict['owner']['login']}")  # 2
print(f"Stars: {repo_dict['stargazers_count']}")  # 3
print(f"Repository: {repo_dict['html_url']}")
print(f"Created: {repo_dict['created_at']}")  # 4
print(f"Updated: {repo_dict['updated_at']}")  # 5
print(f"Description: {repo_dict['description']}")

# Here, we print the values for a number of keys from the first repository’s dictionary. We start with the name of the project ❶. An entire dictionary represents the project’s owner, so we use the key owner to access the dictionary representing the owner, and then use the key login to get the owner’s login name ❷. Next, we print how many stars the project has earned ❸ and the URL for the project’s GitHub repository. We then show when it was created ❹ and when it was last updated ❺. Finally, we print the repository’s description.

# The output should look something like this:
#   Status code: 200
#   Total repositories: 248
#   Complete results: True
#   Repositories returned: 30
#   Selected information about first repository:
#   Name: public-apis
#   Owner: public-apis
#   Stars: 191493
#   Repository: https://github.com/public-apis/public-apis
#   Created: 2016-03-20T23:49:42Z
#   Updated: 2022-05-12T06:37:11Z
#   Description: A collective list of free APIs

# We can see that the most-starred Python project on GitHub as of this writing is public-apis. Its owner is an organization with the same name, and it has been starred by almost 200,000 GitHub users. We can see the URL for the project’s repository, its creation date of March 2016, and that it was updated recently. Additionally, the description tells us that public-apis contains a list of free APIs that programmers might be interested in.
