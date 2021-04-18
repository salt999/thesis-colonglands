#!/usr/bin/env python
# -*- coding: utf-8 -*-


# ###find synonyms

H = ['Gänseblümchenartig', 'regelmäßige Anordnung weißer Anteile', 'Drüse klar abgegrenzt', 'Segmente kreisförmig um Mittelpunkt', 'weis vor rotem Grund', 'qshift', 'Blumenförmig', 'Symmetrie ', 'Stroma netzförmig', 'Gland boundary stabil ', 'Gland boundary dicker ', 'Normal crypt architecture', 'H &E', 'Basaly located nuclei', 'No inflammation', 'Goblet cells', 'eosinophile Färbung', 'einschichtiges Epithel', 'Zellkerne', 'physiologisch?', 'Becherzellen?', 'Sehr dunkle Drüsenbegrenzung', 'große weiße Epithelzellen', 'meist runde oder ovale Formen', 'einheitliches und weißes Lumen', 'klar definierte Formen im Inneren der Dr', 'blütenförmige anordnung der Lumen', 'zerfurchtes Äußeres', 'klare Trennungen', 'Ein zentrales Lumen', 'eiförmige Lumen', 'klare Abtrennung durch Mucosa', 'kreisrunde Mitte', 'stroma unauffällig', 'keine auffälligkeiten', 'geordnet', 'zellen geordnet', 'rund']

HY=  ['Zellkerne auserhalb', 'oval', 'starke Kontrastierung', 'Inhomogenes weis im Inneren', 'Drüse schwarz umrandet', 'Oval', 'Asymmetrisch ', 'Löchrig', 'Gland boundary geschwächt', 'Unregelmäßig ', 'vergrößertes Lumen', 'Blaufärbung', 'prominente Zellkerne', 'Hyperplasie der Zellen?', 'Asymmetrie', 'mehr oval als rund Druesengrenze', 'sehr weisses Lumen', 'wenige Epithelzellen', 'Lumen nicht rund ', 'dunkles Bereich ausserhalb von Lumen', 'schwarze Punkte', 'unklare Übergänge', 'Lumen als Insel', 'Avocadoförmige Abtrennung', 'marmorartige Strukturen in Lumen', 'langezogene Drüse', 'heller, unförmiger Kern', 'Drüse hebt sich vom umliegenden Gewebe', 'dunkler, fleckiger Rand', 'vergrößert', 'oval', 'unförmig', 'drüseninhalt', 'evtl infiltration '], 
 
LG =  ['breite Umrandung ', 'heller Kern', 'mehrfärbig', 'von rosa Fäden durchzogen', 'eher rechteckig', 'Stark durchzogen', 'Lumen klein', 'Gland boundary löchrig ', 'Netzartig ', 'Nach innen ziehend ', 'In sich symmetrisch ', 'Deutliche Schichten ', 'Blaufärung', 'prominente Zellkerne', 'nachbart an weitere Drüse', 'Lumen verengt', 'Becherzellen vergrößert?', 'kleines Lumen', 'unklare Druesengrenze', 'weisses Lumen', 'verschwommenes Stroma', 'viele Epithelzellen', 'Mandala', 'keine klare Trennung zu Lumen', 'Anhäufung lila Punkte', '3 runde Schichten', 'Keine klaren Grenzen', 'Quetschung von rechts unten', 'Lumen zentral und hell', 'rosa als Verbindendes Element', 'Quadrat mit abgerundeten Ecken', 'enges lumen', 'rand gut sichtbar', 'dichtes stroma', 'andere drüsenendstücke sichtbar', 'gut beurteilbar'],

HG =  ['längliche Zellen', 'vereinzelte dunkele Flecken', 'in dichten Zellverband eingebettet', 'rot', 'Drüßenanteile nach Innen heller', 'Lumen langförmig', 'Langezogene epith. Cells ', 'Relativ symmetrisch ', 'Feiner durchzogen', 'Dünne gland boundary ', 'eosinophile Färbung', 'mehrschichtig', 'asymmetrisches Lumen', 'dunkle Punkte/Pigmente?', 'Becherzellen?', 'langes Lumen', 'Druesengrenze schwer erkennbar', 'weisse Druesengrenze', 'lange Epithelzellen', 'eckige Druesengrenze', 'Lumen mit Richtung', 'kleine Lumen um zentrales Lumen', 'Katzenauge', 'Spitzes, kantiges Lumen', 'fließende Übergänge', 'von hell (innen) nach dunkel (außen)', 'Pinselstriche nach Außen', 'längliche Kerne', 'verdickter rand', 'zellinfiltration', 'hyperplasie', 'lumen verengt', 'vergrößert']

from PyDictionary import PyDictionary 
dictionary=PyDictionary() 
# print (dictionary.synonym("WHITE"))
# print (dictionary.synonym("elongated"))
# print (dictionary.synonym("ELLIPSE"))
# print (dictionary.synonym("OVAL"))



# ['light-colored', 'value', 'light', 'albescent']
# ['elongate', 'long']
# ['circle', 'conic', 'oval', 'conic section']
# ['elliptic', 'egg-shaped', 'oval-shaped', 'elliptical', 'ovoid', 'prolate', 'ovate', 'rounded', 'oviform']


# from PyDictionary import PyDictionary
# dictionary=PyDictionary()
# print (dictionary.synonym("good"))
# meaning = dictionary.meaning("good")
# #print (dictionary.synonym("Life"))

# translation = dictionary.translate("happy",'de')
# print(translation)

###geht
# dictionary.translate("land",'en')
# a = dictionary.translate("länglich",'en')
# print(a)
# translations = dictionary.synonym(a)
# print(translations)
# b = [dictionary.translate(word,'de') for word in translations]
# print(b)

H_syny =  {}
for feat in H:
    feat_eng = dictionary.translate(feat,'en')
    print(feat_eng)
    feat_eng_syns = dictionary.synonym(feat_eng)
    print(feat_eng_syns)
    feat_de = [dictionary.translate(word,'de') for word in feat_eng_syns]
    #print(feat_de)
    H_syny[feat]= feat_de
print(H_syny)

Hy_syny =  {}
for feat in HY:
    feat_eng = dictionary.translate(feat,'en')
    print(feat_eng)
    feat_eng_syns = dictionary.synonym(feat_eng)
    print(feat_eng_syns)
    feat_de = [dictionary.translate(word,'de') for word in feat_eng_syns]
    #print(feat_de)
    Hy_syny[feat]= feat_de
print(Hy_syny)


Hlg_syny =  {}
for feat in LG:
    feat_eng = dictionary.translate(feat,'en')
    print(feat_eng)
    feat_eng_syns = dictionary.synonym(feat_eng)
    print(feat_eng_syns)
    feat_de = [dictionary.translate(word,'de') for word in feat_eng_syns]
    #print(feat_de)
    Hlg_syny[feat]= feat_de
print(Hlg_syny)


Hhg_syny =  {}
for feat in HG:
    feat_eng = dictionary.translate(feat,'en')
    print(feat_eng)
    feat_eng_syns = dictionary.synonym(feat_eng)
    print(feat_eng_syns)
    feat_de = [dictionary.translate(word,'de') for word in feat_eng_syns]
    #print(feat_de)
    Hhg_syny[feat]= feat_de
print(Hhg_syny)