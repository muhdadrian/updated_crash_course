# Adding Clickable Links
# Because Plotly allows you to use HTML on text elements, we can easily add links to a chart. Let’s use the x-axis labels as a way to let the viewer visit any project’s home page on GitHub. We need to pull the URLs from the data and use them when generating the x-axis labels:

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
repo_links, stars, hover_texts = [], [], []  # 1
# repo_names, stars, hover_texts = [], [], []
# repo_names, stars = [], []
for repo_dict in repo_dicts:
    # Turn repo names into active links.
    repo_name = repo_dict["name"]
    repo_url = repo_dict["html_url"]  # 2
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"  # 3
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
# fig = px.bar(x=repo_names, y=stars, title=title, labels=labels, hover_name=hover_texts)
# fig = px.bar(x=repo_names, y=stars, title=title, labels=labels)
# fig.update_layout(
#     title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20
# )
fig.show()

# We update the name of the list we’re creating from repo_names to repo_links to more accurately communicate the kind of information we’re putting together for the chart ❶. We then pull the URL for the project from repo_dict and assign it to the temporary variable repo_url ❷. Next, we generate a link to the project ❸. We use the HTML anchor tag, which has the form <a href='URL'>link text</a>, to generate the link. We then append this link to repo_links.
# When we call px.bar(), we use repo_links for the x-values in the chart. The result looks the same as before, but now the viewer can click any of the project names at the bottom of the chart to visit that project’s home page on GitHub. Now we have an interactive, informative visualization of data retrieved through an API!
