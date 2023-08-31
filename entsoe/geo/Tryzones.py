from utils import load_zones
import plotly.express as px
import pandas as pd

zones = ['DK_1','DK_2']
start = pd.Timestamp('2023-12-01')

geo_df = load_zones(zones, start)
geo_df[2] = range(1,len(geo_df)+1)

fig = px.choropleth(geo_df,
                   geojson=geo_df.geometry,
                   locations=geo_df.index,
                   color=2,
                   projection="mercator",
                   color_continuous_scale='rainbow')
fig.update_geos(fitbounds="locations", visible=False)
fig.show()
