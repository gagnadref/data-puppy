from collections import Counter
from datetime import datetime

class Metric:
	def __init__(self, logFile):
		self.logFile = logFile
		self.value = None

	def computeValue(self):
		raise Exception("Abstract method should have been implemented")

	def display(self):
		raise Exception("Abstract method should have been implemented")

class Alert(Metric):
	def __init__(self, logFile, threshold):
		super().__init__(logFile)
		self.threshold = threshold
		self.triggered = False

	def check(self):
		self.computeValue()
		if self.triggered:
			self.checkIfDropsBelow()
		else:
			self.checkIfExceeds()

	def checkIfExceeds(self):
		if self.value >= self.threshold:
			self.triggered = True
			self.display()
			
	def checkIfDropsBelow(self):
		if self.value < self.threshold:
			self.triggered = False
			self.display()

class NumberOfRequests(Metric):
	def __init__(self, logFile):
		super().__init__(logFile)

	def computeValue(self):
		logs = self.logFile.getLogs()
		self.value = len(logs)

	def display(self):
		print("Total number of requests: %i" %self.value)

class MostVisitedSections(Metric):
	def __init__(self, logFile):
		super().__init__(logFile)

	def computeValue(self):
		logs = self.logFile.getLogs()
		requests = [log.getSection() for log in logs]
		self.value = Counter(requests).most_common(10)

	def display(self):
		print("Sections of the web site with the most hits:")
		for section in self.value:
			print(section)

class HighTrafficAlert(Alert):
	def __init__(self, logFile, threshold):
		super().__init__(logFile, threshold)

	def computeValue(self):
		logs = self.logFile.getLogs()
		self.value = len(logs)/2

	def display(self):
		if self.triggered:
			print("High traffic generated an alert - hits = %i, triggered at %s" %(self.value, datetime.now().strftime("%X")))
		else:
			print("Alert on high traffic recovered at %s" %datetime.now().strftime("%X"))
