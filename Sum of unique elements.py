class Solutions(object):
    def sumOfUnique(self,nums):
        list1=[]
        for i in nums:
           if nums.count(i)==1:
               list1.append(i)
        return(sum(list1))
