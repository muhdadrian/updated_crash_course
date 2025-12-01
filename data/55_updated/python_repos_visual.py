# Adding Custom Tooltips

# In Plotly, you can hover the cursor over an individual bar to show the information the bar represents. This is commonly called a tooltip, and in this case, it currently shows the number of stars a project has. Let’s create a custom tooltip to show each project’s description as well as the project’s owner.

# We need to pull some additional data to generate the tooltips:

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
repo_names, stars, hover_texts = [], [], []  # 1
# repo_names, stars = [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict["name"])
    stars.append(repo_dict["stargazers_count"])

    # Build hover texts.
    owner = repo_dict["owner"]["login"]  # 2
    description = repo_dict["description"]
    hover_text = f"{owner}<br />{description}"  # 3
    hover_texts.append(hover_text)

# Make visualization.
# fig = px.bar(x=repo_names, y=stars)
title = "Most-Starred Python Projects on GitHub"
labels = {"x": "Repository", "y": "Stars"}
fig = px.bar(
    x=repo_names, y=stars, title=title, labels=labels, hover_name=hover_texts
)  # 4
# fig = px.bar(x=repo_names, y=stars, title=title, labels=labels)
fig.update_layout(
    title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20
)
fig.show()

# We first define a new empty list, hover_texts, to hold the text we want to display for each project ❶. In the loop where we process the data, we pull the owner and the description for each project ❷. Plotly allows you to use HTML code within text elements, so we generate a string for the label with a line break (<br />) between the project owner’s username and the description ❸. We then append this label to the list hover_texts.

# In the px.bar() call, we add the hover_name argument and pass it hover_texts ❹. This is the same approach we used to customize the label for each dot in the map of global earthquake activity. As Plotly creates each bar, it will pull labels from this list and only display them when the viewer hovers over a bar. The figure shows one of these custom tooltips.

# Hovering over a bar shows the project’s owner and description.
