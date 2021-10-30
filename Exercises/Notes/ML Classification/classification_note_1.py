"""
There are many ways to model classifications, all follow a similar and basic procedure:

model = SomeClassifierModel(...)
model.fit(X_train, y_train)
y_predicted = model.predict(X_test)
somehow_compare_results = (y_test, y_predicted)
"""

from sklearn.naive_bayes import GaussianNB

X_train, X_valid = [] #Fill data set
y_train, y_valid = [] #Fill data set

model = GaussianNB()
model.fit(X_train, y_train)

y_predicted = model.predict(y_valid)

print(model.theta_) #Sample means for each category in each dimension
print(model.sigma_) #Sample variances for each category in each dimension

from sklearn.metrics import classification_report
print(classification_report(y_valid, y_predicted))   #Will display a classification report, precision can be found here

"""
Example of creating a Prior:

model = GaussaianNB(priors=[1/7, 3/7, 3/7]) #By default, Priors are calculated from training data, so unless we know more than that, specifying explicitly won't help
model.fit(X_train, y_train)
print(model.score(X_valid, y_valid)

"""

"""
Adding a transform to a pipeline and training it.

def de_skew(X):
    X0 = X[:, 0] - X[:, 1]
    X1 = X[:, 1]
    
    return np.stack([X0, X1], axis=1)
    
model = make_pipeline(
    FunctionTransformer(de_skew, validate=True),
    GaussianNB()
)

model.fit(X_train, y_train)
"""