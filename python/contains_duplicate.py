def containsDuplicate(self, nums) -> bool:
       hashmap = dict()
       for i in range(len(nums)):
        if nums[i] in hashmap.keys():
            return True
        else:
            hashmap[nums[i]] = i
      
       return False
