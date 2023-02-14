#After installing the lib this is how you can bring it into
#the scope of a file/script
from LargestLogger import largestLogger

#This line is needed in any script that uses this lib,
#it should only be ran once and just prepares the logger,
#colorama and cleans it's surrounding directory
#Entering no extra args disables debugs entirely!
#largestLogger.startUp

#This allows debug prints to execute upto level 5
#The depth/complexity of the log levels are set by you
#and your script/program!
largestLogger.startUp(debugMode=True, debugValue=5)

#Passing in True launches it in testing mode, this just displays
#all possible prints/logs the program executes
#largestLogger.startUp(testingMode=True)

#Just some examples of the logging code being used
largestLogger.info("This is to be used when displaying basic information")
largestLogger.warning("This is to be used to warn the user in the case of somthing unexpected occuring or possibly informing them of somthing irregular")
largestLogger.success("This is to be used when a task has completed and reports such to the user!")
largestLogger.error("This is to be used on exception or where a feature/function has failed completely")
#Iterates to show debug in use
largestLogger.info("Testing debugs 1-10 (Your usage of the debug system is set above and anything at or blow your set log level will be stated) :")
count = 1
while count <= 10:
    largestLogger.debug(f"This is a debug level {count}", count)
    count = count + 1
largestLogger.success("Debugs 1-10 ran!")