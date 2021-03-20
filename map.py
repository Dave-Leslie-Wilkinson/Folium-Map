import folium
import pandas

data = pandas.read_csv("volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

html = """<h4>Volcano information:</h4>
Height: %s m
"""

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation <3000:
        return'orange'
    else:
        return'red'

map = folium.Map(locations=[39.133529018839056, -108.08811360985828], zoom_start=5, zoom_control=True, TileLayer="Mapbox Bright")

fg = folium.FeatureGroup(name="Volcano Map")

for lt, ln, el in zip(lat, lon, elev):
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color=color_producer(el))))

map.add_child(fg)
map.save("volcanomap.html")
