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

        time.sleep(10)
        self.id=self.connection.checkCurrentUserID()

    def getUserID(self):
        return self.id

    def getMoney(self):
        return self.connection.getMoney()

    def checkRegionresource(self):
        results=self.connection.checkRegionresource()
        print(results)

    def checkUserStats(self, userId):
        stats=self.connection.checkUserStats(userId)
        print(stats)

    def debug(self):
        self.connection.CheckAvailableResource()

