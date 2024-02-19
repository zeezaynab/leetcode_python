class solution(object):
    def PlusOne(self,digits):
        stop=len(digits)
        num=""
        for i in range(stop):
            num+= str(digits[i])
        num2=str(int(num)+1)
        list2=[]
        for i in num2:
            list2.append(int(i))
        return(list2)    

