import arcpy
import re
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\Users\shrouk\Desktop\gis\data"
countries = r"C:\Users\shrouk\Desktop\gis\data\ne_10m_admin_0_countries.shp"
urban = r"C:\Users\shrouk\Desktop\gis\data\ne_10m_urban_areas.shp"
Output= r"C:\Users\shrouk\Desktop\gis\output\point9"

arcpy.MakeFeatureLayer_management(urban, 'urban_layer', """  "area_sqkm" > 50.0 """)

countries_cursors = arcpy.SearchCursor(countries, ['FID', 'SOVEREIGNT', 'REGION_UN'])
for country_row in countries_cursors:
    country_fid = country_row.getValue('FID')
    country_name = re.sub(r'[^a-zA-Z0-9]', '', country_row.getValue('SOVEREIGNT'))
    region = country_row.getValue('REGION_UN')

    if region == 'Africa':

        sql_expression = """ "FID" = {}   """.format(country_fid)

        arcpy.MakeFeatureLayer_management(countries, 'countries_layer', sql_expression)

        arcpy.SelectLayerByLocation_management('urban_layer', 'WITHIN', 'countries_layer')

        output_name = "UrbanAreas_in_{}_{}".format(country_name, country_fid)
        arcpy.FeatureClassToFeatureClass_conversion('urban_layer', Output, output_name)
