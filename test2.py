from Classes.controller import rrbot
from Classes.me import Me
from Classes.User import User
import login_data

client= rrbot(login_data.headless)
client.login(login_data.username, login_data.password, login_data.method)

myProfile=Me(client)
print(myProfile.getStrength())
print(myProfile.getResidency())
wolf= User(client, 2000349734)
print(wolf.getResidency())