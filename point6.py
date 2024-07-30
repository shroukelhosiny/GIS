import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\Users\shrouk\Desktop\gis\data"
countries = r"C:\Users\shrouk\Desktop\gis\data\ne_10m_admin_0_countries.shp"
populated_places =r"C:\Users\shrouk\Desktop\gis\data\ne_10m_populated_places.shp"
disputed_areas =r"C:\Users\shrouk\Desktop\gis\data\ne_10m_admin_0_disputed_areas.shp"
outpath =r"C:\Users\shrouk\Desktop\gis\output\point6"

disputed_list = ['1. High income: OECD', '2. High income: nonOECD', '3. Upper middle income']
arcpy.MakeFeatureLayer_management(countries, "countries_layer")
for i in disputed_list:
    arcpy.MakeFeatureLayer_management( disputed_areas, 'disputed_layer',
                                       """ "INCOME_GRP" = '{}' AND "TYPE" = 'Disputed' """.format(i))
    arcpy.SelectLayerByLocation_management( 'countries_layer', 'WITHIN', 'disputed_layer' )
    arcpy.FeatureClassToFeatureClass_conversion( 'countries_layer', outpath, "disputed_in_{}".format( i ) )

    # Print names in disputed_layer
    print(".......................................................")
    print("name of disputed countries with",i)
    with arcpy.da.SearchCursor('disputed_layer', ['NAME'] ) as cursor:
        for row in cursor:
            print(row[0])