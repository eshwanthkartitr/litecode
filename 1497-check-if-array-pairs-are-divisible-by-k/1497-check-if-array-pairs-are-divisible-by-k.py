class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        cnt = 0
        arr_dict=defaultdict(int)
        for i in range(len(arr)):
            arr_dict[((arr[i]+k)+k)%k]+=1
        for i in range(k-1):
            if i ==0:
                if arr_dict[i]%2!=0:
                    return False
            elif arr_dict[i]!=arr_dict[k-i]:
                return False
        return True