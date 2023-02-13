#Importing all required modules/librarys
import os, shutil, colorama
from datetime import datetime
from colorama import Fore, Style
#Creating containing class
class LargestLogger:
    #Creating variable to store the current directory where logs will be stored
    LogDir = None
    #Function to clean up log files into a folder and name them by the time the first log was ran
    def StartUp(TestingMode:bool = False):
        #Initiates the colorama lib allowing coloured prints to run as intended
        colorama.init()
        #Stores the directory where the logs will be placed
        LargestLogger.LogDir = os.getcwd()
        #If a previos log is present
        if os.path.isfile(f"{LargestLogger.LogDir}/Latest.log"):
            #Create a "Logs" folder if one isnt present
            if not os.path.isdir(f"{LargestLogger.LogDir}/Logs"):
                os.mkdir(f"{LargestLogger.LogDir}/Logs")
            #Read the time the first log was ran to be placed in the name of the moved log file
            with open('Latest.log') as Log:
                NewName = Log.read(24)
                NewName = NewName.replace("[","").replace("]","").replace('/', '-').replace(':', '.')
            #Moves the old log into the folder and naming it appropriately by the date and time the first log was ran
            shutil.move(f"{LargestLogger.LogDir}/Latest.log",
                        f"{LargestLogger.LogDir}/Logs/{NewName}.log")
        #If the startup was ran in testing mode display an example of all possible logs
        if TestingMode:
            LargestLogger.Info("This is an Info test!")
            LargestLogger.Warning("This is an Warning test!")
            LargestLogger.Success("This is an Success test!")
            LargestLogger.Error("This is an Error test!")
        #Create a log to display the logger as ready
        LargestLogger.Success("LargestLogger running!")
    #Functions to be externally called to change the way logs are displayed and saved
    def Info(Log:str):
        LargestLogger.Output(0, Log)
    def Warning(Log:str):
        LargestLogger.Output(1, Log)
    def Success(Log:str):
        LargestLogger.Output(2, Log)
    def Error(Log:str):
        LargestLogger.Output(3, Log)
    #The main function all other log types call back to
    #It parses the data and prepares a string to be saved
    #And outputted appropriately
    def Output(LogType, Log):
        #Creates variables to be used later within the logging process
        Type = None
        TypeColour = None
        now = datetime.now()
        StringedNow = str(now.strftime("%d/%m/%Y %I:%M:%S %p"))
        #Depending on the passed in "LogType" a different colour and header text is set
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
        #Output the text generated into a "Latest.log" file
        with open(f"{LargestLogger.LogDir}/Latest.log", "a+", encoding="utf-8") as LogFile:
            LogFile.writelines(f"[{StringedNow}] {Type} {Log}\n")
        #Output the log into the console with correct formatting and colours
        print(f"[{Fore.GREEN}{StringedNow}{Style.RESET_ALL}] {TypeColour}{Type}{Style.RESET_ALL} {Log}")