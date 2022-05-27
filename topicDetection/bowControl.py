from ast import literal_eval

def saveBowToFile(bowArray, finalDate):

    # define list of places

    with open('bowfiles/bowFile_' + str(finalDate) + '.txt', 'w', encoding="utf-8") as filehandle:
        for bow in bowArray:
            filehandle.write('%s\n' % bow)

def readBowFromFile(fileName):

    bowArray = []

    # open file and read the content in a list
    with open('bowfiles/' + fileName, 'r', encoding="utf-8") as filehandle:
        for bow in filehandle:
            # remove linebreak which is the last character of the string
            currentBow = bow[:-1]

            # add item to the list
            bowArray.append(literal_eval(currentBow))

    return bowArray
