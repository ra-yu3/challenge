from pyknp import KNP
from tqdm import tqdm
import json
import re
import collections as cl


o = open('stop.txt', 'r')
a = o.read()
stopwords = a.split()

for a in tqdm(range(1, 25)):

    f = open('texts/%s.txt' % a)
    text = f.readlines()
    f.close()
    knp = KNP()
    dic = {}

    for t in tqdm(text):
        t = t.strip()

        print(t)
        if len(t) == 0:
            continue
        result = knp.parse(t)

        for mrph in result.mrph_list():
            if(mrph.genkei in stopwords == True):
                continue

            else:
                if(mrph.hinsi == "動詞" or mrph.hinsi == "名詞"or mrph.hinsi == "形容詞"):
                    if(dic.get(mrph.genkei) == None):
                        dic[mrph.genkei] = 1
                    else:
                        num = int(dic[mrph.genkei])+1
                        dic[mrph.genkei] = num
                else:
                    continue

    fw = open('freq/%s.json' % a, 'w')
    json.dump(dic, fw, ensure_ascii=False, indent=4)
