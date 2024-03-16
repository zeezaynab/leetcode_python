class Solution(object):
    def isPerfectSquare(self, num):
        sq = pow(num, 0.5)
        if int(sq) == sq:
            return True
        else:
            return False
