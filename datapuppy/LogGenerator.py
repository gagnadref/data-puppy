import LogFile
import time
import datetime

class LogGenerator:
	def __init__(self, sourceFileName, destinationFilename, requestsByMinute):
		logFile = LogFile.LogFile(sourceFileName,0)
		self.logs = logFile.getAllLogs()
		self.numberOfLogs = len(self.logs)
		self.destinationFilename = destinationFilename
		if self.numberOfLogs == 0:
			raise Exception("Must provide a file with at least one HTTP log")
		self.requestsByMinute = requestsByMinute

	def run(self, timeout):
		startTime = time.time()
		i=0
		while True:
			if i==self.numberOfLogs:
				i=0
			if time.time() > startTime + timeout:
				break
			log = self.logs[i]
			log.dateTime=datetime.datetime.now()
			with open(self.destinationFilename,"a") as destinationFile:
				destinationFile.write(str(log))
			i+=1
			time.sleep(60/self.requestsByMinute)




