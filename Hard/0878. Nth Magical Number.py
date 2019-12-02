def get_gcd(a,b):
    if b == 0:
        return a
    return get_gcd(b,a%b)

class Solution(object):
    def nthMagicalNumber(self, N, A, B):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        gcd = get_gcd(A,B)
        lcm = A*B/gcd
        lo = 1
        hi = pow(10,18)
        while lo < hi:
            mid = (lo+hi)/2
            cur = mid/A + mid/B - mid/lcm
            if cur >= N:
                hi = mid
            else:
                lo = mid+1
        return lo%(pow(10,9)+7)
