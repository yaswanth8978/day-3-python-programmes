def backtrack():
    global ans, curr, visited, nums
    if (len(curr) == len(nums)):
        print(*curr)
 
    for i in range(len(nums)):
 
        if (visited[i]):
            continue
 
        if (i > 0 and nums[i] == nums[i - 1] and visited[i - 1]==False):
            continue
 
        visited[i] = True
 
        curr.append(nums[i])
 
        backtrack()
 
        visited[i] = False
 
        del curr[-1]
 

def permuteDuplicates(nums):
    global ans, visited, curr
    nums = sorted(nums)
 
   
    backtrack()
    return ans
 

def getDistinctPermutations(nums):
    global ans, curr, visited
     
    
    ans = permuteDuplicates(nums)
 

if __name__ == '__main__':
    visited = [False]*(5)
    ans,curr = [], []
    nums = [-1,0,1]
 
    
    getDistinctPermutations(nums)
 
