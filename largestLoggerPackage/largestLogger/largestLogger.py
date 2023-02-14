#Importing all required modules/librarys
import os, shutil, colorama
from datetime import datetime
from colorama import Fore, Style
#Creating containing class
class largestLogger:
    #Creating variable to store the current directory where logs will be stored
    logDir = None
    #Creating variables to be used in the debug scope
    debugMode = None
    debugValue = None
    #Function to clean up log files into a folder and name them by the time the first log was ran
    def startUp(debugMode:bool = False, debugValue:int = 0, testingMode:bool = False):
        #Initiates the colorama lib allowing coloured prints to run as intended
        colorama.init()
        #Stores the directory where the logs will be placed
        largestLogger.logDir = os.getcwd()
        #Stores the values to be used within the debug system
        largestLogger.debugMode = debugMode
        largestLogger.debugValue = debugValue
        #If a previos log is present
        if os.path.isfile(f"{largestLogger.logDir}/Latest.log"):
            #Create a "Logs" folder if one isnt present
            if not os.path.isdir(f"{largestLogger.logDir}/Logs"):
                os.mkdir(f"{largestLogger.logDir}/Logs")
            #Read the time the first log was ran to be placed in the name of the moved log file
            with open('Latest.log') as Log:
                newName = Log.read(24)
                newName = newName.replace("[","").replace("]","").replace('/', '-').replace(':', '.')
            #Moves the old log into the folder and naming it appropriately by the date and time the first log was ran
            shutil.move(f"{largestLogger.logDir}/Latest.log",
                        f"{largestLogger.logDir}/Logs/{newName}.log")
        #If the startup was run in testing mode display an example of all possible logs
        if testingMode:
            largestLogger.info(f"The logging path: {largestLogger.logDir}")
            largestLogger.info("This is an Info test!")
            largestLogger.warning("This is an Warning test!")
            largestLogger.success("This is an Success test!")
            largestLogger.error("This is an Error test!")
            #Iterates to show debug in use
            largestLogger.info("Testing debugs 1-10:")
            count = 1
            while count <= 10:
                largestLogger.debug(f"This is a debug level {count}", count)
                count = count + 1
            largestLogger.success("Debugs 1-10 ran!")
        #Create a log to display the logger as ready
        largestLogger.success("largestLogger is running!")
    #Functions to be externally called to change the way logs are displayed and saved
    def info(log:str):
        largestLogger.output(0, log)
    def warning(log:str):
        largestLogger.output(1, log)
    def success(log:str):
        largestLogger.output(2, log)
    def error(log:str):
        largestLogger.output(3, log)
    def debug(log:str, logLevel: int):
        if largestLogger.debugMode:
            if largestLogger.debugValue >= logLevel:
                largestLogger.output(4, log)
    #The main function all other log types call back to
    #It parses the data and prepares a string to be saved
    #And outputted appropriately
    def output(logType: int, log: str):
        #Creates variables to be used later within the logging process
        type = None
        typeColour = None
        now = datetime.now()
        stringedNow = str(now.strftime("%d/%m/%Y %I:%M:%S %p"))
        #Depending on the passed in "LogType" a different colour and header text is set
        match logType:
            case 0:
                type = "Info:          "
                typeColour = Fore.WHITE
            case 1:
                type = "Warning:       "
                typeColour = Fore.YELLOW
            case 2:
                type = "Success:       "
                typeColour = Fore.GREEN
            case 3:
                type = "Error:         "
                typeColour = Fore.RED
            case 4:
                type = "Debug:         "
                typeColour = Fore.CYAN
        #Output the text generated into a "Latest.log" file
        with open(f"{largestLogger.logDir}/Latest.log", "a+", encoding="utf-8") as LogFile:
            LogFile.writelines(f"[{stringedNow}] {type} {log}\n")
        #Output the log into the console with correct formatting and colours
        print(f"[{Fore.GREEN}{stringedNow}{Style.RESET_ALL}] {typeColour}{type}{Style.RESET_ALL} {log}")