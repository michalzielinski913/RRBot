from Classes.Connect import Connect
import time
class Client:

    def __init__(self, username, password, method):
        self.username=username
        self.password=password
        self.method=method
        self.connection=Connect(True)

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
        except:
            print("Couldn't download user ID")
            self.id = self.connection.checkCurrentUserID()

    def getUserID(self):
        if self.id is None:
            self.id = self.connection.checkCurrentUserID()
        return self.id

    def getMoney(self):
        return self.connection.getMoney()

    def checkRegionresource(self):
        results=self.connection.checkRegionresource()
        print(results)

    def checkUserStats(self):
        if self.id is None:
            self.id = self.connection.checkCurrentUserID()
        stats=self.connection.checkUserStats(self.id)
        print(stats)

    def CheckAvailableResources(self):
        return self.connection.CheckAvailableResources()

