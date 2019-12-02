class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        arr = intervals
        cur = newInterval
        N = len(intervals)
        res = []
        for i in range(N):
            if cur[1] < arr[i][0]:
                res.append(cur)
                res = res + arr[i:]
                return res
            if cur[0] <= arr[i][1]:
                cur = [min(cur[0],arr[i][0]),max(cur[1],arr[i][1])]
            else:
                res.append(arr[i])
        res.append(cur)
        return res
