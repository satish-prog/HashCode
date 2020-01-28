def pizza(nums, target):
    if len(nums) == 0 or nums == None:
        return -1
    d = {}
    helper(0, nums, target, [], d)
    keys = list(d.keys())
    mx = max(keys)
    print (mx)
    l = d.get(mx)
    print(l)
def helper(index, nums, target,sub, d):
    l = sub.copy()
    if sum(l) < target:
        d[sum(l)] = l
    if index == len(nums):
        return    
    else:
        sub.append(nums[index])
        helper(index+1, nums, target,sub, d)        
        sub.pop()
        helper(index+1, nums, target,sub, d) 
nums = [2, 5, 6, 8]
target = 17
pizza(nums, target)        
