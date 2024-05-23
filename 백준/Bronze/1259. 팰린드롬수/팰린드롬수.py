while 1:
    lst = list(input())
    if lst == ['0']: break
    R_lst = lst[::-1]
    if R_lst == lst:
        print('yes')
    else:
        print('no')
