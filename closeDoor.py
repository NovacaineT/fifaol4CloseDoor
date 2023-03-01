import win32gui,win32con,win32api,win32com
import time
from PIL import ImageGrab,Image
import pytesseract
import requests

class closeDoor():


    def __init__(self):
        #临时截图存放位置，写绝对路径
        self.tempFileDir = "临时截图存放位置，写绝对路径"

        #堵门成功后截图存放位置，写绝对路径
        self.logFileDir = "堵门成功后截图存放位置，写绝对路径"

        self.main()

    
    #模拟鼠标点击
    def mouseClick(self,x,y):
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

    #模拟鼠标移动
    def mouseMove(self,x,y):
        win32api.SetCursorPos((x,y))

    #通过QQ小号发送堵门图片
    #userId输入要接收图片的QQ号
    def sendPic(self,sendMsg):
        host = "http://127.0.0.1:5700"
        userId = 12345677
        tempUrl = "{}{}?message_type={}&user_id={}&message={}".format(host,"/send_msg","private",userId,sendMsg)
        re = requests.get(tempUrl)
 
    #模拟键盘输入
    def keyboardInput(self,content):
        win32api.keybd_event(content, 0, 0, 0)
        win32api.keybd_event(content, 0, win32con.KEYEVENTF_KEYUP, 0)

    #根据像素获取颜色
    def getColor(self,x,y):
        color = ImageGrab.grab().getpixel((x,y))
        return str(color)

    #OCR识别中文
    def getWord(self,imgFile):
        text = pytesseract.image_to_string(Image.open("{}/{}.jpg".format(self.tempFileDir,imgFile)),lang="chi_sim+eng")
        text = text.replace(' ','').strip()
        return text

    #OCR识别英文
    def getWord2(self,imgFile):
        text = pytesseract.image_to_string(Image.open("{}/{}.jpg".format(self.tempFileDir,imgFile)))
        text = text.replace(' ','').strip()
        return text

    #OCR所需图片截图，
    def printScreen(self,x1,y1,x2,y2,n):
        img = ImageGrab.grab(bbox=(x1,y1,x2,y2))
        img.save('{}/{}.jpg'.format(self.tempFileDir,n))

    #堵门结束后截图保存
    def imgLogSave(self,x1,y1,x2,y2,type):
        img = ImageGrab.grab(bbox=(x1,y1,x2,y2))
        if (type == "buy"):
            tempFile = "{}年-{}月-{}日-{}时-{}分-购买成功.jpg".format(time.localtime()[0],time.localtime()[1],time.localtime()[2],time.localtime()[3],time.localtime()[4])
            butFileAll = "{}/".format(self.logFileDir)+tempFile
            img.save(butFileAll)
        elif (type == "get"):
            tempFile = "{}年-{}月-{}日-{}时-{}分-获得成功.jpg".format(time.localtime()[0],time.localtime()[1],time.localtime()[2],time.localtime()[3],time.localtime()[4])
            getFileAll = "{}/".format(self.logFileDir)+tempFile
            img.save(getFileAll)
        return tempFile

    def main(self):
        isOK = 0
        errNum = 0
        buyRgb = "(175, 1, 1)"
        greenRgb = "(165, 235, 13)"
        getRgb = "(148, 212, 13)"
        numEnue = {0:96,1:97,2:98,3:99,4:100,5:101,6:102,7:103,8:104,9:105}
        hwnd = win32gui.FindWindow("FIFAKC","FIFA ONLINE 4") 
        win32gui.SetForegroundWindow(hwnd)
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
        self.mouseClick(745,1010)
        while(True):
            self.printScreen(950,175,1025,205,1)
            tempText = self.getWord(1)
            if(tempText == "交易目录"):
                break
        self.mouseClick(990,190)
        time.sleep(1)
        self.printScreen(1107,258,1205,294,2)
        nowValue = self.getWord(2)
        while(True):
            while(True):
                self.mouseMove(957,337)
                time.sleep(0.1)
                self.mouseMove(957,282)
                time.sleep(0.2)
                greenColor = self.getColor(1497,277)
                if greenColor == greenRgb:
                    self.mouseClick(1497,277)
                    break
                else:
                    errNum+=1
                if errNum == 3:
                    errNum = 0
                    logDir = win32gui.FindWindow(None,"log") 
                    win32gui.SetForegroundWindow(logDir)
                    win32gui.ShowWindow(logDir, win32con.SW_MAXIMIZE)
                    win32gui.SetForegroundWindow(hwnd)
                    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
                    logTxt = open("{}\\log.txt".format(self.logFileDir),"a")
                    logTxt.write("{}年-{}月-{}日-{}时-{}分-{}秒".format(time.localtime()[0],time.localtime()[1],time.localtime()[2],time.localtime()[3],time.localtime()[4],time.localtime()[5])+"莫名其妙放大一次\n")
                    print("莫名其妙放大一次")
                    logTxt.flush()
                    logTxt.close()
            while(True):
                redColor = self.getColor(1139,808)
                getColor = self.getColor(1137,685)
                if(redColor == buyRgb):
                    while(True):
                        self.printScreen(1370,418,1448,452,3)
                        highValue = self.getWord2(3)
                        if(highValue == nowValue and isOK == 0 ):
                            if(int(time.localtime()[4])>30):
                                logTxt = open("{}\\log.txt".format(self.logFileDir),"a")
                                logTxt.write("{}年-{}月-{}日-{}时-{}分-{}秒".format(time.localtime()[0],time.localtime()[1],time.localtime()[2],time.localtime()[3],time.localtime()[4],time.localtime()[5])+"未变门\n")
                                try:
                                    self.sendPic("{}年-{}月-{}日-{}时-{}分-{}秒".format(time.localtime()[0],time.localtime()[1],time.localtime()[2],time.localtime()[3],time.localtime()[4],time.localtime()[5])+"未变门")
                                except:
                                    pass
                                logTxt.flush()
                                logTxt.close()
                                self.mouseClick(1369,810)
                                return True
                            self.mouseClick(1369,810)
                        elif(highValue == nowValue and isOK == 1 ):
                            isOK = 0
                            tempFileName = self.imgLogSave(362,183,1556,878,"buy")
                            time.sleep(0.5)
                            try:
                                sendMsg = "[CQ:image,file=file:///{}\\{},type=show,id=40000]".format(self.logFileDir,tempFileName)
                                self.sendPic(sendMsg)
                                sendMsg = "最高价：{}".format(str(highValue))
                                self.sendPic(sendMsg)
                            except Exception as errMsg:
                                pass
                            self.mouseClick(1369,810)
                            return True
                        else:
                            self.keyboardInput(numEnue[int(highValue[:1])])
                            self.keyboardInput(numEnue[int(highValue[1:2])])
                            self.keyboardInput(numEnue[int(highValue[2:])])
                            self.keyboardInput(13)
                            nowValue = highValue
                            isOK = 1
                        break
                    break
                elif(getColor == getRgb):
                    tempFileName = self.imgLogSave(529,300,1390,762,"get")
                    try:
                        self.sendPic(tempFileName)
                    except Exception as errMsg:
                        pass
                    self.mouseClick(1164,692)
                    exit(0)