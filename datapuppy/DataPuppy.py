import os
import threading
import time
import Metric
from datetime import datetime

class DataPuppy:
	"""
	DataPuppy monitors a HTTP access log 
	"""
	def __init__(self):
		self.metrics = []
		self.alerts = []
		self.metricMessages = []
		self.alertMessages = []

	def run(self, timeout):
		metricComputation = threading.Thread(None, self.computeAndDisplayMetrics, None, (timeout,), None)
		alertChecking = threading.Thread(None, self.checkAndDisplayAlerts, None, (timeout,), None)

		metricComputation.start() 
		alertChecking.start()

	def computeAndDisplayMetrics(self, timeout):
		startTime = time.time()
		while True:
			if time.time() > startTime + timeout:
				break
			self.metricMessages = []
			for metric in self.metrics:
				metric.computeValue()
				self.metricMessages.append(metric.getValueAsString())
			self.display()
			time.sleep(10)

	def checkAndDisplayAlerts(self, timeout):
		startTime = time.time()
		while True:
			if time.time() > startTime + timeout:
				break
			for alert in self.alerts:
				if alert.hasStatusChanged():
					self.alertMessages.append(alert.getValueAsString())
					self.display()
			time.sleep(1)

	def addMetric(self, metric):
		self.metrics.append(metric)

	def addAlert(self, alert):
		self.alerts.append(alert)

	def display(self):
		print("\n******************************************************************")
		print(datetime.now().strftime("%X"))
		for metricMessage in self.metricMessages:
			print(metricMessage)
		if self.alertMessages:	
			print("Recent Alerts:")
		for alertMessage in self.alertMessages:
			print(alertMessage)

if __name__ == "__main__":
	DataPuppy().run(os.path.abspath(os.path.join(os.path.dirname(__file__), "resources/access.log")))
