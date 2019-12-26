class Solution(object):
    def threeEqualParts(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        N = len(A)
        cnt = 0
        for i in range(N):
            if A[i]:
                cnt += 1
        if cnt%3:
            return [-1,-1]
        if cnt == 0:
            return [0,2]
        trail = 0
        for i in range(N-1,-1,-1):
            if A[i]:
                break
            trail += 1
        nums = [[] for x in range(3)]
        ind = 0
        cur = 0
        zro = 0
        ans = [0,0,0]
        for i in range(N):
            if A[i] == 1:
                cur += 1
            elif cur == cnt/3:
                zro += 1
            if cur:
                nums[ind].append(A[i])
            if cur == cnt/3 and zro == trail:
                ans[ind] = i
                ind += 1
                cur = 0
                zro = 0
            elif cur > cnt/3:
                return [-1,-1]
        if nums[0] == nums[1] == nums[2]:
            return [ans[0],ans[1]+1]
        return [-1,-1]
