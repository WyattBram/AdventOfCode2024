##Pt 1
import heapq

left = []
right = []
with open("day1.txt", "r") as file:
    for line in file.readlines():
        tmp = line.split("   ")
        heapq.heappush(left, int(tmp[0]))
        heapq.heappush(right, int(tmp[1].strip("\n")))


num = 0
for i in range(len(left)):
    num += abs(heapq.heappop(left) - heapq.heappop(right))

print(num)


##Pt 2
left = []
similarityMap = {}
value = 0

with open("day1.txt", "r") as file:
    for line in file.readlines():
        tmp = line.split("   ")
        left.append(int(tmp[0]))
        value = int(tmp[1].strip("\n"))
        similarityMap[value] = similarityMap.get(value, 0) + 1

score = 0
for n in left:
    score += (n * similarityMap.get(n, 0))

print(score)