from gensim.parsing.preprocessing import STOPWORDS
import re, uuid
from unzipper import fileGetter, outletGetter, unzip
from pathlib import Path
import json, spacy

def tokenGetter(articleDict):
#Gets the tokens from data
    tokens = []

    for key in articleDict:
         tokensFound = []

         for token in articleDict[key]['tokens']:
             tokensFound.append(token.lemma_)

         tokens.append(tokensFound)

    return tokens

def removeStopWords(articleTokens, sp):
#Removes stopwords from a collection of tokens
    all_stopwords_gensim = STOPWORDS.union(set(['-', '—', '+', '´', ':', '?', '$', '.', ',', "'", '´', ' ', '  ', '’', '&', '..', '"', 'wsj', '   ','|',';','#', '...', '    ', '\xa0','daily','news','york','year','star','(',')','–','★','world','express','…']))
    processed_tokens = []

    for tokens in articleTokens:
        token_no_sw = [word for word in tokens if not word in all_stopwords_gensim]
        processed_tokens.append(token_no_sw)

    return processed_tokens

def dictionaryMaker(jsonData, articlePath, sp):

    articleDict = {}
    outlet = outletGetter(articlePath)

    #Put every article in a dictionary
    for article in jsonData:

        wordStripped = re.sub(r'\b\w{1,3}\b', '', jsonData[article]['title'].lower() + jsonData[article]['description'].lower())

        articleDict[str(uuid.uuid4())] = {
        'tokens':sp(wordStripped),
        'Outlet': outlet, 'Published': fileGetter(articlePath)
        }

    return articleDict

def prepTokens(articlePaths):

    allTokens = []
    articleCounter, missingFileCounter = 0, 0

    for articlePath in articlePaths:
        stringObj = ""
        
        if Path(articlePath + ".txt").exists():
            #print(".txt existed")
            stringObj = Path(articlePath + ".txt").read_text(encoding="utf-8")
        elif Path(articlePath + ".gz").exists():
            #print(".gz existed")
            stringObj = Path(unzip(articlePath + ".gz")).read_text(encoding="'utf-8'")
        else:
            continue

        if stringObj != "":
            print("Working on:", articlePath)
            jsonData = json.loads(stringObj)
            sp = spacy.load('en_core_web_sm')
            articleDict = dictionaryMaker(jsonData, articlePath, sp)

            #Get tokens from titles and descriptions
            tokens = tokenGetter(articleDict)
            #Remove stopwords and add to total token collection
            allTokens = allTokens + removeStopWords(tokens,sp)

            # Progress tracker
            articleCounter = articleCounter + 1
            #print("Progress: %d out of %d" %(articleCounter, (len(articlePaths) - missingFileCounter)))

    return allTokens
