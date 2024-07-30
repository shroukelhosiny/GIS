import arcpy

arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\Users\shrouk\Desktop\gis\data"
countries = arcpy.GetParameterAsText(0)
all_areas = 0
updated_areas = 0

with arcpy.da.UpdateCursor(countries, ['ECONOMY', 'NAME', 'POP_YEAR', 'TYPE']) as UpdateCursor:
    for i in UpdateCursor:
        all_areas += 1
        if i[3] == 'Disputed' and i[2] < '2014':
            updated_areas += 1
            i[0] = 'updated'
            UpdateCursor.updateRow(i)
            arcpy.AddMessage("Updated area: " + str(i[1]))

arcpy.AddMessage("Number of updated areas: " + str(updated_areas))
arcpy.AddMessage("Number of all areas: " + str(all_areas))


