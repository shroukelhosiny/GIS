import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\Users\shrouk\Desktop\gis\data"
countries = r"C:\Users\shrouk\Desktop\gis\data\ne_10m_admin_0_countries.shp"
populated_places = r"C:\Users\shrouk\Desktop\gis\data\ne_10m_populated_places.shp"
disputed_areas = r"C:\Users\shrouk\Desktop\gis\data\ne_10m_admin_0_disputed_areas.shp"
outpath = r"C:\Users\shrouk\Desktop\gis\output\poin2"

data_list = arcpy.ListFeatureClasses()
print(data_list)

print('\n')
city_features = []
area_features = []
# Search cursor for cities and disputed areas in Palestine
with arcpy.da.SearchCursor(populated_places, ['NAME', 'ADM0NAME']) as cities_cursor:
    for city_row in cities_cursor:
        if city_row[1] == "Palestine":
            city_name = city_row[0]
            city_features.append(city_name)
            print("City in Palestine: ", city_name)

with arcpy.da.SearchCursor(disputed_areas, ['ADMIN', 'GEOUNIT']) as area_cursor:
    for area_row in area_cursor:
        if area_row[0] == "Palestine":
            area_name = area_row[1]
            area_features.append(area_name)
            print("Disputed area in Palestine: ", area_name)

# Construct expression for selecting cities
city_expression = ""
for city in city_features:
    city_expression += "NAME = '{0}' OR ".format(city)
city_expression = city_expression[:-4]  # Remove the last " OR "

# Construct expression for selecting disputed areas
area_expression = ""
for area in area_features:
    area_expression += "GEOUNIT = '{0}' OR ".format(area)
area_expression = area_expression[:-4]  # Remove the last " OR "

# Create feature layers for selected cities and disputed areas
arcpy.MakeFeatureLayer_management(populated_places, 'cities_layer', city_expression)
arcpy.MakeFeatureLayer_management(disputed_areas, 'areas_layer', area_expression)

# Export selected cities and disputed areas to shapefiles
arcpy.FeatureClassToFeatureClass_conversion('cities_layer', outpath, 'cities_in_palestine')
arcpy.FeatureClassToFeatureClass_conversion('areas_layer', outpath, 'disputed_areas_in_palestine')