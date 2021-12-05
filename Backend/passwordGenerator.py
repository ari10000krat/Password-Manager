import random
import subprocess
from tkinter import  *

class Pgenerator(object):
	def __init__(self):
		self.characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%*()"
		self.Pass = ''

	# Used in forgotPassFrame and setupFrame to generate OTP once
	def generatePass(self):
		for _ in range(10):
			self.Pass += random.choice(self.characters)
		return self.Pass

	def c2c(self, txt):
    	#Windows
		# cmd='echo '+(txt).strip()+'|clip'
		# return subprocess.check_call(cmd, shell=True)

		#Linux
		r = Tk()
		msg = Label(text='Password has been copied')
		msg.pack()
		r.withdraw()
		r.clipboard_clear()
		r.clipboard_append(txt)
		r.deiconify()
		r.mainloop()
