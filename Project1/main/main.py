__author__ = 'Luke'

import math
import numpy as np
from sklearn import cross_validation
from sklearn import datasets


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


if __name__ == "__main__":
    main()