__author__ = 'ash'
import json
import numpy
import matplotlib.pyplot as plt



class VarInput:
    # create an empty class to set attributes for instances linked to config files
    pass

key_input = []
# create a list to hold keys from user input


def getInput(jsonpath):
    """
    read config file written in JSON
    load contents into dictionary
    *maybe construct a class instance with name of key pairing with correct value
    *maybe insert keys into a list for future reference

    L = length of X and Y
    D = number of features (dimensions) of X
    xlow, xhigh = range of value x in dataset X
    wlow, whigh = range of value w in W
    tlow, thigh = range of theta
    ycut = cutoff value to determine the binary value for y in Y
    noise = number of y with noise in Y
    iters = number of iterations run at most to train W
    c = step guess
    freq = iteration frequency to count for evaluation
    overd = number of dimensions we want to set to zero in real W to know about overfitting
    testportion = the portion of test size to train size given by the user
    lam = lambda value used to weight regulizer to avoid complexity of W to avoid overfitting

    @param jsonpath:
    @return:
    """
    with open(jsonpath) as json_file:
        confDict = json.load(json_file)
    return confDict
    # for key in configDict:
    #     setattr(VarInput, key, configDict[key])
    #     key_input.append(key)


def genX(l, d, low, high):
    """
    take in length, dimensions, wanted range of value for x's features
    create X with desired dimensions (number of features = dimensions + 1, set the last digit to 1) for latter
    theta info
    @param l:
    @param d:
    @param low:
    @param high:
    @return:
    """
    X = []
    for i in xrange(l):
        xfloat = numpy.random.rand(d+1)
        # xfloat is a d+1 dimension vector where each feature is a random float from 0 to 1
        xmultiplier = numpy.random.random_integers(low, high, d+1)
        # xmultiplier is a d+1 dimension vector where each feature is a random integer from xlow to xhigh
        xi = xfloat * xmultiplier
        # xi is a d+1 dimension vector where each feature is the product of a xfloat feature and a xmultiplier
        # feature in corresponding position
        xi[d] = 1
        # set the d+1 dimension of xi to 1 for future convenience while considering theta
        X.append(xi)
    #     X is a list of xi with length L given by the user
    return X


def genRealW(d, wlow, whigh, tlow, thigh, overd):
    """
    d is the number of features, and the loss function is w*x + theta comparing with y. To make things easier,
    we set x to 'd+1' dimensions where the last digit is 1, and set w to 'd+1' dimensions too where the last
    digit is theta
    @param d:
    @param wlow:
    @param whigh:
    @param tlow:
    @param thigh:
    @return:
    """
    wfloat = numpy.random.rand(d+1)
    # wfloat is a d+1 dimension vector where each feature is a random float from 0 to 1

    wmultiplier = numpy.random.random_integers(wlow, whigh, d+1)
    # wmultiplier is a d+1 dimension vector where each feature is a random integer from wlow to whigh

    w = wfloat * wmultiplier
    # w is a d+1 dimension vector where each feature is the product of a wfloat feature and a wmultiplier

    w[d] = numpy.random.random_integers(tlow, thigh, 1)
    # set the d+1 dimension of w to theta which is a random integer generated accordingly with tlow and thigh

    for i in range(overd):
        w[i] = 0
    # what we did above is to set a given number of dimensions in real W to zero to know about overfitting
    return w


def genVar(conf):
    """
    After getting input from config file, we want to create variables corresponding with user's input.
    We create a real w vector according to the x, and then create y according to the cutoff. Finally,
    we want to make some noise to the y to make it more realistic.
    @param conf:
    @return:
    """
    L = conf['L']
    D = conf['D']
    xlow = conf['xlow']
    xhigh = conf['xhigh']
    wlow = conf['wlow']
    whigh = conf['whigh']
    tlow = conf['tlow']
    thigh = conf['thigh']
    ycut = conf['ycut']
    noise = conf['noise']
    iters = conf['iters']
    c = conf['c']
    freq = conf['freq']
    overd = conf['overd']
    testportion = conf['testportion']
    lam = conf['lam']

    X = genX(L, D, xlow, xhigh)
    W = genRealW(D, wlow, whigh, tlow, thigh, overd)
    Y = []
    xTest = genX(L/testportion, D, xlow, xhigh)
    yTest = []

    for i in xrange(L):
        if numpy.dot(X[i], W) >= ycut:
            Y.append(1)
        else:
            Y.append(-1)

    for i in xrange(L/testportion):
        if numpy.dot(xTest[i], W) >= ycut:
            yTest.append(1)
        else:
            yTest.append(-1)
    # if the dot product of Xi and W is larger than or equal to the cutoff value given by user
    # we then set Yi's binary value to 1; else, Yi would be -1

    for i in range(noise):
        pos = numpy.random.randint(0, L - 1)
        y = -1 * Y[pos]
        Y[pos] = y
    # according to the number of noise the user wants, we randomly pick the noise number of positions in Y
    # and change the Yi value to its negative to make noise

    for i in range(noise/testportion):
        pos = numpy.random.randint(0, L/testportion - 1)
        y = -1 * yTest[pos]
        yTest[pos] = y
    #also make noise to testing set, as shown above

    return X, Y, iters, c, freq, ycut, W, xTest, yTest, lam
    #the W returned above is the real W for future reference


