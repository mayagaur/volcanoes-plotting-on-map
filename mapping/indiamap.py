import folium
import pandas
df1= pandas.read_csv("volcanoes.txt")
lat= list(df1["LAT"])
lon= list(df1["LON"])
elev= list(df1["ELEV"])
name1= list(df1["NAME"])
def clr(h):
    if h < 1000:
        return "green"
    elif 1000 < h < 2000:
        return "orange"
    else :
        return "red"

html = """<h4>Volcano information:</h4>
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

map= folium.Map(location=[38.58 , -99.99],zoom_start=5,tiles="Stamen Terrain")


fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open("world.json","r",encoding="utf-8-sig").read(),
style_function= lambda x: {"fillColor": "green" if x ["properties"]["POP2005"] < 1000000 
else "orange" if 1000000 < x["properties"]["POP2005"] <2000000 else "red "}))

fgv = folium.FeatureGroup(name="Volcanoes")
for lt,ln,el,nm in zip(lat,lon,elev,name1) :
    iframe = folium.IFrame(html=html %((nm, nm, el)), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=[lt,ln], popup=folium.Popup(iframe),color=clr(el),fill=True,
    fill_color= clr(el),fill_opacity=0.7,icon=folium.Icon(color=clr(el))))

map.add_child(fgp)
map.add_child(fgv)

map.add_child(folium.LayerControl())
map.save("India_map1.html")

