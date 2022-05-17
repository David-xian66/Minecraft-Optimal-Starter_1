import requests
from PyQt6.QtCore import *
import sys
a_1 = 1
b_1 = 1
c_1 = 1
d_1 = 1
e_1 = 1
f_1 = 1
g_1 = 1
h_1 = 1
i_1 = 1
j_1 = 1
k_1 = 1

#url2 = 'https://91.132.59.77/MOS/MOS00.html'

# url2 = 'https://api.xiaoyistudio.top/MOS/MOS000.html'

url2 = 'http://129.226.30.17'


url = 'http://129.226.30.17'

# url = 'https://api.xiaoyistudio.top/MOS/MOS000.html'

# url = 'https://91.132.59.77/MOS/MOS00.html'

class Thread(QThread):
    def __init__(self):
        super(Thread,self).__init__()
    def run(self):
        while a_1 <= 1:
            try:
                r=strhtml = requests.get(url, verify = False)
                r2=strhtml = requests.get(url2, verify = False)
            except requests.exceptions.ConnectionError:
                print("1号错误")
            print("ok!1")
            Thread.msleep(0)



class Thread_1(QThread):
    def __init__(self):
        super(Thread_1,self).__init__()
    def run(self):
        while b_1 <= 1:
            try:
                r=strhtml = requests.get(url, verify = False)
                r2=strhtml = requests.get(url2, verify = False)
            except requests.exceptions.ConnectionError:
                print("2号错误")
            print("ok!2")
            Thread_1.msleep(1)



class Thread_2(QThread):
    def __init__(self):
        super(Thread_2,self).__init__()
    def run(self):
        while c_1 <= 1:
            try:
                r=strhtml = requests.get(url, verify = False)
                r2=strhtml = requests.get(url2, verify = False)
            except requests.exceptions.ConnectionError:
                print("3号错误")
            print("ok!3")
            Thread_2.msleep(7)




class Thread_3(QThread):
    def __init__(self):
        super(Thread_3,self).__init__()
    def run(self):
        while d_1 <= 1:
            try:
                r=strhtml = requests.get(url, verify = False)
                r2=strhtml = requests.get(url2, verify = False)
            except requests.exceptions.ConnectionError:
                print("4号错误")
            print("ok!4")
            Thread_3.msleep(3)




class Thread_4(QThread):
    def __init__(self):
        super(Thread_4,self).__init__()
    def run(self):
        while e_1 <= 1:
            try:
                r=strhtml = requests.get(url, verify = False)
                r2=strhtml = requests.get(url2, verify = False)
            except requests.exceptions.ConnectionError:
                print("5号错误")
            print("ok!5")
            Thread_4.msleep(2)




class Thread_5(QThread):
    def __init__(self):
        super(Thread_5,self).__init__()
    def run(self):
        while f_1 <= 1:
            try:
                r=strhtml = requests.get(url, verify = False)
                r2=strhtml = requests.get(url2, verify = False)
            except requests.exceptions.ConnectionError:
                print("6号错误")
            print("ok!6")
            Thread_5.msleep(2)



class Thread_6(QThread):
    def __init__(self):
        super(Thread_6,self).__init__()
    def run(self):
        while g_1 <= 1:
            try:
                r=strhtml = requests.get(url, verify = False)
                r2=strhtml = requests.get(url2, verify = False)
            except requests.exceptions.ConnectionError:
                print("7号错误")
            print("ok!7")
            Thread_6.msleep(2)



class Thread_7(QThread):
    def __init__(self):
        super(Thread_7,self).__init__()
    def run(self):
        while h_1 <= 1:
            try:
                r=strhtml = requests.get(url, verify = False)
                r2=strhtml = requests.get(url2, verify = False)
            except requests.exceptions.ConnectionError:
                print("8号错误")
            print("ok!8")
            Thread_7.msleep(2)



class Thread_8(QThread):
    def __init__(self):
        super(Thread_8,self).__init__()
    def run(self):
        while i_1 <= 1:
            try:
                r=strhtml = requests.get(url, verify = False)
                r2=strhtml = requests.get(url2, verify = False)
            except requests.exceptions.ConnectionError:
                print("9号错误")
            print("ok!9")
            Thread_8.msleep(2)




class Thread_9(QThread):
    def __init__(self):
        super(Thread_9,self).__init__()
    def run(self):
        while j_1 <= 1:
            try:
                r=strhtml = requests.get(url, verify = False)
                r2=strhtml = requests.get(url2, verify = False)
            except requests.exceptions.ConnectionError:
                print("10号错误")
            print("ok!10")
            Thread_9.msleep(2)



class Thread_10(QThread):
    def __init__(self):
        super(Thread_10,self).__init__()
    def run(self):
        while k_1 <= 1:
            try:
                r=strhtml = requests.get(url, verify = False)
                r2=strhtml = requests.get(url2, verify = False)
            except requests.exceptions.ConnectionError:
                print("11号错误")
            print("ok!11")
            Thread_10.msleep(3)


if __name__=='__main__':
    from PyQt6.QtWidgets import *
    app =QApplication(sys.argv)
    thread =Thread()
    thread_1 =Thread_1()
    thread_2 =Thread_2()
    thread_3 =Thread_3()
    thread_4 =Thread_4()
    thread_5 =Thread_5()
    thread_6 =Thread_6()
    thread_7 =Thread_7()
    thread_8 =Thread_8()
    thread_9 =Thread_9()
    thread_10 =Thread_10()
    thread.start()
    thread_1.start()
    thread_2.start()
    thread_3.start()
    thread_4.start()
    thread_5.start()
    thread_6.start()
    thread_7.start()
    thread_8.start()
    thread_9.start()
    thread_10.start()
    sys.exit(app.exec())
