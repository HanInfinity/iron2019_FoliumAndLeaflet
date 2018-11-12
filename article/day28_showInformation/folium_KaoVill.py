import folium
import pandas as pd

newList = []
def switchLatLng(geos):
    for geo in geos:
        if isinstance(geo[0],list):
            switchLatLng(geo)
        else:
            newList.append([geo[1], geo[0]])
    return newList

myMap = folium.Map([22.73444963475145, 120.28458595275877], zoom_start=14)
kaoVill = folium.FeatureGroup()
i = 1
for feature in pd.read_json('../../dist/mapdata/KaoVillageRange.json')["features"]:
    villpopup = '這裡是<h3>'+feature['properties']['TV_ALL']+'</h3>總面積為'+feature['properties']['AREA']+'平方公尺'
    coors = [switchLatLng(feature['geometry']['coordinates'])]
    villRange = folium.Polygon(coors, 
                               popup = villpopup,
                               fill = True).add_to(kaoVill)
    i = i + 1
    print(i)
kaoVill.add_to(myMap)
myMap.fit_bounds(kaoVill.get_bounds())
myMap.save('Folium_KaoVillpopup.html')