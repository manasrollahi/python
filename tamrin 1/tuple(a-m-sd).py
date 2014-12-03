from math import sqrt

__author__ = 'Mohammad ali'

import math

def tup(a):
    n=len(a)
    if n==0:
        return None,None,None
    elif n==1:
        return a[0],a[0],None
    else:
        avg=sum(a)/n
        if n%2!=0:
            mid=a[int(n/2)]
        else:
            mid=(a[int((n/2)-1)]+a[int(n/2)])/2
        a1=[(i-avg)**2 for i in a]
        s=(sum(a1))/(n-1)
        sd=sqrt(s)
        return avg,mid,sd


def main():
    print (tup([42,7,12,3,1]))
    print (tup([5,2,8,11,13,31]))
    print (tup([4,21,12,9,4]))
    print (tup([1,6,15,71,4,41,24,18]))
    print (tup([5,7,12]))
    print (tup([5]))
    print (tup([]))

if __name__ == '__main__':
        main()