import pandas as pd

with open('weight-height.csv') as r:
    iqr_file = pd.read_csv(r)
q1 = iqr_file.iloc[:, 1].quantile(0.25)
q3 = iqr_file.iloc[:, 1].quantile(0.75)
print(iqr_file.describe())
iqr_range = q3 - q1
lower_limit_h = q1 - 1.5 * iqr_range
upper_limit_h = q3 + 1.5 * iqr_range
print(lower_limit_h, upper_limit_h)

q1_w = iqr_file.iloc[:, 2].quantile(0.25)
q3_w = iqr_file.iloc[:, 2].quantile(0.75)
iqr_range_w = q3_w - q1_w
lower_limit_w = q1_w - 1.5 * iqr_range_w
upper_limit_w = q3_w + 1.5 * iqr_range_w
print(lower_limit_w, upper_limit_w)
print(iqr_file)
