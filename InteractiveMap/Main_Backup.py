import folium
m = folium.Map(location=[29.598905207229713, -95.6271957200079], zoom_start=12)

folium.Marker([29.598905207229713, -95.6271957200079],
              popup="<h1>My favorite place to eat</h1><img scr = 'Pinpoint.jpg' width=400px><p>Best Pizza Spot</p>",
              tooltip='My Favorite Food Spot',
              icon=folium.Icon(icon='heart', icon_color='red', color='green')).add_to(m)

Cicon = folium.features.CustomIcon('Heart.png', icon_size=(35,35))
folium.Marker([29.58703600651286, -95.62729880743488],
              popup="<h1>My favorite movie theater to visit</h1><p>Best Movie Spot</p>",
              tooltip="My Favortie Movie Spot",
              icon=Cicon).add_to(m)

folium.Circle(
    location=(29.615311218229433, -95.64336011270625),
    radius=800,
    popup='Love Sugarland',
    color='blue',
    fill=True,
    fill_color='blue'
).add_to(m)

m.save('map.html')