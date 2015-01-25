import tornado

__author__ = 'mojtaba.banaie'


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        list1=[]
        with open('cntgb.txt',encoding='utf-8')as f:
            for l in f:
                list1.append(l)
        f.close()
        list2=[]
        with open('tenm.txt',encoding='utf-8')as f:
            for l in f:
                list2.append(l)
        f.close()
        list3=[]
        with open('tenb.txt',encoding='utf-8')as f:
            for l in f:
                list3.append(l)
        f.close()
        list4=[]
        with open('teng.txt',encoding='utf-8')as f:
            for l in f:
                list4.append(l)
        f.close()
        list5=[]
        with open('avg_age.txt',encoding='utf-8')as f:
            for l in f:
                list5.append(l)
        f.close()
        self.render('index.html',UN= "Hello!",list1=list1,list2=list2,list3=list3,list4=list4,list5=list5)
        # else :
        #     session.set('LoggedIn', {"_id":"12222222","name":"ali"})
        #     self.render('index.html',UN="U Are Not Logged In..")
