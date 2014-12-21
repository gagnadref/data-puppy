import sys, os
import threading
import time
from datetime import datetime, timedelta
testdir = os.path.dirname(__file__)
srcdir = '../datapuppy'
resdir = os.path.join(testdir, "resources/access.log")
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import LogSource
import LogGenerator
import unittest

class TestLogSource(unittest.TestCase):
	def test_getAllLogs(self):
		logSource = LogSource.LogSource(os.path.abspath(os.path.join(testdir, "resources/access.log.template")),None)
		self.assertEqual(len(logSource.getAllLogs()),3)

	def generateLogs(self):
		logGenerator = LogGenerator.LogGenerator(os.path.abspath(os.path.join(testdir, "resources/access.log.template")),
			os.path.abspath(os.path.join(testdir, "resources/access.log")),
			[(60,5),(180,10)])
		logGenerator.run()		

	def test_getLogs(self):
		logGeneration = threading.Thread(None, self.generateLogs, None, (), None)
		logGeneration.start()

		timeslot = 10
		logSource = LogSource.LogSource(os.path.abspath(os.path.join(testdir, "resources/access.log")),timeslot)
		for i in range(0,2):
			time.sleep(5)
			now = datetime.now()
			logs = logSource.getLogs()
			self.assertTrue(len(logs)>0)
			for log in logs:
				self.assertTrue(log.dateTime >= now - timedelta(seconds=timeslot))

if __name__ == '__main__':
	unittest.main()