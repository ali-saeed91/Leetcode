class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        ans = []
        s= Counter(nums)
        # print(s)
        for num,freq in s.items():
            maxHeap.append([-freq, num])
        # print(maxHeap)
        heapify(maxHeap)
        # print(maxHeap)
        for i in range(k):
            freq, num = heappop(maxHeap)
            ans.append(num)
            # print(maxHeap)
        return (ans)