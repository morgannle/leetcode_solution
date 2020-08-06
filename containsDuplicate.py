nums = [1,2,3,4,5,6,6]

def containsDuplicate(nums):
    nums_sort = sorted(nums)
    for i in range(0,len(nums)-1):
        if nums_sort[i] == nums_sort[i+1]:
            return True
            break
    return False
        
containsDuplicate(nums)