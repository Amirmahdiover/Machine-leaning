import pandas as pd

with open('number.csv') as r:
    my_csv = pd.read_csv(r)
    q1 = my_csv.rate.quantile()
    q3 = my_csv.rate.quantile(0.75)
    print(q1)
    print(q3)
    iqr = q3 - q1
    # print(iqr)
print(my_csv.describe())
lower_limit = q1 - 1.5 * iqr
upper_limit = q3 + 1.5 * iqr
print(lower_limit)
print(upper_limit)
no_outlier = my_csv[(my_csv > lower_limit) & (my_csv < upper_limit)]
print(no_outlier)
