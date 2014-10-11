__author__ = 'Luke'

from sklearn import tree

def getTrainingDataLeaveOneOut(rawMatrix, ignoredUser):
    #getting all the samples for all users except the ignored one
    relevantMatrix = rawMatrix[rawMatrix[:, 0] != ignoredUser, :]

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