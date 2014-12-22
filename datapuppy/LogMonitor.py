import os
import sys
import threading
import time
from datetime import datetime
import LogSource
import Metric

class LogMonitor:
    """
    Monitors metrics and alerts, and displays the results in the console 
    """
    def __init__(self, metricTimeslot, alertTimeslot):
        self.metricTimeslot = metricTimeslot
        self.alertTimeslot = alertTimeslot
        self.metrics = []
        self.alerts = []
        self.metricMessages = []
        self.alertMessages = []

    def run(self, timeout):
        metricComputation = threading.Thread(
            target=self.computeAndDisplayMetrics, 
            args=(timeout,))
        alertChecking = threading.Thread(
            target=self.checkAndDisplayAlerts, 
            args=(timeout,))

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
            time.sleep(self.metricTimeslot)

    def checkAndDisplayAlerts(self, timeout):
        startTime = time.time()
        while True:
            if time.time() > startTime + timeout:
                break
            for alert in self.alerts:
                if alert.hasStatusChanged():
                    self.alertMessages.append(alert.getValueAsString())
                    self.display()
            time.sleep(self.alertTimeslot)

    def addMetric(self, metric):
        self.metrics.append(metric)

    def addAlert(self, alert):
        self.alerts.append(alert)

    def display(self):
        print("********************************************************************************")
        print("************************ Application status at %s ************************" 
            %datetime.now().strftime("%X"))
        print("********************************************************************************")
        for metricMessage in self.metricMessages:
            print(metricMessage)
        if self.alertMessages:  
            print("Recent Alerts :")
            for alertMessage in self.alertMessages:
                print(alertMessage)
            print("")

if __name__ == '__main__':
        if len(sys.argv)<2:
            raise Exception("Must provide the path to the monitored access.log")

        filename = sys.argv[1]

        logMonitor = LogMonitor(10,1)

        logSourceForMetrics = LogSource.LogSource(filename,10)
        logSourceForAlerts = LogSource.LogSource(filename,120)

        numberOfRequests = Metric.NumberOfRequests(logSourceForMetrics)
        uniqueVisitors = Metric.UniqueVisitors(logSourceForMetrics)
        mostVisitedSections = Metric.MostVisitedSections(logSourceForMetrics)
        highTrafficAlert = Metric.HighTrafficAlert(logSourceForAlerts,65)

        logMonitor.addMetric(numberOfRequests)
        logMonitor.addMetric(uniqueVisitors)
        logMonitor.addMetric(mostVisitedSections)
        logMonitor.addAlert(highTrafficAlert)

        logMonitor.run(timeout=float('inf'))
