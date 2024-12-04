#
# tempo = []
#
# with open("day3.txt", 'r') as file:
#     tempList = file.read()
#     ptr = 0
#
#     for i in range(0, len(tempList)-3):
#         if tempList[i:i+4] == "mul(":
#
#             comma = 1
#
#             counter = i+4
#             tmp = ""
#             while True:
#
#                 if counter > len(tempList)-1:
#                     break
#
#                 if tempList[counter] == ',' and comma:
#                     comma-=1
#                     tmp+=tempList[counter]
#                     counter +=1
#
#                     continue
#                 elif tempList[counter] == ',' and not comma:
#                     break
#
#                 if not(tempList[counter].isnumeric()):
#                     break
#                 else:
#                     tmp+=tempList[counter]
#                     counter+=1
#                 if tempList[counter] == ")" and not comma:
#                     tempo.append(tmp)
#                     break
#
# total = 0
# for x in tempo:
#     aList = x.split(',')
#     aList = list(map(int, aList))
#     total += aList[0] * aList[1]
# print(total)
#




tempo = []

with open("day3.txt", 'r') as file:
    tempList = file.read()
    ptr = 0
    good = True


    for i in range(0, len(tempList)-3):
        if tempList[i:i+4] == 'do()':
            good = True

        elif i < len(tempList)-7 and tempList[i:i+7] == "don't()":
            good = False

        elif tempList[i:i+4] == "mul(" and good:

            comma = 1

            counter = i+4
            tmp = ""
            while True:

                if counter > len(tempList)-1:
                    break

                if tempList[counter] == ',' and comma:
                    comma-=1
                    tmp+=tempList[counter]
                    counter +=1

                    continue
                elif tempList[counter] == ',' and not comma:
                    break

                if not(tempList[counter].isnumeric()):
                    break
                else:
                    tmp+=tempList[counter]
                    counter+=1
                if tempList[counter] == ")" and not comma:
                    tempo.append(tmp)
                    break

total = 0
for x in tempo:
    aList = x.split(',')
    aList = list(map(int, aList))
    total += aList[0] * aList[1]
print(total)
