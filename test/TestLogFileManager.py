from datapuppy import LogFileManager
import unittest

class TestHTTPLog(unittest.TestCase):
    def test_getNewLogs(self):
    	logFileManager = LogFileManager.LogFileManager("test/resources/access.log")
    	self.assertEqual(len(logFileManager.getNewLogs()),3)
    	self.assertEqual(len(logFileManager.getNewLogs()),0)

if __name__ == '__main__':
    unittest.main()