# File timeseqs_timer2.py
"Test the relative speed of iteration tools alternatives."

import sys, timer2
reps = 10000
repslist = list(range(reps))

def forLoop():
    res = []
    for x in repslist:
        res.append(x + 10)
    return res

def listComp():
    return [x + 10 for x in repslist]

def mapCall():
    return list(map((lambda x: x + 10), repslist))

def genExpr():
    return list(x + 10 for x in repslist)

def genFunc():
    def gen():
        for x in repslist:
            yield x + 10
    return list(gen())

print(sys.version)
for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    (total, result) = timer2.bestoftotal(test, _reps1=5, _reps=1000
                                         )
    print('%-9s: %.5f => [%s...%s]' %
          (test.__name__, bestof, result[0], result[-1]))
