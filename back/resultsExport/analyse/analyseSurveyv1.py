#!/usr/bin/env python
# -*- coding: utf-8 -*-


### analyse survey results 


LASTPAGE = 'lastpage'
LANGUAGE = 'startlanguage'
PATHOLOGIST= 'G05Q18[SQ01]'
PATHOLOGIST_comment='G05Q18[SQ01comment]'
DOCTOR='G05Q18[SQ02]'
DOCTOR_comment='G05Q18[SQ02comment]'
MED_STUD='G05Q18[SQ03]'
MED_STUD_comment='G05Q18[SQ03comment]'
EDU_OTHER = 'G05Q18[SQ04]'
EDU_OTHER_comment = 'G05Q18[SQ04comment]'

AGE='G05Q17'

VOCAB_OK = 'G07Q18'

HEALTHY_TF_1 = 'G01Q01' #drüse rund
HEALTHY_TF_2 = 'G01Q02' #lumen unförmig
HEALTHY_FEATURES = ['G01Q03[SQ01_SQ01]','G01Q03[SQ01_SQ02]','G01Q03[SQ01_SQ03]','G01Q03[SQ02_SQ01]','G01Q03[SQ02_SQ02]','G01Q03[SQ02_SQ03]','G01Q03[SQ03_SQ01]','G01Q03[SQ03_SQ02]','G01Q03[SQ03_SQ03]']

Hyperplastic_TF_1 = 'G02Q01' #drüse rund
Hyperplastic_TF_2 = 'G02Q02' #lumen unförmig
Hyperplastic_FEATURES = ['G02Q03[SQ01_SQ01]','G02Q03[SQ01_SQ02]','G02Q03[SQ01_SQ03]','G02Q03[SQ02_SQ01]','G02Q03[SQ02_SQ02]','G02Q03[SQ02_SQ03]','G02Q03[SQ03_SQ01]','G02Q03[SQ03_SQ02]','G02Q03[SQ03_SQ03]']

LG_ADENOMA_TF_1 = 'G03Q01' #Nuclei lila
LG_ADENOMA_TF_2 = 'G03Q02' #lumen unförmig
LG_ADENOMA_FEATURES = ['G03Q03[SQ01_SQ01]','G03Q03[SQ01_SQ02]','G03Q03[SQ01_SQ03]','G03Q03[SQ02_SQ01]','G03Q03[SQ02_SQ02]','G03Q03[SQ02_SQ03]','G03Q03[SQ03_SQ01]','G03Q03[SQ03_SQ02]','G03Q03[SQ03_SQ03]']

HG_ADENOMA_TF_1 = 'G04Q01' #drüse rund
HG_ADENOMA_TF_2 = 'G04Q02' #lumen unförmig
HG_ADENOMA_FEATURES = ['G04Q03[SQ01_SQ01]','G04Q03[SQ01_SQ02]','G04Q03[SQ01_SQ03]','G04Q03[SQ02_SQ01]','G04Q03[SQ02_SQ02]','G04Q03[SQ02_SQ03]','G04Q03[SQ03_SQ01]','G04Q03[SQ03_SQ02]','G04Q03[SQ03_SQ03]']

END_COMMENT='G08Q19'


import csv
from csv import DictReader

filename= 'results-survey1234_100421'

with open(filename + '.csv', 'r', encoding='utf8') as read_obj:
    csv_dict_reader = DictReader(read_obj)
    with open('healthy_gland_features' + str(filename[-6:]) + '.csv', mode='w', encoding='utf8') as csv_file:
        fieldnames = ['HEALTHY_FEATURES', 'Hyperplastic_FEATURES']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
    

        
        for row in csv_dict_reader:
            #print('edu'), row[]
            print('AGE: ', row['G05Q17'])
            # for id in HEALTHY_FEATURES:
            #     print(str(row[id]))

            for id in range(len(HEALTHY_FEATURES)):
                if row[HEALTHY_FEATURES[id]] != '':
                    writer.writerow({'HEALTHY_FEATURES': row[HEALTHY_FEATURES[id]]})
                if row[Hyperplastic_FEATURES[id]] != '':
                    writer.writerow({'Hyperplastic_FEATURES': row[Hyperplastic_FEATURES[id]]})



            # for id in Hyperplastic_FEATURES:
            #     if row[id] != '':
            #         writer.writerow({'Hyperplastic_FEATURES': row[id]})
        # for id in Hyperplastic_FEATURES:
        #     writer.writerow({'Hyperplastic_FEATURES': row[id]})

#import pandas as pd
#df = pd.read_csv('results-survey562626.csv')


#write

# with open('healthy_gland_features.csv', mode='w') as csv_file:
#     fieldnames = ['HEALTHY_FEATURES']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

#     writer.writeheader()
#     for id in HEALTHY_FEATURES:
#         writer.writerow({'HEALTHY_FEATURES': row[id]})
