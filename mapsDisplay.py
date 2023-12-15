from urllib.request import urlopen
import json

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/justicht/Minnesota-Teams/main/MinnesotaCountyTeamCount.csv",
                   dtype={"FIPS": str})

import plotly.express as px
import plotly.graph_objects as go




fig = px.choropleth(df, geojson=counties, locations='FIPS', color='Range',
                           color_discrete_map={
                                "30+": "#9900ff",
                                "20-29": "#ff9900",
                                "6-10": "#ffff00",
                                "4-5": "#00ff00",
                                "2-3": "#46c6a8",
                                "1": "#4a86e8"},
                           range_color=(0, 30),
                           scope="usa",
                           labels={'unemp':'unemployment rate'},
                           category_orders={"Range": ["30+", "20-29", "6-10", "4-5","2-3","1"]
                              }
                          )
fig.update_geos(fitbounds="locations")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


df["Total"] = df["Total"].astype(str)



lats = [46.78156,44.977063,45.561937]

lons = [-92.097938,-93.228313,-94.156937]

fig.add_scattergeo(
        lon = lons,
        lat = lats,
        
        mode = 'markers',
        marker_color = "red",
        marker_size = 16
        )


##fig.add_scattergeo(
##  geojson=counties,
##  locations = df['GEO_ID'],
##  text = df['Total'],
##  featureidkey="properties.GEO_ID",
##  mode = 'text') 

fig.show()
