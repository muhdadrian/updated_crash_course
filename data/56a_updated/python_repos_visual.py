# Customizing Marker Colors
# Once a chart has been created, almost any aspect of the chart can be customized through an update method. We’ve used the update_layout() method previously. Another method,update_traces(), can be used to customize the data that’s represented on a chart.
# Let’s change the bars to a darker blue, with some transparency:

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
repo_links, stars, hover_texts = [], [], []
# repo_names, stars, hover_texts = [], [], []
# repo_names, stars = [], []
for repo_dict in repo_dicts:
    # Turn repo names into active links.
    repo_name = repo_dict["name"]
    repo_url = repo_dict["html_url"]
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    # repo_names.append(repo_dict["name"])
    stars.append(repo_dict["stargazers_count"])

    # Build hover texts.
    owner = repo_dict["owner"]["login"]
    description = repo_dict["description"]
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# Make visualization.
# fig = px.bar(x=repo_names, y=stars)
title = "Most-Starred Python Projects on GitHub"
labels = {"x": "Repository", "y": "Stars"}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts)
fig.update_layout(
    title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20
)
fig.update_traces(marker_color="SteelBlue", marker_opacity=0.6)
fig.show()

# In Plotly, a trace refers to a collection of data on a chart. The update_traces() method can take a number of different arguments; any argument that starts with marker_ affects the markers on the chart. Here we set each marker’s color to 'SteelBlue'; any named CSS color will work here. We also set the opacity of each marker to 0.6. An opacity of 1.0 will be entirely opaque, and an opacity of 0 will be entirely invisible.


# More About Plotly and the GitHub API
# Plotly’s documentation is extensive and well organized; however, it can be hard to know where to start reading. A good place to start is with the article “Plotly Express in Python,” at https://plotly.com/python/plotly-express. This is an overview of all the plots you can make with Plotly Express, and you can find links to longer articles about each individual chart type.
# If you want to understand how to customize Plotly charts better, the article “Styling Plotly Express Figures in Python” will expand on what you’ve seen in Chapters 15–17. You can find this article at https://plotly.com/python/styling-plotly-ex press.
# For more about the GitHub API, refer to its documentation at https://docs.github.com/en/rest. Here you’ll learn how to pull a wide variety of information from GitHub. To expand on what you saw in this project, look for the Search section of the reference in the sidebar. If you have a GitHub account, you can work with your own data as well as the publicly available data from other users’ repositories.
