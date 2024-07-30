import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\Users\shrouk\Desktop\gis\data"
airports = r"C:\Users\shrouk\Desktop\gis\data\ne_10m_airports.shp"
coun=0
airports_cursors = arcpy.SearchCursor(airports, ["name", "location", "wikipedia"])
for airport in airports_cursors:
    if (airport.getValue("location") == "ramp"):
        print("Airport Name:", airport.getValue("name"))
        print("Location:", airport.getValue("location"))
        print("Wikipedia:", airport.getValue("wikipedia"))
        print("=" * 20)  # Separate airport information

