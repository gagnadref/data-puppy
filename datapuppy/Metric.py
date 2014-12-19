from collections import Counter
from datetime import datetime


class Metric:
	def compute(self, logs):
		raise Exception("Abstract method should have been implemented")

	def print(self):
		raise Exception("Abstract method should have been implemented")

class Alert:
	def __init__(self, threshold):
		self.threshold = threshold
		self.triggered = False

	def check(self, logs):
		if self.triggered:
			self.checkIfDropsBelow(logs)
		else:
			self.checkIfExceeds(logs)

	def checkIfExceeds(self, logs):
		raise Exception("Abstract method should have been implemented")

	def checkIfDropsBelow(self, logs):
		raise Exception("Abstract method should have been implemented")

	def print(self):
		raise Exception("Abstract method should have been implemented")

class NumberOfRequests(Metric):
	def compute(self, logs):
		self.result = len(logs)

	def print(self):
		print("Total number of requests: %i" %self.result)

class MostVisitedSections(Metric):
	def compute(self, logs):
		requests = [log.getSection() for log in logs]
		self.result = Counter(requests).most_common(10)

	def print(self):
		print("Sections of the web site with the most hits:")
		for section in self.result:
			print(section)

class HighTrafficAlert(Alert):
	def _init__(self, threshold):
		super.init(threshold)

	def checkIfExceeds(self, logs):
		if len(logs) >= self.threshold:
			self.result = len(logs)
			self.triggered = True
			self.print()
			
	def checkIfDropsBelow(self, logs):
		if len(logs) < self.threshold:
			self.triggered = False
			self.print()

	def print(self):
		if self.triggered:
			print("High traffic generated an alert - hits = %i, triggered at %s" %(self.result, datetime.now()))
		else:
			print("Alert on high traffic recovered at %s" %datetime.now())
