#After installing the lib this is how you can bring it into
#the scope of a file/script
from LargestLogger import LargestLogger

#This line is needed in any script that uses this lib,
#it should only be ran once and just prepares the logger,
#colorama and cleans it's surrounding directory
LargestLogger.StartUp()

#Passing in True launches it in testing mode, this just displays
#all possible prints/logs the program executes
#LargestLogger.StartUp(True)

LargestLogger.Info("This is to be used when displaying basic information")
LargestLogger.Warning("This is to be used to warn the user in the case of somthing unexpected occuring or possibly informing them of somthing irregular")
LargestLogger.Success("This is to be used when a task has completed and reports such to the user!")
LargestLogger.Error("This is to be used on exception or where a feature/function has failed completely")