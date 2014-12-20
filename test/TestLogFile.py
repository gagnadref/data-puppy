import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../datapuppy'
resdir = os.path.join(testdir, "resources/access.log")
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import LogFile
import unittest

class TestLogFile(unittest.TestCase):
    def test_getNewLogs(self):
    	logFile = LogFile.LogFile(os.path.abspath(resdir))
    	self.assertEqual(len(logFile.getNewLogs()),3)
    	self.assertEqual(len(logFile.getNewLogs()),0)

if __name__ == '__main__':
    unittest.main()