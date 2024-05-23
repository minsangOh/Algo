word = input()
word = word.upper()
lst = list(word)
ord_lst = []
for i in lst:
    ord_lst.append(ord(i))

bucket = [0] * 30
for j in ord_lst:
    j -= 65
    bucket[j] += 1
Max_1 = max(bucket)
Max_pt_1 = bucket.index(max(bucket))

bucket[Max_pt_1] = 0

Max_2 = max(bucket)
Max_pt_2 = bucket.index(max(bucket))

if Max_1 > Max_2:
    print(chr(Max_pt_1 + 65))
else:
    print('?')
