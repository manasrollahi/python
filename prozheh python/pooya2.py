__author__ = 'Mohammad ali'

from pooyagrabber import PooyaGrabber
from statinfo import StatInfo

def ret_ten(dic):
    li=sorted(dic.values())
    li=li[-10:]
    # print(li)
    # i=len(li)-1
    list1=[]
    for i in li:
        for j in dic:
            if dic[j]==i:
                list1.insert(0,j)
                # i-=1
    # print(list1[:10])
    return list1[:10]


def main():
    s=StatInfo('output.txt')
    tp=s.getGirlBoyInfo()
    listm=s.getTopicStat()
    dboy=tp[len(tp)-2]
    dgirl=tp[len(tp)-1]

    with open("cntgb.txt",encoding='utf-8',mode='w') as f:
        f.write(str(tp[0])+'\n')
        f.write(str(tp[1])+'\n')
    f.close()

    # li=sorted(listm.values())
    # i=len(li)-1
    # list1=[]
    # for d in range(10):
    #     for j in listm:
    #         if listm[j]==li[i]:
    #             list1.append(j)
    #             i-=1
    list1=ret_ten(listm)
    # print(list1)
    with open("tenm.txt",encoding='utf-8',mode='w') as f:
        for i in list1:
            f.write(i+'\n')
    f.close()

    listb=ret_ten(dboy)
    with open("tenb.txt",encoding='utf-8',mode='w') as f:
        for i in listb:
            f.write(i+'\n')
    f.close()
    #
    listg=ret_ten(dgirl)
    with open("teng.txt",encoding='utf-8',mode='w') as f:
        for i in listg:
            f.write(i+'\n')
    f.close()

    listsen=[]
    with open("output.txt",encoding='utf-8') as f:
        for l in f:
            sh=""
            adad=""
            for i in l:
                if sh=="##":
                    if i!="#":
                        adad+=i
                if i=="#":
                    sh+=i
            listsen.append(int(adad))
            # print(adad)
    f.close()
    listsen=sorted(listsen)
    with open("avg_age.txt",encoding='utf-8',mode='w') as f:
        f.write(str(listsen[0])+'\n')
        f.write(str(listsen[-1])+'\n')
        sum=0
        for i in listsen:
            sum+=i
        f.write(str(sum/len(listsen))+'\n')
    f.close()


if __name__ == '__main__':
    main()