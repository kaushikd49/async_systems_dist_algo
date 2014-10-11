from BankServer import *
class BankChain:
	bankName = None
	length = 0
	head = None
	tail = None
	serverMap = {}
	bankServers = []

	def __init__(self):
		self.serverMap = {}

	def createChain(self,chainArr,name):
		print('Enters chain')

		self.bankServers = list(chainArr)
		print("bank servers = ",self.bankServers)
		length = len(chainArr)
		self.length = length
		self.serverMap[name]={}
		bankServerArr = []

		for serverProcess in self.bankServers:
			server = BankServer(serverProcess) 
			bankServerArr.append(server)

		print(len(bankServerArr))

		for i in range(length - 2 ):
			bankServerArr[i].addNextServer(bankServerArr[i+1])

		self.serverMap[name]['head'] = bankServerArr[0]
		self.serverMap[name]['tail'] = bankServerArr[length-1]
		self.serverMap[name]['body'] = bankServerArr[1:length-2]
		self.serverMap[name]['allServers'] = bankServerArr;

	def getAllServers(self,name):
		return self.serverMap[name]['allServers']

	def getHeadServer(self,name):
		return serverMap[name]['head']

	def getTailServer(self,name):
		return serverMap[name]['tail']







