#!/usr/bin/python
#-*- coding: utf-8 -*-

from PIL import Image
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
    img = Image.open(i)
    head, tail = splitext(i)
    convert = img.rotate(180)
    out = "./out/" + head.replace(".", "", 1) + tail
    convert.save(out)
