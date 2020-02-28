from PIL import Image, ExifTags
from os.path import splitext
from glob import glob
import os

images = glob("./*.jpg")

try:
    os.mkdir("./out")
except:
    pass

for i in images:
    print("Now processing %s." %i)
    try:
        image=Image.open(i)
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation]=='Orientation':
                break
        exif=dict(image._getexif().items())

        if exif[orientation] == 3:
            image=image.rotate(180, expand=True)
        elif exif[orientation] == 6:
            image=image.rotate(270, expand=True)
        elif exif[orientation] == 8:
            image=image.rotate(90, expand=True)
        head, tail = splitext(i)
        out = "./out/" + head.replace(".", "", 1) + tail
        image.save(out)
        image.close()
    except (AttributeError, KeyError, IndexError):
        image=Image.open(i)
        head, tail = splitext(i)
        out = "./out/" + head.replace(".", "", 1) + tail
        image.save(out)
        image.close()
