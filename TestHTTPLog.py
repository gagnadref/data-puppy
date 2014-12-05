import HTTPLog
import unittest

class TestHTTPLog(unittest.TestCase):
    def test_parse(self):
        log = HTTPLog.Parser.parse("82.67.154.104 - - [05/Dec/2014:14:01:02 +0200] \"GET /pages/create HTTP/1.1\" 200 181 \"-\" \"-\"")
        assert(log.ip == "82.67.154.104")
        assert(log.client == "-")
        assert(log.user == "-")
        assert(log.dateTime == "[05/Dec/2014:14:01:02 +0200]")
        assert(log.request == "GET /pages/create HTTP/1.1")
        assert(log.status == 200)
        assert(log.bytes == 181)
        assert(log.referer == "-")
        assert(log.agent == "-")

        self.assertRaises(ValueError,HTTPLog.Parser.parse,"82.67.154.104 - - \"GET /pages/create HTTP/1.1\" 200 181 \"-\" \"-\"")

if __name__ == '__main__':
    unittest.main()

