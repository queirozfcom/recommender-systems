# -*- coding: utf-8 -*-

#######################################################################
# @queirozfcom: adapted from https://gist.github.com/kljensen/5452382
#######################################################################

# Small script that shows hot to do one hot encoding
# of categorical columns in a pandas DataFrame.
# See:
#   http://scikit-learn.org/dev/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder
#   http://scikit-learn.org/dev/modules/generated/sklearn.feature_extraction.DictVectorizer.html

import pandas
import random
import numpy
from sklearn.feature_extraction import DictVectorizer

def one_hot_dataframe(data, cols, replace=False):
    """ Takes a dataframe and a list of columns that need to be encoded.
        Returns a 3-tuple comprising the data, the vectorized data,
        and the fitted vectorizor.
    """
    vec = DictVectorizer()
    mkdict = lambda row: dict((col, row[col]) for col in cols)
    vecData = pandas.DataFrame(vec.fit_transform(data[cols].apply(mkdict, axis=1)).toarray())
    vecData.columns = vec.get_feature_names()
    vecData.index = data.index
    if replace is True:
        data = data.drop(cols, axis=1)
        data = data.join(vecData)
    return (data, vecData, vec)