# coding: utf-8

from keyboard import *
from colorama import Back, Fore, Style, init
init()
import os

class UTCI():
	def __init__(self):
		self.select = 0
		self.page = 0
		self.lenscr = 0
		self.favorites = []

		# Folders where you store scripts
		self.pathsWithScripts = ["C:\\Scripts", "D:\\Python Scripts"]

		# Path to cfg with yr favorites scripts
		self.configpath = "ScriptMenuSettings.cfg"

		self.parseExtensions = ["py", "pyw", "bat"]

	def getFavoriteScripts(self):
		with open(self.configpath, "r", encoding="utf8") as RWF:
			for line in RWF:
				self.favorites.append(line)

	def addFavoriteScripts(self):
		if self.pythonfiles[self.page][self.select] in self.favorites:
			self.show_menu(True)
			self.show_menu(False)
		else:
			self.favorites.append(self.pythonfiles[self.page][self.select])
			with open(self.configpath, "w", encoding="utf8") as RWF:
				RWF.write("\n".join(self.favorites))
		self.show_menu(False)

	def delFavoriteScripts(self):
		if self.pythonfiles[self.page][self.select] not in self.favorites:
			self.show_menu(True)
			self.show_menu(False)
		else:
			self.favorites.remove(self.pythonfiles[self.page][self.select])
			with open(self.configpath, "w", encoding="utf8") as RWF:
				RWF.write("\n".join(self.favorites))
		self.show_menu(False)

	def getAllScripts(self):
		lists = []
		for objScripts in self.pathsWithScripts:
			lists += list(os.walk(objScripts))

		pythonfiles = []
		pythonfilesfor = []

		for __ in lists:
			for item in __[-1]:
				if item.split(".")[-1] in self.parseExtensions:
					pythonfilesfor.append(__[0]+"\\"+item)
					self.lenscr += 1
				if len(pythonfilesfor) == 25:
					pythonfiles.append(pythonfilesfor)
					pythonfilesfor = []
		if len(pythonfilesfor) != 0:
			pythonfiles.append(pythonfilesfor)

		self.pythonfiles = pythonfiles

	def event_handler(self):
		self.getAllScripts()
		self.getFavoriteScripts()
		while True:
			self.choose()

	def choose(self):
		self.show_menu(False)

		add_hotkey("up", self.up)
		add_hotkey("down", self.down)
		add_hotkey("right", self.right)
		add_hotkey("left", self.left)
		add_hotkey("+", self.addFavoriteScripts)
		add_hotkey("-", self.delFavoriteScripts)

		wait("enter")

		unhook_all_hotkeys()

		os.system("cls")

		if self.pythonfiles[self.page][self.select].split(".")[-1] == "bat":
			os.system('"'+str(self.pythonfiles[self.page][self.select])+'"')
		else: 
			os.system('start "'+str(self.pythonfiles[self.page][self.select])+'"')

		print("Press ESC to back")

		wait("esc")

	def show_menu(self, err, error_type=None):
		os.system("cls")

		print("Page: "+str(self.page+1)+" из "+str(len(self.pythonfiles))+"    Scripts count: "+str(self.lenscr)+"\nScripts: \n")

		for __ in self.pythonfiles[self.page]:

			marker = Fore.YELLOW+Style.BRIGHT+" * Pinned *"+Style.RESET_ALL if __ in self.favorites else "" 

			if len(self.pythonfiles[self.page])-1 < self.select:
				self.select = len(self.pythonfiles[self.page])-1
			if self.pythonfiles[self.page][self.select] == __:

				if err == True:
					print(Back.RED+"> "+str(__)+" <"+Style.RESET_ALL+marker)
				else:
					print(Back.GREEN+"> "+str(__)+" <"+Style.RESET_ALL+marker)
			else:
				print("  "+str(__)+marker)

	def up(self):
		if self.select > 0:
			self.select-=1
			self.show_menu(False)
		else:
			self.show_menu(True)
			self.show_menu(False)

	def down(self):
		if self.select < len(self.pythonfiles[self.page])-1:
			self.select+=1
			self.show_menu(False)
		else:
			self.show_menu(True)
			self.show_menu(False)

	def right(self):
		if self.page < len(self.pythonfiles)-1:
			self.page+=1 
			self.show_menu(False)
		else:
			self.show_menu(True)
			self.show_menu(False)

	def left(self):
		if self.page > 0:
			self.page -=1
			self.show_menu(False)
		else:
			self.show_menu(True)
			self.show_menu(False)

localacc = UTCI()

localacc.event_handler()