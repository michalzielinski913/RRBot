from Classes.Client import Client
import login_data
import  time
client= Client(login_data.username, login_data.password, login_data.method)
client.login()
print("Your current ID")
print(client.getUserID())
print("Your current region resources")
client.checkRegionresource()
print("Your current stats")
client.checkUserStats()
print("Your current balance")
print(client.getMoney())
print("Checking if resources are available")
print(client.CheckAvailableResources())
print("You residency region ID")
print(client.CheckResidency())