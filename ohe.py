from sklearn.feature_extraction import DictVectorizer
import pandas as pd
import scipy.sparse

def one_hot_dataframe(data, cols, replace=False):
    """ Takes a dataframe and a list of columns that need to be encoded.
        Returns a 3-tuple comprising the data, the vectorized data,
        and the fitted vectorizor."""
    vec = DictVectorizer(sparse=False)
    vecData = pd.DataFrame(vec.fit_transform(data[cols].T.to_dict().values()))
    vecData.columns = vec.get_feature_names()
    vecData.index = data.index
    if replace is True:
        data = data.drop(cols, axis=1)
        data = data.join(vecData)
    return (data, vecData, vec)

def ohe_dataframe_to_sparse(data, cols, replace=True, sort=True):
    """ Takes a dataframe and a list of columns that need to be encoded.
        Returns a 3-tuple comprising the data converted to csr matrix (csr), the vectorized data as csr,
        and the fitted vectorizor."""
    data_temp = data.copy()
    vec = DictVectorizer(sparse=True, sort=sort)
    data_categorical = vec.fit_transform(data_temp[cols].T.to_dict().values())
    
    if replace is False:
        data_sparse = scipy.sparse.csr_matrix(data_temp.as_matrix())
    else:
        data_temp = data_temp.drop(cols, axis=1)
        if len(data_temp.columns) <= 0:
            data_sparse = data_categorical
        else:
            data_sparse = scipy.sparse.csr_matrix(data_temp.as_matrix())
            data_sparse = scipy.sparse.hstack((data_sparse, data_categorical), format='csr')        
    
    return (data_sparse, data_categorical, vec)
