from operator import itemgetter

import requests

# Make an API call and check the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"  # 1
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()  # 2
submission_dicts = []  # 3
for submission_id in submission_ids[:5]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"  # 4
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    submission_dict = {  # 5
        "title": response_dict["title"],
        "hn_link": f"https://news.ycombinator.com/item?id={submission_id}",
        "comments": response_dict["descendants"],
    }
    submission_dicts.append(submission_dict)  # 6
    submission_dicts = sorted(
        submission_dicts, key=itemgetter("comments"), reverse=True
    )  # 7

for submission_dict in submission_dicts:  # 8
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

# First, we make an API call and print the status of the response ❶. This API call returns a list containing the IDs of up to 500 of the most popular articles on Hacker News at the time the call is issued. We then convert the response object to a Python list ❷, which we assign to submission_ids. We’ll use these IDs to build a set of dictionaries, each of which contains information about one of the current submissions.
# We set up an empty list called submission_dicts to store these dictionaries ❸. We then loop through the IDs of the top 30 submissions. We make a new API call for each submission by generating a URL that includes the current value of submission_id ❹. We print the status of each request along with its ID, so we can see whether it’s successful.
# Next, we create a dictionary for the submission currently being processed ❺. We store the title of the submission, a link to the discussion page for that item, and the number of comments the article has received so far. Then we append each submission_dict to the list submission_dicts ❻.
# Each submission on Hacker News is ranked according to an overall score based on a number of factors, including how many times it’s been voted on, how many comments it’s received, and how recent the submission is. We want to sort the list of dictionaries by the number of comments. To do this, we use a function called itemgetter() ❼, which comes from the operator module. We pass this function the key 'comments', and it pulls the value associated with that key from each dictionary in the list. The sorted() function then uses this value as its basis for sorting the list. We sort the list in reverse order, to place the most-commented stories first.
# Once the list is sorted, we loop through the list ❽ and print out three pieces of information about each of the top submissions: the title, a link to the discussion page, and the number of comments the submission currently has:
#  Status code: 200
# id: 31390506
# id: 31389893
# id: 31390742
# --snip--
# status: 200
# status: 200
# status: 200
# Title: Fly.io: The reclaimer of Heroku's magic
# Discussion link: https://news.ycombinator.com/item?id=3139050
# 6
# Comments: 134
# Title: The weird Hewlett Packard FreeDOS option
# Discussion link: https://news.ycombinator.com/item?id=3138989
# 3
# Comments: 64
# Title: Modern JavaScript Tutorial
# Discussion link: https://news.ycombinator.com/item?id=3139074
# 2
# Comments: 20
# --snip--

# You would use a similar process to access and analyze information with any API. With this data, you could make a visualization showing which submissions have inspired the most active recent discussions. This is also the basis for apps that provide a customized reading experience for sites like Hacker News. To learn more about what kind of information you can access through the Hacker News API, visit the documentation page at https://github.com/HackerN ews/API.

# Hacker News sometimes allows companies it supports to make special hiring posts, and comments are disabled on these posts. If you run this program while one of these posts is present, you’ll get a KeyError. If this causes an issue, you can wrap the code that builds submission_dict in a try-except block and skip over these posts.
