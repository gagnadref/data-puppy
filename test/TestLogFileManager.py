import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../datapuppy'
resdir = os.path.join(testdir, "resources/access.log")
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import LogFileManager
import unittest

class TestLogFileManager(unittest.TestCase):
    def test_getNewLogs(self):
    	logFileManager = LogFileManager.LogFileManager(os.path.abspath(resdir))
    	self.assertEqual(len(logFileManager.getNewLogs()),3)
    	self.assertEqual(len(logFileManager.getNewLogs()),0)

if __name__ == '__main__':
    unittest.main()