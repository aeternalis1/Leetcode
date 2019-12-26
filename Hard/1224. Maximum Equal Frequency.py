class Solution(object):
    def maxEqualFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        freq = [0 for x in range(100001)]
        cnt = [0 for x in range(100001)]
        unique = 0
        ans = 1
        lst = [[0,0] for x in range(3)]
        for i in range(N):
            if not freq[nums[i]]:
                unique += 1
            freq[nums[i]] += 1
            cnt[freq[nums[i]]-1] -= 1
            cnt[freq[nums[i]]] += 1
            for j in range(3):
                if lst[j][0] == freq[nums[i]]:
                    lst[j][1] += 1
                elif lst[j][0] == freq[nums[i]]-1:
                    lst[j][1] -= 1
            lst[i%3] = [freq[nums[i]], cnt[freq[nums[i]]]]
            if cnt[freq[nums[i]]] == 1 and cnt[freq[nums[i]]-1] == unique-1:
                ans = i
            elif cnt[freq[nums[i]]+1] == 1 and cnt[freq[nums[i]]] == unique-1:
                ans = i
            elif freq[nums[i]] == 1 and cnt[1] == unique:
                ans = i
            elif cnt[1] == 1 and unique-1 in [lst[0][1], lst[1][1], lst[2][1]]:
                ans = i
        return ans+1
