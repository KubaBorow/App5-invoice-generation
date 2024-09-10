import pandas as pd
import glob

filepaths = glob.glob("invoices/*.xlsx")
#  Ładowanie danych z plików invoices do programu python, odczyt plików excela
for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name='Sheet 1')
    print(df)
