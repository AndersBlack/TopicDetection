from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.metrics import confusion_matrix, accuracy_score
import numpy as np, pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pickle

from unzipper import loadDict
from preprocessing import tokenGetterJson, removeStopWords

class Data:
  def __init__(self, data, target, target_names):
    self.data = data
    self.target = target
    self.target_names = target_names

topic_names = ["Cars","Tech","sport","Covid"]

def getDataFronJSONfiles():

    carData = loadDict("carDict.json")
    techData = loadDict("techDict.json")
    politData = loadDict("politicalDict.json")
    sportData = loadDict("sportsDict.json")
    covidData = loadDict("covidDict.json")

    car_test_data = []
    tech_test_data = []
    polit_test_data = []
    sport_test_data = []
    covid_test_data = []

    test_targetArray = []

    # Making test data

    for jsonObject in carData[:1000]:
         test_targetArray = test_targetArray + [0]
         car_test_data = car_test_data + [jsonObject['tokens']]

    for jsonObject in techData[:1000]:
         test_targetArray = test_targetArray + [1]
         tech_test_data = tech_test_data + [jsonObject['tokens']]

    for jsonObject in politData[:1000]:
         test_targetArray = test_targetArray + [2]
         polit_test_data = polit_test_data + [jsonObject['tokens']]

    for jsonObject in sportData[:1000]:
         test_targetArray = test_targetArray + [3]
         sport_test_data = sport_test_data + [jsonObject['tokens']]

    for jsonObject in covidData[:1000]:
         test_targetArray = test_targetArray + [4]
         covid_test_data = covid_test_data + [jsonObject['tokens']]

    test_dataArray = car_test_data + tech_test_data + polit_test_data + sport_test_data + covid_test_data

    print(car_test_data)

    print("Total unique test data entries:",len(list(set(test_dataArray))))

    test_data = Data(test_dataArray,test_targetArray,["Cars","Tech","Political","sport","Covid"])

    #print("Finished test data: " + str(len(test_dataArray)))

    return test_data

def getVerifiedData():

    car_test_data = []
    tech_test_data = []
    polit_test_data = []
    sport_test_data = []
    covid_test_data = []

    test_targetArray = []

    with open('../verified articles/verified_cars.txt') as f:
        lines = f.readlines()

        for line in lines:
            test_targetArray = test_targetArray + [0]
            car_test_data = car_test_data + [line]

    f.close()

    with open('../verified articles/verified_tech.txt') as f:
        lines = f.readlines()

        for line in lines:
            test_targetArray = test_targetArray + [1]
            tech_test_data = tech_test_data + [line]

    f.close()

    # with open('../verified articles/verified_politics.txt') as f:
    #     lines = f.readlines()
    #
    #     for line in lines:
    #         test_targetArray = test_targetArray + [2]
    #         polit_test_data = polit_test_data + [line]
    #
    # f.close()

    with open('../verified articles/verified_sports.txt') as f:
        lines = f.readlines()

        for line in lines:
            test_targetArray = test_targetArray + [2]
            sport_test_data = sport_test_data + [line]

    f.close()

    with open('../verified articles/verified_covid.txt') as f:
        lines = f.readlines()

        for line in lines:
            test_targetArray = test_targetArray + [3]
            covid_test_data = covid_test_data + [line]

    f.close()

    test_dataArray = car_test_data + tech_test_data + sport_test_data + covid_test_data
    test_data = Data(test_dataArray,test_targetArray,["Cars","Tech","sport","Covid"])

    print("Total unique test data entries:",len(list(set(test_dataArray))))

    return test_data


test_data = getVerifiedData()

#test_data = getDataFronJSONfiles()

loaded_model = pickle.load(open("text_cluster.sav", 'rb'))

predicted_categories = loaded_model.predict(test_data.data)

wrongData = []

for x in range(len(predicted_categories)):
    if predicted_categories[x] != test_data.target[x]:
        wrongData.append(test_data.data[x] + " True: " + topic_names[test_data.target[x]] + " Guess: " + topic_names[predicted_categories[x]])
        #print("Articles:" + test_data.data[x] + " True topic: " + topic_names[test_data.target[x]] + " False topic: " + topic_names[predicted_categories[x]])

print("Wrong guesses:",len(wrongData))

wrongData = list(set(wrongData))

print("Unique wrong guesses:",len(wrongData))

for x in range(len(wrongData)):
     print(wrongData[x],"\n")

print(np.array(test_data.target_names)[predicted_categories])

print("The accuracy is {}".format(accuracy_score(test_data.target, predicted_categories)))

# # plot the confusion matrix
mat = confusion_matrix(test_data.target, predicted_categories)
sns.heatmap(mat.T, square = True, annot=True, fmt = "d", xticklabels=["Cars","Tech","Sport","Covid"],yticklabels=["Cars","Tech","Sport","Covid"])

plt.xlabel("true labels")

plt.ylabel("predicted label")

plt.savefig("target-predicted.png")

'''
    Important notes:
    Of the training data, only 2560 articles are unique.
    Wrong guesses: 1441
    Unique wrong guesses: 835
'''
