import json
import math
docnum = 24

p = open('date.json', 'r')
words = json.load(p)
for j1 in range(1, 25):
    tf = {}
    idf={}
    tfidf={}
    o = open('freq/%s.json' % j1, 'r')
    dic = json.load(o)
    sum = 0
    for k, v in dic.items():
        sum = sum+int(v)


    for k, v in dic.items():

        tf[k] = int(dic[k])/sum
        nnn=0
        for j2 in range(1, 25):
            p = open('freq/%s.json' % j2, 'r')
            dic2 = json.load(p)
            if(k in dic2):
                nnn=nnn+1
            else:
                continue


        idf[k]=math.log(docnum/nnn)+1
        tfidf[k]=tf[k]*idf[k]


    tfidf = sorted(tfidf.items(), key=lambda x: -x[1])
    tfidf = dict(tfidf)
    fw = open('tfidf_result/tfidf%s.json' % j1, 'w')
    json.dump(tfidf, fw, ensure_ascii=False, indent=4)










    

    
# tf = {}
# for j1 in range(1, 25):
#     o = open('jso3/%s.json' % j1, 'r')
#     dic = json.load(o)

#     for k, v in dic.items():
#         if (k in tf):
#             tf[k] = v/tf[k]

#         else:
#             continue
    













