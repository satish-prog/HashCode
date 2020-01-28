def openFile():
    fileForInput = open('d.in','r')
    l = []
    for N in fileForInput:
        l.append(N)
    return l    
def saveFile(lis, nums):
    op = ""
    op += str(len(lis))+"\n"
    lis.reverse()
    for i in lis:
        op += str(nums.index(i))+" "
    fileForOutput = open("d.out","w")
    fileForOutput.write(op)    

def pizza(s, t):
    if len(s) == 0 or s == None:
        return -1
    n = len(s)    
    k = [[0 for x in range(t+1)] for x in range(n+1)] 
    for i in range(n+1):
        for j in range(t+1):
            if i == 0 or j == 0:
                k[i][j] = 0
            elif j >= s[i-1]:
                k[i][j] = max(k[i-1][j-s[i-1]]+s[i-1], k[i-1][j])
            else:
                k[i][j] = k[i-1][j]
    
    total = k[i][j] 
    w = j
    res = []
    for m in range(n+1, 0, -1):
        if total <= 0:
            break 
        if total == k[m-1][w]:
            continue
        else:
            res.append(s[m-1])
            
            total -= s[m-1]
            w -= s[m-1]
    saveFile(res, s)

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