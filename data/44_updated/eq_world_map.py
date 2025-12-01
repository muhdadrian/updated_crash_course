# Customizing Marker Colors

# We can use Plotly’s color scales to customize each marker’s color, according to the severity of the corresponding earthquake. We’ll also use a different projection for the base map.

import json
from pathlib import Path

import plotly.express as px

# Read data as a string and convert to a Python object.
path = Path("eq_data/eq_data_30_day_m1.geojson")
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
fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    size=mags,
    title=title,
    color=mags,  # 1
    color_continuous_scale="Viridis",  # 2
    labels={"color": "Magnitude"},  # 3
    projection="natural earth",  # 4
)
fig.show()

# All the significant changes here occur in the px.scatter_geo() function call. The color argument tells Plotly what values it should use to determine where each marker falls on the color scale ❶. We use the mags list to determine the color for each point, just as we did with the size argument.

# The color_continuous_scale argument tells Plotly which color scale to use ❷. Viridis is a color scale that ranges from dark blue to bright yellow, and it works well for this dataset. By default, the color scale on the right of the map is labeled color; this is not representative of what the colors actually mean. The labels argument, shown in Chapter 15, takes a dictionary as a value ❸. We only need to set one custom label on this chart, making sure the color scale is labeled Magnitude instead of color.

# We add one more argument, to modify the base map over which the earthquakes are plotted. The projection argument accepts a number of common map projections ❹. Here we use the 'natural earth' projection, which rounds the ends of the map. Also, note the trailing comma after this last argument. When a function call has a long list of arguments spanning multiple lines like this, it’s common practice to add a trailing comma so you’re always ready to add another argument on the next line.

# When you run the program now, you’ll see a much nicer- looking map. In Figure 16-9, the color scale shows the severity of individual earthquakes; the most severe earthquakes stand out as light-yellow points, in contrast to many darker points. You can also tell which regions of the world have more significant earthquake activity.

# The chart shows: In 30 days’ worth of earthquakes, color and size are used to represent the magnitude of each earthquake.

# Other Color Scales:
# You can choose from a number of other color scales. To see the available color scales, enter the following two lines in a Python terminal session:
# >>> import plotly.express as px
# >>> px.colors.named_colorscales()
# ['aggrnyl', 'agsunset', 'blackbody', ..., 'mygbm']

# Feel free to try out these color scales in the earthquake map, or with any dataset where continuously varying colors can help show patterns in the data.
