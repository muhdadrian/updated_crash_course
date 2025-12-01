# The Hacker News API

# To explore how to use API calls on other sites, let’s take a quick look at Hacker News (https://news.ycombinator.com). On Hacker News, people share articles about programming and technology and engage in lively discussions about those articles. The Hacker News API provides access to data about all submissions and comments on the site, and you can use the API without having to register for a key.
# The following call returns information about the current top article as of this writing:
#   https://hacker-news.firebaseio.com/v0/item/31353677.json
# When you enter this URL in a browser, you’ll see that the text on the page is enclosed by braces, meaning it’s a dictionary. But the response is difficult to examine without some better formatting. Let’s run this URL through the json.dumps() method, like we did in the earthquake project in Chapter 16, so we can explore the kind of information that’s returned about an article:

import json

import requests

# Make an API call, and store the response.
url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")
# Explore the structure of the data.
response_dict = r.json()
response_string = json.dumps(response_dict, indent=4)
print(response_string)  # 1

# Everything in this program should look familiar, because we’ve used it all in the previous two chapters. The main difference here is that we can print the formatted response string ❶ instead of writing it to a file, because the output is not particularly long.

# The output is a dictionary of information about the article with the ID 31353677:
# Status code: 200
# {
#     "by": "sohkamyung",
#     "descendants": 307, #1
#     "id": 31353677,
#     "kids": [ #2
#         31354987,
#         31354235,
#         31354040,
#         31358602,
#         31354201,
#         31354991,
#         31354315,
#         31353775,
#         31353925,
#         31354169,
#         31354273,
#         31354437,
#         31356902,
#         31358694,
#         31363418,
#         31353862,
#         31357186,
#         31356379,
#         31356826,
#         31355085,
#         31369435,
#         31357936,
#         31354142,
#         31354213,
#         31356311,
#         31357865,
#         31353929,
#         31364954,
#         31354621,
#         31356002,
#         31356407,
#         31355491,
#         31359235,
#         31356053,
#         31354347,
#         31355326,
#         31354703,
#         31353802
#     ],
#     "score": 786,
#     "time": 1652361401,
#     "title": "Astronomers reveal first image of the black hole at the heart of our galaxy", #3
#     "type": "story",
#     "url": "https://public.nrao.edu/news /astronomers-reveal-first-image-of-the-black-hole-at-the-heart-of-our-galaxy/"
# } #4

# The dictionary contains a number of keys we can work with. The key "descendants" tells us the number of comments the article has received ❶. The key "kids" provides the IDs of all comments made directly in response to this submission ❷. Each of these comments might have comments of their own as well, so the number of descendants a submission has is usually greater than its number of kids. We can see the title of the article being discussed ❸ and a URL for the article being discussed as well ❹.
# The following URL returns a simple list of all the IDs of the current top articles on Hacker News:
#   https://hacker-news.firebaseio.com/v0/topstories.json
# We can use this call to find out which articles are on the home page right now, and then generate a series of API calls similar to the one we just examined. With this approach, we can print a summary of all the articles on the front page of Hacker News at the moment. Go to the next updated folder.
