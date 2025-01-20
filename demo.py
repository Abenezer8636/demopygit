
def search(list,n):
    low = 0
    upp = len(list) -1
    while low <= upp:
        mid = (low + upp) // 2
        if list[mid] == n:
            return mid
        elif list[mid] < n:
            low = mid + 1
        else:
            upp = mid-1
    return -1 # if not found in a list

list = [56,67,89,45,34,22,85,23,5]
list.sort()
n = 89
poss = search(list,n)

if poss != -1:
    print(f'{n} is found at position {poss}')
else:
    print('Not Found')
