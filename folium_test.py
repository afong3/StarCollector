import folium
from folium.plugins import BeautifyIcon

# Make an empty map
m = folium.Map(location=[15, 0], tiles="OpenStreetMap", zoom_start=2)

# square marker
icon_square = BeautifyIcon(
    icon_shape='rectangle-dot', 
    border_color='red', 
    border_width=10,
)
folium.Marker([50, -70], tooltip='square', icon=icon_square).add_to(m)



# circle marker
icon_circle = BeautifyIcon(
    icon_shape='circle-dot', 
    border_color='green', 
    border_width=10,
)
folium.Marker([-20, 25], tooltip='circle', icon=icon_circle).add_to(m)

# star marker
icon_star = BeautifyIcon(
    icon='star',
    inner_icon_style='color:blue;font-size:30px;',
    background_color='transparent',
    border_color='transparent',
)

folium.Marker([60, 125], tooltip='star', icon=icon_star).add_to(m)

m.save('markers_on_folium_map.html')