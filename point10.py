#Imports and Urls
import arcpy
import re
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\Users\shrouk\Desktop\gis\data"
countries = arcpy.GetParameterAsText(0)
urban = arcpy.GetParameterAsText(1)
Output= arcpy.GetParameterAsText(2)
reg = arcpy.GetParameterAsText(3)
number =arcpy.GetParameterAsText(4)

expression = """ "area_sqkm" > {} """.format(float(number))
arcpy.MakeFeatureLayer_management(urban, 'urban_layer', expression)

countries_cursors = arcpy.SearchCursor(countries, ['FID', 'SOVEREIGNT', 'REGION_UN'])
for country_row in countries_cursors:
    country_fid = country_row.getValue('FID')
    country_name = re.sub(r'[^a-zA-Z0-9]', '', country_row.getValue('SOVEREIGNT'))
    region = country_row.getValue('REGION_UN')

    if region == str(reg):

        sql_expression = """ "FID" = {}   """.format(country_fid)

        arcpy.MakeFeatureLayer_management(countries, 'countries_layer', sql_expression)

        arcpy.SelectLayerByLocation_management('urban_layer', 'WITHIN', 'countries_layer')

        output_name = "UrbanAreas_in_{}_{}".format(country_name, country_fid)
        arcpy.FeatureClassToFeatureClass_conversion('urban_layer', Output, output_name)
        arcpy.AddMessage("Created shapefile for urban areas in {}".format(country_name) )
