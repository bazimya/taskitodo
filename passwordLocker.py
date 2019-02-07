import argparse
import requests
from firebase import firebase

parser = argparse.ArgumentParser()
parser.add_argument("username", help="Enter name")
parser.add_argument("password", help="Enter password")
args = parser.parse_args()

# Communication to the server
class passwordLocked:
	def __init__(self, username, password):

		# ask firebase for this credentials
		print("Asking firebase, "+username)		

		firebase = firebase.FirebaseApplication('https://learnbase-baa6d.firebaseio.com/', None)
		result = firebase.get('/forums', None)
		print(result)
		# response = requests.post(self.apiAddress, data = {'action':'carExit', 'carPlate':plateNumber, 'parkId':parking, 'cameraId':camera})