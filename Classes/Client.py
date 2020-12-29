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
            self.id = self.connection.checkCurrentUserID()

    def getUserID(self):
        if self.id is None:
            self.id = self.connection.checkCurrentUserID()
        return self.id

    def getMoney(self):
        return self.connection.getMoney()

    #Check current resources of user residency region
    def checkRegionresource(self):
        results=self.connection.checkRegionresource(self.residency)
        return results

    #Check statistics of user
    def checkUserStats(self):
        if self.id is None:
            self.id = self.connection.checkCurrentUserID()
        stats=self.connection.checkUserStats(self.id)
        return (stats)

    #Check which resourcess are available in current region
    def CheckAvailableResources(self):
        return self.connection.CheckAvailableResources()

    #Residency region id
    def CheckResidency(self):
        return self.residency