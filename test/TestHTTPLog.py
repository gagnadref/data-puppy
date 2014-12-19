import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../datapuppy'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

from datetime import datetime
import HttpLog
import unittest

class TestHttpLog(unittest.TestCase):
    def test_parse(self):
        log = HttpLog.Parser.parse("82.67.154.104 - - [05/Dec/2014:14:01:02 +0200] \"GET /pages/create HTTP/1.1\" 200 181 \"-\" \"-\"")
        self.assertEqual(log.ip, "82.67.154.104")
        self.assertEqual(log.client, "-")
        self.assertEqual(log.user, "-")
        self.assertEqual(log.dateTime, datetime.strptime("05/Dec/2014:14:01:02","%d/%b/%Y:%X"))
        self.assertEqual(log.request, "GET /pages/create HTTP/1.1")
        self.assertEqual(log.status, 200)
        self.assertEqual(log.bytes, 181)
        self.assertEqual(log.referer, "-")
        self.assertEqual(log.agent, "-")

        self.assertRaises(ValueError,HttpLog.Parser.parse,"82.67.154.104 - - \"GET /pages/create HTTP/1.1\" 200 181 \"-\" \"-\"")

    def test_getURL(self):
        log = HttpLog.Parser.parse("82.67.154.104 - - [05/Dec/2014:14:01:02 +0200] \"GET /pages/create HTTP/1.1\" 200 181 \"-\" \"-\"")
        self.assertEqual(log.getURL(), "/pages/create")

    def test_getSection(self):
        log = HttpLog.Parser.parse("82.67.154.104 - - [05/Dec/2014:14:01:02 +0200] \"GET /pages/create HTTP/1.1\" 200 181 \"-\" \"-\"")
        self.assertEqual(log.getSection(), "/pages")


if __name__ == '__main__':
    unittest.main()

