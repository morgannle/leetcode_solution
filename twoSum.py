nums = [0,3,3,2,2,6,4]
target = 6

def twoSum(nums, target):
    flag = 0 
    temp = list()
    keys = list(range(0,len(nums)))
    temp_dict = dict(zip(keys,nums))
    for indx, value in temp_dict.items():
        num_1 = value
        num_2 = target - num_1
        if num_2 in temp_dict.values() and indx not in temp:
            temp.append(indx)
            for key, num in temp_dict.items():
                if num_2 == num and key not in temp:
                    temp.append(key)
                    flag = 1
                    break
                else: flag = 0
            if flag == 0: temp.pop(len(temp)-1)
        else: continue
    return temp
                    
twoSum(nums,target)