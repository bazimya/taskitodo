from firebase import firebase
class user:
	def login(self, username, password):

		""""
			Function to login the user
		"""

		# ask firebase for this credentials
		print("Asking firebase, "+username)		

		firebase = firebase.FirebaseApplication('https://learnbase-baa6d.firebaseio.com/', None)
		result = firebase.get('/forums', None)
		print(result)