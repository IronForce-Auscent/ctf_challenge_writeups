inputMn = input()
n = int(inputMn.split(" ")[0])
m = int(inputMn.split(" ")[1])

edges = []
for i in range(m):
    x = input()
    edges.append(x)

K = int(input())
k = input()

toRemove = 0

removedIndexes = []

if K >= 2:
    splitK = k.split(" ")
    for j in edges:
        for l in range(K):
            if j.find(splitK[l]) >= 0:
                if j not in removedIndexes:
                    removedIndexes.append(j)
                    toRemove += 1
                else:
                    pass
else: 
    for j in edges:
        if j.find(k) >= 0:
            if  j not in removedIndexes:
                removedIndexes.append(j)
                toRemove += 1
            else:
                pass

print(toRemove)