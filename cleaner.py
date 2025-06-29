import pandas as pd
import re

with open("data.txt", "r") as f:
    lines = f.readlines()

clean_data = []

for i, line in enumerate(lines):
    parts = re.split(r'[\s,]+', line.strip())
    
    if i == 0 and not parts[0].replace('.', '', 1).isdigit():
        continue

    if len(parts) >= 9:
        try:
            draft = float(parts[0])        
            disp = float(parts[1])         
            tpc = float(parts[2])          
            lcf = float(parts[5])          
            mtc = float(parts[3])         
            clean_data.append([draft, disp, lcf, tpc, mtc])
        except ValueError:
            print(f"error happened")
    else:
        print(f"error happened")


if clean_data:
    df = pd.DataFrame(clean_data, columns=["Draft(E)", "TPC", "MTC"])
    df.to_csv("hydrostatics_table.csv", index=False)
    print("Saved to hydrostatics_table.csv")
else:
    print("no rows.")
