from sklearn.linear_model import LinearRegression
import numpy as np
from matplotlib import pyplot as plt

#Creating Linear Regression Model
model = LinearRegression(fit_intercept=False)

#Training Data
x = [15, 2, -19, 5]
y = [2, 3, 4, 3]

X = np.stack([x], axis=1)
y = np.stack([y], axis=1)

#Setting up the intercept manually
X_with = np.concatenate([np.ones(X.shape), X], axis=1)
# print(X_with, '\n')

model.fit(X_with, y)
# print(model.coef_)

#Polynomial Regression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

poly = PolynomialFeatures(degree=3, include_bias=True)

y = [23, 32, 455]
X_poly = np.array([[2], [3], [4]])

poly.fit_transform(X)

model = LinearRegression(fit_intercept=False)
model.fit(X_poly, y)

print(model.coef_)

#Making a pipeline model
model = make_pipeline(
    PolynomialFeatures(degree=3, include_bias=True),
    LinearRegression(fit_intercept=False)
) #This model takes our x values, creates polynomial features, and does a linear fit on them

y = [2, 3, 4, 3]
y = np.stack([y], axis=1)

model.fit(X, y)
plt.plot(X_poly[:, 0], model.predict(X_poly), 'r.-')
# plt.show()

#Pipeline example:
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import SimpleImputer

model = make_pipeline(
    SimpleImputer(strategy='mean'),     #input missing values
    MinMaxScaler(),     #scale each feature to 0-1
    PolynomialFeatures(degree=3, include_bias=True),
    LinearRegression(fit_intercept=False)
)

#Creating a custom basis function for linear regression using pipeline model
def sigmoid_basis(X):  # [[x]] -> [[1, x, 1/(1 + e^x)]]
    one = np.ones(X.shape)
    sigmoid = 1 / (1 + np.exp(X))
    return np.concatenate((one, X, sigmoid), axis=1)

from sklearn.preprocessing import FunctionTransformer
model = make_pipeline(
    FunctionTransformer(sigmoid_basis, validate=True),
    LinearRegression(fit_intercept=False)
)

model.fit(X, y)
print(model.named_steps['linearregression'].coef_)
# plt.plot(model.predict(X_poly), 'r-')

###
###Splitting data
###
from sklearn.model_selection import train_test_split

#data set
x = [15, 2, -19, 5, 202, 22, 1, 3, 4, 5, 6, 7, 33, 10, 2, 200, 32, 12]
y = [2, 3, 4, 3, 3 ,4 ,5 , 5, 10, 2, -1, 22, 134, 22, 55, -1, 0, 10]

X = np.stack([x], axis=1)
y = np.stack([y], axis=1)

X_train, X_valid, y_train, y_valid = train_test_split(X, y)

def score_polyfit(n):
    model = make_pipeline(
        PolynomialFeatures(degree=n, include_bias=True),
        LinearRegression(fit_intercept=False)
    )
    model.fit(X_train, y_train)
    print('n=%i: score(train)=%.5g, score(valid)=%.5g' % (n, model.score(X_train, y_train), model.score(X_valid, y_valid)))
    plt.plot(X_train, y_train, 'r-')
    plt.plot(X_train[:, 0], model.predict(X_train), 'b.')
    plt.plot(X_valid[:, 0], model.predict(X_valid), 'g.')
    plt.show()

print()
score_polyfit(1)
score_polyfit(5)
score_polyfit(9)
score_polyfit(13)
score_polyfit(17)