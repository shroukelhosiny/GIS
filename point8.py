import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\Users\shrouk\Desktop\gis\data"
countries = r"C:\Users\shrouk\Desktop\gis\data\ne_10m_admin_0_countries.shp"
populated_places = r"C:\Users\shrouk\Desktop\gis\data\ne_10m_populated_places.shp"
outpath =r"C:\Users\shrouk\Desktop\gis\output\point8"

arcpy.MakeFeatureLayer_management(populated_places, 'populated_places_layer')
SearchCursor = arcpy.SearchCursor(countries, ['FID', 'NAME','SUBREGION','REGION_WB'])
for i in SearchCursor:
    if ((i.getValue('SUBREGION') =='Western Asia' and i.getValue('REGION_WB') =='Middle East & North Africa') or
            (i.getValue('SUBREGION') =='Northern Africa' and i.getValue('REGION_WB') =='Middle East & North Africa')):

        name = str(i.getValue('NAME')).replace(" ", "_").replace(".", "")
        arcpy.MakeFeatureLayer_management(countries, 'countries_layer', """ "FID"={} """.format(i.getValue('FID')))
        arcpy.SelectLayerByLocation_management('populated_places_layer', 'WITHIN', 'countries_layer')
        arcpy.FeatureClassToFeatureClass_conversion('populated_places_layer',outpath,'cities_in_{}'.format(name))


