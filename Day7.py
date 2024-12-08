truth = False

def stackMath(target, list, stack):
    global truth
    if stack[-1] == target:
        truth = True

    if not list:
        return


    stack[-1] += list[0]

    stackMath(target, list[1:], stack)

    stack[-1] -= list[0]

    stack[-1] *= list[0]

    stackMath(target, list[1:], stack)

    stack[-1] //= list[0]

with open('day7.txt') as file:
    total = 0
    for line in file.readlines():
        temp = line.split(': ')
        numbers = list(map(int, temp[1].split()))
        num = int(temp[0])

        stack = []

        stack.append(numbers[0] + numbers[1])
        stackMath(num, numbers[2:], stack)
        print(truth)


        stack.pop()
        stack.append(numbers[0] * numbers[1])
        stackMath(num, numbers[2:], stack)
        print(truth)
        if truth:
            total += num

        truth = False




    print(total)