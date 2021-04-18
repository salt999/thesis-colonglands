from limesurvey_keywords import *
import os
import csv
from csv import DictReader

filename= 'results-survey1234_130421' #results-survey562626_v2'
folder = os.getcwd() + "\\finoutput\\"
extendfolder = filename


### preparation for saving
resultfiles = ['HEALTHY_FEATURES', 'Hyperplastic_FEATURES', 'LG_ADENOMA_FEATURES', 'HG_ADENOMA_FEATURES']

for file in resultfiles:
   exec("%s_dict = {file:[], 'ID':[],'AGE':[], 'job':[], 'RF1': [],'RF2': []}" % (file))
    # res.append(exec("%s_dict" % (file)))

resultdicts = [HEALTHY_FEATURES_dict, Hyperplastic_FEATURES_dict, LG_ADENOMA_FEATURES_dict, HG_ADENOMA_FEATURES_dict]



### get info from exported result survey
def getJOB(row):
    jobs = ['pathologe', 'Arzt', 'MedStudent','' ]
    further_jobdetail = [PATHOLOGIST_comment, DOCTOR_comment,MED_STUD_comment, EDU_OTHER_comment]
    for enum,job in enumerate([PATHOLOGIST, DOCTOR,MED_STUD, EDU_OTHER]):
        #print(row[job])
        if row[job] == 'Ja':
            joblist = jobs[enum]+'  '+str(row[further_jobdetail[enum]])
            # print(joblist)
            return joblist 

print(RF1)
with open(filename + '.csv', 'r', encoding='utf8') as read_obj:
    csv_dict_reader = DictReader(read_obj)

    for row in csv_dict_reader:
        if row[LANGUAGE] == 'de':
            age = row[AGE]
            job = getJOB(row)

            for enum,features in enumerate([HEALTHY_FEATURES,Hyperplastic_FEATURES,LG_ADENOMA_FEATURES,HG_ADENOMA_FEATURES]):
                print(enum)
                rf1 = row[RF1[enum]]
                rf2 = row[RF2[enum]]

                # print(rf1)
                for id in range(len(features)):
                    if len(row[features[id]]) > 1:
                        resultdicts[enum][str(resultfiles[enum])].append(row[features[id]])
                        resultdicts[enum]['ID'].append(row['\ufeff"id"'])
                        resultdicts[enum]['AGE'].append(age)
                        resultdicts[enum]['job'].append(job)
                        resultdicts[enum]['RF1'].append(rf1)
                        resultdicts[enum]['RF2'].append(rf2)

# print(HEALTHY_FEATURES_dict)
# print(HEALTHY_FEATURES_dict['ID'])


### analyse

def getOBJECT(res):
    OBJECTS_LUMEN = ['LUMEN']
    OBJECTS_DRÜSE = ['DRÜSE','Druese', 'GLAND', 'BLUME']
    OBJECT_ZELLE = ['ZELLE', 'EPITHEL','epith' 'BECHER', 'CELL', 'GOBLET', 'SEKRET']#sekret, mucin
    OBJECT_STROMA = ['STROMA']
    OBJECT_ZELLKERN = ['ZELLKERN','KERN','NUCLEI','NUKLEI','NUCL']

    # ALL_OBJEKTS_LIST = ["OBJECTS_LUMEN","OBJECTS_DRÜSE", "OBJECT_ZELLE", "OBJECT_STROMA", "OBJECT_ZELLKERN"]

    object_dict = {}
    # for enum, result in enumerate(resultdicts):
    #     for en,res in enumerate(resultdicts[enum][str(resultfiles[enum])]):    
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
    for obj in OBJECT_ZELLKERN:
        if obj in res.upper():
            object_dict[res].append('ZELLKERN')
    #print(object_dict)
    return object_dict

richigFalsch1 = ["DRÜSE RUND","DRÜSE RUND","NUCLEI LILA", "DRÜSE RUND"]

print(resultdicts[enum]['RF1'])

for enum, result in enumerate(resultdicts):
    print(folder + resultfiles[enum] + extendfolder)
    #print(result)
    with open(folder + resultfiles[enum] + extendfolder + '.csv', mode='w', encoding='utf8', newline ='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["ID", resultfiles[enum],"JOB","AGE",richigFalsch1[enum],"LUMEN UNFÖRMIG","", "OBJEKT zuordnung" ,"Kategorie"])
        writer.writeheader()
        #writer.writerow(result)
        for en,res in enumerate(resultdicts[enum][str(resultfiles[enum])]):
            object_dict = getOBJECT(res)
            writer.writerow({resultfiles[enum]: res, "ID":resultdicts[enum]['ID'][en],"JOB": resultdicts[enum]['job'][en] ,"AGE": resultdicts[enum]['AGE'][en],richigFalsch1[enum]: resultdicts[enum]['RF1'][en], "LUMEN UNFÖRMIG": resultdicts[enum]['RF2'][en], "OBJEKT zuordnung": object_dict[res]}) 