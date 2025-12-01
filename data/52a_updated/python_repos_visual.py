# Styling the Chart

# Plotly supports a number of ways to style and customize the plots, once you know the information in the plot is correct. We’ll make some changes in the initial px.bar() call and then make some further adjustments to the fig object after it’s been created.

# We’ll start styling the chart by adding a title and labels for each axis:

import plotly.express as px
import requests

# Make an API call and check the response.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process overall results.
response_dict = r.json()
print(f"Complete results: {not response_dict['incomplete_results']}")

# Process repository information.
repo_dicts = response_dict["items"]
repo_names, stars = [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict["name"])
    stars.append(repo_dict["stargazers_count"])

# Make visualization.
# fig = px.bar(x=repo_names, y=stars)
title = "Most-Starred Python Projects on GitHub"
labels = {"x": "Repository", "y": "Stars"}
fig = px.bar(x=repo_names, y=stars, title=title, labels=labels)
fig.update_layout(
    title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20
)  # 1
fig.show()

# We first add a title and labels for each axis, as we did in Chapters 15 and 16. We then use the fig.update_layout() method to modify specific elements of the chart ❶. Plotly uses a convention where aspects of a chart element are connected by underscores. As you become familiar with Plotly’s documentation, you’ll start to see consistent patterns in how different elements of a chart are named and modified. Here we set the title font size to 28 and the font size for each axis title to 20.

# A title has been added to the main chart, and to each axis as well.
