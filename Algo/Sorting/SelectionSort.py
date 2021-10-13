# T(O) = O(n^2)
# S(O) = 1 (in place)
# exchange the smallest value to the left, scanning the array from the left
def selection(a):
    n = len(a)
    # Sort a[] into increasung order
    for i in range(0, n):
        minIndex = i # index of a minimal entry
        for j in range(i+1, len(a)):
            if a[j] < a[minIndex]:
                minIndex = j
        # exchange a[i] and a[minIndex]
        min = a[minIndex]
        a[minIndex] = a[i]
        a[i] = min
    
    return a

a = [6,8,2,3,4,5,1]
selection(a)
print(a)