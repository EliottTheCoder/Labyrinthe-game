# -*-coding:Latin-1 -*

from random import randrange 
from os import system

def perte(cause):
	""" Fonction affichant la defaite du joueur et sa cause."""
	print "\nVous avez choisi la MAUVAISE PORTE."
	print cause
	
def gagne(cause):
	"""Fonction affichant la victoire du joueur et sa cause"""
	print "\nVous avez choisi la BONNE PORTE."
	print cause

def choix_portes(niveau):
	""" Fonction prenant en compte le choix de porte du joueur"""

	vue = """
	 ____________________ 
	|%d  __    __    __   |
	|  |1 |  |2 |  |3 |  |
	|__|__|__|__|__|__|__|           
	""" % niveau	# Mon joli dessin de 3 portes 
	
	if niveau == 1:	
		print "\n\nVous etes au niveau 1. Vous penetrez dans une salle sombre et la lumiere de securite clignontante devoile 3 portes : "
		print vue
	elif niveau == 2: 
		print "\n\nVous etes au niveau 2. Cette fois ci, la salle a les couleurs d'un arc-en-ciel. Vous etes de nouveau face a 3 portes : "
		print vue
	else:
		print "\n\nVous etes au niveau 3. Le stress monte et vous entendez le son d'une machine a sous au loin. Pour la derniere fois, vous etes face a 3 portes: "  
		print vue 
		
	porteChoisie = 0
	while(porteChoisie < 1 or porteChoisie > 3): # Teste l'entree du joueur
	
		print "\nQuelle porte choisissez vous ? ('1', '2', '3')"
		porteChoisie = raw_input("> ")
			
		try:
			porteChoisie = int(porteChoisie)
		except ValueError:
			print "Vous n'avez pas entre un nombre.\n"
			porteChoisie = 0 # Renvoie au debut de la boucle
			continue
		if porteChoisie < 1:
			print "Le nombre saisi est inferieur a 1.\n"
		if porteChoisie > 3:
			print "Le nombre saisi est superieur a 3.\n"
	
	return porteChoisie

def continuer_partie():
	""" Le joueur choisit s'il continue ou non la partie"""
	
	partie = -1
	while partie < 0 or partie > 1: # Teste l'entree du joueur
		print "\nVoulez vous recommencer ? Oui (1), Non (0)"
		partie = raw_input("> ")
		try :
			partie = int(partie)
		except ValueError:
			"Vous n'avez pas saisi un nombre.\n"
			partie = -1
			continue
		if partie < 0:
			print "Le nombre saisi est inferieur a 0.\n"
		if partie > 1:
			print "Le nombre saisi est superieur a 1.\n"
	
	if partie == 1:
		return True # Renvoie a la 1ere boucle
	else:
		return False # Quitte la boucle et le jeu
 	
print "\n\n************************ LE LABYRINTHE ************************"
print "\n\nBonjour a vous. Vous etes tombes par hasard dans un labyrinthe."
	
continuerPartie = True
while(continuerPartie): # Boucle principale du jeu: le joueur choisit s'il poursuit 
	fin = False			#une fois la partie finit
	niveau = 1
	
	while(fin == False): # 2e boucle: determine si le joueur a finit la partie en cours
			
		porteChoisie = choix_portes(niveau)
		bonnePorte = randrange(1, 4) # Generation d'un nombre pseudo-aleatoire
		
		if porteChoisie == bonnePorte:
		
			if niveau == 1: 
				gagne("Vous traverser un couloir etroit rempli d'animaux empailes.")
			elif niveau == 2:
				gagne("Vous traversez un couloir aux murs taches de sang, peut-etre une ancienne boucherie...")
			else:
				gagne("Vous entrez dans une salle qui contient une vieille machine a sous...")
				print "Voulez-vous actionner le levier ? Oui = '1', Non = '0'"
				rep = raw_input('> ')
				rep = int(rep)
				if rep == 1:
					print "Les colonnes tournent... Vous gagnez %d $ !!!" % randrange(1000, 100000000)
				elif rep == 2:
					print "Vous n'utilisez pas la machine, dommage..."
				else:
					print "Vous ne savez pas tapper un nombre correctement et ne meritez donc pas ce cadeau."
				print "Vous QUITTEZ LE LABYRINTHE, a une prochaine fois !"	
				fin = True
			niveau += 1
		
		else:
			nb = randrange(1, 3) # Choisit un nombre au "hasard"
			if niveau == 1:
				if nb == 1: # La cause de la defaite est choisi aleatoirement pour chaque niveau
					perte("Vous entrez dans une salle pleine de hautes-herbes et vous vous faites capturer par un Pokemon;")				
				else:
					perte("Vous entrez et rencontrez un ours affame, il vous devore.")
			elif niveau == 2:
				if nb == 1:
					perte("Vous entrez sans le faire expres dans la gueule du loup (literalement).")
				else:
					perte("Vous tombez dans un puit et y rester jusqu'a mourir de faim/froid/fatigue.")
			else:
				if nb == 1:
					perte("Vous tombez dans un trou noir et rejoignez une dimension parrallele.")
				else:
					perte("Vous entrez dans une salle pleine de nourriture et mourrez a force de manger.\nIl ne fallait pas etre si gourmand !")
			fin = True # Le joueur a perdu
		
	continuerPartie = continuer_partie()
	
		
print "\nVous quittez la partie."
		
system("Pause")