import os
import threading
import time
import Metric

class DataPuppy:
	"""
	DataPuppy monitors a HTTP access log 
	"""
	def __init__(self):
		self.metrics = []
		self.alerts = []

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
			for metric in self.metrics:
				metric.computeValue()
				metric.display()
			time.sleep(10)

	def checkAndDisplayAlerts(self, timeout):
		startTime = time.time()
		while True:
			if time.time() > startTime + timeout:
				break
			for alert in self.alerts:
				alert.check()
			time.sleep(1)

	def addMetric(self, metric):
		self.metrics.append(metric)

	def addAlert(self, alert):
		self.alerts.append(alert)


if __name__ == "__main__":
	DataPuppy().run(os.path.abspath(os.path.join(os.path.dirname(__file__), "resources/access.log")))
