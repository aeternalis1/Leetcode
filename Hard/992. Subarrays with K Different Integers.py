class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        N = len(A)
        nums = A
        f1 = [0 for x in range(N+1)]
        f2 = [0 for x in range(N+1)]
        cnt1 = 1
        cnt2 = 1
        r1 = 0
        r2 = 0
        f1[nums[0]] = 1
        f2[nums[0]] = 1
        ans = 0
        for i in range(N):
            while r1 < N-1 and cnt1 < K:
                r1 += 1
                f1[nums[r1]] += 1
                if f1[nums[r1]] == 1:
                    cnt1 += 1
            while r2 < N-1 and cnt2 <= K:
                r2 += 1
                f2[nums[r2]] += 1
                if f2[nums[r2]] == 1:
                    cnt2 += 1
            if cnt2 == K:
                ans += N-r1
            else:
                ans += r2-r1
            f1[nums[i]] -= 1
            f2[nums[i]] -= 1
            if not f1[nums[i]]:
                cnt1 -= 1
            if not f2[nums[i]]:
                cnt2 -= 1
        return ans
