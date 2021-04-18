from limesurvey_keywords import *
import os
import csv
from csv import DictReader

filename= 'results-survey562626_v2' #'results-survey1234_130421' 
folder = os.getcwd() + "\\finoutput\\"
extendfolder = filename


### preparation for saving
resultfiles = ['HEALTHY_FEATURES', 'Hyperplastic_FEATURES', 'LG_ADENOMA_FEATURES', 'HG_ADENOMA_FEATURES']

for file in resultfiles:
   exec("%s_dict = {file:[], 'ID':[],'AGE':[], 'job':[]}" % (file))
    # res.append(exec("%s_dict" % (file)))

resultdicts = [HEALTHY_FEATURES_dict, Hyperplastic_FEATURES_dict, LG_ADENOMA_FEATURES_dict, HG_ADENOMA_FEATURES_dict]



### get info from exported result survey
def getJOB(row):
    jobs = ['pathologe', 'Arzt', 'MedStudent','' ]
    further_jobdetail = [PATHOLOGIST_comment, DOCTOR_comment,MED_STUD_comment]
    for enum,job in enumerate([PATHOLOGIST, DOCTOR,MED_STUD]):
        print(row[job])
        if row[job] == 'Ja':
            joblist = jobs[enum]+'  '+str(row[further_jobdetail[enum]])
            print(joblist)
            return joblist 

with open(filename + '.csv', 'r', encoding='utf8') as read_obj:
    csv_dict_reader = DictReader(read_obj)

    for row in csv_dict_reader:
        # if row[LANGUAGE] == 'de':
        #age = row[AGE]
        job = getJOB(row)
        for enum,features in enumerate([HEALTHY_FEATURES,Hyperplastic_FEATURES,LG_ADENOMA_FEATURES,HG_ADENOMA_FEATURES]):
            for id in range(len(features)):
                if len(row[features[id]]) > 1:
                    resultdicts[enum][str(resultfiles[enum])].append(row[features[id]])
                    resultdicts[enum]['ID'].append(row['\ufeff"id"'])
                    #resultdicts[enum]['AGE'].append(age)
                    resultdicts[enum]['job'].append(job)

# print(HEALTHY_FEATURES_dict)
# print(HEALTHY_FEATURES_dict['ID'])



for enum, result in enumerate(resultdicts):
    print(folder + resultfiles[enum] + extendfolder)
    #print(result)
    with open(folder + resultfiles[enum] + extendfolder + '.csv', mode='w', encoding='utf8', newline ='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["ID", resultfiles[enum],"JOB","AGE","", "OBJEKT zuordnung" ,"BAUM STRUKTUR", "","SYNONYMS-woxikon","", "SYNONYMS-thesaurus", "HIERARCHY"])
        writer.writeheader()
        #writer.writerow(result)
        for en,res in enumerate(resultdicts[enum][str(resultfiles[enum])]):
            writer.writerow({resultfiles[enum]: res, "ID":resultdicts[enum]['ID'][en],"JOB": resultdicts[enum]['job'][en] ,"AGE": [],  "OBJEKT zuordnung": []}) 