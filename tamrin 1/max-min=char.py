__author__ = 'Mohammad ali'


def mmc(a):
    dic={}
    for j in a:
        if j in dic.keys():
            dic[j]+=1
        else:
            dic[j]=1
    dic1=sorted(dic.values())
    print(sorted(dic.items()))
    for i in dic.keys():
        if dic[i]==dic1[0]:
            min=i
        elif dic[i]==dic1[-1]:
            max=i
    return min,max

def main():
    print(mmc('akgzmashzssbhrfsbrcraucejcaujmshjgdzjuedjdacrfa'))
    print(mmc('mohammad'))
    print(mmc('alirezaalifff'))
    print(mmc('hasanhosain'))
    print(mmc('googleg'))


if __name__ == '__main__':
    main()