from PIL import Image, ExifTags
from os.path import splitext
from glob import glob
import os
import sys

filePath = os.path.dirname(sys.argv[0])

images = glob(filePath + "/*.jpg") + glob(filePath + "/*.png")


if not os.path.exists(filePath + "/out"):
    os.mkdir(filePath + "/out")

for i in images:
    print("Now processing %s." % os.path.basename(i))
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
        out = filePath + "/out/" + os.path.basename(i)
        image.save(out)
        image.close()
    except (AttributeError, KeyError, IndexError):
        image=Image.open(i)
        out = filePath + "/out/" + os.path.basename(i)
        image.save(out)
        image.close()
    finally:
        print("%s Done!" % os.path.basename(i))
