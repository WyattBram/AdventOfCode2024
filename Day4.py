
# total = 0
# tm = 0
# with open('Day4.txt', 'r') as file:
#     data = file.read().split('\n')
#
#     for i in range(len(data)):
#         for j in range(len(data[i])):
#             tm+=1
#
#             if data[i][j] == 'X':
#
#             # check up
#                 if i >= 3:
#                     if data[i-1][j] == 'M' and data[i-2][j] == 'A' and data[i-3][j] == 'S':
#                         total +=1
#             # check down
#                 if i <= len(data) - 4:
#                     if data[i +1][j] == 'M' and data[i + 2][j] == 'A' and data[i + 3][j] == 'S':
#                         total += 1
#
#             # check left
#                 if j >= 3:
#                     print(i,j)
#                     if data[i][j-1] == 'M' and data[i][j-2] == 'A' and data[i][j-3] == 'S':
#                         total += 1
#
#             # check right
#                 if j <= len(data[i]) - 4:
#                     if data[i][j + 1] == 'M' and data[i][j + 2] == 'A' and data[i][j + 3] == 'S':
#                         total += 1
#
#             # check up-right
#                 if i >= 3 and j <= len(data[i]) - 4:
#                     if data[i-1][j + 1] == 'M' and data[i-2][j + 2] == 'A' and data[i-3][j + 3] == 'S':
#                         total += 1
#             # up- left
#                 if i >= 3 and j >= 3:
#                     if data[i-1][j - 1] == 'M' and data[i-2][j - 2] == 'A' and data[i-3][j - 3] == 'S':
#                         total += 1
#
#             # check down right
#                 if i <= len(data) - 4 and j <= len(data[i]) - 4:
#                     if data[i+1][j + 1] == 'M' and data[i+2][j + 2] == 'A' and data[i+3][j + 3] == 'S':
#                         total += 1
#
#             # down left
#                 if i <= len(data) - 4 and j >= 3:
#                     if data[i+1][j - 1] == 'M' and data[i+2][j - 2] == 'A' and data[i+3][j - 3] == 'S':
#                         total += 1
#
#
# print(total)


total = 0
tm = 0
with open('Day4.txt', 'r') as file:
    data = file.read().split('\n')

    for i in range(len(data)):
        for j in range(len(data[i])):
            if i <= len(data) - 3 and j <= len(data) - 3:
                if data[i][j] == 'M' and data[i][j+2] == 'S' and data[i+1][j+1] == 'A' and data[i+2][j+2] == 'S' and data[i+2][j] == 'M':
                    total +=1
                elif data[i][j] == 'M' and data[i][j + 2] == 'M' and data[i + 1][j + 1] == 'A' and data[i + 2][j + 2] == 'S' and data[i + 2][j] == 'S':
                    total += 1
                elif data[i][j] == 'S' and data[i][j + 2] == 'M' and data[i + 1][j + 1] == 'A' and data[i + 2][j + 2] == 'M' and data[i + 2][j] == 'S':
                    total += 1
                elif data[i][j] == 'S' and data[i][j + 2] == 'S' and data[i + 1][j + 1] == 'A' and data[i + 2][j + 2] == 'M' and data[i + 2][j] == 'M':
                    total += 1

print(total)










