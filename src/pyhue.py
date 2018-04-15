from http.client import HTTPConnection
import json

def rgb2xy(r, g, b):
    X = 0.412453 * r + 0.357580 * g + 0.180423 * b
    Y = 0.212671 * r + 0.715160 * g + 0.072169 * b
    Z = 0.019334 * r + 0.119193 * g + 0.950227 * b

    mag = (X+Y+Z)
    if mag == 0:
    	return (0,0)

    x = X / mag
    y = Y / mag
    return x, y

class Bridge:

	def __init__(self, bridge_ip, username):

		self.connection = HTTPConnection(bridge_ip)
		self.username   = username

	#get requests
	def getLights(self):
		call = '/api/' + self.username + '/lights'
		self.connection.request('GET', call)
		response = json.loads(self.connection.getresponse().read())
		print("ID", "Name")

		for key in response:
			print(key, response[key]['name'])

	def getLight(self, light_id):
		call = '/api/' + self.username + '/lights/' + str(light_id)
		self.connection.request('GET', call)
		response = json.loads(self.connection.getresponse().read())
		print(response['state'])

	#put requests
	def setState(self, light_id, new_state):
		call = '/api/' + self.username + '/lights/' + str(light_id) + '/state/'
		self.connection.request('PUT', call, new_state)
		response = json.loads(self.connection.getresponse().read())
		print(response)