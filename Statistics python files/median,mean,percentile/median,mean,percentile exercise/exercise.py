import pandas as pd

with open('AB_NYC_2019.csv', encoding='utf8') as r:
    my_file = pd.read_csv(r)
per_night = my_file.price
# print(per_night)
print(per_night.shape)
# print(per_night.describe())
q1 = per_night.quantile(0.25)
q3 = per_night.quantile(0.75)
iqr_range = q3 - q1
lower_limit = q1 - 1.5 * iqr_range
upper_limit = q3 + 1.5 * iqr_range
# print(lower_limit, upper_limit)
no_outlier = per_night[(per_night > lower_limit) & (per_night < upper_limit)]
# print(no_outlier)
print(no_outlier.shape)
# print(no_outlier.describe())
