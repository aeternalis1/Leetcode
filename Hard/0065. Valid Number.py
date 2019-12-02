class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        nums = '0123456789'

        if s.count('e'):
            s = s.split('e')
            if len(s) != 2:
                return False
        else:
            s = [s]
        two = 0
        for i in s:
            if i.count('+') or i.count('-'):
                if i[0] == '+' or i[0] == '-':
                    i = i[1:]
                else:
                    return False
            f = 0
            if i.count('.'):
                if two:
                    return False
                while i[0] in nums:
                    f = 1
                    i = i[1:]
                if i[0] != '.':
                    return False
                i = i[1:]
                for j in i:
                    if j not in nums:
                        return False
                    f = 1
            else:
                for j in i:
                    if j not in nums:
                        return False
                    f = 1
            if not f:
                return False
            two = 1
        return True
