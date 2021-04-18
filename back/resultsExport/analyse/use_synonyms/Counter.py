from collections import Counter
import pandas as pd
import re

###FILES
pathinput = r'hyperplastic_combined_csv4.csv'
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

dffeature = df.Hyperplastic_FEATURES

## clean words
ch = {}
healthy_list = list(dffeature)
cleanedwords_healthy = []
for healty in healthy_list:
    # print('WORD: ', healty)
    cleanedwords_healthy += [healthyword for healthyword in healty.split() if healthyword not in stopwords]
    m = [healthyword for healthyword in healty.split() if healthyword not in stopwords]
    print(healty)
    ch[str(healty)] = m

### count cleaned words
hc = Counter(cleanedwords_healthy)
for letter, count in hc.most_common(10):
    print('cleanedwords_healthy count  : ', letter, count)


def getcleanedwords(coloumn):
    sych ={}
    synon = list(coloumn)
    cleanedwords_syno = []
    tmp =[]
    for nr,sy in enumerate(synon):
        if isinstance(sy, str):
            tmp =[]
            for s in sy.split():
                s_word = ''.join(e for e in s if e.isalnum())
                #print(s_word)
                if s_word not in stopwords:
                    if len(s_word) > 0:
                        cleanedwords_syno.append(s_word)
                        tmp.append(s_word)
            sych[str(dffeature[nr])] = tmp
    
    syc = Counter(cleanedwords_syno)
    # for letter, count in syc.most_common(10):
    #     print(' cleanedwords_syno count:  ', letter, count)

    print(type(sych))
    print(type(syc))
    print(type(cleanedwords_syno))

    return [cleanedwords_syno, syc, sych]


[cleanedwords_syno, syc, sych] = getcleanedwords(df['SYNONYMS-woxikon']) 
[cleanedwords_thsych, thsyc, thsych] = getcleanedwords(df['SYNONYMS-thesaurus']) 


# thsych ={}
# synon = list(df['SYNONYMS-thesaurus'])
# cleanedwords_thsych = []
# for nr,sy in enumerate(synon):
#     # print('WORD: ', sy)
#     if isinstance(sy, str):
#         #[print('s',s) for s in sy.split() if str(s).replace("'", '') not in stopwords]
#         cleanedwords_thsych += [s for s in sy.split() if str(s).replace("'", '') not in stopwords]
#         m = [s for s in sy.split() if str(s).replace("'", '') not in stopwords]
#         keyy = ''.join(e for e in str(dffeature[nr]) if e.isalnum())
#         thsych[keyy)] = m

# thsyc = Counter(cleanedwords_syno)
# for letter, count in thsyc.most_common(10):
#     print(' cleanedwords_thsyno count:  ', letter, count)

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

###merge dicts
def mergeDict(dict1, dict2):
   ''' Merge dictionaries and keep values of common keys in list'''
   dict3 = {**dict1, **dict2}
   for key, value in dict3.items():
       if key in dict1 and key in dict2:
               dict3[key] = [value , dict1[key]]
   return dict3

finaldict = mergeDict(mergeDict(e, sye), thsye)
print('keys  ', finaldict.keys())
###write results to file

# from csv import reader
# from csv import writer
import os
import csv

filename= 'bloa' #results-survey562626_v2'
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
    

with open("sorteddoppel1.csv", mode='w', encoding='utf8', newline ='') as write_obj:
    writer = csv.DictWriter(write_obj, fieldnames=["doppelvorkommen","NR", "in feature"])
    writer.writeheader()
    for res in finaldict.keys():
        cres = ''.join(e for e in res if e.isalnum())
        if cres not in stopwords:
            writer.writerow({"doppelvorkommen": cres, "NR": hc[res] , "in feature":finaldict[res]})
