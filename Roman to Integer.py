class Solution(object):
    def romanToInt(self, s):
        roman={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        s1=s[::-1]
        previous_value=0
        result=0
        for char in s1:
            value=roman[char]
            if value<previous_value:
                result=result-value
            else:
                result=result+value
            previous_value=value
        return result

