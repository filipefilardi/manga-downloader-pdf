# manga-downloader-pdf

Manga downloader made in python to create pdf volumes.

The crawler script will download all volumes available in [Manga Fox](http://mangafox.me/directory/) from a choosed manga ([example](http://mangafox.me/manga/hunter_x_hunter/)) and convert each volume in pdf.

This script was made with no money intentions. I just want to provide a different option to read mangas offline and take no credits for creation, editing, publishing or hosting the images downloaded.

Don't forget to support the mangaka and Manga Fox in any way you can.

Feel free to contribute with the project in any way.

## Features ##

 * Simple text UI;
 * Download manga via name input;
 * Download manga via direct Manga Fox url;
 * Automatically transform all jpgs downloaded in separated pdfs, divided by volumes;
 * Automatically create 'tmp' and 'downloaded' folders;
 * Check volumes inside downloaded folder and skip volumes already downloaded.
 
## Installation ##

`$ pip install beautifulsoup4`

Check [official beautifulsoup4 documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) if needed.


`$ pip install requests`

Check [official requests documentation](http://docs.python-requests.org/en/master/) if needed.

`$ pip install fpdf`

`$ pip install image`

Check [official fpdf documentation](https://pyfpdf.readthedocs.io/en/latest/) if needed.


## Usage ##

You may or may not find some issues while downloading searching some mangas via name input. If this happens, just use the direct url input option to download your pdf while the full version is not yet developed. If you encounter some issue, put in the issue session.

Your pdf volumes will be inside downloaded folder.

The source-code has only been tested on Linux with python 2.

## Run ##

`$ python download_manga.py`

## Next Features ## 
 
 * Make the downlaod via manga name string 100% functional with no issues;
 * Convert the jpgs to differents formats;
