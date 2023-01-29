import geopandas
import shapely
import matplotlib
import matplotlib.pyplot as plt
import plotly.express as px
import pandas
import sentinelsat as ss


tile= geopandas.GeoSeries(
    [
        shapely.geometry.Polygon([(0.904463466083483,19.202724681933127),
         (0.904820387748182,20.189322178518527),
         (-0.088473813037585,20.189421634272794),
         (-0.088438915806152,19.202945060483668),
         (0.904463466083483,19.202724681933127)])
    ],
    
)
country=geopandas.GeoSeries(
    [
        shapely.geometry.Polygon([(17.63317458105382,-0.2141676135894528),
        (18.48984703033579,4.065777633265725),
        (26.985182152381956,5.275344177099342),
        (29.697978241774862,4.49291869667158),
        (31.268544398791796,2.212520412166498),
        (30.840208174150813,-8.464377561082301),
        (29.34103138790737,-13.716607006604164),
        (22.202094310557644,-11.20736095286324),
        (11.922024919174035,-5.7017156348930484),
        (17.63317458105382,-0.2141676135894528),
        (17.63317458105382,-0.2141676135894528)])
    ]

)
#print(country.intersects(tile))
df=pandas.read_csv("COUNTRIES.csv")
#print(df)
#using geopandas to convert lat and long to points
df_geo=geopandas.GeoDataFrame(df,geometry=geopandas.points_from_xy(df.LATITUDE, df.LONGITUDE))
#points_from_xy indicates 2 dimensions
#print(df_geo)
'''world_data=geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
axis=world_data[world_data.continent=='Africa'].plot(color='blue', edgecolor='black' )
print(df_geo.plot(ax=axis, color='black'))
#guessing country names
f=px.choropleth(
    df,
    locationmode='country names',
    locations=df['COUNTRY'],
    scope='africa',
    color=df['COUNTRY']
)
f.show()'''
tilename=input("enter tile name")
df2=geopandas.read_file('/Users/indukatoch/Desktop/tile-country-mapping/Sentinel-2-Shapefile-Index/sentinel_2_index_centroid.shp')
df2_geo=geopandas.GeoDataFrame(df2,geometry=geopandas.points_from_xy(df2.POINT_X, df2.POINT_Y))

for i in df2_geo.index:
    if df2_geo['Name'][i]==tilename:
        print(df2_geo['geometry'][i]) 
        tile_point=df2_geo['geometry'][i]


for j in df.index:
    country_name=df['COUNTRY'][j]
    country_point=df['geometry'][j]
    
    if country_point.intersects(tile_point)!=False:
        print('tile lies in',country_name)
    else:
        continue

