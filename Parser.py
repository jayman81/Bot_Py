    
'''
    Parser File

    [S]    = Data for Server Control
        [1..n] = Server Option/Function Handle
    [M]    = Data for Movement Control
        [1..n] = Direction
                [0-254] = Speed
    [C]    = Data for Camera Control
        [1..n] = Camera Option/Function
    [I]    = Data for I2C Control
        [1..n] = Sensornumber
                [xxx] = SensorValues

'''



import socket, sys, signal, threading
from multiprocessing import Process, Queue
import server3
from server3 import *
#import _sysconfigdata_m

class ParserClass(object):
    def __init__(self, value):
        self.qParserIn = Queue()
        self.qParserOut = Queue()
        self.__sortedDataArray = [2]
        self.__recvData = ""
        self.__dataToSend = ""
        print ("__init__ Konstruktor \"", value, "\" done!")

# qIn = was vom Client kommt
# qOut = was zum Client gesendet werden soll

    def ParserWorker(self, qOut, qIn): # muss mit signals gemacht werden! 
        # damit die cpu nicht immer auf 100% rennt 
        print("ParserWorker")
        self.qServerIn = qIn # from server
        self.qServerOut = qOut # to server
        while 1:
            if self.qServerIn.empty() == False:
                self.setRecvData(self.qServerIn.get())
                self.setSortArray(self.getRecvData())
                self.setRecvData("")
            else:
                pass
            if self.getDataToSend() != "":
                try:
                    self.qServerOut.put(self.getDataToSend())
                except:
                    pass
            if self.__sortedDataArray != "":
                self.handleData()
            else:
                pass

    def setRecvData(self,data):
        self.__recvData = data
        
    def getRecvData(self):
        return self.__recvData

    def setSortArray(self, data):
        i=0
        data = data.split(";")
        self.__sortedDataArray = data[0].split(":")

    def handleData(self): #[S],[123]
        if self.getSortArray() != "":
            if (self.__sortedDataArray[0] == "S"):
                print("System Command")
                self.setDataToSend("S:ACK")
            elif (self.__sortedDataArray[0] == "M"):
                print("Movement Command")
            self.__sortedDataArray = ""
        else:
            pass

    def getSortArray(self):
        return self.__sortedDataArray

    def setDataToSend(self,data):
        self.__dataToSend = data

    def getDataToSend(self):
        return self.__dataToSend        
        
    def setInQueue(self):
        if self.getDataToSend()!= None:
            self.qParserIn.put(self.getDataToSend())
        else:
            print("No Data InQueue: No Data!")
        
    def getInQueue(self):
        return self.qParserIn.get()
        

