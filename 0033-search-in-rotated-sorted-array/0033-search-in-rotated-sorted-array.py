class Solution:
    def search(self, arr: List[int], target: int) -> int:
        left=0
        right=len(arr)-1
        while left<=right:
            mid=(left+right)//2
            if arr[mid]==target:
                return mid
            if arr[left]<=arr[mid]:
                if arr[left]<=target and target<arr[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if arr[right]>=target and target>arr[mid]:
                    left=mid+1
                else:
                    right=mid-1
        return -1