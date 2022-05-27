''' The following code is written for a Bachelor Project for SDU
 Subject: Topic Detection & Context Mining
 Author: Anders Black Larsen
 Description: An implementation of LDA, Latent Dirichlet Allocation, in python. (Might change)
 Prerequirements: The program needs a list of K topics '''

from unzipper import unzip, pathConstructor
from bowControl import readBowFromFile, saveBowToFile
from stats import documentCountPrTopic, generateWordcloud
from preprocessing import prepTokens
from LDA import generateLDA
from gensim import models, corpora
from pprint import pprint
import os

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

i = 0
monthCounter = 0
year = 2015
month = 7
day = 1
startday = ""
days = []
articlePaths = []

# ------------------------------------- Setup ----------------------------------

#
# while year <= 2021:
#     while month <= 12:
#         while day <= 31:
#
#             if month > 9 and day > 9:
#                 startday = str(year) + str(month) + str(day)
#             elif month > 9:
#                 startday = str(year) + str(month) + "0" + str(day)
#             elif day > 9:
#                 startday = str(year) + "0" + str(month) + str(day)
#             else:
#                 startday = str(year) + "0" + str(month) + "0" + str(day)
#
#             for ol in outlets:
#                     articlePaths = articlePaths + ["../../news_articles/release/" + ol + "/per_day/" + startday]
#
#             day = day + 1
#             print(startday)
#
#         monthCounter = monthCounter + 1
#
#         if monthCounter == 2:
#
#             print("Contructing tokens from the %d days that was found" %(len(articlePaths)))
#             #print(startday)
#             allTokens = prepTokens(articlePaths)
#             saveBowToFile(allTokens, startday)
#
#             articlePaths = []
#             i = i + 1
#             monthCounter = 0
#             month = month - 1
#
#         day = 0
#         month = month + 1
#
#     month = 1
#     year = year + 1


# # ------------------------------------- LDA ----------------------------------

bowDir = list(os.listdir("bowfiles"))
bowDir.sort()

for file in bowDir:

    allTokens = readBowFromFile(file)

    print("Running LDA..")
    lda_model, corpus = generateLDA(allTokens)

    lda_model.save('lda_' + file + '.model')
    corpora.MmCorpus.serialize('corpus_' + file, corpus)

# # --------------------------------Construct visuals ----------------------------

# corpus = corpora.MmCorpus('corpus')
# lda_model =  models.LdaModel.load('lda.model')
#
# pprint(lda_model.print_topics(num_topics=25,num_words=10))
#
# print("Creating Visuals..")
# documentCountPrTopic(corpus, lda_model)

# generateWordcloud(lda_model)
