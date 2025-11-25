import os

scores = [35,76,89,45,67,90,100,43,56,111,259,65,888]

#print(max(scores))
#print(sum(scores))

total =0

#for score in scores:
   # total += score

#print(total)

for score in scores:
    if score > total:
        total = score

print(total)

