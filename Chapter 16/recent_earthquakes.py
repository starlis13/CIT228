import json
import datetime

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = "data/last_day_earthquakes.json"
with open(filename, 'r', encoding="utf-8") as data_file:
    earthquake_data = json.load(data_file)

earthquake_dictionaries = earthquake_data["features"]

magnitudes = []
longitudes = []
latitudes = []
tooltips = []

for earthquake_dictionary in earthquake_dictionaries:
    magnitude = earthquake_dictionary["properties"]["mag"]
    longitude = earthquake_dictionary["geometry"]["coordinates"][0]
    latitude = earthquake_dictionary["geometry"]["coordinates"][1]
    tooltip = earthquake_dictionary["properties"]["title"]
    
    magnitudes.append(magnitude)
    longitudes.append(longitude)
    latitudes.append(latitude)
    tooltips.append(tooltip)

data = [{
    "type": "scattergeo",
    "lon": longitudes,
    "lat": latitudes,
    "text": tooltips,
    "marker": {
        "size": [10 * mag for mag in magnitudes],
        "color": magnitudes,
        "colorscale": "Viridis",
        "reversescale": True,
        "colorbar": {"title": "Magnitude"},
    },
}]

layout = Layout(title="Noteable Earthquakes\n(3/19/2021 - 3/20/2021)")

figure = {"data": data, "layout": layout}
offline.plot(figure, filename="recent_earthquakes.html")