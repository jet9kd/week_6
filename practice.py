# %%
import pandas as pd
import numpy as np
import sklearn as sk
# %%

# Loading Data
# Merging Data
# sklearn

# load the data, column titles in salary in first row
salary_data = pd.read_csv("2025_salaries.csv", header=1, encoding="latin-1")
stats = pd.read_csv("nba_2025.txt")
# %%
salary_data.head()

stats = pd.read_csv("nba_2025.txt", sep=",", encoding='latin-1')

# %%
help(pd.merge)

# %%
merged_data = pd.merge(salary_data, stats, on='Player')
merged_data.head()

# %%
duplicates = merged_data[merged_data.duplicated(subset='Player', keep=False)]
print(duplicates)

# %%
# Sklearn
# 1. Create instance of model
# 2. Fit model to the data
# 3. Make predictions using model
# 4. evaluate model's performance

# the most variance, helps you separate out the data (separating good and bad players)