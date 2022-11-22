#############################################
#-Jeux de rôle, entre player & IA			#
#-Attack random entre 3 & 11 attack damage	#
#-50 HP										#
#-3 Potion du joeur qui heal 25 HP			#
#############################################
import random
import time
import json
from os import path

###################Save and load Score#####################

data = {
	"win" : 0,
	"lose" : 0,
	"ratio" : float(0),
	"timePlayed": 0,
}

def load(dataRead):
	if not path.exists("data_file.json"):
		with open("data_file.json", "w") as write_file:
			json.dump(dataRead, write_file)
	else:
		with open("data_file.json", "r") as read_file:
			dataRead = json.load(read_file)
			return dataRead

def write(dataWrite):
	with open("data_file.json", "w") as write_file:
		json.dump(dataWrite, write_file)



###########################################################





class Player:
	def __init__(self, name, damageMax=11):
		self.name = name
		self.heal = 50
		self.damageMax = damageMax
	def damage(self):
		damage = random.randrange(3,self.damageMax+1)
		self.heal -= damage

###################Intro avant partie######################
def intro():
	print("Hello there, ce jeux est un jeu de rôle qui se joue au tour par tour.")
	print("Vous avez le choix entre attaquer l'ennemi ou prendre une potion pour vous régénerer")
	print("[P]Potion | [A]Attack | Bonne chance")

def chooseName():
	player = input("Quel est votre pseudo : ")
	IA = input("Le pseudo de votre ennemi : ")
	name = [player, IA]
	return name

def presentation(player, IA):
	print(f"le player : {player} va jouer contre : {IA}")
#######################################################

#####################################GAMEPLAY##################################
def game(player, ennemi, _dataGame):
	potion = 3
	while True:
		awnser = ""
		while  awnser != "P" and awnser != "A":
			print("[P]Potion | [A]Attack")
			awnser = input("Quelle action voulez-vous faire : ")
		if awnser == "A":
			ennemi.damage()
		else:
			if potion > 0:
				potion -= 1
				player.heal += 25
			else:
				print("vous n'avez plus de potion ! Tour sauté")
		if ennemi.heal <= 0:
			print("le joueur : ", player.name, " à gagné")
			_dataGame["win"] += 1
			break
		player.damage()
		if player.heal <= 0:
			print("le joueur : ", ennemi.name, " à gagné")
			_dataGame["lose"] += 1
			break
		
		print("le joueur : ", player.name, " à ", player.heal, "point de vie")
		print("le joueur : ", ennemi.name, " à ", ennemi.heal, "point de vie")
		time.sleep(0.1)
		_dataGame["timePlayed"] += 1
	_dataGame["ratio"] = _dataGame["win"] / (_dataGame["lose"]+1)
	
	return _dataGame
##################################################################################



######################################## END #####################################

def outro(_dataEnd):
	

	print("votre ratio est de :", _dataEnd["ratio"])
	
	print("vous venez de terminer votre partie, vous avez le choix entre : [T]TimePlayed, [C]Continue, ou [Q]Quitter")
	choice = ""

	while choice != "T" and choice != "C" and choice != "Q":
		choice = input("Choix : ")
		if choice == "T": 
			print("Vous avez joué : ", _dataEnd["timePlayed"]/60, "min")
			choice = ""
		elif choice == "C": 
			main(_dataEnd)
		else:
			pass



##################################################################################











def main(_dataMain):
	_dataMain = load(_dataMain)
	name = chooseName()
	player = Player(name[0], 19)
	ennemi = Player(name[1])
	presentation(player.name, ennemi.name)
	_dataMain = game(player, ennemi, _dataMain)
	write(_dataMain)
	outro(_dataMain)
main(data)


time.sleep(30)