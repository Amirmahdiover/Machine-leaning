import pandas as pd
from sklearn.preprocessing import StandardScaler

std = StandardScaler()
with open('age&income.csv') as r:
    my_csv = pd.read_csv(r)
new_std = std.fit_transform(my_csv)
print(new_std)