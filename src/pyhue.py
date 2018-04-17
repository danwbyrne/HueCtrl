from http.client import HTTPConnection
import json
import math

def RGBtoHEX(rgb):
	return  ''.join(['%X' % value for value in rgb])

def HEXtoRGB(rgb):
	try:
		return ( int(rgb[:2],16), int(rgb[2:4],16), int(rgb[4:6],16) )

	except ValueError:
		return (0, 0, 0)


def enhanceColor(value):
	if value > 0.04045:
		return math.pow( (value + .055)/(1.055), 2.4)
	return value / 12.92
		
def RGBtoXY(r,g,b):
	r = enhanceColor(r)
	g = enhanceColor(g)
	b = enhanceColor(b)

	X = 0.65*r + .1035*g + .197*b
	Y = .234*r + .743*g + .023*b
	Z = .053*g + 1.036*b

	mag = X+Y+Z

	if mag == 0:
		return (0,0)

	return X / mag, Y / mag

def getBri(rgb):
	return int((0.299*rgb[0] + 0.587*rgb[1] + 0.0722*rgb[2])*255.)


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
		#print(response['state'])

	#put requests
	def setState(self, light_id, new_state):
		call = '/api/' + self.username + '/lights/' + str(light_id) + '/state/'
		self.connection.request('PUT', call, new_state)
		response = json.loads(self.connection.getresponse().read())
		#print(response)