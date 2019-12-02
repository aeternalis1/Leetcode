def s_split(s):
    cnt = 0
    arr = []
    tmp = []
    for i in s:
        tmp.append(i)
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt -= 1
            if not cnt:
                if i == ',':
                    tmp = []
                    continue
                arr.append("".join(tmp))
                tmp = []
        elif not cnt and (i == 't' or i == 'f'):
            tmp = []
            arr.append(i)
    return [x.strip(',') for x in arr]

    
class Solution(object):
    def parseBoolExpr(self, expression):
        """
        :type expression: str
        :rtype: bool
        """
        def AND(s):
            arr = s_split(s)
            res = 1
            for i in arr:
                if len(i) == 1:
                    if i == 'f':
                        return False
                else:
                    if i[0] == '&':
                        res &= AND(i[2:-1])
                    elif i[0] == '|':
                        res &= OR(i[2:-1])
                    else:
                        res &= NOT(i[2:-1])
            return res
        
        def OR(s):
            arr = s_split(s)
            res = 0
            for i in arr:
                if len(i) == 1:
                    if i == 't':
                        return True
                else:
                    if i[0] == '&':
                        res |= AND(i[2:-1])
                    elif i[0] == '|':
                        res |= OR(i[2:-1])
                    else:
                        res |= NOT(i[2:-1])
            return res
        
        def NOT(i):
            if len(i) == 1:
                if i == 't':
                    return False
                elif i == 'f':
                    return True
            else:
                if i[0] == '&':
                    return True^AND(i[2:-1])
                elif i[0] == '|':
                    return True^OR(i[2:-1])
                else:
                    return True^NOT(i[2:-1])
        
        if len(expression) == 1:
            if expression == 't':
                return True
            else:
                return False
        else:
            if expression[0] == '&':
                return AND(expression[2:-1])
            elif expression[0] == '|':
                return OR(expression[2:-1])
            else:
                return NOT(expression[2:-1])
        
