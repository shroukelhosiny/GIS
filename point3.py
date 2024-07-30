import arcpy

# Set workspace
arcpy.env.workspace = r"C:\Users\shrouk\Desktop\gis\data"
countries = r"C:\Users\shrouk\Desktop\gis\data\ne_10m_admin_0_countries.shp"
populated_places = r"C:\Users\shrouk\Desktop\gis\data\ne_10m_populated_places.shp"
disputed_areas = r"C:\Users\shrouk\Desktop\gis\data\ne_10m_admin_0_disputed_areas.shp"

# Update SOV0NAME in populated places where ADM0NAME is "Palestine"
with arcpy.da.UpdateCursor(populated_places, ['ADM0NAME', 'SOV0NAME']) as cities_cursor:
    for city_row in cities_cursor:
        if city_row[0] == "Palestine":
            city_row[1] = "Palestine"
            cities_cursor.updateRow(city_row)
            print("SOV0NAME in Palestine updated")

# Update SOVEREIGNT in disputed areas where ADMIN is "Palestine"
with arcpy.da.UpdateCursor(disputed_areas, ['ADMIN', 'SOVEREIGNT']) as area_cursor:
    for area_row in area_cursor:
        if area_row[0] == "Palestine":
            area_row[1] = "Palestine"
            area_cursor.updateRow(area_row)
            print("SOVEREIGNT in Palestine updated")
