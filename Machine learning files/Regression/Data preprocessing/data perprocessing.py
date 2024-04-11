import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import numpy

with open('Data.csv') as r:
    data_csv = pd.read_csv(r)

x = data_csv.iloc[:, :-1].values
y = data_csv.iloc[:, -1].values
# print(x)
print(y)
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])
# print(x)
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
x=ct.fit_transform(x)
print(x)
