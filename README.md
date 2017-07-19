# manga-downloader-pdf

Basic manga downloader made in python.

The crawler script will download all volumes available in [Manga Fox](http://mangafox.me/directory/) from a certain manga url ([example](http://mangafox.me/manga/hunter_x_hunter/)) and convert each volume in pdf.

This script was made with no money intentions. I just want to provide a different option to read mangas offline and take no credits for creation, editing, publishing or hosting the images downloaded.

Don't forget to support the mangaka and [Manga Fox](http://mangafox.me/directory/) in any way you can.

Feel free to contribute with the project in any way.

## Features ##

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

This version is limited. You should change the url in [this line](https://github.com/filipefilardi/manga-downloader/blob/master/src/download_manga.py#L111) to your manga url hosted on Manga Fox. The script will do the rest.

At this point, the source-code has only been tested on Linux with python 2.

## Run ##

`$ python download_manga.py`

## Next Features ## 
 
 * Search manga by name, excluding partially the direct url usage;
 * Convert the jpgs to differents formats;