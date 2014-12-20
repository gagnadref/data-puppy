import LogFileManager
import time
from datetime import datetime

class LogGenerator:
	def __init__(self, sourceFileName, destinationFilename, requestsByMinute):
		logFileManager = LogFileManager.LogFileManager(sourceFileName)
		self.logs = logFileManager.getAllLogs()
		self.numberOfLogs = len(self.logs)
		self.destinationFilename = destinationFilename
		if self.numberOfLogs == 0:
			raise Exception("Must provide a file with at least one HTTP log")
		self.requestsByMinute = requestsByMinute

	def run(self, timeout):
		startTime = time.time()
		with open(self.destinationFilename,"w") as destinationFile:
			i=0
			while True:
				if i==self.numberOfLogs:
					i=0
				if time.time() > startTime + timeout:
					break
				log = self.logs[i]
				log.dateTime=datetime.now()
				destinationFile.write(str(log))
				time.sleep(60/self.requestsByMinute)



