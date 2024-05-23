num = int(input())
checker = [1] * 2 + [0] * 2000000

for i in range(2, 2000000):
    if checker[i] == 1: continue
    for j in range(2 * i, 2000000, i):
        checker[j] = 1
for i in range(num, 2000000):
    if checker[i] == 0:
        st = list((str(i)))
        R_st = st[::-1]
        if st == R_st:
            print(i)
            break
