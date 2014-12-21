from collections import Counter
from datetime import datetime

class Metric:
	def __init__(self, logFile):
		self.logFile = logFile
		self.value = None

	def computeValue(self):
		raise Exception("Abstract method should have been implemented")

	def getValueAsString(self):
		raise Exception("Abstract method should have been implemented")

class Alert(Metric):
	def __init__(self, logFile, threshold):
		super().__init__(logFile)
		self.threshold = threshold
		self.triggered = False
		self.message = ""

	def hasStatusChanged(self):
		self.computeValue()
		if self.triggered:
			return self.hasValueDroppedBelowThreshold()
		else:
			return self.hasValueExceededThreshold()

	def hasValueExceededThreshold(self):
		if self.value >= self.threshold:
			self.triggered = True
			self.updateMessage()
			return True
		return False
			
	def hasValueDroppedBelowThreshold(self):
		if self.value < self.threshold:
			self.triggered = False
			self.updateMessage()
			return True
		return False

	def getValueAsString(self):
		return self.message

	def updateMessage(self):
		raise Exception("Abstract method should have been implemented")

class NumberOfRequests(Metric):
	def __init__(self, logFile):
		super().__init__(logFile)

	def computeValue(self):
		logs = self.logFile.getLogs()
		self.value = len(logs)

	def getValueAsString(self):
		return "Number of requests in the last 10s: %i" %self.value

class MostVisitedSections(Metric):
	def __init__(self, logFile):
		super().__init__(logFile)

	def computeValue(self):
		logs = self.logFile.getLogs()
		requests = [log.getSection() for log in logs]
		self.value = Counter(requests).most_common(10)

	def getValueAsString(self):
		if not self.value:
			return ""
		s = "Sections of the website with the most hits:"
		for section in self.value:
			s += "\n"
			s += str(section)
		return s

class HighTrafficAlert(Alert):
	def __init__(self, logFile, threshold):
		super().__init__(logFile, threshold)

	def computeValue(self):
		logs = self.logFile.getLogs()
		self.value = len(logs)/2

	def updateMessage(self):
		if self.triggered:
			self.message = "High traffic generated an alert - hits = %i, triggered at %s" %(self.value, datetime.now().strftime("%X"))
		else:
			self.message = "Alert on high traffic recovered at %s" %datetime.now().strftime("%X")
