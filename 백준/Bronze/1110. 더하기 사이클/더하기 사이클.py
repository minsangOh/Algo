num = int(input())
num_0 = num
flag = 1
i = 0
while flag:
    a = num_0 // 10
    b = num_0 % 10
    c = (a + b) % 10
    num_0 = (10 * b) + c
    i += 1
    if num == num_0:
        flag = 0
        break
    else:
        continue
print(i)