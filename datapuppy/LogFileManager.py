import HTTPLog

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
			for line in logFile:
				logs.append(HTTPLog.Parser.parse(line))
			if logs:
				self.lastLogDateTime = logs[0].dateTime
			self.lastLogDateTime
			return logs

	def getNewLogs(self):
		with open(self.filename,"r") as logFile:
			logs = []
			for line in reversed(logFile.readlines()):
				log = HTTPLog.Parser.parse(line)
				if self.lastLogDateTime is None or self.lastLogDateTime < log.dateTime:
					logs.append(log)
				else:
					break
			if logs:
				self.lastLogDateTime = logs[0].dateTime
			return logs