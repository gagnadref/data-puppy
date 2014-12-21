import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../datapuppy'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

from datetime import datetime
import threading
import LogMonitor
import LogGenerator
import LogSource
import Metric
import unittest

class TestLogMonitor(unittest.TestCase):
    def generateLogs(self):
        logGenerator = LogGenerator.LogGenerator(os.path.abspath(os.path.join(testdir, "resources/access.log.template")),
            os.path.abspath(os.path.join(testdir, "resources/access.log")),
            [(60,60),(180,10),(60,60)])
        logGenerator.run()

    def test_run(self):
        logGeneration = threading.Thread(None, self.generateLogs, None, (), None)
        logGeneration.start()

        filename = os.path.abspath(os.path.join(testdir, "resources/access.log"))

        logMonitor = LogMonitor.LogMonitor(10,1)

        logSourceForMetrics = LogSource.LogSource(filename,timeslot=10)
        logSourceForAlerts = LogSource.LogSource(filename,timeslot=120)

        numberOfRequests = Metric.NumberOfRequests(logSourceForMetrics)
        uniqueVisitors = Metric.UniqueVisitors(logSourceForMetrics)
        mostVisitedSections = Metric.MostVisitedSections(logSourceForMetrics)
        highTrafficAlert = Metric.HighTrafficAlert(logSourceForAlerts,threshold=65)

        logMonitor.addMetric(numberOfRequests)
        logMonitor.addMetric(uniqueVisitors)
        logMonitor.addMetric(mostVisitedSections)
        logMonitor.addAlert(highTrafficAlert)

        logMonitor.run(timeout=180)

if __name__ == '__main__':
    unittest.main()