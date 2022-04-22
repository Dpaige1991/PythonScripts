import folium
m = folium.Map(location=[52.37613757431285, 4.927801674596649], zoom_start=12)

folium.Marker([52.376111375557294, 4.927876776449689],
              popup="<h1>My favorite spot</h1><img src = 'Pinpoint.jpg' width=400px><p>Best Spot</p>",
              tooltip='My Favorite Spot',
              icon=folium.Icon(icon='heart', icon_color='red', color='green')).add_to(m)

Cicon = folium.features.CustomIcon('Heart.png', icon_size=(35,35))
folium.Marker([52.37359636059762, 4.911647337958452],
              popup="<h1>My favorite club</h1><p>Best Spot</p>",
              tooltip='My Favorite Spot',
              icon=Cicon).add_to(m)

folium.Circle(
    location=(52.37478871986263, 4.9191236142479635),
    radius=800,
    popup='Love this area',
    color='blue',
    fill=True,
    fill_color='blue'
).add_to(m)

m.save('map.html')