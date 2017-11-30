from scipy.stats import norm
import numpy as np
import random
import matplotlib.pyplot as plt

# a = [random.normalvariate(0,1) for i in range(100)]
# mean, std = norm.fit(a)

# plt.hist(a, bins = 10, normed=True)

# import ipdb; ipdb.set_trace()
# min_x = np.min(a)
# max_x = np.max(a)
# x = np.linspace(min_x, max_x, 100)
# y = norm.pdf(x, mean, std)
# plt.plot(x, y)
# plt.show()
class RandomPractice:
	def linear_regression(self):
		from sklearn import linear_model
		from sklearn.datasets import load_boston
		from sklearn.metrics import mean_squared_error

		boston = load_boston()
		num_examples = boston["data"].shape[0]

		cutoff = int(0.8*num_examples)

		x_train = boston["data"][:cutoff, :-1]
		y_train = boston["data"][:cutoff, -1]

		x_test = boston["data"][cutoff:, :-1]
		y_test = boston["data"][cutoff:, -1]

		[print(element.shape) for element in [x_train, y_train, x_test, y_test]]

		linear = linear_model.LinearRegression()

		linear.fit(x_train, y_train)
		print("training cost: {}".format(linear.score (x_train, y_train)))

		print("coeff: {} ".format(linear.coef_))
		print("bias: {} ".format(linear.intercept_))

		y_predict = linear.predict(x_test)
		print("predictions: {}".format(y_predict))
		print("test score: {}".format(mean_squared_error(y_predict, y_test)))

class BayesianClassifier:
	def __init__(self):

		pass

	def train(self):

