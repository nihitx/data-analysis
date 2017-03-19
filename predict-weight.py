import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

dataframe = pd.read_fwf('data/brain_body.txt')
x_values = dataframe[['Brain']]
y_values = dataframe[['Body']]

#train the model
regr = linear_model.LinearRegression()
regr.fit(x_values, y_values)

#visualize the result
plt.scatter(x_values, y_values)
plt.plot(x_values, regr.predict(x_values))
plt.show()