from collections import Counter
from datetime import datetime

class Metric:
	def __init__(self, logFile):
		self.logFile = logFile

	def compute(self):
		raise Exception("Abstract method should have been implemented")

	def display(self):
		raise Exception("Abstract method should have been implemented")

class Alert:
	def __init__(self, logFile, threshold):
		self.logFile = logFile
		self.threshold = threshold
		self.triggered = False

	def check(self):
		if self.triggered:
			self.checkIfDropsBelow()
		else:
			self.checkIfExceeds()

	def checkIfExceeds(self):
		raise Exception("Abstract method should have been implemented")

	def checkIfDropsBelow(self):
		raise Exception("Abstract method should have been implemented")

	def display(self):
		raise Exception("Abstract method should have been implemented")

class NumberOfRequests(Metric):
	def __init__(self, logFile):
		super().__init__(logFile)

	def compute(self):
		logs = self.logFile.getLogs()
		self.result = len(logs)

	def display(self):
		print("Total number of requests: %i" %self.result)

class MostVisitedSections(Metric):
	def __init__(self, logFile):
		super().__init__(logFile)

	def compute(self):
		logs = self.logFile.getLogs()
		requests = [log.getSection() for log in logs]
		self.result = Counter(requests).most_common(10)

	def display(self):
		print("Sections of the web site with the most hits:")
		for section in self.result:
			print(section)

class HighTrafficAlert(Alert):
	def __init__(self, logFile, threshold):
		super().__init__(logFile, threshold)

	def checkIfExceeds(self):
		logs = self.logFile.getLogs()
		if len(logs)/2 >= self.threshold:
			self.result = len(logs)/2
			self.triggered = True
			self.display()
			
	def checkIfDropsBelow(self):
		logs = self.logFile.getLogs()
		if len(logs)/2 < self.threshold:
			self.triggered = False
			self.display()

	def display(self):
		if self.triggered:
			print("High traffic generated an alert - hits = %i, triggered at %s" %(self.result, datetime.now().strftime("%X")))
		else:
			print("Alert on high traffic recovered at %s" %datetime.now().strftime("%X"))
