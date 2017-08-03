#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, os.path
import urllib
import requests
import re

from bs4 import BeautifulSoup
from pdfconverter import to_pdf

TESTE = "TESTE" 

DIR_DOWNLOADED = os.path.join("../downloaded/")
DIR_TEMP = os.path.join("../tmp/")

def checkFolder():
    print "Checking dependencies..."
    if not os.path.isdir(DIR_TEMP):
        print"Creating tmp folder"
        os.makedirs(DIR_TEMP)
    else:
        # Delete all files in tmp folder to avoid misunderstanding during pdf creation
        files = os.listdir(DIR_TEMP)
        if files:
            print "Deleting all files inside tmp folder"
            for file in files:
                os.remove(DIR_TEMP + file)

    if not os.path.isdir(DIR_DOWNLOADED):
        print "Creating downloaded folder"
        os.makedirs(DIR_DOWNLOADED)

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

def crawler(manganame, mangalink):
    
    checkFolder()

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


        volume = manganame + "_Volume_" + volumetodownload[0] + ".pdf"        
        alreadydownloaded = checkVolumesDownloaded(manganame)
        if volume in alreadydownloaded:
            print "[  Volume", volumetodownload[0], " ] Is already in your folder downloaded"       
        else:
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

def manuallyMode():
    mangalink = raw_input('Enter your mangafox link: ')
        
    manganame = mangalink.replace("http://mangafox.me/manga/","")
    manganame = manganame.replace("/","")
    manganame = manganame.title()

    crawler(manganame, mangalink)    

def options():
    option = raw_input('\n[MANGA DOWNLOADER PDF]\n\n[1] Type manga name\n[2] Manually insert url\n\nor anything else to exit:\n\n')
    
    if option == '1':
        
        manganame = raw_input('Manga to download: ')

        manganame = manganame.lower().strip().replace(' ', '_')
        mangalink = 'http://mangafox.me/manga/%s/' % manganame

        manga = requests.get(mangalink).content            
        soup = BeautifulSoup(manga, 'html.parser')

        if soup.title.text == "Search for  Manga at Manga Fox - Page 0":
            restart = raw_input('Manga not found! Do you wanna try again? (Y/N) ')
            if restart.lower() == 'n' :
                manuallyMode()
            else:
                options()
        else:
            title = soup.title.text
            title = title.split(' - ', 1)

            response = raw_input('Do you want to download {}? (Y/N) '.format(title[0]))
            if response.lower() == 'y':
                manganame = title[0].replace(' Manga', '')
                manganame = manganame.strip().replace(' ', '_')
                crawler(manganame, mangalink)        
            else:
                options()

    if option == '2':
        manuallyMode()
    else:
        return

if __name__ == "__main__":
    
    options()

    # # For this version you need to edit this link
    # mangalink = "http://mangafox.me/manga/hunter_x_hunter/"
    
    # manganame = mangalink.replace("http://mangafox.me/manga/","")
    # manganame = manganame.replace("/","")
    # manganame = manganame.title()

    # crawler(manganame, mangalink)