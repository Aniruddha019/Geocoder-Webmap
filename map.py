import folium
import pandas
df = pandas.read_json("out.json")
res_list = []
rdf = pandas.DataFrame([])
for i in range(0,len(df)):
    r1 = df.restaurants[i]
    d1 = r1['restaurant']['location']
    d1["name"] = r1['restaurant']['name']
    res_list.append(d1)
rdf = pandas.DataFrame(res_list)
rdf = rdf.drop(columns = ["city","zipcode","city_id","country_id","locality_verbose","locality"])
bangalore_location = [12.9716, 77.5946]

m = folium.Map(location=bangalore_location, zoom_start=12)
fg = folium.FeatureGroup(name="My Map")
for i in range(0,len(rdf)):
    fg.add_child(folium.Marker(location=[rdf.iloc[i].latitude,rdf.iloc[i].longitude],popup=rdf.iloc[i]['name'],icon=folium.Icon(color='green')))

fg.add_child(folium.Marker(location=[12.936784, 77.610424],popup="Perfios",icon=folium.Icon(color='blue')))
m.add_child(fg)
m.save("Map.html")
