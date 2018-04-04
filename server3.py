
#!/usr/bin/env python3
#-*- coding: utf-8 -*-




import socket, sys, signal, threading, time
from multiprocessing import Process, Queue
import Parser
import Movement
from symbol import except_clause



class ServerClass():
    def __init__(self, parent=None):
        super(ServerClass, self).__init__(parent)
        self.parent = parent
        print("Python Version: ", sys.version)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.HOST = "127.0.0.1"
        self.PORT = 50007
        self.qParserIn = Queue()
        self.qParserOut = Queue()
        self.qMovementIn = Queue()
        self.qMovementOut = Queue()
        self.qI2CIn = Queue()
        self.qI2COut = Queue()
        self.qCameraIn = Queue()
        self.qCameraOut = Queue()
                
        self.connection = 0;
        
        ''' +++++++++++++ Start the Parser Process ++++++++++++++++++++ '''
        #p = Parser.ParserClass("Parser")
        #self.processParser = Process(target=p.ParserWorker, args=(self.qParserIn, self.qParserOut))
        #self.processParser.demon = True
        #self.processParser.start()

        ''' +++++++++++++ Start the Movement Process ++++++++++++++++++++ '''
        #m = Movement.MovementClass("Movement")
        #self.processMovement = Process(target=m.MovementWorker, args=(self.qMovementIn, self.qMovementOut))
        #self.processMovement.demon = True
        #self.processMovement.start()
        

    def ServerRun(self):
        print("Server Run")
        while True:
            if (self.connection == 0):
                try:
                    self.s.bind((self.HOST, self.PORT)) 
                    self.s.listen(1)
                    clientsocket, addr = self.s.accept()
                    if (addr != 0):
                        self.connection = 1;
                        print('Connected by:', addr)
                        data = "Bot online"
                        clientsocket.send(data.encode())
                        continue
                except:
                    self.serverSleep() #TODO
                    continue
            else:
                try:
                    data = clientsocket.recv(1024).decode()
                
                    if not data:
                        self.serverSleep()
                        continue
                    else:
                        self.setInQueue(str(data))
                except:
                    self.serverSleep()
                    continue
        
        print ("quit while")
        self.close_application()
    #                 if str(data) == "q":
#                     print("Received q: ", str(data))
#                 
#                     
#                 elif str(data) == "s":
#                     clientsocket.send(data.encode())
#                     print("Send: ", data)                    
#                     print("Received a: ", str(data))
#                 else:
#                     print("Received else: ", str(data))
#                     continue                        

    def serverSleep(self): #TODO
        if cnt == 20:
            sys.stdout.write('\n')
            cnt = 0
        cnt = cnt+1
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(0.1)


    def setInQueue(self, data):
        self.qParserIn.put(data)
        
    def getOutQueue(self):
        if self.qParserOut.empty()==False:
            return self.qParserOut.get()
        else: 
            print("OutQueue is empty!")

    def close_application(self):
        if self.processTCP.is_alive():
            self.processTCP.terminate()
        else:
            pass
#            if self.processLogic.is_alive():
#                self.processLogic.terminate()
#            if self.processCamera.is_alive():
#                self.processCamera.terminate()
        clientsocket.close()  # beendet verbindung und gibt port frei
        sys.exit()

if __name__ == '__main__':
    #signal.signal(signal.SIGINT, signalInterrupt_handler)  
    run = ServerClass.ServerRun()
    run.ServerRun()





    