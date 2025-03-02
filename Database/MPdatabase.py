import sqlite3
import hashlib

#Это класс MasterTable, где пароль приложения (хешированный) и электронная почта хранятся в masterTable.
class PMPDatabase:
	def __init__(self):
		try:
			self.connect = sqlite3.connect("pwmdatabase.db")
			self.cursor = self.connect.cursor()
		except Exception as e:
			print(e)

	# Это создаст masterTable (что делается в файле passwordManagerApp.py)
	def createTable(self):
		qCreate = """
			CREATE TABLE IF NOT EXISTS masterTable (masterPass varchar(200), email varchar(100))
		"""
		self.cursor.execute(qCreate)
		self.connect.commit()

	# Эта функция будет хешировать пароль и вставить его вместе с введенным адресом электронной почты
	def insertIntoTable(self, mp, em):

		bytesMP = bytes(mp, 'utf-8')
		hashedMP = hashlib.sha256(bytesMP).hexdigest()

		qInsert = """
			INSERT INTO masterTable (masterPass, email)
			VALUES (?, ?)
		"""
		self.cursor.execute(qInsert, (hashedMP, em))
		self.connect.commit()

	# Эта функция обновит существующий пароль (хешированный) вместо того, чтобы создавать новую строку в базе данных
	# Эта функция вызывается в resetPassFrame.py
	def updateIntoTable(self, mp):
		mail = self.getMail()		
		bytesMP = bytes(mp, 'utf-8')
		hashedMP = hashlib.sha256(bytesMP).hexdigest()

		qUpdate = """
			UPDATE masterTable SET masterPass = ? WHERE email = ?
		"""
		self.cursor.execute(qUpdate, (hashedMP, mail))
		self.connect.commit()


	# Это используется, чтобы проверить, есть ли существующий пользователь в passwordManagerApp.py
	# Если пользователь существует:
	# -> если True: setupFrame поднимается
	# -> if False: создается loginFrame
	def isEmpty(self):
		qCount = """
			SELECT COUNT(*) FROM masterTable
		"""
		self.cursor.execute(qCount)
		entries = self.cursor.fetchall()
		if (entries[0][0] == 0):
			return True
		return False

	# Используется в loginFrame.py для проверки пароля в базе данных
	def loginCheck(self, mp):
		bytesMP = bytes(mp, 'utf-8')
		hashedMP = hashlib.sha256(bytesMP).hexdigest()

		qSelect = """
			SELECT * FROM masterTable
		"""
		self.cursor.execute(qSelect)
		data = self.cursor.fetchall()

		if hashedMP == data[0][0]:
			return True
		return False

	# Это используется в ForgotPassFrame.py для проверки электронной почты, введенной с базой данных
	def mailCheck(self, mail):
		qSelect = """
			SELECT * FROM masterTable
		"""
		self.cursor.execute(qSelect)
		data = self.cursor.fetchall()
		if mail == data[0][1]:
			return True
		return False


	# Используется в updateIntoTable () для получения почты из базы данных
	def getMail(self):
		qSelect = """
			SELECT * FROM masterTable
		"""
		self.cursor.execute(qSelect)
		data = self.cursor.fetchall()
		# print(data[0][1])
		mail = data[0][1]
		return mail