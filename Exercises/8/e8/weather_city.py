import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import FunctionTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import sys

data_labelled = pd.read_csv(sys.argv[1])
data_unlabelled = pd.read_csv(sys.argv[2])

X = pd.DataFrame()
y = pd.DataFrame()

y['city'] = data_labelled['city']
X = data_labelled
X = X.drop('city', axis=1)

X_unlabelled = data_unlabelled
X_unlabelled = X_unlabelled.drop('city', axis=1)

X_train, X_valid, y_train, y_valid = train_test_split(X, y)

model = make_pipeline(
    StandardScaler(),
    SVC()
    )
model.fit(X_train, y_train.values.ravel())

print('score:', model.score(X_valid, y_valid))


y_prediction = model.predict(X_unlabelled)
labels = pd.DataFrame(y_prediction)

labels.to_csv(sys.argv[3], index=False, header=False)