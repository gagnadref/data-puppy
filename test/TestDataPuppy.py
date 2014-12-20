import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../datapuppy'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

from datetime import datetime
import threading
import DataPuppy
import LogGenerator
import LogFile
import Metric
import unittest

class TestDataPuppy(unittest.TestCase):
    def generateLogs(self):
        logGenerator = LogGenerator.LogGenerator(os.path.abspath(os.path.join(testdir, "resources/access.log.template")),
            os.path.abspath(os.path.join(testdir, "resources/access.log")),
            180)
        logGenerator.run(30)

    
    def runDataPuppy(self):
        filename = os.path.abspath(os.path.join(testdir, "resources/access.log"))

        dataPuppy = DataPuppy.DataPuppy()

        logFileForMetrics = LogFile.LogFile(filename,timeslot=10)
        logFileForAlerts = LogFile.LogFile(filename,timeslot=120)

        mostVisitedSections = Metric.MostVisitedSections(logFileForMetrics)
        numberOfRequests = Metric.NumberOfRequests(logFileForMetrics)
        highTrafficAlert = Metric.HighTrafficAlert(logFileForAlerts,threshold=10)

        dataPuppy.addMetric(mostVisitedSections)
        dataPuppy.addMetric(numberOfRequests)
        dataPuppy.addAlert(highTrafficAlert)

        dataPuppy.run(timeout=30)

    def test_run(self):
        logGeneration = threading.Thread(None, self.generateLogs, None, (), None)
        dataPuppy = threading.Thread(None, self.runDataPuppy, None, (), None)

        logGeneration.start()
        dataPuppy.start()

if __name__ == '__main__':
    unittest.main()