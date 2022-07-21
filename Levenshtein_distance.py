from logging import raiseExceptions


def LevenshteinDistance(s,t):
    d = [[0 for j in range(len(t) + 1 )] for i in range(len(s) + 1 )]
    for i in range(len(s) + 1):
        d[i][0] = i
    
    for j in range(len(t) + 1):
        d[0][j] = j

    for j in range(1,len(t) + 1):
        for i in range(1,len(s) + 1):
            if s[i-1] == t[j-1]:
                substitutionCost = 0
            else:
                substitutionCost = 1
            
            d[i][j] = min(
                d[i-1][j] + 1,
                d[i][j-1] + 1,
                d[i-1][j-1] + substitutionCost
            )

    return d[len(s)][len(t)]

x = LevenshteinDistance("Pandas in China and Koalas in Australia are similar because they both only feed on one thing. Pandas eat bamboo and Koalas eucalyptus leaves. Unlike pythons which eat just about everything including Alligators.","Pandas in China only eat bamboo and Koalas in Australia eat exclusively eucalyptus leaves. They are both restricted to one food while pythons eat a variety of foods")

#if x != 138:
#    raise Exception("incorrect distance")

print(x)