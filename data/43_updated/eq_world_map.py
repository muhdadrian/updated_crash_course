# Building a World Map

# Using the information we’ve pulled so far, we can build a simple world map. Although it won’t look presentable yet, we want to make sure the information is displayed correctly before focusing on style and presentation issues. Here’s the initial map:

import json
from pathlib import Path

import plotly.express as px

# Read data as a string and convert to a Python object.
path = Path("eq_data/eq_data_1_day_m1.geojson")
contents = path.read_text()
all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data["features"]

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

title = "Global Earthquakes"
fig = px.scatter_geo(lat=lats, lon=lons, title=title)  # 1
fig.show()

# We import plotly.express with the alias px, just as we did in Chapter 15. The scatter_geo() function ❶ allows you to overlay a scatterplot of geographic data on a map. In the simplest use of this chart type, you only need to provide a list of latitudes and a list of longitudes. We pass the list lats to the lat argument, and lons to the lon argument.

# When you run this file, you should see a map that looks like the one in the chart. This again shows the power of the Plotly Express library; in just three lines of code, we have a map of global earthquake activity.

# The chart shows a simple map showing where all the earthquakes in the last 24 hours occurred.

# Now that we know the information in our dataset is being plotted correctly, we can make a few changes to make the map more meaningful and easier to read at 43a_updated
