__author__ = 'Mohammad ali'

from bs4 import BeautifulSoup
import urllib3
import codecs



class PooyaGrabber:

    def __init__(self,url,file_address):
        self.url = url
        self.file_address=file_address


    def getImageList(self,url):
        page = urllib3.PoolManager()
        r = page.request("GET",url)
        soup = BeautifulSoup(r.data)
        link1 = soup.find_all("h3",{"class":"catItemTitle"})
        link="http://www.pooyatv.ir"
        list=[]
        for l in link1:
            list.append(link+l.a['href'])
        return list


    def Delprime(self,s):
        if s[0]==" ":
            return s[1:]
        elif s[-1]==" ":
            return s[:-1]
        else:
            return s



    def getImageInfo(self,LinkImg):
        page = urllib3.PoolManager()
        item=page.request("GET",LinkImg)
        newsoup=BeautifulSoup(item.data)
        names=newsoup.find("div",{"class":"itemBody"})
        strng=""
        fn=""
        ln=""
        age=""
        mozooe=""
        cnt=0
        names=str(names)

        for i in names:
            if strng[-10:]=="</strong>:":
                if i!="<":
                    if cnt==0:
                        fn+=i
                    elif cnt==1:
                        ln+=i
                    elif cnt==2:
                        age+=i
                    else:
                        mozooe+=i
                else:
                    strng+=i
                    cnt+=1
            else:
                strng+=i

        age1=int(age)
        fn1=self.Delprime(fn)
        ln1=self.Delprime(ln)
        mozooe1=self.Delprime(mozooe)
        with open(self.file_address,encoding="utf-8",mode="a") as file:
            sline="%s#%s#%d#%s\n"%(fn1,ln1,age1,mozooe1)
            file.write(str(sline))
        file.close()
        print(" نام : %s "%(fn))
        print(" نام خانوادگی : %s "%(ln))
        print(" سن : %d "%(age1))
        print(" موضوع : %s "%(mozooe))
        print("***************************************")


    def grabImages(self,n,startpage=0):
        page_s="http://www.pooyatv.ir/naghashi?start="+str(startpage*20)
        page = urllib3.PoolManager()
        r = page.request("GET",page_s)
        soup = BeautifulSoup(r.data)

        cnt=0
        list=[]
        while len(list)<n:
            list.extend(self.getImageList(page_s))
            link = soup.find("li",{"class":"pagination-next"})
            page_s="http://www.pooyatv.ir"+link.a['href']
            page = urllib3.PoolManager()
            r = page.request("GET",page_s)
            soup = BeautifulSoup(r.data)

        while cnt<n:
            self.getImageInfo(list[cnt])
            cnt+=1

#
p=PooyaGrabber("http://www.pooyatv.ir/naghashi?limitstart=0",'output.txt')
p.grabImages(20)
list=p.getImageList(p.url)
for l in list:
    p.getImageInfo(l)