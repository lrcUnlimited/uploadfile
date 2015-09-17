__author__ = 'li'
import requests, random, threading


url = "http://118.123.173.106/manager/picture/pictureUpload/upload"
cookies = dict(JSESSIONID='003C73333A202C8DE344358D38CD5F91', easyuiThemeName='default')


class UpLoadThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def get_random_word(self):
        rword = ""
        for i in range(0, 100):
            rword = rword + chr(random.randint(97, 122))
        return rword

    def run(self):
        upNum = 0
        while True:
            r = open('1.jpg', 'rb')
            f = {'file': r}
            imgDescription = {'plate': self.get_random_word(), 'position': self.get_random_word(),
                              'group': random.randint(1, 130)}
            upNum = upNum + 1
            try:
                r = requests.post(url, files=f, data=imgDescription, cookies=cookies)
                r.close()
                print("**********thread" + str(self.name) + "***********" + str(upNum))
            except Exception as e:
                print e
                r = requests.post(url, files=f, data=imgDescription, cookies=cookies)
                r.close()
                print("**********thread" + str(self.name) + "***********" + str(upNum))


for i in range(0, 10):
    upThread = UpLoadThread(i)
    upThread.start()