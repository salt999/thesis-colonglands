import json, requests
import time

# def get_synonyms(term):
#     d = json.loads(requests.get("http://www.openthesaurus.de/synonyme/search",
#                                 params={"q": term, "format": "application/json"}).text)
#     return [o["term"] for o in d["synsets"][0]["terms"]]

def get_synonyms(term):
    print(term)
    print(type(term))
    # d = json.loads(requests.get("http://www.openthesaurus.de/synonyme/search",
    #                             params={"q": term, "format": "application/json", "similar":"true"}).text) #, "supersynsets":"true"
    m = json.loads(requests.get("https://de.wiktionary.org/w/index.php?title=oval").text)
    print(m)
                                # if 'similarterms' in d:
    #     print('similar')
    # #     print([o["term"] for o in d["similarterms"]])
    # print(d)
    # if 'synsets'in d:
    #     if d['synsets']:
    #         print('entered')
    #         return [o["term"] for o in d["synsets"][0]["terms"]]
    #     else:
    #         return '1'


#get_synonyms('oval')
# a = ['lang ei', 'ei']
# m=[]
# for r in a:
#     for h in r.split():
#         print(get_synonyms(h))
#         m.append()
# H = ['Gänseblümchenartig', 'regelmäßige Anordnung weißer Anteile', 'Drüse klar abgegrenzt', 'Segmente kreisförmig um Mittelpunkt', 'weis vor rotem Grund', 'qshift', 'Blumenförmig', 'Symmetrie', 'Stroma netzförmig', 'Gland boundary stabil ', 'Gland boundary dicker ', 'Normal crypt architecture', 'H&E', 'Basaly located nuclei', 'No inflammation', 'Goblet cells', 'eosinophile Färbung', 'einschichtiges Epithel', 'Zellkerne', 'physiologisch?', 'Becherzellen?', 'Sehr dunkle Drüsenbegrenzung', 'große weiße Epithelzellen', 'meist runde oder ovale Formen', 'einheitliches und weißes Lumen', 'klar definierte Formen im Inneren der Dr', 'blütenförmige anordnung der Lumen', 'zerfurchtes Äußeres', 'klare Trennungen', 'Ein zentrales Lumen', 'eiförmige Lumen', 'klare Abtrennung durch Mucosa', 'kreisrunde Mitte', 'stroma unauffällig', 'keine auffälligkeiten', 'geordnet', 'zellen geordnet', 'rund']
# for enum,h in enumerate(H):
#     print(enum, h)
#     for a in h.strip().split(' '):
#         print(a)
#         if len(a) > 2:
#             time.sleep(3)
#             print(get_synonyms(a))


import os, sys
import re
import argparse

url = 'http://synonyme.woxikon.de/synonyme/'
urlsuffix = '.php'

values = ['länglich', 'lange', 'lang'] #, 'ei', 'eiförmig'
HG =  ['längliche Zellen', 'vereinzelte dunkele Flecken', 'in dichten Zellverband eingebettet', 'rot', 'Drüßenanteile nach Innen heller', 'Lumen langförmig', 'Langezogene epith. Cells ', 'Relativ symmetrisch ', 'Feiner durchzogen', 'Dünne gland boundary ', 'eosinophile Färbung', 'mehrschichtig', 'asymmetrisches Lumen', 'dunkle Punkte/Pigmente', 'Becherzellen', 'langes Lumen', 'Druesengrenze schwer erkennbar', 'weisse Druesengrenze', 'lange Epithelzellen', 'eckige Druesengrenze', 'Lumen mit Richtung', 'kleine Lumen um zentrales Lumen', 'Katzenauge', 'Spitzes, kantiges Lumen', 'fließende Übergänge', 'von hell innen nach dunkel außen', 'Pinselstriche nach Außen', 'längliche Kerne', 'verdickter rand', 'zellinfiltration', 'hyperplasie', 'lumen verengt', 'vergrößert']


searchQuery = 'oval' #args.suchWort[0]

for r in HG:
    # d = requests.get(url + searchQuery + urlsuffix).text
    for searchQuery in r.split():
        d = requests.get(url + searchQuery + urlsuffix).text
        # print(d)

        stripped = re.sub('<[^<]+?>', '', d)
        print(stripped)

        wort=re.findall(r'Bedeutung: (\w+)',str(stripped))
        print(searchQuery, ' : ',  wort)

# print('Synonyme fuer %s:' % (searchQuery))
# for m in re.finditer(r"Bedeutung:", d):
#   print('%s' %  (m.group(1)))
#print html #Debug output

#So werden die Synonyme im HTML-Quelltext ausgegeben:
#<span class="meaningContent">[Synonym]</span>

# print('Synonyme fuer %s:' % (searchQuery))
# for m in re.finditer(r"<span class=\"meaningContent\">(\w+)</span", html):
#   print('%s' %  (m.group(1)))
