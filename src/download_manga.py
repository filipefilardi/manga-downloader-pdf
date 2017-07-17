#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, os.path
import urllib
import requests
import re

from bs4 import BeautifulSoup
from pdfconverter import to_pdf

def download(url, number):
    urllib.urlretrieve(url, os.path.join("../tmp/", number + ".jpg"))

def downloadPages(url, value, number):
    link_page = url + value + ".html"
    chapter_page = requests.get(link_page).content
    soup_page = BeautifulSoup(chapter_page, 'html.parser')
    image = soup_page.find(id="image")
    url = image.get("src")
    download(url, number)

def main():
    
    manganame = "Hunter_x_Hunter_"
    mangalink = "http://mangafox.me/manga/hunter_x_hunter/"
    manga = requests.get(mangalink).content            
    soup = BeautifulSoup(manga, 'html.parser')

    # Find all volumes, but exclude the not complete "TBD" volume
    # for line in soup.findAll("div", { "class" : "slide" }):
    #     volume = line.text
        
    #     if "TBD" in volume:
    #         continue

    #     print volume
    #     print re.findall(r'\d+', volume)

    chapters = []
    volumes = soup.find(id="chapters")
    print"[ Volume 1 ] started"
    for chap in volumes.find_all("a", { "class" : "tips" }):
        #print re.findall(r'\d+', chapters.text)
        chapters.insert(0, chap.get("href"))

    vol = re.findall(r"v(\d+)", chapters[0])
    counter = 1
    for chapter in chapters:
        if re.findall(r"v(\d+)", chapter) == vol:
            print "  [ Download ] from", chapter        
            
            manga = requests.get(chapter).content            
            soup = BeautifulSoup(manga, 'html.parser')

            # Download all pages from volume
            for pages in soup.findAll("option"):
                if pages['value'] == '0' :
                    break
                #print 'value: {}, text: {}'.format(pages['value'], pages.text)
                downloadPages(chapter[:-6], pages.text, str(counter))
                counter = counter + 1
        else:
            
            if not vol:
                to_pdf("TBD", manganame)
                print "[ Volume TBD ] started"
            else:    
                to_pdf(vol[0], manganame)
                print "[ Volume", vol[0]+1, "] started"
           
            vol = re.findall(r"v(\d+)", chapter)
            
            counter = 1     
            print "  [ Download ] from", chapter

    


    # #print re.findall(r'\b\d+([\.,]\d+)?', volume)   
    # vol, inicial,final = re.findall(r'\d+', volume)   
    # volume = "Volume " + vol

    # #print volume, inicial, final
    # print "[" + volume + "] started"

    # counter = 1
    # for chapter in range(int(inicial),int(final) + 1):
    #     print "Downloading jpgs from chapter", str(chapter)
        
    #     link = "http://mangafox.me/manga/hunter_x_hunter/v01/c" + str(chapter) + "/1.html"
    #     manga = requests.get(link).content            
    #     soup = BeautifulSoup(manga, 'html.parser')

    #     # Download all pages from volume
    #     for pages in soup.findAll("option"):
    #         if pages['value'] == '0' :
    #             break
    #         #print 'value: {}, text: {}'.format(pages['value'], pages.text)
    #         downloadPages(link[:-6], pages.text, str(counter))
    #         counter = counter + 1

    # to_pdf(volume, manganame)

if __name__ == "__main__":
	main()
