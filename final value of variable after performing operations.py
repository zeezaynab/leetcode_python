class Solution(object):
    def FinalValueAfterOperations(self,oper):
        x=0
        oper=["--x","++x","++x","--x"]
        for i in oper:
            if i[0]=="+" or i[2]=="+":
                x+=1
            elif i[0] == "-" or i[2] == "-":
                x-=1
        return(x)