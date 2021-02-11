from Classes.controller import rrbot
from Classes.me import Me
from Classes.User import User
from Classes.party import Party
from Classes.Country import Country
import login_data

client= rrbot(login_data.headless)
client.login(login_data.username, login_data.password, login_data.method)

myProfile=Me(client)
print(myProfile.getStrength())
print(myProfile.getResidency())
wolf= User(client, 2000349734)
print(wolf.getResidency())
print(myProfile.getResources())
endochi=Party(client, 272406)
print(endochi.getPartyName())
print(endochi.getPartyPopulation())
print(endochi.getPartyMembersID())
print(myProfile.checkAvailableResources())
#myProfile.moveToRegion(3858)
america=Country(client, 2307)
print(america.getName())
print(america.getRegionsAmount())