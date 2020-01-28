fileForInput = open('a.in','r')
l = []

for N in fileForInput:
    l.append(N)
print(l)    



target = ""
for i in l[0]:
    if i == " ":
        break
    target += i
nums = []
temp = ""
t = l[1].split("\n")
m = t[0].split(" ")
       
for i in m:
    nums.append(int(i))
print(int(target))
print(nums)  