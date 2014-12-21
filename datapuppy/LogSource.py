from datetime import *
import HttpLog

class LogSource:
	"""
	LogSource provides the logs of a given log file within a time slot
	"""
	def __init__(self, filename, timeslot):
		self.filename = filename
		self.timeslot = timeslot
		self.lastFetch = None
		self.currentPositionInFile = 0
		self.logs = []

	def getLogs(self):
		"""
		getLogs updates the logs only if it has not been updated recently (in the last second), then return them
		"""
		now = datetime.now()
		if not self.lastFetch or now - timedelta(seconds=1) > self.lastFetch :
			self.removeOldLogs(now)
			self.addNewLogs(now)
			self.lastFetch = now
		return self.logs

	def removeOldLogs(self, now):
		i = 0
		length = len(self.logs)
		while i<length and self.logs[i].dateTime < now - timedelta(seconds=self.timeslot):
			i+=1
		self.logs = self.logs[i:]

	def addNewLogs(self, now):
		"""
		addNewLogs adds new logs without reading the whole file
		"""
		with open(self.filename,"r") as logFile:
			logFile.seek(self.currentPositionInFile)
			line = logFile.readline()
			while line != '':
				log = HttpLog.Parser.parse(line)
				if log.dateTime >= now - timedelta(seconds=self.timeslot) :
					self.logs.append(log)
				line = logFile.readline()
			self.currentPositionInFile = logFile.tell()

	def getAllLogs(self):
		with open(self.filename,"r") as logFile:
			logs = []
			for line in logFile:
				logs.append(HttpLog.Parser.parse(line))
			return logs
