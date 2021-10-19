# T(O) = O(n^2)
# S(O) = 1 (in place)
# move the smallest to the left, one place a time , starting from the most right
def bubble(a):
    for i in range(0,len(a)-1):
        for j in range(0,len(a)-1-i):
            if a[j] > a[j+1]:
                temp = a[j+1]
                a[j+1] = a[j]
                a[j] = temp
    return a


a = [6,8,2,3,4,5,1]
bubble(a)
print(a)