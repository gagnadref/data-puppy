import re
from datetime import *

class HttpLog:
	def __init__(self, ip, client, user, dateTime, request, status, bytes, referer, agent):
		self.ip = ip
		self.client = client
		self.user = user
		self.dateTime = datetime.strptime(dateTime,"%d/%b/%Y:%X %z").replace(tzinfo=None)#05/Dec/2014:14:01:02 +0200
		self.request = request
		self.status = int(status)
		self.bytes = int(bytes)
		self.referer = referer
		self.agent = agent

	def getURL(self):
		try:
			return self.request.split()[1]
		except IndexOutOfBOund:
			raise ValueError("Cannot find any URL in log")

	def getSection(self):
		regex = r"^\/[^\/]*"
		matchObj = re.match(regex,self.getURL())
		if matchObj:
			return matchObj.group(0)
		else:
			raise ValueError("Cannot find any section in URL")

	def __str__(self):
		str = "%s %s %s [%s] \"%s\" %s %s \"%s\" \"%s\"\n" %(self.ip, self.client, self.user, self.dateTime.strftime("%d/%b/%Y:%X %z"), self.request, self.status, self.bytes, self.referer, self.agent)
		return str

class Parser:
	"""
	The parser parses a w3c-formatted HTTP access log into a HttpLog object
	"""
	ip = "(\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3})?"
	client = "(\\S+)"
	user = "(\\S+)"
	dateTime = "\\[(.+?)\\]"
	request = "\"(.*?)\""
	status = "(\\d{3})"
	bytes = "(\\S+)"
	referer = "\"(.*?)\""
	agent = "\"(.*?)\""
	regex = "%s %s %s %s %s %s %s %s %s" %(ip, client, user, dateTime, request, status, bytes, referer, agent)

	@classmethod
	def parse(cls,string):
		matchObj = re.match(cls.regex, string)
		if matchObj:
			return HttpLog(*matchObj.groups())
		else: 
			raise ValueError("Cannot parse: %s" %string)
