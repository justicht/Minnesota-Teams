from urllib.request import urlopen
import json

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/justicht/Minnesota-Teams/main/MinnesotaCountyTeamCount.csv",
                   dtype={"FIPS": str})

import plotly.express as px





fig = px.choropleth(df, geojson=counties, locations='FIPS', color='Range',
                           color_discrete_map={
                                "30+": "purple",
                                "20-29": "orange",
                                "6-10": "yellow",
                                "4-5": "green",
                                "2-3": "cyan",
                                "1": "blue"},
                           range_color=(0, 30),
                           scope="usa",
                           labels={'unemp':'unemployment rate'},
                           category_orders={"Range": ["30+", "20-29", "6-10", "4-5","2-3","1"]
                              }
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


df["Total"] = df["Total"].astype(str)

fig.add_scattergeo(
  geojson=counties,
  locations = df['GEO_ID'],
  text = df['County']+"\n"+df['Total'],
  featureidkey="properties.GEO_ID",
  mode = 'text') 

fig.show()
