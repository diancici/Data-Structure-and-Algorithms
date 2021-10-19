# improuvement of insertion sort
# n/k partially array - insertion sort 
# mach quicker than insertion sort & selection sort, specially in large arrays
from typing import List
def shellsort(a: List):
    n = len(a)
    h = 1 # an h-sorted array is h independent sorted subsequences
    # decide what increment sequence to use
    while h < n/3 :
        h = 3*h + 1
    while h >= 1:
        for i in range(h, n):
            for j in range(i, h-1 , -1):
                if a[j] < a[j-h]:
                    temp = a[j-h]
                    a[j-h] = a[j]
                    a[j] = temp
                else:
                    break
        h = int(h / 3)
    return a

a = [6,8,2,3,4,5,1,2,5,10,20,1,8]
shellsort(a)
print(a)
