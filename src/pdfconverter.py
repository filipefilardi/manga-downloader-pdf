#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from fpdf import FPDF
from PIL import Image

def to_pdf(volume):
    print "[" + volume + "] Converting all pictures downloaded to pdf..."

    folder = os.path.join("../tmp/")
    lista = os.listdir(folder)
    if(lista):
        cover = Image.open(folder + str(len(lista)) + ".jpg")
        width, height = cover.size

        pdf = FPDF(unit = "pt", format = [width, height])
        for i in range(1, len(lista)+1):
            img = str(i) + ".jpg"     
            pdf.add_page()
            pdf.image(folder + img, 0, 0)

        pdf.output(os.path.join("../downloaded/") + volume + ".pdf", "F")

        print "[" + volume + "] Concluded with success."
        print "[" + volume + "] The pdf is inside your downloaded folder.\n"

        print "Deleting all images in tmp folder...",

        for img in lista:
            os.remove(folder + img)

        print "Done"
    else:
        print "No files on tmp folder. Please make sure you found the correct url. \n"
         