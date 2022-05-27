from gensim.parsing.preprocessing import STOPWORDS
import re, uuid
from unzipper import fileGetter, outletGetter
from pathlib import Path
import json, spacy
import pickle

def tokenGetter(articleDict):
#Gets the tokens from data
    tokens = []

    for key in articleDict:
         tokensFound = []

         for token in articleDict[key]['tokens']:
             tokensFound.append(token.lemma_)

         tokens.append(tokensFound)

    return tokens

def tokenGetterJson(articleJson):
#Gets the tokens from data
    tokens = []
    sp = spacy.load('en_core_web_sm')

    for jsonObject in articleJson:
         tokensFound = []
         spObject = sp(jsonObject['tokens'])

         for token in spObject:
             tokensFound.append(token.lemma_)

         tokens.append(tokensFound)

    return tokens

def removeStopWords(articleTokens):
#Removes stopwords from a collection of tokens
    all_stopwords_gensim = STOPWORDS.union(set(['-', '—', '+', '´', ':', '?', '$', '.', ',', "'", '´', ' ', '  ', '’', '&', '..', '"', 'wsj', '   ','|',';','#', '...', '    ', '\xa0','daily','news','york','year','star','(',')','–','★','world','express','…']))
    processed_tokens = []

    for tokens in articleTokens:
        token_no_sw = [word for word in tokens if not word in all_stopwords_gensim]
        processed_tokens.append(token_no_sw)

    return processed_tokens

def jsonMakerX(jsonData, articlePath, sp):

    articleJson = []

    #Put every article in a dictionary
    for article in jsonData:

        wordStripped = re.sub(r'\b\w{1,3}\b', '', jsonData[article]["title"].lower() + jsonData[article]["description"].lower())

        articleJson.append({
        "tokens": str(sp(wordStripped)),
        "Published": str(fileGetter(articlePath))
        })

    return articleJson

def constructDict(articlePaths, brands):

    allTokens = []
    articleDict = {}
    articleCounter, missingFileCounter = 0, 0

    for articlePath in articlePaths:

        stringObj = Path(articlePath).read_text(encoding="utf-8")

        jsonData = json.loads(stringObj)
        sp = spacy.load('en_core_web_sm')
        articleJson = jsonMakerX(jsonData, articlePath, sp)

        with open('fullDict.json', 'a', encoding='utf8') as data:
                json.dump(articleJson, data, indent=4)

        for article in articleJson:
            for car in brands:
                if " " + car.lower() + " " in article["tokens"]:
                    # print("Found car!" + car + " in " + article["tokens"])
                    with open('carDict.json', 'a', encoding='utf8') as data:
                        json.dump(article, data, indent=4)

        # Progress tracker
        articleCounter = articleCounter + 1
        print("Progress: %d out of %d days" %(articleCounter, (len(articlePaths) - missingFileCounter)))

    return articleDict
