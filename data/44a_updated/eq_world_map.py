# Adding Hover Text

# To finish this map, we’ll add some informative text that appears when you hover over the marker representing an earthquake. In addition to showing the longitude and latitude, which appear by default, we’ll show the magnitude and provide a description of the approximate location as well.

# To make this change, we need to pull a little more data from the file:

import json
from pathlib import Path

import plotly.express as px

# Read data as a string and convert to a Python object.
path = Path("eq_data/eq_data_30_day_m1.geojson")
contents = path.read_text()
all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data["features"]

mags, lons, lats, eq_titles = [], [], [], []  # 1
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    eq_title = eq_dict["properties"]["title"]  # 2
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)

title = "Global Earthquakes"
fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    size=mags,
    title=title,
    color=mags,  # 1
    color_continuous_scale="Viridis",
    labels={"color": "Magnitude"},
    projection="natural earth",
    hover_name=eq_titles,  # 3
)
fig.show()

# We first make a list called eq_titles to store the title of each earthquake ❶. The 'title' section of the data contains a descriptive name of the magnitude and location of each earthquake, in addition to its longitude and latitude. We pull this information and assign it to the variable eq_title ❷, and then append it to the list eq_titles.

# In the px.scatter_geo() call, we pass eq_titles to the hover_name argument ❸. Plotly will now add the information from the title of each earthquake to the hover text on each point. When you run this program, you should be able to hover over any marker, see a description of where that earthquake took place, and read its exact magnitude. An example of this information is shown in the chart.

# The chart shows: The hover text now includes a summary of each earthquake.

# This is impressive! In less than 30 lines of code, we’ve created a visually appealing and meaningful map of global earthquake activity that also illustrates the geological structure of the planet. Plotly offers a wide range of ways you can customize the appearance and behavior of your visualizations. Using Plotly’s many options, you can make charts and maps that show exactly what you want them to.
