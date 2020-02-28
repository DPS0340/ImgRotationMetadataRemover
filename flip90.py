#!/usr/bin/python
#-*- coding: utf-8 -*-

# andreas@grellopolis.de, 2017

##########################################################
# Dieses Skript dreht spiegelverkehrt und auf dem Kopf   #
# JPEGs richtig herum.                                   #
# Ob es bei entsprechender Anpassung auch mit TIFFs      #
# oder anderen Formaten funktioniert, habe ich nicht     #
# getestet.                                              #
# Unter Verwendung des Python-Moduls multiprocessing     #
# wäre auch eine hochperformante Ausführung, also mit    #
# größeren Mengen Bildmaterials denkbar.                 #
##########################################################

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
    convert = img.rotate(270)
    out = "./out/" + head.replace(".", "", 1) + tail
    convert.save(out)
