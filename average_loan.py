import pandas as pd
import matplotlib.pyplot as plt

#import csv files
home_ownership_data = pd.read_csv('home_ownership_data.csv')
loan_data = pd.read_csv('loan_data.csv')

#merge both dataframes
merged = pd.merge(home_ownership_data, loan_data, how='left', on='member_id')
#keeping only the relevant columns
df = merged.loc[ : , ['loan_amnt', 'home_ownership'] ]

#separating based on home ownership and finding the mean of each category
loan_amount = df.groupby(['home_ownership'], as_index=False).mean()

print(loan_amount.head())

#creating a bar graph and setting x,y labels
ax = loan_amount.plot(x ='home_ownership', y='loan_amnt', kind='bar', title='Average Loan Amount per House Ownership', legend=False, rot=0)
ax.set_xlabel('Home Ownership')
ax.set_ylabel('Average Loan Amount ($)')
plt.show()
plt.savefig("loan_amounts.png")

