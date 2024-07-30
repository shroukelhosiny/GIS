import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\Users\shrouk\Desktop\gis\data"

urban = r"C:\Users\shrouk\Desktop\gis\data\ne_10m_urban_areas.shp"
countries = r"C:\Users\shrouk\Desktop\gis\data\ne_10m_admin_0_countries.shp"
output_5 = r"C:\Users\shrouk\Desktop\gis\output\point5"

arcpy.MakeFeatureLayer_management( urban, 'urban_layer' )

continent_list = ['Asia', 'Europe', 'North America']
for i in continent_list:
    arcpy.MakeFeatureLayer_management( countries, 'countries_layer', """ "CONTINENT" = '{}' """.format( i ) )
    airports_cursors = arcpy.SearchCursor( 'countries_layer', ["CONTINENT", "SOVEREIGNT"] )
    for airport in airports_cursors:
        print(airport.getValue("CONTINENT"),airport.getValue("SOVEREIGNT"))
    arcpy.SelectLayerByLocation_management( 'urban_layer', 'WITHIN', 'countries_layer' )
    arcpy.FeatureClassToFeatureClass_conversion( 'urban_layer', output_5, 'urban_areas_in_{}'.format( i ) )
