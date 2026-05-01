#program for FLAMES
a1=input("Enter boy name: ")
b1=input("Enter girl name: ")
a=list(a1)
b=list(b1)

for i in range(len(a)):
    for j in range(len(b)):
        if a1[i]==b[j]:
            a[i]='2'
            b[j]='2'
cnt=0
for i in a:
    if i!='2':
        cnt+=1
for i in b:
    if i!='2':
        cnt+=1
        
idx=0
res=list('FLAMES')
for i in range(5):
    idx=(idx+(cnt-1))%len(res)
    res.pop(idx)
print(res[0])