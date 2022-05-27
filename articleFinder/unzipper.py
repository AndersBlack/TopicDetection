#!/usr/bin/python

import shutil
import gzip
import os.path as pather
import os, sys
import json

def unzip(zipPath):
#Unzips a file as a txt to the same location

    #print("Unzipping:", zipPath)
    extractDir = pather.dirname(zipPath)
    filename = pather.basename(zipPath)

    with gzip.open(zipPath, 'rb') as f_in:
        with open(extractDir + '/' + pather.splitext(filename)[0] + ".txt", 'wb') as f_out:
                #print(f_in)
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

def pathConstructor():
    outlets = ["wsj.com","newsweek.com",
               "nypost.com","bbc.com",
               "dailystar.co.uk",
               "nbcnews.com","independent.co.uk",
               "nytimes.com","bbc.com",
               "thetimes.co.uk","abcnews.go.com",
               "afr.com","apnews.com",
               "cnbc.com","express.co.uk",
               "news.sky.com","thesun.co.uk",
               "usatoday.com","rt.com"]
    days = []
    i = 0
    while i < 631:
        days = days + [str(20200100 + i)]
        i = i + 1

    articlePaths = []

    for ol in outlets:
        for day in days:
            articlePaths = articlePaths + ["../news_articles/release/" + ol + "/per_day/" + day]

    return articlePaths

def txtPathConstructorTotal():

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

        articlePaths = []

        for ol in outlets:
            os.mkdir("../news_articles/text_files/" + ol)
            for file in os.listdir("../news_articles/release/" + ol + "/per_day/"):
                if ".txt" not in file:
                    with gzip.open("../news_articles/release/" + ol + "/per_day/" + file, 'rb') as f_in:
                        articlePaths = articlePaths + ["../news_articles/text_files/" + ol + '/' + pather.splitext(file)[0] + ".txt"]
                        with open("../news_articles/text_files/" + ol + '/' + pather.splitext(file)[0] + ".txt", 'wb') as f_out:
                            shutil.copyfileobj(f_in, f_out)

        return articlePaths

def txtPathGetter():

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

        articlePaths = []

        for ol in outlets:
            for file in os.listdir("../news_articles/text_files/" + ol):
                articlePaths = articlePaths + ["../news_articles/text_files/" + ol + '/' + file]

        return articlePaths

def loadDict(path):

    with open(path) as json_file:
        data = json.load(json_file)

    return data
