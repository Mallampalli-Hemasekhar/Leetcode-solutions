class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        a={'a':26,'b':25,'c':24,'d':23,'e':22,'f':21,'g':20,'h':19,'i':18,'j':17,'k':16,'l':15,'m':14,'n':13,'o':12,'p':11,'q':10,'r':9,'s':8,'t':7,'u':6,'v':5,'w':4,'x':3,'y':2,'z':1}
        in_str=[]
        in_alp=[]
        k=1
        product=[]
        for i in s:
            if i in a:
                in_alp.append(a[i])
                in_str.append(k)
            k+=1
        l=0
        t=0
        for i in range(len(in_str)):
            t=in_str[i]*in_alp[i]
            product.append(t)
        d=sum(product)
        return d