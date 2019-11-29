import json


# 各章までの和を出力します

for j1 in range(1, 25):
    sumdic = {}
    num = j1+1
    for j2 in range(1, num):
        o = open('tfidf_result/tfidf%s.json' % j2, 'r')
        dic = json.load(o)

        for k, v in dic.items():
            if (k in sumdic):
                sumdic[k] = round(int(sumdic[k])+int(v), 5)

            else:
                sumdic[k] = round(v, 5)
    sumdic = sorted(sumdic.items(), key=lambda x: -x[1])
    sumdic = dict(sumdic)
    fw = open('tfidf_chartgot/sum%s.json' % j1, 'w')
    json.dump(sumdic, fw, ensure_ascii=False, indent=4)
