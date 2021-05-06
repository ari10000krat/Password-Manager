from sqlite3.dbapi2 import SQLITE_ALTER_TABLE
import tkinter as tk
from Frames.forgotPassFrame import ForgotPassFrame
from Database.MPdatabase import PMPDatabase


class LoginFrame(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		#colors
		self.primaryColor = '#6200ee'
		self.secondaryColor = '#3700b3'
		self.backgroundColor = '#000000'
		self.surface1Color = '#121212'
		self.surface2Color = '#212121'
		self.successColor = '#03dac6'
		self.errorColor = '#cf6679'
		self.priTextColor = '#000000'
		self.secTextColor = '#ffffff'

		#fonts
		self.labelFont = ("Rockwell", 12, "bold")
		self.entryFont = ("Rockwell", 16)

		self.controller = controller

		self.loginFrame = tk.LabelFrame(self, text="Login", bd=5, bg=self.backgroundColor, fg=self.secTextColor)
		self.loginFrame.place(relx=0, rely=0, relwidth=1, relheight=1)
		self.mpassentry = tk.Entry(self.loginFrame, show = "*", width = 20, font = self.entryFont, bg=self.surface1Color, fg=self.primaryColor)
		self.mpassentry.place(relx=0.275, rely=0.384, relwidth=0.45, relheight=0.07)
		self.mpassentry.bind("<Return>", self.shortcuts)
		self.mpassentry.delete(0, 'end')
		self.mpassenter = tk.Button(self.loginFrame, text = "Enter", bg=self.primaryColor, fg=self.secTextColor, command = lambda: self.checkPass(), font = self.labelFont)
		self.mpassenter.place(relx=0.35, rely=0.52, relwidth=0.3, relheight=0.1)
		self.forgotPass = tk.Button(self.loginFrame, text = "Forgot Password", bg=self.primaryColor, fg=self.secTextColor, command = lambda: controller.show_frame(ForgotPassFrame))
		self.forgotPass.place(relx=0.35, rely=0.7, relwidth=0.35, relheight=0.08)


	# Shortcut for Enter key 
	def shortcuts(self, event):
		key = event.char
		if key == '\r':
			self.checkPass()

	# Check entered password with database (Pending: raises next frame) 
	def checkPass(self):
		mp = self.mpassentry.get()
		pdb = PMPDatabase()
		if (pdb.loginCheck(mp)):
			confirmLabel = tk.Label(self.loginFrame, text = "Login Successful", font = self.labelFont, bg = self.successColor, fg=self.priTextColor)
			confirmLabel.place(relx=0.16, rely=0.02, relwidth=0.7, relheight=0.05)
			confirmLabel.after(2000, confirmLabel.destroy)
			from Frames.homeFrame import HomeFrame
			self.controller.show_frame(HomeFrame)
			return
		errorLabel = tk.Label(self.loginFrame, text = "Wrong Password... try again", font = self.labelFont, bg = self.errorColor, fg = self.priTextColor)
		errorLabel.place(relx=0.16, rely=0.02, relwidth=0.7, relheight=0.05)
		errorLabel.after(2000, errorLabel.destroy)