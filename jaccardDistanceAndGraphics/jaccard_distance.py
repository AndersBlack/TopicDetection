from stats import documentCountPrTopic, generateWordcloud
import os
from gensim import models, corpora
from pprint import pprint
import re
import sys
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def getListOfListsOfWords():

    print("Getting list of topics from bow files..")

    bowDir = list(os.listdir("bowfiles"))
    bowDir.sort()

    monthList = []

    for file in bowDir:

        corpus = corpora.MmCorpus('models_and_corpus/corpus_' + file)
        lda_model =  models.LdaModel.load('models_and_corpus/lda_' + file + '.model')

        topicForMonthList = []

        for i in range(len(lda_model.print_topics(num_topics=10,num_words=10))):
            x = re.findall("\"{1}[A-z,-]*\"{1}", lda_model.print_topics(num_topics=10,num_words=10)[i][1])
            x_clean = [word.replace('"', '') for word in x]
            topicForMonthList.append( [x_clean,[file]] )

        monthList.append(topicForMonthList)

        # print(lda_model.get_topics())
        # print("Creating Visuals..")
        # documentCountPrTopic(corpus, lda_model, file)
        # generateWordcloud(lda_model, file)

    #pprint(monthList)

    return monthList

def evaluateTopics(topicList, jaccDisThreshold):

    print("Evaluating topics..")

    results = []
    tempList = []

    foundJacc = 0
    x = []
    month = 1

    for monthList in topicList:

        #print("Month",month)
        #print("Result length",len(results))
        for topic in monthList:
            if len(results) < 10:
                results.append(topic)
                continue
            for resultTopic in results:
                x = x + topic[1]
                #print("Topic",topic[0],topic[1],"ResultTopic",resultTopic[0],resultTopic[1])
                if topic[1][0] not in resultTopic[1]:
                    jacDis = jaccardDistance(topic[0],resultTopic[0])
                    if jacDis >= float(jaccDisThreshold):
                        #print("Found jaccard")
                        #resultTopic[0] = topic[0] # Swaps the current topics words for the topic it matched!
                        resultTopic[1] = resultTopic[1] + topic[1]
                        if 2 < len(resultTopic):
                            resultTopic[2] = resultTopic[2] + [jacDis]
                        else:
                            resultTopic.append([jacDis])

                        foundJacc = 1

            if foundJacc == 0:
                tempList.append(topic)

            foundJacc = 0

        results = results + tempList
        tempList = []
        month = month + 1

    x = list(set(x))

    return results, x

def jaccardDistance(topic1, topic2):

    commonWords = 0

    for word in topic1:
        if word in topic2:
            commonWords = commonWords + 1

    jaccard_distance = commonWords / (len(topic1) + len(topic2) - commonWords)

    return jaccard_distance

def generateGraph(results, x):

    # Make a data frame

    #print(results[10])

    for x in range(0,len(results) - 1):
        results[x][1] = re.findall("[0-9]{1,}", ' '.join(map(str,results[x][1])))
        if len(results[x]) > 2:
            if len(results[x][2]) > 1:
                results[x][2] = [results[x][2][0]] + results[x][2]

    for x in range(0,len(results) - 1):
        if len(results[x]) > 2:
            if len(results[x][2]) > 10:


                df = pd.DataFrame({'x': results[x][1], str(len(results[x][2])) + "months  ": results[x][2]})
                #df=pd.DataFrame({str(len(results[x][2])) + "months  ": results[x][2], 'x': results[x][1]})

                print("words",results[x][0],"\n months",results[x][1],"\n jac count:",str(len(results[x][2])),"\n jac dis:", [ '%.5f' % elem for elem in results[x][2] ])
                print("\n")

                # Change the style of plot
                plt.style.use('seaborn-darkgrid')
                plt.figure(figsize=(25,10))

                # Create a color palette
                palette = plt.get_cmap('Set1')

                # Plot multiple lines
                num=0
                for column in df.drop('x', axis=1):
                    num+=1

                plt.plot(df['x'], df[column], marker='', linewidth=1, alpha=0.9, label=column)

                # Add legend
                plt.legend(loc=2, ncol=2)

                # Add titles
                plt.title(str(results[x][0]), loc='left', fontsize=12, fontweight=0, color='black')
                plt.xlabel("Period end")
                plt.ylabel("Jaccard Distance")

                # Show the graph
                plt.savefig(str(results[x][0]) + ".png")
                plt.show()

# --------------------- Main ----------------

# Data i want to achieve:
# List of longest running topics with month count and start date.
# If a topic disappears and reappears, note when it reappears

jaccDisThreshold = sys.argv[1]

topicLists = getListOfListsOfWords()

results, x = evaluateTopics(topicLists, jaccDisThreshold)

generateGraph(results, x)

longestRunningTopic = results[0]
flashNews = 0
runningList = []

# Clean up results
for result in results:
    result[1] = re.findall("[0-9]{1,}", ' '.join(map(str,result[1])))
    runningList.append(len(result[1]))
    if len(longestRunningTopic[1]) < len(result[1]):
        longestRunningTopic = result
    if len(result[1]) == 1:
        flashNews = flashNews + 1

runningList_sorted = runningList.sort(reverse=True)

print("Longest running topic:",longestRunningTopic)
print("Topics that only lasted one period:",flashNews)
print("RunningList, sorted:",runningList)
print("There was a total of",len(runningList),"topics")


#pprint(results)
