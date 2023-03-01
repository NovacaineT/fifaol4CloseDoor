from closeDoor import *
import time

#这个文件主要是起到一个启动脚本然后控制时间的作用，具体的堵门逻辑在closeDoor里面

a = int(time.localtime()[3])%2 == 0 and int(time.localtime()[4]) == 0

if __name__ == "__main__":
    logFileDir = "和closeDoor文件里面的self.logFileDir一样就好了"
    logTxt = open("{}\\log.txt".format(logFileDir),"a")
    while(True):
        a = int(time.localtime()[3])%2 == 0 and int(time.localtime()[4]) == 0
        if(a):
            logTxt.write("{}年-{}月-{}日-{}时-{}分-{}秒".format(time.localtime()[0],time.localtime()[1],time.localtime()[2],time.localtime()[3],time.localtime()[4],time.localtime()[5])+"开始堵门\n")
            logTxt.flush()
            closeDoor()
            logTxt.write("{}年-{}月-{}日-{}时-{}分-{}秒".format(time.localtime()[0],time.localtime()[1],time.localtime()[2],time.localtime()[3],time.localtime()[4],time.localtime()[5])+"堵门完成\n")
            logTxt.flush()
        time.sleep(30)
        