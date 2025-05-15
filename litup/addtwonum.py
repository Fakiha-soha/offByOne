l1 = [2,4,3]
l2 = [5,6,4]

p,q=0,0
for i in range (len(l1)-1,-1,-1):
    p+=l1[i]*(10**i)
for i in range (len(l2)-1,-1,-1):
    q+=l2[i]*(10**i)

r=p+q
r = str(r)
print(list(r[::-1]))