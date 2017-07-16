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
    
    # link = "http://mangafox.me/manga/hunter_x_hunter/"
    # manga = requests.get(link).content            
    # soup = BeautifulSoup(manga, 'html.parser')

    # # Find all volumes
    # for line in soup.findAll("div", { "class" : "slide" }):
    #     print line.text

    volume = "Volume 01 Chapter 1 - 8" 
    #print re.findall(r'\b\d+([\.,]\d+)?', volume)   
    v, inicial,final = re.findall(r'\d+', volume)   
    volume = "Volume " + v

    #print volume, inicial, final

    counter = 1
    for chapter in range(int(inicial),int(final) + 1):
        link = "http://mangafox.me/manga/hunter_x_hunter/v01/c" + str(chapter) + "/1.html"
        manga = requests.get(link).content            
        soup = BeautifulSoup(manga, 'html.parser')

        # Download all pages from volume
        for pages in soup.findAll("option"):
            if pages['value'] == '0' :
                break
            #print 'value: {}, text: {}'.format(pages['value'], pages.text)
            downloadPages(link[:-6], pages.text, str(counter))
            counter = counter + 1

    to_pdf(volume)

if __name__ == "__main__":
	main()
