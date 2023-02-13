#After installing the lib this is how you can bring it into
#the scope of a file/script
from LargestLogger import LargestLogger

#This line is needed in any script that uses this lib,
#it should only be ran once and just prepares the logger,
#colorama and cleans it's surrounding directory
#Entering no extra args disables debugs entirely!
#LargestLogger.StartUp()

#This allows debug prints to execute upto level 5
#The depth/complexity of the log levels are set by you
#and your script/program!
LargestLogger.StartUp(DebugMode=True, DebugValue=5)

#Passing in True launches it in testing mode, this just displays
#all possible prints/logs the program executes
#LargestLogger.StartUp(TestingMode=True)

#Just some examples of the logging code being used
LargestLogger.Info("This is to be used when displaying basic information")
LargestLogger.Warning("This is to be used to warn the user in the case of somthing unexpected occuring or possibly informing them of somthing irregular")
LargestLogger.Success("This is to be used when a task has completed and reports such to the user!")
LargestLogger.Error("This is to be used on exception or where a feature/function has failed completely")
#Iterates to show debug in use
LargestLogger.Info("Testing debugs 1-10 (Your usage of the debug system is set above and anything at or blow your set log level will be stated) :")
count = 1
while count <= 10:
    LargestLogger.Debug(f"This is a debug level {count}", count)
    count = count + 1
LargestLogger.Success("Debugs 1-10 ran!")