__author__ = 'Mohammad ali'


from bs4 import BeautifulSoup
import urllib3
import pickle

class StatInfo:

    def __init__(self,file_address):
        self.file_address=file_address


    def cleanData(self,name):
        if name[:4]=="سید ":
            name=name[4:]
        elif name[:5]=="سیده ":
            name=name[5:]
        elif name[:8]=="السادات ":
            name=name[8:]
        elif name[:6]=="سادات ":
            name=name[6:]
        elif name[4:]=="سید ":
            name=name[:4]
        elif name[5:]=="سیده ":
            name=name[:5]
        elif name[8:]=="السادات ":
            name=name[:8]
        elif name[6:]=="سادات ":
            name=name[:6]
        elif name[:3]=="سید":
            name=name[3:]
        elif name[:4]=="سیده":
            name=name[4:]
        elif name[:7]=="السادات":
            name=name[7:]
        elif name[:5]=="سادات":
            name=name[5:]
        elif name[3:]=="سید":
            name=name[:3]
        elif name[4:]=="سیده":
            name=name[:4]
        elif name[7:]=="السادات":
            name=name[:7]
        elif name[5:]=="سادات":
            name=name[:5]
        return name


    def getGirlBoyInfo(self):
        listBoy=[]
        with open("nameboy.txt",encoding="utf-8")as fb:
            for i in fb:
                listBoy.append(i[:-1])
        fb.close()

        listGirl=[]
        with open("namegirl.txt",encoding="utf-8")as fg:
            for i in fg:
                listGirl.append(i[:-1])
        fg.close()
        cntGirl=0
        cntBoy=0
        cntNune=0
        dboy={}
        dgirl={}
        with open(self.file_address,encoding="utf-8") as file:
            for l in file:
                name=""
                for i in l.split('#'):
                    name=i
                    break

                name = self.cleanData(name)
                if name in listBoy:
                    if name in dboy:
                        dboy[name]+=1
                    else:
                        dboy[name]=1
                    cntBoy+=1
                elif name in listGirl:
                    if name in dgirl:
                        dgirl[name]+=1
                    else:
                        dgirl[name]=1
                    cntGirl+=1
                else:
                    cntNune+=1

        file.close()
        # print(dboy)
        # print(dgirl)
        return cntBoy,cntGirl,cntNune,dboy,dgirl

    def getTopicStat(self):
        listmozooe={}
        with open(self.file_address,encoding="utf-8") as file:
            for l in file:
                mozooe=""
                sp=0
                for i in l.split('#'):
                    if i[-1]=="\n":
                        mozooe=i[:-1]
                    # else:
                    #     mozooe=i

                if mozooe in listmozooe.keys():
                    listmozooe[mozooe]+=1
                else:
                    listmozooe[mozooe]=1
        file.close()
        # for i,j in listmozooe.items():
        #     print("%s : %s"%(i,j))
        return listmozooe

# s=StatInfo('output.txt')
# with open(s.file_address,encoding="utf-8") as file:
#     for l in file:
#         d=""
#         name=""
#         family=""
#         for i in l:
#             if i=="#":
#                 d+=i
#             if d=="":
#                 name+=i
#             elif d=="#" and i!="#":
#                 family+=i
#         print(s.cleanData(name))
#         print(s.cleanData(family))
#         print("**************************************")
# file.close()
# s.getTopicStat()
# print(s.getGirlBoyInfo())