def openFile():
    fileForInput = open('b.in','r')
    l = []
    for N in fileForInput:
        l.append(N)
    return l    
def saveFile(lis, nums):
    op = ""
    op += str(len(lis))+"\n"
    for i in lis:
        op += str(nums.index(i))+" "
    fileForOutput = open("ans.out","w")
    fileForOutput.write(op)    

def pizza(nums, target):
    if len(nums) == 0 or nums == None:
        return -1
    d = {}
    helper(0, nums, target, [], d)
    keys = list(d.keys())
    mx = max(keys)
    l = d.get(mx)
    saveFile(l, nums)

def helper(index, nums, target,sub, d):
    l = sub.copy()
    if sum(l) <= target:
        d[sum(l)] = l
    if index == len(nums):
        return    
    else:
        sub.append(nums[index])
        helper(index+1, nums, target,sub, d)        
        sub.pop()
        helper(index+1, nums, target,sub, d) 

#Driver Code
if __name__ == "__main__":
    l = openFile()
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
    pizza(nums, int(target))