__author__ = 'Mohammad ali'




def hegza(n):
    x=''
    if n==0:
        x='0'
    else:
        while (n>0):
             if n%16<10:
                x+=str(n%16)
             elif n%16==10:
                 x+='A'
             elif n%16==11:
                 x+='B'
             elif n%16==12:
                 x+='C'
             elif n%16==13:
                 x+='D'
             elif n%16==14:
                 x+='E'
             else:
                 x+='F'
             n=int(n/16)

    a=len(x)
    b=''
    while a>0:
       b+=x[a-1]
       a-=1
    return b


def main():
    print(hegza(45))
    print(hegza(74))
    print(hegza(15))
    print(hegza(30))
    print(hegza(32))

if __name__ == '__main__':
    main()