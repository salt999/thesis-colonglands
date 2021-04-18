
# import re

# wort=re.findall(r'(\w+)',str(text))

from re import match
import re

values = ['länglich', 'lange', 'lang', 'ei', 'eiförmig']
HG =  ['längliche Zellen', 'vereinzelte dunkele Flecken', 'in dichten Zellverband eingebettet', 'rot', 'Drüßenanteile nach Innen heller', 'Lumen langförmig', 'Langezogene epith. Cells ', 'Relativ symmetrisch ', 'Feiner durchzogen', 'Dünne gland boundary ', 'eosinophile Färbung', 'mehrschichtig', 'asymmetrisches Lumen', 'dunkle Punkte/Pigmente', 'Becherzellen', 'langes Lumen', 'Druesengrenze schwer erkennbar', 'weisse Druesengrenze', 'lange Epithelzellen', 'eckige Druesengrenze', 'Lumen mit Richtung', 'kleine Lumen um zentrales Lumen', 'Katzenauge', 'Spitzes, kantiges Lumen', 'fließende Übergänge', 'von hell innen nach dunkel außen', 'Pinselstriche nach Außen', 'längliche Kerne', 'verdickter rand', 'zellinfiltration', 'hyperplasie', 'lumen verengt', 'vergrößert']
values = HG
# filtered_values = list(filter(lambda v: match('^\d+$', v), values))

# print(filtered_values)
a = []

# for value in values:
#     # if isinstance(value, list):
#     #     for l in value:
#     #         word = ".*"+l + "*"
#     #         print(type(word))
#     #         r = re.compile(word)
#     #         newlist = list(filter(r.match, values)) # Read Note
#     #         print(newlist)
#     # else:
#         b = set()
#         for le in range(len(value)-1):
#             #print(le,value[le:le+3])
#             word = value[le:le+5]
#             r = re.compile(word)
#             newlist = list(filter(r.match, values)) # Read Note
#             b.update(newlist)
#         a.append(list(b))
# #print(a)

# for all in a:
#     if len(all)> 2:
#         print(all)


# for value in values:
#     r = re.compile('lumen')
#     newlist = list(filter(r.match, values))
#     print(newlist)
for value in values:
    if 'lumen' in value.lower():
        print(value)
