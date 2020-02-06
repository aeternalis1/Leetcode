def solve(formula):
    res = {}
    n = len(formula)
    i = 0
    lets = "abcdefghijklmnopqrstuvwxyz"
    while i < n:
        if formula[i] == '(':
            cnt = 1
            i += 1
            j = i
            while i < n:
                if formula[i] == '(':
                    cnt += 1
                elif formula[i] == ')':
                    cnt -= 1
                if cnt == 0:
                    break
                i += 1
            cur = solve(formula[j:i])
            i += 1
        else:
            temp = formula[i]
            i += 1
            while i < n and formula[i] in lets:
                temp = temp+formula[i]
                i += 1
            cur = {temp:1}
        mult = 0
        while i < n and formula[i].isdigit():
            mult *= 10
            mult += int(formula[i])
            i += 1
        mult = max(mult, 1)
        for key in cur:
            if key in res:
                res[key] += cur[key] * mult
            else:
                res[key] = cur[key] * mult
    return res


class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        ans = solve(formula)
        res = []
        for key in ans:
            if ans[key] == 1:
                res.append([key,""])
            else:
                res.append([key,ans[key]])
        return "".join([i[0]+str(i[1]) for i in sorted(res)])
