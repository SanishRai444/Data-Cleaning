import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('./fifa_data.csv')

print(data['Release Clause'].head(20))