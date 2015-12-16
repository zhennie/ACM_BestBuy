import numpy

__author__ = 'ash'
import redo_functions

jsonpath = '../data/g_configFile'

if __name__ == '__main__':
    # set random seed
    numpy.random.seed(0)

    print numpy.random.rand()
    conf = redo_functions.getInput(jsonpath)
    X, Y, iters, c, freq, ycut, wReal, xTest, yTest, lam = redo_functions.genVar(conf)

    print wReal

    w, t, f, ftr = redo_functions.train(X, Y, iters, c, freq, ycut, xTest, yTest, lam)

    print w

    redo_functions.eval(t, f, ftr)