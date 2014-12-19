import os
import LogFileManager
import time
import Metric
from datetime import datetime
from collections import Counter

class DataPuppy:
	"""
	DataPuppy monitors a HTTP access log 
	"""
	def run(self,filename):
		logFileManager = LogFileManager.LogFileManager(filename)

		mostVisitedSections = Metric.MostVisitedSections()
		numberOfRequests = Metric.NumberOfRequests()

		highTrafficAlert = Metric.HighTrafficAlert(10)

		while True:
			newLogs = logFileManager.getNewLogs()
			mostVisitedSections.compute(newLogs)
			mostVisitedSections.print()
			numberOfRequests.compute(newLogs)
			numberOfRequests.print()

			last2MinutesLogs = logFileManager.getLastLogsWithTimeSlot(120)
			highTrafficAlert.check(last2MinutesLogs)

			time.sleep(10)


if __name__ == "__main__":
	DataPuppy().run(os.path.abspath(os.path.join(os.path.dirname(__file__), "resources/access.log")))
