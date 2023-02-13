import os, shutil, colorama
from datetime import datetime
from colorama import Fore, Style
class LargestLogger:
    TestingMode = None
    LogDir = None
    def StartUp(TestingMode:bool = False):
        LargestLogger.TestingMode = TestingMode
        colorama.init()
        LargestLogger.LogDir = os.getcwd()
        if os.path.isfile(f"{LargestLogger.LogDir}/Latest.log"):
            if not os.path.isdir(f"{LargestLogger.LogDir}/Logs"):
                os.mkdir(f"{LargestLogger.LogDir}/Logs")
            with open('Latest.log') as Log:
                NewName = Log.read(24)
                NewName = NewName.replace("[","").replace("]","").replace('/', '-').replace(':', '.')
            shutil.move(f"{LargestLogger.LogDir}/Latest.log",
                        f"{LargestLogger.LogDir}/Logs/{NewName}.log")
        if LargestLogger.TestingMode:
            LargestLogger.Info("This is an Info test!")
            LargestLogger.Warning("This is an Warning test!")
            LargestLogger.Success("This is an Success test!")
            LargestLogger.Error("This is an Error test!")
    def Info(Data:str):
        LargestLogger.Output(0, Data)
    def Warning(Data:str):
        LargestLogger.Output(1, Data)
    def Success(Data:str):
        LargestLogger.Output(2, Data)
    def Error(Data:str):
        LargestLogger.Output(3, Data)
    def Output(LogType, Data):
        Type = None
        TypeColour = None
        now = datetime.now()
        StringedNow = str(now.strftime("%d/%m/%Y %I:%M:%S %p"))
        match LogType:
            case 0:
                Type = "Info:          "
                TypeColour = Fore.WHITE
            case 1:
                Type = "Warning:       "
                TypeColour = Fore.YELLOW
            case 2:
                Type = "Success:       "
                TypeColour = Fore.GREEN
            case 3:
                Type = "Error:         "
                TypeColour = Fore.RED
        with open(f"{LargestLogger.LogDir}/Latest.log", "a+", encoding="utf-8") as LogFile:
            LogFile.writelines(f"[{StringedNow}] {Type} {Data}\n")
        print(f"[{Fore.GREEN}{StringedNow}{Style.RESET_ALL}] {TypeColour}{Type}{Style.RESET_ALL} {Data}")