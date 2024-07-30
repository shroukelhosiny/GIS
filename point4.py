import arcpy
arcpy.env.overwriteOutput = True

arcpy.env.workspace = r"C:\Users\shrouk\Desktop\gis\data"
countries = r"C:\Users\shrouk\Desktop\gis\data\ne_10m_admin_0_countries.shp"
airports=r"C:\Users\shrouk\Desktop\gis\data\ne_10m_airports.shp"
output_4 = r"C:\Users\shrouk\Desktop\gis\output\point4"

arcpy.MakeFeatureLayer_management(countries, 'countries_layer')
airport_types = arcpy.SearchCursor(airports, ['type'])
for i in airport_types:
    if "military" in i.getValue('type').lower():
        arcpy.MakeFeatureLayer_management(airports, 'airports_layer', """ "type" = '{}' """.format(i.getValue('type')))
        arcpy.SelectLayerByLocation_management('countries_layer', 'INTERSECT', 'airports_layer')
        arcpy.FeatureClassToFeatureClass_conversion('countries_layer', output_4, 'Countries_airports_type_{}'.format(i.getValue('type')))
        for x in arcpy.SearchCursor('countries_layer', ['NAME']):
            print(x.getValue('NAME') + "  is have:  " + i.getValue('type'))