
tempo = []

with open("day3.txt", 'r') as file:
    shitList = file.read()
    ptr = 0

    for i in range(0, len(shitList)-3):
        if shitList[i:i+4] == "mul(":

            comma = 1

            counter = i+4
            tmp = ""
            while True:

                if counter > len(shitList)-1:
                    break

                if shitList[counter] == ',' and comma:
                    comma-=1
                    tmp+=shitList[counter]
                    counter +=1

                    continue
                elif shitList[counter] == ',' and not comma:
                    break

                if not(shitList[counter].isnumeric()):
                    break
                else:
                    tmp+=shitList[counter]
                    counter+=1
                if shitList[counter] == ")" and not comma:
                    tempo.append(tmp)
                    break

total = 0
for x in tempo:
    aList = x.split(',')
    aList = list(map(int, aList))
    total += aList[0] * aList[1]
print(total)
