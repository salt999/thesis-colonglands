#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
from csv import DictReader
import os
import json, requests
import time
import re

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






filename= 'results-survey1234_100421'
resultfiles = ['HEALTHY_FEATURES', 'Hyperplastic_FEATURES', 'LG_ADENOMA_FEATURES', 'HG_ADENOMA_FEATURES']
healthylist = []
hyperlist = []
LGAlist =[]
HGAlist = []
count = 0
# resultfiles = [element + str(filename[-6:]) for element in resultfiles]
folder = os.getcwd() + "\\test\\"
# 'D:/Universität/Master/MASTER-THESIS/share_online/resultsExport/analyse/test/'
extendfolder = str(filename[-6:])
#resultfiles = [folder + element + extendfolder for element in resultfiles_]
# fieldnames = ['HEALTHY_FEATURES', 'Hyperplastic_FEATURES',]


with open(filename + '.csv', 'r', encoding='utf8') as read_obj:
    csv_dict_reader = DictReader(read_obj)

    for row in csv_dict_reader:
    #print('edu'), row[]
        print('AGE: ', row['G05Q17'])
        # if row['G05Q17']:
        #     count += 1

        if row[LANGUAGE]:
            print(row[LANGUAGE])
        #print(row)
        # for id in HEALTHY_FEATURES:
        #     print(str(row[id]))
        if row[LANGUAGE] == 'de':
            if row['G05Q17']:
                count += 1
            for id in range(len(HEALTHY_FEATURES)):
                if len(row[HEALTHY_FEATURES[id]]) > 1:
                    healthylist.append(row[HEALTHY_FEATURES[id]])
                if len(row[Hyperplastic_FEATURES[id]]) > 1:
                    hyperlist.append(row[Hyperplastic_FEATURES[id]])
                if len(row[LG_ADENOMA_FEATURES[id]]) > 1:
                    LGAlist.append(row[LG_ADENOMA_FEATURES[id]])
                if len(row[HG_ADENOMA_FEATURES[id]]) > 1:
                    HGAlist.append(row[HG_ADENOMA_FEATURES[id]])

    ALL = [healthylist, hyperlist, LGAlist, HGAlist]
    #print(ALL)

##get OBJECT if avail
OBJECTS_LUMEN = ['LUMEN']
OBJECTS_DRÜSE = ['DRÜSE', 'GLAND', 'BLUME']
OBJECT_ZELLE = ['ZELLE', 'EPITHEL', 'BECHER', 'CELL', 'GOBLET', 'ZELL']
OBJECT_STROMA = ['STROMA']

object_dict = {}
for enum, result in enumerate(ALL):
    for res in result:    
        object_dict[res] = []
        for obj in OBJECTS_DRÜSE:
            if obj in res.upper():
                object_dict[res].append('DRÜSE')
        for obj in OBJECTS_LUMEN:
            if obj in res.upper():
                object_dict[res].append('LUMEN')
        for obj in OBJECT_ZELLE:
            if obj in res.upper():
                object_dict[res].append('ZELLE')
        for obj in OBJECT_STROMA:
            if obj in res.upper():
                object_dict[res].append('STROMA')

# print(object_dict)    


### get synonyme  openthesueus
def get_synonyms(term):
    d = json.loads(requests.get("http://www.openthesaurus.de/synonyme/search",
                                params={"q": term, "format": "application/json", "similar":"false", "supersynsets":"false"}).text)
    if d["synsets"]:
        return [o["term"] for o in d["synsets"][0]["terms"]]
    else:
        return ''

object_syno1 = {}
for enum, result in enumerate(ALL):
    for res in result:
        object_syno1[res] = []
        for h in res.split():
            time.sleep(1)
            object_syno1[res].append(get_synonyms(h))

### get synonyme  woxicon
url = 'http://synonyme.woxikon.de/synonyme/'
urlsuffix = '.php'
object_syno2 = {}
for enum, result in enumerate(ALL):
    for res in result:
        object_syno2[res] = []
        #print(object_syno2)

        for searchQuery in res.split():
            time.sleep(1)
            d = requests.get(url + searchQuery + urlsuffix).text
            stripped = re.sub('<[^<]+?>', '', d)

            wort=re.findall(r'Bedeutung: (\w+)',str(stripped))
            # print(searchQuery, ' : ',  wort)
            object_syno2[res].append(wort)



####fill file
for enum, result in enumerate(ALL):
    print(folder + resultfiles[enum] + extendfolder)
    #print(result)
    with open(folder + resultfiles[enum] + extendfolder + '.csv', mode='w', encoding='utf8', newline ='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=[resultfiles[enum],"", "OBJEKT" ,"","SYNONYMS-woxikon","", "SYNONYMS-thesaurus", "HIERARCHY"])
        writer.writeheader()
        #writer.writerow(result)
        for res in result:
            writer.writerow({resultfiles[enum]: res, "OBJEKT": object_dict[res], "SYNONYMS-thesaurus": object_syno1[res], "SYNONYMS-woxikon": object_syno2[res]})
            # if 'lumen' in res.lower():
            #     writer.writerow({resultfiles[enum]: res, "OBJEKT": 'LUMEN'})
            # elif 'drüse' in res.lower():
            #     writer.writerow({resultfiles[enum]: res, "OBJEKT": 'DRÜSE'})#
            # elif 'zelle' or 'cell' or 'epithel' or 'becher' in res.lower():
            #     writer.writerow({resultfiles[enum]: res, "OBJEKT": 'ZELLE'})
            # else:
            #     writer.writerow({resultfiles[enum]: res})
                        #writer.writerow(res)

        writer.writerow({resultfiles[enum]: '    '})
        writer.writerow({resultfiles[enum]: 'info:'})
        writer.writerow({resultfiles[enum]: 'number of survery part:' + str(count)})


