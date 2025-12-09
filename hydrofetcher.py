import pandas as pd
import openpyxl

data = pd.read_csv('hydrostatics_table1.csv', usecols=['Draft(E)', 'DISP', 'LCF', 'TPC', 'MTC'])
 


mask = (data["Draft(E)"].apply(lambda x: round(x * 100) % 20 == 0))   
df_even = data[mask].reset_index(drop=True)

df_even.to_excel("hydrostatics_final.xlsx", index=False)
print("Perfect.")
