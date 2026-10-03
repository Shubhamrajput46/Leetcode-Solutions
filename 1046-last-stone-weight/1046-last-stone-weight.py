import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        heap=[]

        for i in stones:
            heapq.heappush(heap,-i)

        while len(heap)>1:
            a=-heapq.heappop(heap)
            b=-heapq.heappop(heap)

            diff=a-b

            if diff!=0:
                heapq.heappush(heap,-diff)
                
        if len(heap)==0:
            return 0
        else:
            return -heap[0]

        