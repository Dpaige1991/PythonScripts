import phonenumbers
from MyPhone import number
from phonenumbers import geocoder
import folium

Key = "d8447bcffa984438aa3aa16a2676ba96"

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(Key)
query = str(location)
results = geocoder.geocode(query)
##print(results)

lat = results[0]['geometry']['lat']
lon = results[0]['geometry']['lng']
print(lat, lon)

map = folium.Map(location=[lat, lon], zoom_start=9)
folium.Marker([lat, lon], popup=location).add_to((map))
map.save("location.html")