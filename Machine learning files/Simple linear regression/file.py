import pandas as pd
from sklearn.model_selection import train_test_split

# data preprocessing
# ----------------
with open('Salary_Data.csv') as r:
    my_csv = pd.read_csv(r)

x = my_csv.iloc[:, 0].values
y = my_csv.iloc[:, -1].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
