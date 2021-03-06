from collections import Counter
from datetime import datetime

class Metric:
    """
    Abstract class to create statistics on logs
    """
    def __init__(self, logSource):
        self.logSource = logSource
        self.value = None

    def computeValue(self):
        raise Exception("Abstract method computeValue should have been implemented")

    def getValueAsString(self):
        raise Exception("Abstract method getValueAsString should have been implemented")

class Alert(Metric):
    """
    Abstract class to create alerts on statistics
    """
    def __init__(self, logSource, threshold):
        super().__init__(logSource)
        self.threshold = threshold
        self.triggered = False
        self.message = ""

    def hasStatusChanged(self):
        self.computeValue()
        if self.triggered:
            return self.hasValueDroppedBelowThreshold()
        else:
            return self.hasValueExceededThreshold()

    def hasValueExceededThreshold(self):
        if self.value >= self.threshold:
            self.triggered = True
            self.updateMessage()
            return True
        return False
            
    def hasValueDroppedBelowThreshold(self):
        if self.value < self.threshold:
            self.triggered = False
            self.updateMessage()
            return True
        return False

    def getValueAsString(self):
        return self.message

    def updateMessage(self):
        raise Exception("Abstract method updateMessage should have been implemented")

class NumberOfRequests(Metric):
    """
    Number of requests to the website in the last period
    """
    def computeValue(self):
        logs = self.logSource.getLogs()
        self.value = len(logs)

    def getValueAsString(self):
        return "Number of requests in the last %is : %i" %(
            self.logSource.timeslot, self.value)

class UniqueVisitors(Metric):
    """
    Number of unique visitors of the website in the last 10s
    """
    def computeValue(self):
        logs = self.logSource.getLogs()
        ip = Counter(map(lambda log: log.ip, logs))
        self.value = len(ip.keys())

    def getValueAsString(self):
        return "Unique visitors : %i" %self.value

class MostVisitedSections(Metric):
    """
    Sections of the website with the most hits
    """
    def computeValue(self):
        logs = self.logSource.getLogs()
        requests = [log.getSection() for log in logs]
        self.value = Counter(requests).most_common(10)

    def getValueAsString(self):
        if not self.value:
            return ""
        message = "Sections of the website with the most hits :\n"
        for (section, visits) in self.value:
            message += "%s : %i\n" %(section, visits)
        return message

class HighTrafficAlert(Alert):
    """
    Alert when the number of requests per minute exceeds a threshold
    """
    def computeValue(self):
        logs = self.logSource.getLogs()
        self.value = len(logs)*60/self.logSource.timeslot

    def updateMessage(self):
        if self.triggered:
            self.message = "High traffic generated an alert - hits = %i, triggered at %s" %(
                self.value, datetime.now().strftime("%X"))
        else:
            self.message = "Alert on high traffic recovered at %s" %(
                datetime.now().strftime("%X"))
