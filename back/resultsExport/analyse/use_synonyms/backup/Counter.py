from collections import Counter
import pandas as pd
import re

###FILES
pathinput = r'HEALTHY_FEATURES130421-Kopie.csv'
path_stopwords = "stopwords.csv"

# ###count of all words
# with open(pathinput) as f:
#                p = Counter(f.read().split())
#                #print(p)

# print('Most common:')
# for letter, count in p.most_common(12):
#     print(letter, count)

### collect stop words
df = pd.read_csv(pathinput)
stopwords =  pd.read_csv(path_stopwords)
stopwords = list(stopwords.STOP)

## clean words
ch = {}
healthy_list = list(df.HEALTHY_FEATURES)
cleanedwords_healthy = []
for healty in healthy_list:
    # print('WORD: ', healty)
    cleanedwords_healthy += [healthyword for healthyword in healty.split() if healthyword not in stopwords]
    m = [healthyword for healthyword in healty.split() if healthyword not in stopwords]
    ch[str(healty)] = m

### count cleaned words
hc = Counter(cleanedwords_healthy)
for letter, count in hc.most_common(10):
    print('cleanedwords_healthy count  : ', letter, count)

sych ={}
synon = list(df['SYNONYMS-woxikon'])
cleanedwords_syno = []
for nr,sy in enumerate(synon):
    # print('WORD: ', sy)
    if isinstance(sy, str):
        #[print('s',s) for s in sy.split() if str(s).replace("'", '') not in stopwords]
        cleanedwords_syno += [s for s in sy.split() if str(s).replace("'", '') not in stopwords]
        m = [s for s in sy.split() if str(s).replace("'", '') not in stopwords]
        sych[str(df.HEALTHY_FEATURES[nr])] = m

syc = Counter(cleanedwords_syno)
for letter, count in syc.most_common(10):
    print(' cleanedwords_syno count:  ', letter, count)


thsych ={}
synon = list(df['SYNONYMS-thesaurus'])
cleanedwords_thsych = []
for nr,sy in enumerate(synon):
    # print('WORD: ', sy)
    if isinstance(sy, str):
        #[print('s',s) for s in sy.split() if str(s).replace("'", '') not in stopwords]
        cleanedwords_thsych += [s for s in sy.split() if str(s).replace("'", '') not in stopwords]
        m = [s for s in sy.split() if str(s).replace("'", '') not in stopwords]
        thsych[str(df.HEALTHY_FEATURES[nr])] = m

thsyc = Counter(cleanedwords_syno)
for letter, count in thsyc.most_common(10):
    print(' cleanedwords_thsyno count:  ', letter, count)

# c = Counter(df['SYNONYMS-woxikon'])
# for letter, count in c.most_common(8):
#     print('syno simple:  ', letter, count)

# if 'ab' in stopwords:
#     print('daa')

# c = Counter(cleanedwords_healthy + cleanedwords_syno)
# for letter, count in c.most_common(20):
#     letter_m = letter.replace("'", '')
#     letter_m = letter_m.replace(",", '')
#     if letter_m not in stopwords:
#         print('together cleaned   ', letter_m, count)


# for i in range(len(cleanedwords_healthy)):
#     for h in cleanedwords_healthy:
#         if h in cleanedwords_healthy:
#             print(h, ' in sich')
#         if h in cleanedwords_syno:
#             print(h, ' in syno')
#     for h in cleanedwords_syno:
#         if h in cleanedwords_syno:
#                 print('3',h)
#                 wort=re.findall(h,str(cleanedwords_syno))
#                 print('4', wort, ' in woxicon')


def anydup(thelist,controlldict):
    ch = controlldict
    resdict = {}
    characters_to_remove = ",'[]',"
    pattern = "[" + characters_to_remove + "]"
    seen = set()
    # print(ch.keys())
    for thelist in ch.keys():
        for x in ch[thelist]:
            x = re.sub(pattern, "", x)
            #x = ''.join(e for e in x if e.isalnum())
            #print('s',x)
            if x in seen:
                if x not in resdict.keys():
                    resdict[x] = set()
                # print('duict',thelist)
                # print(x)
                resdict[x].add(thelist) 
            seen.add(x)
    for thelist in ch.keys():
        for x in ch[thelist]:
            x = re.sub(pattern, "", x)
            # x = ''.join(e for e in x if e.isalnum())
            if x in resdict.keys():
                # print('duict',thelist)
                # print(x)
                resdict[x].add(thelist) 
    
    return resdict



##realt features
e =anydup(cleanedwords_healthy, ch)

##woxicon
sye =anydup(cleanedwords_healthy, sych)
d2 = {tuple(v): k for k, v in sye.items()}
sye = {v: list(k) for k, v in d2.items()}


##theseus
thsye = anydup(cleanedwords_thsych, thsych)
d2 = {tuple(v): k for k, v in thsye.items()}
thsye = {v: list(k) for k, v in d2.items()}

# print(sye)

###write results to file

# from csv import reader
# from csv import writer
import os
import csv

filename= 'healthy_combined_csv0 - Kopie' #results-survey562626_v2'
folder = os.getcwd() + "\\"

default_text = 'addinfo'

# with open(folder + filename +'.csv', mode='r', encoding='utf8', newline ='') as read_obj:
#     with open(folder + filename + '1.csv', mode='w', encoding='utf8', newline ='') as write_obj:
#         csv_reader = reader(read_obj)
#         csv_writer = writer(write_obj)
#         for enum,row in enumerate(csv_reader):
#             if row[0] in e.keys():
#                 print(row)
#                 row.append(e[row[0]])
#                 csv_writer.writerow(row)

with open(folder + filename + 'doppel1.csv', mode='w', encoding='utf8', newline ='') as write_obj:
    writer = csv.DictWriter(write_obj, fieldnames=["doppelvorkommen", "wo","NR", "in feature"])
    writer.writeheader()
    for res in e.keys():
        cres = ''.join(e for e in res if e.isalnum())
        if cres not in stopwords:
            writer.writerow({"doppelvorkommen": cres, "wo": 'in features selber', "NR": hc[res] , "in feature":e[res]})
    for res in sye.keys():
        cres = ''.join(e for e in res if e.isalnum())
        if cres not in stopwords:
            writer.writerow({"doppelvorkommen": cres,"wo": 'woxikon', "NR": syc[res] , "in feature":sye[res]})
    for res in thsye.keys():
        cres = ''.join(e for e in res if e.isalnum())
        if cres not in stopwords:
             writer.writerow({"doppelvorkommen": cres,"wo": 'theseus', "NR": thsyc[res] , "in feature":thsye[res]})