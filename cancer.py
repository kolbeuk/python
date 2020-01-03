import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()

print(cancer.DESCR) # Print the data set description

cancer.keys()

def answer_one():
    
    # Your code here
    df = pd.DataFrame(cancer.data, columns=cancer.feature_names)
    df['target'] = pd.Series(cancer.target)
    df.index = pd.RangeIndex(start=0, stop=569, step=1)
    return df

answer_one()

def answer_two():
    cancerdf = answer_one()
    
    # Your code here
    data = np.array([0,1])   
    ser = pd.Series(data, index=['malignant', 'benign']) 
    for index, row in cancerdf.iterrows():
        ser[0] = (cancerdf['target'] == 0).sum()
        ser[1] = (cancerdf['target'] == 1).sum()
    return ser

answer_two()

def answer_three():
    cancerdf = answer_one()
    
    # Your code here
    y = cancerdf['target']
    X = cancerdf.drop('target', 1)
    
    return X, y

answer_three()

from sklearn.model_selection import train_test_split

def answer_four():
    X, y = answer_three()
    
    # Your code here
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
    
    return X_train, X_test, y_train, y_test

answer_four()


from sklearn.neighbors import KNeighborsClassifier

def answer_five():
    X_train, X_test, y_train, y_test = answer_four()
    
    # Your code here
    knn = KNeighborsClassifier(n_neighbors = 1)
    
    return knn.fit(X_train, y_train)

answer_five()

def answer_six():
    cancerdf = answer_one()
    knn = answer_five()
    means = cancerdf.mean()[:-1].values.reshape(1, -1)
    # Your code here
    cancer_prediction = knn.predict(means)
    return cancer_prediction

answer_six()

def answer_seven():
    X_train, X_test, y_train, y_test = answer_four()
    knn = answer_five()
    
    # Your code here
    cancer_prediction = knn.predict(X_test)
    return cancer_prediction

answer_seven()

def answer_eight():
    X_train, X_test, y_train, y_test = answer_four()
    knn = answer_five()
    
    # Your code here
    
    return knn.score(X_test, y_test)

answer_eight()
