import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

with open('Salary_Data.csv') as r:
    my_csv = pd.read_csv(r)
x = my_csv.iloc[:, 0:1]
y = my_csv.iloc[:, -1]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

regressor = LinearRegression()
regressor.fit(x_train, y_train)
y_pred = regressor.predict(x_test)
print(y_pred)
plt.scatter(x_train, y_train, color='red')
plt.plot(x_train, regressor.predict(x_train), color='blue')
# plt.title('Salary vs Experience (Training set)')
# plt.xlabel('Experience')
# plt.ylabel('Salary')
# plt.show()
# test set visualisation

plt.scatter(x_test, y_test,color='red')
plt.scatter([2,2,4,5],[32,21,43,33],color='blue')
plt.title('Salary vs Experience(Test set)')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.legend()
plt.show()