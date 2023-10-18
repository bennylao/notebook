listA = [5, 23, 7, 89, 7, 90]
listB = [89, 25, 89, 7, 14, 76, 5, 11, 5]
listC =[]

for x in listB:
    for y in listA:
        if x == y:
            listC.append(x)

listC = list(dict.fromkeys(listC))

print(listC)




