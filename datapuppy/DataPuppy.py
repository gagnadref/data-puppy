import os
import LogFileManager
import time
from datetime import datetime
from collections import Counter

class DataPuppy:
	"""
	DataPuppy monitors a HTTP access log 
	"""
	def __init__(self):
		self.threshold = 3

	def run(self,filename):
		logFileManager = LogFileManager.LogFileManager(filename)

		while True:
			newLogs = logFileManager.getNewLogs()
			requests = [log.getSection() for log in newLogs]

			print("Sections of the web site with the most hits:")
			counter = Counter(requests)
			for a in counter.most_common(10):
				print(a)

			print("Total number of requests: %s" %len(newLogs))

			last2MinutesLogs = logFileManager.getLastLogsWithTimeSlot(120)

			if len(last2MinutesLogs) >= self.threshold:
				print("High traffic generated an alert - hits = %i, triggered at %s" %(len(last2MinutesLogs), datetime.now()))

			time.sleep(10)


if __name__ == "__main__":
	DataPuppy().run(os.path.abspath(os.path.join(os.path.dirname(__file__), "resources/access.log")))
