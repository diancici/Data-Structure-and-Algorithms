# T(0) = O(n^2) for randomly ordered array
# T(O) = O(n) for ordered array 
# move the smallest to the left, one place a time, starting from the most right
# efficient for partially sorted array
# slow for large unordered array

def insertion(a):
    if len(a) <= 1:
        return a
    
    for i in range(1,len(a)):
        for j in range(i, 0, -1):
            if a[j] < a[j-1]:
                temp = a[j-1]
                a[j-1] = a[j]
                a[j] = temp
            else:
                break
    
    return a

a = [6,8,2,3,4,5,1]
insertion(a)
print(a)