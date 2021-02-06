from Classes.Client import Client
import login_data
client= Client(login_data.username, login_data.password, login_data.method, login_data.headless)
client.login()
#Ported
print("Your current ID")
print(client.getUserID())

print("Your current region resources")
print(client.checkRegionresource())
#Ported
print("Your current stats")
print(client.checkUserStats())
#Ported
print("Your current balance")
print(client.getMoney())
#Ported
print("Your username")
print(client.getUsername())
print("Checking if resources are available")
print(client.checkAvailableResources())
#Ported
print("You residency region ID")
print(client.checkResidency())
#Ported
print("Your party ID")
partyID=client.getUserParty()
print(partyID)
print("Your party name")
print(client.getPartyName(partyID))
#Endochi was used as an example
print("Endochi has "+str(client.checkPartyPopulation(272406))+" members")
print("Endochi party members:")
result=client.checkPartyMembers("272406")
print(result)
client.moveToRegion(3808)

client.getCountryRegions(2307)