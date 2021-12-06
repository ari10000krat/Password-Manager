import tkinter as tk
import PIL
from tkinter.font import families
from PIL import ImageTk , Image
from Frames.forgotPassFrame import ForgotPassFrame
from Frames.loginFrame import LoginFrame
from Frames.setupFrame import SetupFrame
from Frames.resetPassFrame import ResetPassFrame
from Frames.searchPassFrame import SearchPassFrame
from Frames.addPassFrame import AddPassFrame
from Frames.homeFrame import HomeFrame
from Database.MPdatabase import PMPDatabase
from Database.PDatabase import siteData
from Backend.encryption import EncryptDeCrypt


database = PMPDatabase()
database.createTable()

Pdb = siteData()
Pdb.createDataTable()

en = EncryptDeCrypt()
en.generate_key()

class PasswordManagerApp(tk.Tk):
	def __init__(self, *args , **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		tk.Tk.geometry(self, '550x500+450+120')
		tk.Tk.title(self, 'Password Manager')
		tk.Tk.resizable(self, width=False, height=False)
		pwmLogo = tk.PhotoImage(file="img/pwm.png")
		pwmLogo = (pwmLogo.zoom(25)).subsample(32)
		tk.Tk.iconphoto(self, True , pwmLogo)

		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in (LoginFrame, ForgotPassFrame, SetupFrame, ResetPassFrame, HomeFrame, SearchPassFrame, AddPassFrame):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row=0, column=0, sticky="nsew")

		# Это вызовет setupFrame при первом открытии (означает, что пользователь не существует)
		# И поднимаем loginFrame в остальное время
		if(database.isEmpty()):
			self.show_frame(SetupFrame)
		elif(not database.isEmpty()):
			self.show_frame(LoginFrame)

	# Поднимает фрейм во всех файлах
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()