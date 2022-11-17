import folium
map = folium.Map(location = [24.81917,121.02026], zoom_start = 20, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name = "My Map")


for coordinates in [[24.81917,121.02026],[24.81930,121.02026]]:
    fg.add_child(folium.Marker(location = coordinates, popup = "My home", icon = folium.Icon(color = 'blue')))

map.add_child(fg)
map.save("Maphome.html")