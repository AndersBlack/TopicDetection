import numpy as np, pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import confusion_matrix, accuracy_score

sns.set() # use seaborn plotting style

# Load the dataset
data = fetch_20newsgroups() # Get the text categories
text_categories = data.target_names # define the training set
train_data = fetch_20newsgroups(subset="train", categories=text_categories) # define the test set
test_data = fetch_20newsgroups(subset="test", categories=text_categories)

print(data.target_names)

# print("We have {} unique classes".format(len(text_categories)))
# print("We have {} training samples".format(len(train_data.data)))
# print("We have {} test samples".format(len(test_data.data)))

# Build the model
model = make_pipeline(TfidfVectorizer(), MultinomialNB()) # Train the model using the training data
model.fit(train_data.data, train_data.target )# Predict the categories of the test data
predicted_categories = model.predict(test_data.data)

print(np.array(test_data.target_names)[predicted_categories])

# plot the confusion matrix
mat = confusion_matrix(test_data.target, predicted_categories)
sns.heatmap(mat.T, square = True, annot=True, fmt = "d", xticklabels=train_data.target_names,yticklabels=train_data.target_names)
plt.xlabel("true labels")
plt.ylabel("predicted label")
plt.show()

print("The accuracy is {}".format(accuracy_score(test_data.target, predicted_categories)))
