import folium
import pandas
data = pandas.read_csv("Volcanoes.txt") 
lat = list(data["LAT"])
lon = list(data["LON"])
popname = list(data["NAME"])
ele = list(data["ELEV"])

def colorproducer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 2000:
        return "blue"
    elif 2000 <= elevation < 3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location = [24.81917,121.02026], zoom_start = 10, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name = "My Map Volcanoes")
fgp = folium.FeatureGroup(name = "My Map Population")

for lt, ln, name, el in zip(lat, lon, popname, ele):
    fg.add_child(folium.CircleMarker(location = [lt, ln],radius=10, popup = f"{name} "+str(el)+"m", 
    fill_color = colorproducer(el), color = 'white'))

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding = 'utf-8-sig').read(),
style_function = lambda x: {'fillColor':'Blue' if x['properties']['POP2005'] < 10000000 else 'orange' 
if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fg)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("MapVolcanoes.html")