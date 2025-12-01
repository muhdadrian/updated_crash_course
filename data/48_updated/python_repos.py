# Using an API

# Most apps that use external data sources, such as apps that integrate with social media sites, rely on API calls.

# The requested data through API call will be returned in an easily processed format, such as JSON or CSV.

# We’ll base our visualization on information from GitHub (https://github.com), a site that allows programmers to collaborate on coding projects.

# We’ll use GitHub’s API to request information about Python projects on the site, and then generate an interactive visualization of the relative popularity of these projects using Plotly.

# We’ll write a program to automatically download information about the most-starred Python projects on GitHub, and then we’ll create an informative visualization of these projects.

# To see what an API call looks like, enter the following into your browser’s address bar and press ENTER:https://api.github.com/search/repositories?q=language:python+sort:stars

# This call returns the number of Python projects currently hosted on GitHub, as well as information about the most popular Python repositories. Let’s examine the call. The first part, https://api.github.com/, directs the request to the part of GitHub that responds to API calls. The next part, search/repositories, tells the API to conduct a search through all the repositories on GitHub.

# The question mark after repositories signals that we’re about to pass an argument. The q stands for query, and the equal sign (=) lets us begin specifying a query (q=). By using language:python, we indicate that we want information only on repositories that have Python as the primary language. The final part, +sort:stars, sorts the projects by the number of stars they’ve been given.

# The following snippet shows the first few lines of the response:
# {
# "total_count": 8961993,     #1
# "incomplete_results": true, #2
# "items": [ {                #3
#     "id": 54346799,
# "node_id": "MDEwOlJlcG9zaXRvcnk1NDM0Njc5OQ==",
#         "name": "public-apis",
#         "full_name": "public-apis/public-apis",
#         --snip--
# You can see from the response that this URL is not primarily intended to be entered by humans, because it’s in a format that’s meant to be processed by a program. GitHub found just under nine million Python projects as of this writing ❶. The value for "incomplete_results" is true, which tells us that GitHub didn’t fully process the query ❷. GitHub limits how long each query can run, in order to keep the API responsive for all users. In this case it found some of the most popular Python repositories, but it didn’t have time to find all of them; we’ll fix that in a moment. The "items" returned are displayed in the list that follows, which contains details about the most popular Python projects on GitHub ❸.


# Installing Requests:
# The Requests package allows a Python program to easily request information from a website and examine the response. Use pip to install Requests:
# python3 -m pip install requests

# go to 48a_updated
