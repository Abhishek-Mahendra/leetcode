class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if(int(num1)==0 or int(num2)==0):
            return '0'
        m=len(num1)
        n=len(num2)
        i=n-1
        x=m+n
        res=[0]*x
        pf=0
        while(i>=0):
            ival=ord(num2[i])-48
            i+=-1
            carry=0
            j=m-1
            k=len(res)-1-pf
            while(j>=0 or carry!=0):
                if j>=0:
                    jval=ord(num1[j])-48
                else:
                    jval=0
                prod=ival*jval + carry + res[k]
                res[k]=prod%10
                carry=prod//10
                k+=-1
                j+=-1
            pf+=1
        flag=0
        i=0
        s=''
        while(res[i]==0):
            i+=1
        for i in range(i,len(res)):
            s=s+str(res[i])
        return s
