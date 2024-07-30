import arcpy
arcpy.env.overwriteOutput = True
airports = arcpy.GetParameterAsText(0)

fields_list = arcpy.ListFields(airports)
field_names = []

for x in fields_list:
    print(x.name)
    print(x.type)
    if x.type == 'String':  # Note the proper case 'String'
        field_names.append(x.name)
    else:
        print("This is not a string, it's a {}".format(x.type))


for field in field_names:
    with arcpy.da.UpdateCursor(airports, ['name_en', field]) as airports_cursor:
        for row in airports_cursor:
            if row[1] is None or row[1] == " ":
                row[1] = row[0]
                airports_cursor.updateRow(row)
                arcpy.AddMessage("Success")
