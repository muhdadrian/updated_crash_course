# Mapping Global Datasets: GeoJSON Format

# In this section, you’ll download a dataset representing all the earthquakes that have occurred in the world during the previous month. Then you’ll make a map showing the location of these earthquakes and how significant each one was. Because the data is stored in the GeoJSON format, we’ll work with it using the json module. Using Plotly’s scatter_geo() plot, you’ll create visualizations that clearly show the global distribution of earthquakes.

# Downloading Earthquake Data

# Make a folder called eq_data inside the folder where you’re saving this chapter’s programs. Copy the file eq_1_day_m1.geojson into this new folder. Earthquakes are categorized by their magnitude on the Richter scale. This file includes data for all earthquakes with a magnitude M1 or greater that took place in the last 24 hours (at the time of this writing). This data comes from one of the United States Geological Survey’s earthquake data feeds, at https://earthq uake.usgs.gov/earthquakes/feed.

# Examining GeoJSON Data

# When you open eq_1_day_m1.geojson, you’ll see that it’s very dense and hard to read.

# This file is formatted more for machines than humans. But we can see that the file contains some dictionaries, as well as information that we’re interested in, such as earthquake magnitudes and locations.

# The json module provides a variety of tools for exploring and working with JSON data. Some of these tools will help us reformat the file so we can look at the raw data more easily before we work with it programmatically.

# Let’s start by loading the data and displaying it in a format that’s easier to read. This is a long data file, so instead of printing it, we’ll rewrite the data to a new file. Then we can open that file and scroll back and forth through the data more easily:

import json
from pathlib import Path

# Read data as a string and convert to a Python object.
path = Path("eq_data/eq_data_1_day_m1.geojson")
contents = path.read_text()
all_eq_data = json.loads(contents)  # 1
# Create a more readable version of the data file.
path = Path("eq_data/readable_eq_data.geojson")  # 2
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)  # 3

# We read the data file as a string, and use json.loads() to convert the string representation of the file to a Python object ❶. This is the same approach we used in Chapter 10. In this case, the entire dataset is converted to a single dictionary, which we assign to all_eq_data. We then define a new path where we can write this same data in a more readable format ❷. The json.dumps() function that you saw in Chapter 10 can take an optional indent argument ❸, which tells it how much to indent nested elements in the data structure.
# When you look in your eq_data directory and open the file readable_eq_data.json, here’s the first part of what you’ll see:

# readable_eq_data.json

# {
#     "type": "FeatureCollection",
# 1     "metadata": {
#         "generated": 1649052296000,
#         "url": "https://earthquake.usgs.gov/earthquakes/.../
# 1.0_day.geojson",
#         "title": "USGS Magnitude 1.0+ Earthquakes, Past Day",
#         "status": 200,
#         "api": "1.10.3",
#         "count": 160
#     },
# 2     "features": [
# --snip--

#  The first part of the file includes a section with the key "metadata"❶. This tells us when the data file was generated and where we can find the data online. It also gives us a human-readable title and the number of earthquakes included in this file. In this 24-hour period, 160 earthquakes were recorded.
# This GeoJSON file has a structure that’s helpful for location-based data. The information is stored in a list associated with the key "features" ❷. Because this file contains earthquake data, the data is in list form where every item in the list corresponds to a single earthquake. This structure might look confusing, but it’s quite powerful. It allows geologists to store as much information as they need to in a dictionary about each earthquake, and then stuff all those dictionaries into one big list.


# Let’s look at a dictionary representing a single earthquake:
# readable_eq_data.json
# --snip--
#         {
#             "type": "Feature",
# 1             "properties": {
#                 "mag": 1.6,
#                 --snip--
# 2                "title": "M 1.6 - 27 km NNW of Susitna, Alaska"
#
# },
# 3             "geometry": {
#                 "type": "Point",
#                 "coordinates": [
# 4                -150.7585,
# 5                    61.7591,
#                     56.3
# ] },
#             "id": "ak0224bju1jx"
#         },

#  The key "properties" contains a lot of information about each earthquake ❶. We’re mainly interested in the magnitude of each earthquake, associated with the key "mag". We’re also interested in the "title" of each event, which provides a nice summary of its magnitude and location ❷.
# The key "geometry" helps us understand where the earthquake occurred ❸. We’ll need this information to map each event. We can find the longitude ❹ and the latitude ❺ for each earthquake in a list associated with the key "coordinates".
# This file contains way more nesting than we’d use in the code we write, so if it looks confusing, don’t worry: Python will handle most of the complexity. We’ll only be working
# with one or two nesting levels at a time. We’ll start by pulling out a dictionary for each earthquake that was recorded in the 24-hour time period.

# Many geospatial frameworks list the longitude first and then the latitude, because this corresponds to the (x, y) convention we use in mathematical representations. The GeoJSON format follows the (longitude, latitude) convention. If you use a different framework, it’s important to learn what convention that framework follows.
