__author__ = 'Mohammad ali'


from tokenize import Tokenize

class Process():


    def isDigit(self,str):
        if str.isdigit():
            return True
        elif len(str)>1:
            raise ValueError
        elif str in['+','-','*','/','%','(',')','^']:
            return False
        else:
            raise ValueError

    def olaviat(self,str):
        if str in ['*','/']:
            return 2
        elif str in ['+','-']:
            return 1
        else:
            return 0

    def checkstack(self,ostack,str):
        if str=='(':
            return True
        elif len(ostack)==0:
            return True
        elif ostack[-1]=='(':
            return True
        elif self.olaviat(str)>self.olaviat(ostack[-1]):
            return True
        else:
            return False

    def Apply(self,ostack,nstack):
        op=ostack[-1]
        ostack.pop(-1)
        n1=int(nstack[-1])
        n2=int(nstack[-2])
        nstack.pop(-1)
        nstack.pop(-1)
        if op=='+':
            nstack.append(n2+n1)
        elif op=='-':
            nstack.append(n2-n1)
        elif op=='*':
            nstack.append(n2*n1)
        elif op=='/':
            nstack.append(n2/n1)

        return


    def proces(self,str):
        t=Tokenize()
        list1=t.get_tokens(str)
        nstack=[]
        ostack=[]
        for i in list1:
            if self.isDigit(i):
                nstack.append(i)
            else:
                if self.checkstack(ostack,i):
                    ostack.append(i)
                else:
                    if i==')':
                        if ostack[-1]=='(':
                            ostack.pop(-1)
                        else:
                            while ostack[-1]!='(':
                                self.Apply(ostack,nstack)
                            ostack.pop(-1)
                    else:
                        self.Apply(ostack,nstack)
                        ostack.append(i)

        while len(ostack)>0:
            self.Apply(ostack,nstack)
        result='(%s) = %d' %(str,nstack[0])
        return result

p=Process()
print(p.proces('5+6-(2*6-3)/3'))
print(p.proces('12+2*6-(15/3*2)-7'))
print(p.proces('5/1-5+2*(7+2/2*7)-4/2'))
print(p.proces('(8/2*6)-4+(14*2)-50'))