import pandas as pd
#get input
expense_df = pd.read_csv('expense-report.csv')

#cartesian join
expense_df.insert(1,'key', 1)
expense2_df = expense_df.copy()
expense3_df = expense_df.copy()

cartesian_df = pd.merge(expense_df,expense2_df, on='key')
cartesian2_df = pd.merge(cartesian_df, expense3_df, on='key')

# find two values that add up to 2020
result_df = cartesian2_df[(cartesian2_df.value_x + cartesian2_df.value_y + cartesian2_df.value) == 2020]

#print out the first row (since there will be duplicates
print (result_df.iloc[0].value_x * result_df.iloc[0].value_y * result_df.iloc[0].value)

