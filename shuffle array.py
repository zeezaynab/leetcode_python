class Solution(object):
    def shuffleArray(self,num,n):
        list=[]
        for i in n:
            list.append(num[i])
            list.append(num[n+i])
        return(list)


