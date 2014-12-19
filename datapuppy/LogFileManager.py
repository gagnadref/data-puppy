import HttpLog
from datetime import *

class LogFileManager:
	"""
	LogFileManager is responsible of a log file and provides the new logs
	"""
	def __init__(self, filename):
		self.filename = filename
		self.lastLogDateTime = None

	def getAllLogs(self):
		with open(self.filename,"r") as logFile:
			logs = []
			for line in reversed(logFile.readlines()):
				logs.append(HttpLog.Parser.parse(line))
			return logs

	def getNewLogs(self):
		with open(self.filename,"r") as logFile:
			logs = []
			if self.lastLogDateTime is None:
				logs = self.getAllLogs()
			else:
				logs = self.getLogsSinceDateTime(self.lastLogDateTime)
			if logs:
				self.lastLogDateTime = logs[0].dateTime
			return logs

	def getLogsSinceDateTime(self,dateTime):
		with open(self.filename,"r") as logFile:
			logs = []
			for line in reversed(logFile.readlines()):
				log = HttpLog.Parser.parse(line)
				if dateTime < log.dateTime:
					logs.append(log)
				else:
					break
			return logs

	def getLastLogsWithTimeSlot(self,timeSlot):
		return self.getLogsSinceDateTime(datetime.utcnow()-timedelta(seconds=timeSlot))
