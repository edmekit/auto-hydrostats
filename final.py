import pandas as pd

disp = pd.read_csv("hydrostatics_table.csv")
mtc = pd.read_csv("hydrostatics_table1.csv")

merge = pd.merge(disp, mtc, on="Draft(E)", how="inner")


merge = merge[["Draft(E)", "DISP(E)", "LCF", "TPC", "MTC"]]

merge.to_csv("hydrostatics_FINAL.csv", index=False)
