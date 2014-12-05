import LogFileManager
import time
from collections import Counter

class DataPuppy:
	"""
	DataPuppy monitors a HTTP access log 
	"""
	def run(self,filename):
		logFileManager = LogFileManager.LogFileManager(filename)

		while True:
			logs = logFileManager.getNewLogs()
			requests = [log.getSection() for log in logs]

			print("Sections of the web site with the most hits:")
			counter = Counter(requests)
			for a in counter.most_common(10):
				print(a)

			print("Total number of requests: %s" %len(logs))

			time.sleep(10)

if __name__ == "__main__":
	DataPuppy().run("resources/access.log")
