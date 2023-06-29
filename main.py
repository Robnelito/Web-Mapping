import folium


def my_color_function():
    return '#008000'


mapping = folium.Map(location=[-21.4610988, 47.097573], zoom_start=15.6)

folium.GeoJson(data=(open("geojson/eni.geojson", "r", encoding="utf-8-sig").read()), tooltip="ENI", name="ENI",
               style_function=lambda feature: {
                   'fillColor': '#007f0e',
                   'color': '#007f0e'
               }).add_to(mapping)
folium.GeoJson(data=(open("geojson/emit.geojson", "r", encoding="utf-8-sig").read()), tooltip="EMIT", name="EMIT",
               style_function=lambda feature: {
                   'fillColor': '#61A1FE',
                   'color': '#61A1FE'
               }).add_to(mapping)
folium.GeoJson(data=(open("geojson/ens.geojson", "r", encoding="utf-8-sig").read()), tooltip="ENS", name="ENS",
               style_function=lambda feature: {
                   'fillColor': '#DADAD9',
                   'color': '#DADAD9'
               }).add_to(mapping)
folium.GeoJson(data=(open("geojson/facmed.geojson", "r", encoding="utf-8-sig").read()), tooltip="Fac Médecine",
               name="Fac Médecine", style_function=lambda feature: {
        'fillColor': '#F339E0',
        'color': '#F339E0'
    }).add_to(mapping)
folium.GeoJson(data=(open("geojson/facscience.geojson", "r", encoding="utf-8-sig").read()), tooltip="Fac Science",
               name="Fac Science", style_function=lambda feature: {
        'fillColor': 'gray',
        'color': 'black'
    }).add_to(mapping)
folium.GeoJson(data=(open("geojson/eniversuf.geojson", "r", encoding="utf-8-sig").read()), tooltip="ENI - UF = 3.05",
               name="ENI vers UF", style_function=lambda feature: {
        'fillColor': 'orange',
        'color': 'orange'
    }).add_to(mapping)

folium.LayerControl().add_to(mapping)
mapping.save("index.html")
