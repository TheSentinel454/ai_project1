from __future__ import division
__author__ = 'Luke'

import numpy as np
from sklearn import datasets
import classifier as cls

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

    total_correct = 0
    total = 0
    # Iterate through the users leaving one out at a time
    for ignoredUserId in range(0, 7):

        # Pass the data, and the ignored user ID
        classifier = cls.getClassifierLeaveOneOut(data, ignoredUserId)

        # Get the test set
        original_test = data[data[:, 0] == ignoredUserId, :]
        test_set = original_test[:, 0:-1]
        correct_values = original_test[:, -1]

        # Predict the value based on the classifier
        prediction = classifier.predict(test_set)

        # Fina any differences
        diff = correct_values - prediction
        correct = len(np.where(diff == 0)[0])
        total_correct += correct
        total += len(correct_values)


        print("User: " + str(ignoredUserId))
        print("Correct: " + str(total_correct))
        print("Wrong: " + str(total-total_correct))

    print("Accuracy: " + str(total_correct/total))

if __name__ == "__main__":
    main()