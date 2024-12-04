


goodLines = 0
with open("day2.txt", 'r') as file:
    for line in file.readlines():
        data = list(map(int, line.split()))
        prev = data[0]

        allowed = 1

        good = True

        direction = ''

        for i in range(1, len(data)):
            x = data[i]

            #[6,4,2]
            if x < prev:
                if direction == '':
                    direction = 'decending'
                elif direction == 'ascending':
                    if allowed:
                        allowed-=1
                        continue
                    else:
                        good = False
                        break
                if x < prev - 3:
                    if allowed:
                        allowed-=1
                        continue
                    else:
                        good = False
                    break
                prev = x

            elif x > prev:
                if direction == '':
                    direction = 'ascending'
                elif direction == 'decending':
                    good = False
                    break

                if x > prev + 3:
                    good = False
                    break
                prev = x
            else:
                good = False
                break
        if good:
            goodLines+=1

print(goodLines)


