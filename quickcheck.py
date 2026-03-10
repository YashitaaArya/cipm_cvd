from tabpfn import TabPFNClassifier
import pandas as pd
print("TabPFN imported successfully")
df= pd.read_csv("data/framingham_tabpfn_ready.csv")
print(df.head())

# Print just the column names to check the order
print(df.columns.tolist())