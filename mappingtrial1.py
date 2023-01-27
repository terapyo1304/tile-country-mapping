import geopandas
import shapely
s = geopandas.GeoSeries(
    [
         shapely.geometry.Polygon([(0, 0), (2, 2), (0, 2)]),
         shapely.geometry.LineString([(0, 0), (2, 2)]),
         shapely.geometry.Point(1, 1),
         shapely.geometry.Point(0, 1),
     ],
     
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