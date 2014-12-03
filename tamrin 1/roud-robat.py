__author__ = 'Mohammad ali'


def roud(a):
    i=0
    j=0
    r=0
    l=0
    u=0
    d=0
    list=[]
    for k in a:
        if k=='r':
            i+=1
            r+=1
        elif k=='l':
            i-=1
            l+=1
        elif k=='u':
            j+=1
            u+=1
        else:
            j-=1
            d+=1
        p=(i,j)
        list.append(p)
    dict={}
    for ij in list:
        if ij in dict.keys():
            dict[ij]+=1
        else:
            dict[ij]=1
    print(list)
    print(dict.items())
    return


def main():
    print(roud(['r','u','l','d','d','d','l','u','r','d','d','l','l','u','u']))
    print(roud(['l','u','r','r','d','l','r','u','u','l','l','l','r','u','d']))
    print(roud(['u','l','l','d','u','d','l','u','d','l','l','u','r','l','d']))
    print(roud(['d','r','d','u','d','d','r','u','u','l','l','l','r','u','d']))
    print(roud(['r','d','u','d','d','d','r','u','u','l','l','l','r','u','d']))


if __name__ == '__main__':
    main()