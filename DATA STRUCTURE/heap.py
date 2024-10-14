import heapq
heap=[]
heapq.heappush(heap,1)
heapq.heappush(heap,100)
heapq.heappush(heap,2)
heapq.heappush(heap,3)
heapq.heappush(heap,4)
print(heapq.heappop(heap))
print('heap[0]',heap[0])
nums=[9,8,7,1,2,3,4,6,12]
print(nums)
heapq.heapify(nums)
print(nums)
