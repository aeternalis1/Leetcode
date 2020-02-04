class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        ans = 0
        N = len(row)
        for i in range(N/2):
            if row[i*2]/2 != row[i*2+1]/2:
                for j in range(i*2+2, N):
                    if row[j]/2 == row[i*2]/2:
                        row[i*2+1], row[j] = row[j], row[i*2+1]
                        ans += 1
                        break
        return ans