def train(x, y, iters, c, freq, ycut, xTest, yTest, lam):
    """
    with x, and y (with noise), and the step guessed by user (c), as well as the cutoff to determine y's binary
    value, we want to train a w (default value is set to 0 in d+1 dimensions) according to the given variables
    above. 'iter' is the maximum number of iterations allowed to train a w given by the user.
    @param x:
    @param y:
    @param iter:
    @param c:
    @param ycut:
    @return:
    """
    w = numpy.ones(len(x[0]))
    # x[0] is the first xi in X where it has d+1 dimensions. Hence we are generating a d+1 dimensional zeor
    #  vector here as the original value for w to train

    # TO PLOT performance of W:
    # plotting variables are based on both training and testing set
    timeEachTwenty = []
    fOneEachTwenty = []
    fOnTraining = []
    tcurrent = 0

    # variables for PLOTTING ends here
    ind = 0
    while ind < iters:
        # ind counts the iteration numbers and the upper limit is the iteration given by the user
        i = ind % len(y)
        # for each round, we use the remainder of total iterations on X's and Y's length
        # to represent the correct position of xi or yi in X or Y
        ind += 1
        print ind
        if numpy.dot(w, x[i]) >= ycut:
            py = 1
        # py here is the y value got from the guessed w
        else:
            py = -1

        if y[i] != py:
            # Loss is |yi - xi * W|, however, yi and xi*W have the same sign when guess is correct
            # So when yi*(xi*W) is -1, we guessed wrong, if we change loss to -yi*(xi*W), the more error we
            #   have, the larger the loss is, and we can minimize the loss during training
            # If the y value we get based on the guessed w is wrong:
            xy = numpy.dot(y[i], x[i])
            update = numpy.dot(c, xy)
            # take in L-2 regulizer as below:
            update -= numpy.dot(lam*c / (1.0*numpy.linalg.norm(w,2)), w)
            w += update

    #     for PLOT starting below based on testing, and training set:
        if (i+1) % freq == 0:
            # for testing set, we have:
            TP = 0
            FP = 0
            TN = 0
            FN = 0
            precision = 0
            recall = 0
            F_one = 0
            # for training set, we have:
            TPtr = 0
            FPtr = 0
            TNtr = 0
            FNtr = 0
            precTr = 0
            recallTr = 0
            f1Tr = 0
            # every given number of iterations (freq defined by the user), we do see how w performs on both
            #    testing and training set, and the coordinate on time line plus one:
            tcurrent += 1
            # looping into testing set and calculate F-1 score:
            for ii in xrange(len(yTest)):
                if numpy.dot(w, xTest[ii]) >= ycut:
                    py = 1
                else:
                    py = -1
                if yTest[ii] == 1 and py == 1:
                    TP += 1
                elif yTest[ii] == -1 and py == 1:
                    FP += 1
                elif yTest[ii] == -1 and py == 1:
                    FN += 1
                else:
                    TN += 1

            if TP + FP != 0:
                precision = TP/float(TP+FP)
            if TP + FN != 0:
                recall = TP/float(TP+FN)
            if precision + recall != 0:
                F_one = 2 * precision * recall / (precision + recall)

            # looping into training set and calculate F-1 score:
            for ii in xrange(len(y)):
                if numpy.dot(w, x[ii]) >= ycut:
                    py = 1
                else:
                    py = -1
                if y[ii] == 1 and py == 1:
                    TPtr += 1
                elif y[ii] == -1 and py == 1:
                    FPtr += 1
                elif y[ii] == -1 and py == 1:
                    FNtr += 1
                else:
                    TNtr += 1

            if TPtr + FPtr != 0:
                precTr = TPtr/float(TPtr+FPtr)
            if TPtr + FNtr != 0:
                recallTr = TPtr/float(TPtr+FNtr)
            if precision + recall != 0:
                f1Tr = 2 * precTr * recallTr / (precTr + recallTr)

            # Assert F-1 from training set and testing set into lists
            timeEachTwenty.append(tcurrent)

            # FOR F-1 Score:
            fOneEachTwenty.append(F_one)
            fOnTraining.append(f1Tr)

            # FOR ACCURACY:
            # fOneEachTwenty.append((TP+TN)/float(len(yTest)))
            # fOnTraining.append((TPtr+TNtr)/float(len(y)))

    # methods for PLOTTING ends here
    return w, timeEachTwenty, fOneEachTwenty, fOnTraining


def eval(time, fone, ftr):
    plt.plot(time, ftr, 'r')
    plt.plot(time, fone, 'b')
    plt.show()

    # for printing ACCURACY starting here
    # oknum = 0
    # for i in xrange(5000):
    #     if numpy.dot(wguess, x[i]) >= ycut:
    #         py = 1
    #     else:
    #         py = -1
    #
    #     if y[i] == py:
    #         oknum += 1
    #
    # print oknum
#   printing ACCURACY ends here
