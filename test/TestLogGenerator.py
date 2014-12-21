import os
import sys
testdir = os.path.dirname(__file__)
srcdir = '../datapuppy'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

import unittest
import LogGenerator

class TestLogGenerator(unittest.TestCase):
    def test_run(self):
        logGenerator = LogGenerator.LogGenerator(
            os.path.abspath(os.path.join(testdir, "resources/access.log.template")),
            os.path.abspath(os.path.join(testdir, "resources/access.log")),
            [(60,10),(180,5),(60,10)])
        logGenerator.run()

if __name__ == '__main__':
    unittest.main()