# Summarizing the Top Repositories

# When we make a visualization for this data, we’ll want to include more than one repository. Let’s write a loop to print selected information about each repository the API call returns so we can include them all in the visualization:

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
# repo_dict = repo_dicts[0]

print("\nSelected information about each repository:")  # 1
for repo_dict in repo_dicts:  # 2
    # print("\nSelected information about first repository:")
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    # print(f"Created: {repo_dict['created_at']}")
    # print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")

# We first print an introductory message ❶. Then we loop through all the dictionaries in repo_dicts ❷. Inside the loop, we print the name of each project, its owner, how many stars it has, its URL on GitHub, and the project’s description:

#   Status code: 200
#   Total repositories: 248
#   Complete results: True
#   Repositories returned: 30
#   Selected information about each repository:
#   Name: public-apis
#   Owner: public-apis
#   Stars: 191494
#   Repository: https://github.com/public-apis/public-apis
#   Description: A collective list of free APIs
#   Name: system-design-primer
#   Owner: donnemartin
#   Stars: 179952
#   Repository: https://github.com/donnemartin/system-design-primer
#    Description: Learn how to design large-scale systems. Prep for the system design interview.  Includes Anki flashcards.
#    --snip--
#    Name: PayloadsAllTheThings
#    Owner: swisskyrepo
#    Stars: 37227
#    Repository: https://github.com/swisskyrepo/PayloadsAllTheThings
#    Description: A list of useful payloads and bypass for Web Application Security and Pentest/CTF

# Some interesting projects appear in these results, and it might be worth looking at a few. But don’t spend too much time here, because we’re about to create a visualization that will make the results much easier to read.
