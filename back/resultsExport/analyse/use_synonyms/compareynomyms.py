import os
import csv
from csv import DictReader
import pandas as pd
import re

filename= '\healthy_combined_csv0 - Kopie' #results-survey562626_v2'
folder = os.getcwd() + "\\"
# extendfolder = filename
resultfiles = ['HEALTHY_FEATURES', 'Hyperplastic_FEATURES', 'LG_ADENOMA_FEATURES', 'HG_ADENOMA_FEATURES']

folder = r"D:\Universität\Master\MASTER-THESIS\share_online\resultsExport\analyse\use_synonyms"
df = pd.read_csv(folder + filename + '.csv')
# HEALTHY_FEATURES = df.HEALTHY_FEATURES
syn_results = []
woxicon = []
# print(df.HEALTHY_FEATURES)
# print(df['SYNONYMS-woxikon'])

# for row in df['SYNONYMS-woxikon']:
#     print('k',type(row))

# healthy = [h.split() for h in df.HEALTHY_FEATURES]
# p=[str(m).replace('[', '') for m in df['SYNONYMS-woxikon']]
# p=[str(m).replace('[', '') for m in p]
# [woxicon.append(f) for f in p if len(f)>2]


# cleanedW = str(df['SYNONYMS-woxikon']).replace('[', '')
# [str(m).replace('[', '') for m in df['SYNONYMS-woxikon']]

# original_string = str(df['SYNONYMS-woxikon'])

# characters_to_remove = "[]"


# pattern = "[" + characters_to_remove + "]"

# pattern = "[" + [] + "]"

# new_string = re.sub(pattern, "", original_string)


# print(new_string)
# m = [ re.sub(pattern, "", original_string) for original_string in df['SYNONYMS-woxikon'] if isinstance(original_string, str)]



for i in range(len(df.HEALTHY_FEATURES)):
    # print(i)
    # print('FEATURE', df.HEALTHY_FEATURES[i])
    for h in df.HEALTHY_FEATURES[i].split():
        #print(h)
        if h in df.HEALTHY_FEATURES:
            print(h, ' in sich')
    if isinstance(df['SYNONYMS-woxikon'][i],str):
        for h in df['SYNONYMS-woxikon'][i].split():
            # synonymsPerword = str(h).replace('[', '')
            # synonymsPerword = str(synonymsPerword).replace(']', '')
            # print('1', synonymsPerword)
            # print('2', h)
            # # for synonyms in synonymsPerword:
            if h in df['SYNONYMS-woxikon']:
                print('3',h)
                wort=re.findall(h,str(woxicon))
                print('4', wort, ' in woxicon')



#         for m in l:
#             print('l', m)
#             if df.HEALTHY_FEATURES[i] in m:
#                 print(df.HEALTHY_FEATURES[i], 'in woxicon')
    # dict_Woxicon = []
# [dict_Woxicon.append(m) for m in df['SYNONYMS-woxikon']]
# dict_theseus  = []
# [dict_theseus.apppend(m) for m in df['SYNONYMS-thesaurus']]
# print(type(list(HEALTHY_FEATURES)))


# with open(folder + filename + '.csv', 'r', encoding='utf8') as read_obj:
#     csv_dict_reader = DictReader(read_obj)

#     for row in csv_dict_reader:
#         print(type(row['SYNONYMS-woxikon']))
#         content = list(row[i] for i in ['c'])
        #print(content)
    # for row in csv_dict_reader:
    #     print(row['HEALTHY_FEATURES'])
    #     if row['HEALTHY_FEATURES'] in csv_dict_reader['HEALTHY_FEATURES']:
    #         print(row['HEALTHY_FEATURES'])

import pandas as pd
df = pd.read_csv(folder + filename + '.csv')
saved_column = df.HEALTHY_FEATURES
print(saved_column[0])