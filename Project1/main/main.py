from __future__ import division
__author__ = 'Luke'

import numpy as np
from sklearn import datasets
import classifier as cls
import collections

raw = "raw"
feat1 = "feat1"
feat2 = "feat2"
feat3 = "feat3"
all = "all"

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
    data = np.hstack((data, np.reshape(iris.target, (-1, 1))))

    total_correct = collections.defaultdict(int)
    total = collections.defaultdict(int)

    # Iterate through the users leaving one out at a time
    for ignoredUserId in range(0, 7):

        #get the training set
        training_data = data[data[:, 0] != ignoredUserId, :]
        training_label = training_data[:, -1]

        classifiers = cls.getAllClassifiers(splitDataOnFeatures(training_data), training_label)

        # Get the test set
        testData = data[data[:, 0] == ignoredUserId, :]
        allTestData = splitDataOnFeatures(testData)
        correct_values = testData[:, -1]

        # Predict the value based on the classifier
        results = predictAll(classifiers, allTestData, correct_values)

        # Find any differences
        for type, result in results.iteritems():
            total_correct[type] = total_correct[type] + result[0]
            total[type] = total[type] + result[1]

    for type, correct in total_correct.iteritems():
        print("Accuracy for " + str(type) + ": " + str(correct/total[type]))

def splitDataOnFeatures(data):
    finalData = {}

    raw_data = data[:, 1:-4]
    ex_feature1 = data[:, -4]
    ex_feature2 = data[:, -3]
    ex_feature3 = data[:, -2]

    feature_1 = np.hstack((raw_data, np.reshape(ex_feature1, (-1, 1))))
    feature_2 = np.hstack((raw_data, np.reshape(ex_feature2, (-1, 1))))
    feature_3 = np.hstack((raw_data, np.reshape(ex_feature3, (-1, 1))))
    feature_all = data[:, 1:-1]

    finalData[raw] = raw_data
    finalData[feat1] = feature_1
    finalData[feat2] = feature_2
    finalData[feat3] = feature_3
    finalData[all] = feature_all

    return finalData
    

def predictAll(classifiers, test_data, test_label):
    all_result = {}
    size = len(test_label)

    for type, classifier in classifiers.iteritems():
        correct = predict(classifier, test_data[type], test_label)
        all_result[type] = correct, size

    return all_result

def predict(classifier, test_data, test_label):
    prediction = classifier.predict(test_data)
    diff = test_label - prediction
    correct = len(np.where(diff == 0)[0])

    return correct

if __name__ == "__main__":
    main()