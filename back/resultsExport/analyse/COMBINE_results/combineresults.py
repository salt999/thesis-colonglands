import os
import glob
import pandas as pd
os.chdir(r"D:\Universität\Master\MASTER-THESIS\share_online\resultsExport\analyse\COMBINE_results")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
files = ['HEALTHY_FEATURES_comb.csv', 'HG_ADENOMA_FEATURES_comb.csv', 'Hyperplastic_FEATURES_comb.csv',  'LG_ADENOMA_FEATURES_comb.csv']

#combine all files in the list
for i in [0,2,4,6]:
    print(i)
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames[i:i+2]])
    #export to csv
    combined_csv.to_csv( "combined_csv"+str(i)+".csv", index=False, encoding='utf-8-sig')