import time
import datetime
import LogSource

class LogGenerator:
	def __init__(self, sourceFileName, destinationFilename, trafficSequence):
		logSource = LogSource.LogSource(sourceFileName,0)
		self.logs = logSource.getAllLogs()
		self.numberOfLogs = len(self.logs)
		self.destinationFilename = destinationFilename
		if self.numberOfLogs == 0:
			raise Exception("Must provide a file with at least one HTTP log")
		self.trafficSequence = trafficSequence

	def generate(self, requestsPerMinute, period):
		"""
		Adds logs to a destination file, during a given period, with a given traffic
		"""
		startTime = time.time()
		timeBetweenRequests = 60/requestsPerMinute
		i=0
		while True:
			if i==self.numberOfLogs:
				i=0
			if time.time() > startTime + period:
				break
			log = self.logs[i]
			log.dateTime=datetime.datetime.now()
			with open(self.destinationFilename,"a") as destinationFile:
				destinationFile.write(str(log))
			i+=1
			time.sleep(timeBetweenRequests)

	def run(self):
		for (requestsPerMinute, period) in self.trafficSequence:
			self.generate(requestsPerMinute, period)
