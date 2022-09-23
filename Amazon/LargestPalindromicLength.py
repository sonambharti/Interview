str = input()
s = set(str)
print(s)
res = []

for i in s:
    res.append(str.count(i))
    
print(res)
countLength = 0
for i in res:
    if i%2 == 0:
       countLength += i
       
       
print(sum+1)