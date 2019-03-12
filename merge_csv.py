import shutil
import glob

path = r'/Users/USER/Documents/FOLDER'

all_files = glob.glob(path + "/*.csv")
with open(path + '/OUTFILE.csv', 'wb') as outfile:
    for i, fname in enumerate(all_files):
        with open(fname, 'rb') as infile:
            if i != 0:
                infile.readline()
            shutil.copyfileobj(infile, outfile)
            print(fname + " has been imported.")
