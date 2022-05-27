import shutil
import gzip
import os.path as pather

def unzip(zipPath):
#Unzips a file as a txt to the same location

    print("Unzipping:", zipPath)
    extractDir = pather.dirname(zipPath)
    filename = pather.basename(zipPath)
    #print("test")
    with gzip.open(zipPath, 'rb') as f_in:
        with open(extractDir + '/' + pather.splitext(filename)[0] + ".txt", 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

    return extractDir + '/' + pather.splitext(filename)[0] + ".txt"

def fileGetter(zipPath):
#Gets the name of the file a path points at without extension
    filename = pather.basename(zipPath)
    return pather.splitext(filename)[0]

def outletGetter(path):
#Gets the outlet folder from the path
    outlet = pather.basename(pather.dirname(pather.dirname(path)))
    return outlet

def pathConstructor(date):
    outlets = ["wsj.com","newsweek.com",
               "nypost.com","bbc.com",
               "dailystar.co.uk",
               "nbcnews.com","independent.co.uk",
               "nytimes.com",
               "thetimes.co.uk","abcnews.go.com",
               "afr.com","apnews.com",
               "cnbc.com","express.co.uk",
               "news.sky.com","thesun.co.uk",
               "usatoday.com","rt.com"]

    days = []
    articlePaths = []

    for ol in outlets:
            articlePaths = articlePaths + ["../../news_articles/release/" + ol + "/per_day/" + date]

    return articlePaths
