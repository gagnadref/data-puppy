import re

class HTTPLog:
	def __init__(self, ip, client, user, dateTime, request, status, bytes, referer, agent):
		self.ip = ip
		self.client = client
		self.user = user
		self.dateTime = dateTime
		self.request = request
		self.status = int(status)
		self.bytes = int(bytes)
		self.referer = referer
		self.agent = agent

class Parser:
	ip = "(\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3})?"
	client = "(\\S+)"
	user = "(\\S+)"
	dateTime = "(\\[.+?\\])"
	request = "\"(.*?)\""
	status = "(\\d{3})"
	bytes = "(\\S+)"
	referer = "\"(.*?)\""
	agent = "\"(.*?)\""
	regex = r"%s %s %s %s %s %s %s %s %s" %(ip, client, user, dateTime, request, status, bytes, referer, agent)

	def parse(cls,string):
		matchObj = re.match(cls.regex, string)
		if matchObj:
			return HTTPLog(*matchObj.groups())
		else: 
			raise ValueError("Cannot parse: %s" %string)

	parse = classmethod(parse)