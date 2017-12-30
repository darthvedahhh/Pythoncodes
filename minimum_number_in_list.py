
a=[2,3,4,5,1,-6,8,9,0,7,6,8,-1,80,90,70]
min=a[0]
for i  in range(len(a)):
    
    for j in range(len(a)):

        if min<a[j]:
            pass
        else:
            min=a[j]

print(min)
