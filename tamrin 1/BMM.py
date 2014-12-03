from itertools import product

__author__ = 'Mohammad ali'



def bmm(a,b):
    if a!=0 and b!=0:
        a-=(int(a/b)*b)
        return bmm(b,a)
    elif a==0:
        if b==0:
            return a
        else:
            return b
    else:
        return a


def main():
    print(bmm(784,55))
    print(bmm(12,27))
    print(bmm(40,45))
    print(bmm(82,180))
    print(bmm(94,34))
    print(bmm(20,62))





if __name__ == '__main__':
    main()