import os
import arcpy
from PIL import Image, ExifTags
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\Users\shrouk\Desktop\gis\data"
img = r"C:\Users\shrouk\Desktop\gis\img"

img_contents=os.listdir(img)

for image in img_contents:
    full_path=os.path.join(img,image)
    print ("full_path:", full_path)

    pillow_image = Image.open(full_path)
    exif={ExifTags.TAGS[k]: v for k,v in pillow_image.getexif().items() if k in ExifTags.TAGS}
    print ("exif:", exif)
print("=" * 30)

gps_all={}
try:
    for key in exif['GPSInfo'].keys():
        print "this is code value {}".format(key)
        decoded_value=ExifTags.GPSTAGS.get(key)
        print "this is associated label {}".format(decoded_value)
        print("=" * 30)
        gps_all[decoded_value]=exif['GPSInfo'][key]

    long_ref= gps_all.get('GPSLongitudeRef')
    long = gps_all.get('GPSLongitude')
    lat_ref = gps_all.get('GPSLatitudeRef')
    lat = gps_all.get('GPSLatitude')
    print long_ref," ----   ",long
    print lat_ref,"  ---- ",lat
except:
    print "image has no Gps in it".format(full_path)
    pass