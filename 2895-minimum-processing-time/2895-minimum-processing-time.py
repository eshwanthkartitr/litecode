class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse=True)
        bi = len(processorTime)
        cnt=0
        final=0
        for i in range(bi):
            cnt=0
            for m in range(4):
                cnt=max(processorTime[i]+tasks[m+i*4],cnt)
            final=max(final,cnt)
        return final