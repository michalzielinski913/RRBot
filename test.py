from Classes.Client import Client
import login_data
client= Client(login_data.username, login_data.password, login_data.method)
client.login()