# darkweb-crawler

This repository is based on a university level project. 

The objective of this project is to scrape data from the dark web as safely and as anonymously as possible to detect possible criminal activities that take place in the dark web forums. Currently the only task this project performs is to scrape botnet recruitment data in dark web.

Tools and techniques used for this project:
pendrive bootable TAILS OS - for anonymous activities
TOR - for dark web access
Python (Scrapy Framework) - for web scraping

At this level this project does not contain a database and only produces JSON format output.

The program contains a spider named 'bots' that does the main scraping of data.

Running this project:
1. build a safe virtual environment which will keep your details hidden from being traced digitally and have your host device unaffected. I have used TAILS OS for the same reason.

2. configure your TOR network and onion routing

3. Clone the repository in your device

4. go to the main directory and run the command:

```
scrapy crawl bots
```


