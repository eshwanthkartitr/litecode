class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        # def backtrack(li1,li2,i):
        #     nonlocal tmp2
        #     if(len(li1)>(n//2)): return
        #     if(len(li2)>(n//2)): return
            
        #     if(len(li1) == (n//2) and len(li2) == (n//2)):
        #         tmp2.append(abs(sum(li1) - sum(li2)))
        #         return
        #     if(i==n):
        #         return
            
        #     li1.append(nums[i])
        #     backtrack(li1,li2,i+1)
        #     li1.pop()
        #     li2.append(nums[i])
        #     backtrack(li1,li2,i+1)
        #     li2.pop()
        #     return
            
        # backtrack([],[],0)
        tmp = []
        def backtrack(req1,req2,tmp1,tmp2):
            nonlocal tmp
            if(req1 <0 or req2 < 0):
                return
            if(req1==0 and req2==0):
                print(tmp1,tmp2)
                tmp.append(abs(tmp1-tmp2))
                return
            for i in range(n//2):
                tmp1+=left[i]
                backtrack(req1-1,req2,tmp1,tmp2)
                tmp1-=left[i]
            
            for i in range(n//2):
                tmp2+=right[i]
                backtrack(req1,req2-1,tmp1,tmp2)
                tmp2-=right[i]
            return

        n = len(nums)
        total = sum(nums)
        left = nums[:n//2]
        right = nums[n//2:]
        size = n // 2
        left_sums = {k: [] for k in range(size+1)}
        right_sums = {k: [] for k in range(size+1)}
        for k in range(size+1):
            for comb in combinations(left, k):
                left_sums[k].append(sum(comb))

        for k in range(size+1):
            for comb in combinations(right, k):
                right_sums[k].append(sum(comb))
            right_sums[k].sort()

        ans = float('inf')

        for k in range(size+1):
            for left_sum in left_sums[k]:
                target = total//2 - left_sum
                arr = right_sums[size-k]
                idx = bisect_left(arr, target)
                for j in [idx-1, idx]:
                    if 0 <= j < len(arr):
                        curr_sum = left_sum + arr[j]
                        diff = abs(total - 2*curr_sum)
                        ans = min(ans, diff)
        return ans