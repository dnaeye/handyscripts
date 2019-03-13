import pandas as pd
import os
import datetime as dt

path = '/DATA_DIRECTORY'

outfile = "FILENAME.csv"

if os.path.isfile(path + "/" + outfile):
    print("File exists.")
    all_files = pd.read_csv(outfile)
else:
    all_files = pd.DataFrame()

for file in os.listdir(path):
    if file.startswith("FILENAME_PREFIX"):
        if file.endswith(".csv"):
            file_date = str(dt.datetime.strptime(file.split("_")[INDEX_OF_DATESTRING], "%Y%m%d").date())
            df = pd.read_csv(path + "/" + file)
            df['week_start_date'] = file_date
            all_files = all_files.append(df)
            print("Merged " + file + ".")

all_files.to_csv(path + "/" + outfile, index = False)
