# Creating a Series
import pandas as pd

data = [1, 3, 5, 7, 9]
s = pd.Series(data, name="numbers")
print(s)