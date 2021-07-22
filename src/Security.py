import secrets

class Security:
	pass

	@classmethod
	def generateToken(cls):
		token = secrets.token_urlsafe(32)
		with open("./token", "w") as f:
			f.write(token)

	@classmethod
	def validateToken(cls, tokenToCheck):

		tokenToCheck = tokenToCheck.removeprefix("Bearer ")

		token = None
		with open("./token", "r") as f:
			token = f.read()

		if(token is None):
			raise Exception("token not loaded")
		
		return token == tokenToCheck