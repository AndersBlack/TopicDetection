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

'''
    actually running some text clustering on our car training set
'''

class Data:
  def __init__(self, data, target, target_names):
    self.data = data
    self.target = target
    self.target_names = target_names

carData = loadDict("carDict2.json")
techData = loadDict("techDict2.json")
politData = loadDict("politicalDict2.json")
sportData = loadDict("sportsDict2.json")
covidData = loadDict("covidDict2.json")

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
#
# for jsonObject in politData[:1000]:
#      test_targetArray = test_targetArray + [2]
#      polit_test_data = polit_test_data + [jsonObject['tokens']]

for jsonObject in sportData[:1000]:
     test_targetArray = test_targetArray + [2]
     sport_test_data = sport_test_data + [jsonObject['tokens']]

for jsonObject in covidData[:1000]:
     test_targetArray = test_targetArray + [3]
     covid_test_data = covid_test_data + [jsonObject['tokens']]

test_dataArray = car_test_data + tech_test_data + sport_test_data + covid_test_data

test_data = Data(test_dataArray,test_targetArray,["Cars","Tech","sport","Covid"])

print("Finished test data: " + str(len(test_dataArray)))

# Making train data

car_train_data = []
tech_train_data = []
polit_train_data = []
sport_train_data = []
covid_train_data = []

train_targetArray = []

for jsonObject in carData[1000:]:
     train_targetArray = train_targetArray + [0]
     car_train_data = car_train_data + [jsonObject['tokens']]

for jsonObject in techData[1000:]:
     train_targetArray = train_targetArray + [1]
     tech_train_data = tech_train_data + [jsonObject['tokens']]
#
# for jsonObject in politData[1000:]:
#      train_targetArray = train_targetArray + [2]
#      polit_train_data = polit_train_data + [jsonObject['tokens']]

for jsonObject in sportData[1000:]:
     train_targetArray = train_targetArray + [2]
     sport_train_data = sport_train_data + [jsonObject['tokens']]

for jsonObject in covidData[1000:]:
     train_targetArray = train_targetArray + [3]
     covid_train_data = covid_train_data + [jsonObject['tokens']]

train_dataArray = car_train_data + tech_train_data + sport_train_data  + covid_train_data

train_data = Data(train_dataArray,train_targetArray,["Cars","Tech","Sport","Covid"])

print("Finished training data: " + str(len(train_dataArray)))

# Build the model
model = make_pipeline(TfidfVectorizer(), MultinomialNB()) # Train the model using the training data
model.fit(train_data.data, train_data.target )# Predict the categories of the test data

pickle.dump(model, open("text_cluster.sav", 'wb'))

loaded_model = pickle.load(open("text_cluster.sav", 'rb'))

predicted_categories = loaded_model.predict(test_data.data)

print(np.array(test_data.target_names)[predicted_categories])

print("The accuracy is {}".format(accuracy_score(test_data.target, predicted_categories)))

# # plot the confusion matrix
mat = confusion_matrix(test_data.target, predicted_categories)
sns.heatmap(mat.T, square = True, annot=True, fmt = "d", xticklabels=["Cars","Tech","Sport","Covid"],yticklabels=["Cars","Tech","Sport","Covid"])

plt.xlabel("true labels")

plt.ylabel("predicted label")

plt.savefig("target-predicted.png")
