import folium
import pandas
data = pandas.read_csv("worldcities.csv")
data_visited = pandas.read_csv("visited.txt")
visits = list(data_visited["LOCATION"])
visit_admin = list(data_visited["ADMIN"])
latitude = list(data["lat"])
longitude = list(data["lng"])
cityname = list(data["city"])
admin = list(data["admin_name"])
country = list(data["country"])
population = list(data["population"])


def colorproducer(population):
    if population > 20000000:
        return "red"
    elif 15000000 < population <= 20000000:
        return "orange"
    elif 10000000 < population <= 15000000:
        return "yellow"
    elif 5000000 < population <= 10000000:
        return "green"
    elif 2500000 < population <= 5000000:
        return "blue"
    elif 1000000 < population <= 200000:
        return "pink"

def radiusproducer(population):
    if population > 20000000:
        return 50
    elif 15000000 < population <= 20000000:
        return 30
    elif 10000000 < population <= 15000000:
        return 20
    elif 5000000 < population <= 10000000:
        return 15
    else:
        return 10


map = folium.Map(location = [37.7749,-122.4194], zoom_start = 10, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name = "My Map")
fgp = folium.FeatureGroup(name = "My Map Population")
fgv = folium.FeatureGroup(name = "My visited")

for lt, ln, name, pop in zip(latitude, longitude, cityname, population):
    if pop > 200000:
        fg.add_child(folium.CircleMarker(location = [lt, ln],radius=radiusproducer(pop), popup = f"{name} "+str(pop), 
        fill_color = colorproducer(pop), color = 'white'))


for v, v_ad in zip(visits, visit_admin):
    for lt, ln, name, ad, ctry in zip(latitude, longitude, cityname, admin, country):
        if (v == name) and (v_ad == ctry or v_ad == ad):
            fgv.add_child(folium.Marker(location = [lt, ln], popup = v, icon = folium.Icon(color = 'blue')))
            break

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding = 'utf-8-sig').read(),
style_function = lambda x: {'fillColor':'Blue' if x['properties']['POP2005'] < 10000000 else 'orange' 
if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fg)
map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl())

map.save("Citypopulation.html")