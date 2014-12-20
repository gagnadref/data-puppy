import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../datapuppy'
resdir = os.path.join(testdir, "resources")
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import LogGenerator
import unittest

class TestLogGenerator(unittest.TestCase):
    def test_run(self):
        logGenerator = LogGenerator.LogGenerator(os.path.abspath(os.path.join(resdir, "access.log.template")),
            os.path.abspath(os.path.join(resdir, "access.log")),
            180)
        logGenerator.run(10)

if __name__ == '__main__':
    unittest.main()