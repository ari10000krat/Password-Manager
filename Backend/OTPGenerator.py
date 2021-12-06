import random


class Otp:
	def __init__(self):
		self.characters = "abcdefghijklmnopqrstuvwxyz0123456789"
		self.OTP = ''

	# Используется в ForgotPassFrame и setupFrame для однократной генерации OTP
	def generateOTP(self):
		for _ in range(6):
			self.OTP += random.choice(self.characters)
		return self.OTP