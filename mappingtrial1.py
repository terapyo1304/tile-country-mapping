import geopandas
import shapely
'''s = geopandas.GeoSeries(
    [
         shapely.geometry.Polygon([(0, 0), (2, 2), (0, 2)]),
         shapely.geometry.LineString([(0, 0), (2, 2)]),
         shapely.geometry.Point(1, 1),
         shapely.geometry.Point(0, 1),
     ],
     index=range(1, 5),
     
 )
s2 = geopandas.GeoSeries(
     [
         shapely.geometry.LineString([(1, 0), (1, 3),(0,2)]),
         shapely.geometry.LineString([(2, 0), (0, 2)]),
         shapely.geometry.Point(1, 1),
         shapely.geometry.Point(0, 1),
     ],
     index=range(1, 5),
 )
s.intersects(s2,align=True)
line = shapely.geometry.LineString([(-1, 1), (3, 1)])
print(s.intersects(line))'''

tile= geopandas.GeoSeries(
    [
        shapely.geometry.Polygon([0.904463466083483,19.202724681933127],
         [0.904820387748182,20.189322178518527],
         [-0.088473813037585,20.189421634272794],
         [-0.088438915806152,19.202945060483668],
          [0.904463466083483,19.202724681933127])
    ],
    
)
country=geopandas.GeoSeries(
    [
        shapely.geometr.Polygon([17.63317458105382,-0.2141676135894528],
        [18.48984703033579,4.065777633265725],
        [26.985182152381956,5.275344177099342],
        [29.697978241774862,4.49291869667158],
        [31.268544398791796,2.212520412166498],
        [30.840208174150813,-8.464377561082301],
        [29.34103138790737,-13.716607006604164],
        [22.202094310557644,-11.20736095286324],
        [11.922024919174035,-5.7017156348930484],
        [17.63317458105382,-0.2141676135894528],
        [17.63317458105382,-0.2141676135894528])
    ]

)
print(tile.intersects(country,align=True))
