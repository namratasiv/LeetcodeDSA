from collections import Counter
#nums1=[1,2,2,1]
#nums2=[2,2]
nums1=[4,9,5]
nums2=[9,4,9,8,4]
temp = []
a =Counter(nums1)
b = Counter(nums2)

for (i,j) in a.items():
    if i in b and b[i] >= j:
        for x in range(j):
            temp.append(i)

print(temp)