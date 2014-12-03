__author__ = 'Mohammad ali'


def day_month(n):
    if n>365:
        n%=365
    m=int(n/30)
    if n%30==0:
        n-=(m-1)
    else:
        n-=m
    m=(int(n/30)+1)
    d=int(n%30)
    if d==0:
        if m<=6:
            d=31
        else:
            d=30
    m1=''
    if m==1:
        m1='farvardin'
    elif m==2:
        m1='ordibehesht'
    elif m==3:
        m1='khordad'
    elif m==4:
        m1='tir'
    elif m==5:
        m1='mordad'
    elif m==6:
        m1='shahrivar'
    elif m==7:
        m1='mehr'
    elif m==8:
        m1='aban'
    elif m==9:
        m1='azar'
    elif m==10:
        m1='day'
    elif m==11:
        m1='bahman'
    elif m==12:
        m1='esfand'

    return d,m1



def main():
    print(day_month(485))
    print(day_month(48))
    print(day_month(9))
    print(day_month(84))
    print(day_month(215))


if __name__ == '__main__':
    main()