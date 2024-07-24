class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mp={i:mapping[i] for i in range(10)}
        for i in range(len(nums)):
            tmp=""
            print(nums[i])
            for j in str(nums[i]):
                tmp+=str(mp[int(j)])
            nums[i]=[nums[i],int(tmp)]
        print(nums)
        sm = sorted(nums,key=lambda x:x[1])
        return [x[0] for x in sm]
        