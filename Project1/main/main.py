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

        classifiers = cls.getAllClassifiers(getAllTrainingSamples(training_data), training_label)

        # Get the test set
        testData = data[data[:, 0] == ignoredUserId, :]
        allTestData = getAllTestData(testData)
        correct_values = testData[:, -1]

        # Predict the value based on the classifier
        results = predictAll(classifiers, allTestData, correct_values)

        # Find any differences
        for type, result in results.iteritems():
            total_correct[type] = total_correct[type] + result[0]
            total[type] = total[type] + result[1]

    for type, correct in total_correct.iteritems():
        print("Accuracy for " + str(type) + ": " + str(correct/total[type]))

def getAllTrainingSamples(training_data):
    trainingSamples = {}

    raw_training_sample = training_data[:, 1:-4]
    ex_feature1 = training_data[:, -4]
    ex_feature2 = training_data[:, -3]
    ex_feature3 = training_data[:, -2]

    training_sample_1 = np.hstack((raw_training_sample, np.reshape(ex_feature1, (-1, 1))))
    training_sample_2 = np.hstack((raw_training_sample, np.reshape(ex_feature2, (-1, 1))))
    training_sample_3 = np.hstack((raw_training_sample, np.reshape(ex_feature3, (-1, 1))))
    training_sample_all = training_data[:, 1:-1]

    trainingSamples[raw] = raw_training_sample
    trainingSamples[feat1] = training_sample_1
    trainingSamples[feat2] = training_sample_2
    trainingSamples[feat3] = training_sample_3
    trainingSamples[all] = training_sample_all

    return trainingSamples

def getAllTestData(test_data):
    testData = {}

    raw_testing_sample = test_data[:, 1:-4]
    ex_feature1 = test_data[:, -4]
    ex_feature2 = test_data[:, -3]
    ex_feature3 = test_data[:, -2]

    testing_sample_1 = np.hstack((raw_testing_sample, np.reshape(ex_feature1, (-1, 1))))
    testing_sample_2 = np.hstack((raw_testing_sample, np.reshape(ex_feature2, (-1, 1))))
    testing_sample_3 = np.hstack((raw_testing_sample, np.reshape(ex_feature3, (-1, 1))))
    testing_sample_all = test_data[:, 1:-1]

    testData[raw] = raw_testing_sample
    testData[feat1] = testing_sample_1
    testData[feat2] = testing_sample_2
    testData[feat3] = testing_sample_3
    testData[all] = testing_sample_all

    return testData
    

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