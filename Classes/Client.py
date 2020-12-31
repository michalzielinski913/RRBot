from Classes.Connect import Connect
import time
class Client:

    def __init__(self, username, password, method, head):
        self.username=username
        self.password=password
        self.method=method
        self.connection=Connect(head)

    def login(self):
        print("Starting up")
        print("Establishing connection")
        if self.method=='f':
            print("Choosen login method: facebook")
            self.connection.connectFacebook(self.username, self.password)
        else:
            print("nope")


        try:
            self.id = self.connection.checkCurrentUserID()
            self.residency = (self.connection.CheckUserResidency(self.id))
        except:
            print("Couldn't download user ID")

    def getUserID(self):
        if self.id is None:
            self.id = self.connection.checkCurrentUserID()
        return self.id

    def getMoney(self):
        return self.connection.getMoney()

    #Check current resources of user residency region
    def checkRegionresource(self, ID=None):
        try:
            if(ID is None):
                results=self.connection.checkRegionresource(self.residency)
            else:
                results = self.connection.checkRegionresource(ID)
        except:
            print("Couldn't fetch region data")
            return []
        return results

    #Check statistics of user
    def checkUserStats(self, ID=None):
        if ID is None:
            ID=self.id
        stats=self.connection.checkUserStats(ID)
        return (stats)

    #Check which resourcess are available in current region
    def CheckAvailableResources(self):
        return self.connection.CheckAvailableResources()

    #Residency region id
    def CheckResidency(self):
        return self.residency

    #Check how many people are in given party
    def CheckPartyPopulation(self, id):
        return self.connection.checkPartyNumbers(id)

    #Return party members id list
    def CheckPartyMembers(self, id):
        return self.connection.retrievePartyMembersID(id)
