# Literally nothing to see here
# Internet Inspired Codes
# Compiled by Krypto Kiddo

import numpy as np
import pandas as pd
df = pd.read_csv("/content/churn.csv")
df.shape
(10000,14)
df.columns
Index(['RowNumber', 'CustomerId', 'Surname', 'CreditScore', 'Geography', 'Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard','IsActiveMember','EstimatedSalary', 'Exited'], dtype='object')
df.drop(['RowNumber', 'CustomerId', 'Surname', 'CreditScore'], axis=1, inplace=True)
df.shape
# (10000,10)
df_spec = pd.read_csv("/content/churn.csv", usecols=['Gender', 'Age', 'Tenure', 'Balance'])
df_spec.head()
df_partial = pd.read_csv("/content/churn.csv", nrows=5000)
df_partial.shape
# (5000,14)
df_sample = df.sample(n=1000)
df_sample.shape
# (1000,10)
df_sample2 = df.sample(frac=0.1)
df_sample2.shape
# (1000,10)
df.isna().sum()
missing_index = np.random.randint(10000, size=20)
df.loc[missing_index, ['Balance','Geography']] = np.nan
df.iloc[missing_index, -1] = np.nan
mode = df['Geography'].value_counts().index[0]
df['Geography'].fillna(value=mode, inplace=True)
avg = df['Balance'].mean()
df['Balance'].fillna(value=avg, inplace=True)
df.dropna(axis=0, how='any', inplace=True)
df.isna().sum().sum()
# 0
france_churn = df[(df.Geography == 'France') & (df.Exited == 1)]
france_churn.Geography.value_counts()
# France    808
df2 = df.query('80000 < Balance < 100000')
df2['Balance'].plot(kind='hist', figsize=(8,5))
df[df['Tenure'].isin([4,6,9,10])][:3]
df[['Geography','Gender','Exited']].groupby(['Geography','Gender']).mean()
df[['Geography','Gender','Exited']].groupby(['Geography','Gender']).agg(['mean','count'])
df_summary = df[['Geography','Exited','Balance']].groupby('Geography')\
.agg({'Exited':'sum', 'Balance':'mean'})
df_summary.rename(columns={'Exited':'# of churned customers', 'Balance':'Average Balance of Customers'},inplace=True)
print(df_summary)
df_summary = df[['Geography','Exited','Balance']].groupby('Geography')\
.agg(
 Number_of_churned_customers = pd.NamedAgg('Exited', 'Sum'),
 Average_balance_of_customers = pd.NamedAgg('Balance', 'Mean')
)
df_new = df[['Geography','Exited','Balance']]\
.groupby(['Geography','Exited']).mean().reset_index()
print(df_new)
df[['Geography','Exited','Balance']].sample(n=6).reset_index()
df[['Geography','Exited','Balance']]\
.sample(n=6).reset_index(drop=True)
df_new.set_index('Geography')
