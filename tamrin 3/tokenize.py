__author__ = 'Mohammad ali'


class Tokenize():

    def get_tokens(self,str):
        n=''
        r=[]
        b=''
        count=0
        if str[0]=='(':
            r.append(str[0])
            str=str[1:]

        if str[-1]==')':
            str=str[:-1]
            b=')'

        for ch in str:
            if ch.isdigit():
                n+=ch
            else:
                if n!='':
                   r.append(n)
                r.append(ch)
                n=''
            count+=1
            if count==len(str):
                r.append(n)
        if b!='':
            r.append(b)
            # if ch in['+','-','*','/','%','(',')','^']:
            #    if n!='':
            #      r.append(n)
            #    r.append(ch)
            #    n=''
            # else:
            #     n+=ch
        return r