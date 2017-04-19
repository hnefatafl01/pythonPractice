import pandas
import folium

df = pandas.read_csv("Volcanoes-USA.txt")
map = folium.Map(location=[df['LAT'].mean(),df['LON'].mean()],zoom_start=5, tiles="Stamen Terrain")

def color(elevation):
    minimum = int(min(df['ELEV']))
    step = int((max(df['ELEV']) - minimum) / 3)

    if elevation in range(minimum, minimum + step):
        col='green'
    elif elevation in range(minimum + step, minimum + step * 2):
        col='orange'
    else:
        col='red'
    return col

for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
    map.add_child(folium.Marker(location = [lat,lon], popup = name, icon = folium.Icon(color = color(elev), icon_color = 'green')))

map.save(outfile = 'volcanoes.html')
