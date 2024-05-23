nums_lst = list(map(int, input()))
bucket = [0] * 10
for i in range(len(nums_lst)):
    if nums_lst[i] == 6 or nums_lst[i] == 9:
        if bucket[6] <= bucket[9]:
            bucket[6] += 1
        else:
            bucket[9] += 1
    else:
        bucket[nums_lst[i]] += 1

print(max(bucket))
