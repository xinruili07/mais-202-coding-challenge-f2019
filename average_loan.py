import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

home_ownership_data = pd.read_csv('home_ownership_data.csv')
loan_data = pd.read_csv('loan_data.csv')

print(home_ownership_data.head())
print(loan_data.head())

merged = pd.merge(home_ownership_data, loan_data, how='left', on='member_id')
df = merged.loc[ : , ['loan_amnt', 'home_ownership'] ]

print(df.head())

loan_amount = df.groupby(['home_ownership'], as_index=False).mean()

print(loan_amount.head())

ax = loan_amount.plot(x ='home_ownership', y='loan_amnt', kind='bar', title='Average Loan Amount per House Ownership', legend=False)
ax.set_xlabel('Home Ownership')
ax.set_ylabel('Average Loan Amount ($)')
plt.show()
