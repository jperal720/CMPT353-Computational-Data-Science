import pandas as pd
import numpy as np
from skimage.color import rgb2lab
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import FunctionTransformer
import sys
import colour_bayes_hint as cb_hint


# data = pd.read_csv(sys.argv[1])
# X = pd.DataFrame()
# y = pd.DataFrame()
#
# X['R'] = data['R']
# X['G'] = data['G']
# X['B'] = data['B']
#
# #Normalizing Data
# X = X/255
#
# y['Label'] = data['Label']
#
# X_train, X_valid, y_train, y_valid = train_test_split(X, y)
#
# # TODO: build model_rgb to predict y from X.
# model_rgb = GaussianNB()
# model_rgb.fit(X_train, y_train)
#
# # TODO: print model_rgb's accuracy score
# print('scores (RGB):', '\ntrain ->', model_rgb.score(X_train, y_train), '\nvalid ->', model_rgb.score(X_valid, y_valid),'\n')
#
# # TODO: build model_lab to predict y from X by converting to LAB colour first.
# model_lab = make_pipeline(
#     FunctionTransformer(rgb2lab, validate=True),
#     GaussianNB()
# )
#
# model_lab.fit(X_train, y_train)
#
# # TODO: print model_lab's accuracy score
# print('scores (Lab):', '\ntrain ->', model_lab.score(X_train, y_train), '\nvalid ->', model_lab.score(X_valid, y_valid))

data = pd.read_csv(sys.argv[1])

X = pd.DataFrame()
y = pd.DataFrame()

X['R'] = data['R']
X['G'] = data['G']
X['B'] = data['B']

# print(X)
# print(X.apply(lambda x: 0, axis=0, result_type='broadcast')) #Use broadcat to keep the same row-column format of the df


X /= 255

y ['Label'] = data['Label']

#Train_test_split
X_train, X_valid, y_train, y_valid = train_test_split(X, y)

model_rgb = GaussianNB()
model_rgb.fit(X_train, y_train)

print('Train ->', model_rgb.score(X_train, y_train), '\nTest ->', model_rgb.score(X_valid, y_valid))

cb_hint.plot_predictions(model_rgb)

model_lab = make_pipeline(
    FunctionTransformer(rgb2lab, validate=True),
    GaussianNB()
)

model_lab.fit(X_train, y_train)
print('Train ->', model_lab.score(X_train, y_train), '\nTest ->', model_lab.score(X_valid, y_valid))

cb_hint.plot_predictions(model_lab)




# print(X, y)

