Class Solution(object):
     def lengthOfLastWord(self,s):
          w1=s.split()
          w2=w1[-1]
          return (len(w2))