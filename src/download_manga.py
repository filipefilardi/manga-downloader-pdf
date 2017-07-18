#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, os.path
import urllib
import requests
import re

from bs4 import BeautifulSoup
from pdfconverter import to_pdf

def checkFolder():
    if not os.path.isdir(os.path.join("../tmp/")):
        print "nao tem tmp folder"
    if not os.path.isdir(os.path.join("../downloaded/")):
        print "nao tem downloaded folder"

def checkVolumesDownloaded(manganame):
    folder = os.path.join("../downloaded/")
    volumes = os.listdir(folder)

    for volume in volumes:
        if manganame not in volume:
            volumes.remove(volume)

    return volumes

def downloadPages(url, chapterpage, volumepage):
    try:
        link_page = url + chapterpage + ".html"
        chapter_page = requests.get(link_page).content
        soup_page = BeautifulSoup(chapter_page, 'html.parser')
        image = soup_page.find(id="image")
        url = image.get("src")
        urllib.urlretrieve(url, os.path.join("../tmp/", str(volumepage) + ".jpg"))
        return True
    except:
        return False

def crawler():
    
    manganame = "Hunter_x_Hunter_"
    mangalink = "http://mangafox.me/manga/hunter_x_hunter/"
    manga = requests.get(mangalink).content            
    soup = BeautifulSoup(manga, 'html.parser')

    allchapters = []
    volumes = soup.find(id="chapters")
    for chap in volumes.find_all("a", { "class" : "tips" }):
        #print re.findall(r'\d+', allchapters.text)
        allchapters.insert(0, chap.get("href"))

    while allchapters:
        linkstodownload = []
        volumetodownload = re.findall(r"v(\w+)", allchapters[0])
        i = 0
        
        if volumetodownload[0] != "TBD": 
            while re.findall(r"v(\w+)", allchapters[i]) == volumetodownload:
                linkstodownload.append(allchapters[i])
                i = i + 1

            for i in linkstodownload:
                allchapters.remove(i)
        else:
            linkstodownload = allchapters
            allchapters = []

        print "[  Volume", volumetodownload[0], " ] Started"       
        
        numberofpages = 1
        for chapter in linkstodownload:
            print " | Download | From", chapter
            
            manga = requests.get(chapter).content            
            soup = BeautifulSoup(manga, 'html.parser')
            # Download all pages from volume
            for pages in soup.findAll("option"):
                if pages['value'] == '0' :
                    break
                #print 'value: {}, text: {} , np: {}'.format(pages['value'], pages.text, numberofpages)
                downloadsucess = False
                while downloadsucess == False: 
                    downloadsucess = downloadPages(chapter[:-6], pages.text, numberofpages)
                numberofpages = numberofpages + 1

        to_pdf(volumetodownload[0], manganame)        

if __name__ == "__main__":
    checkFolder()
    crawler()