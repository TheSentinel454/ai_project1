__author__ = 'Luke'

import math
import numpy as np
from sklearn import cross_validation
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn import datasets
from sklearn.externals.six import StringIO


def main():

    # TODO: Load the data set, and extract the features
    '''


    '''
    # Temporary: Load the data set
    iris = datasets.load_iris()

    # Get the data length
    dataLength = iris.data.shape[0]
    #iris.data
    data = np.random.random((dataLength, 1))
    Zmax, Zmin = data.max(), data.min()
    data = (data - Zmin) / (Zmax - Zmin)
    data *= 6
    data = np.around(data)

    # Add the new column
    data = np.hstack((data, iris.data))

    # Iterate through the users leaving one out at a time
    for ignoredUserId in range(0, 7):
        # Pass the data, and the ignored user ID
        classifier = getClassifierLeaveOneOut(data, ignoredUserId)

        # Get the test set
        testSet = data[data[:, 0] == ignoredUserId, :]

        # Predict the value based on the classifier
        prediction = classifier.predict(testSet)

def getTrainingDataLeaveOneOut(rawMatrix, ignoredUser):
    #getting all the samples for all users except the ignored one
    relevantMatrix = rawMatrix[rawMatrix[:,0] != ignoredUser, :]

    #remove the label column
    featureMatrix = relevantMatrix[:, 0:-1]
    #label column
    valueArray = relevantMatrix[:, -1]

    return (featureMatrix, valueArray)

def getClassifier(samples, target):
    clf = tree.DecisionTreeClassifier()
    return clf.fit(samples, target)

def getClassifierLeaveOneOut(rawMatrix, ignoredUser):
    trainingData = getTrainingDataLeaveOneOut(rawMatrix, ignoredUser)
    return getClassifier(trainingData[0], trainingData[1])

if __name__ == "__main__":
    main()