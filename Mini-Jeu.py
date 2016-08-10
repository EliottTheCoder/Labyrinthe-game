import random 
import os

print "\n\n************************ LE LABYRINTHE ************************"
print "\n\nBonjour a vous. Vous etes tombes par hasard dans un labyrinthe."

continuerPartie = True
while(continuerPartie): # Boucle principale du jeu: le joueur choisit s'il poursuit 
	fin = False			#une fois la partie finit
	niveau = 1
	
	while(fin == False): # 2e boucle: determine si le joueur a finit la partie en cours

		vue = """
		 ____________________ 
		|%d  __    __    __   |
		|  |1 |  |2 |  |3 |  |
		|__|__|__|__|__|__|__|           
		""" % niveau 				# Mon joli dessin de 3 portes 

	
		print "\n\nVous etes au niveau %d. Vous etes face a trois portes :" % niveau, vue 

		porteChoisie = 0
		while(porteChoisie < 1 or porteChoisie > 3): # 3e boucle: teste l'entree du joueur
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
		
		bonnePorte = random.randrange(1, 4) # Genere un nombre pseudo-aleatoir avec le module random

		if porteChoisie == bonnePorte:
			niveau += 1
			if niveau > 3: # Le joueur gagne au bout de 3 portes franchies
				print "\n\nBRAVOOOOO !!! Vous etes sorti du labyrinthe !"
				fin = True # Quitte la 2e boucle
			else:
				print "\n\nVous avez choisi la bonne porte, vous passez au niveau %d." % niveau 
			
		else : # Il s'il tombe sur la mauvaise porte
			print "\n\nVous vous etes trompe de porte, vous tomber dans un trou noir et atterrissez dans une dimension parallele."
			fin = True # Quitte la 2e boucle
	
	
	partie = -1
	while partie < 0 or partie > 1: # 4e boucle: teste l'entree du joueur
		print "Voulez vous recommencer ? Oui (1), Non (0)"
		partie = raw_input("> ")
		try :
			partie = int(partie)
		except ValueError:
			"Vous n'avez pas saisi un nombre.\n"
			partie = -1
		if partie < 0:
			print "Le nombre saisi est inferieur a 0.\n"
		if partie > 1:
			print "Le nombre saisi est superieur a 1.\n"
	
	if partie == 1:
		continuerPartie = True # Renvoie a la 1ere boucle
	else:
		continuerPartie = False # Quitte la boucle et le jeu
		
print "\nVous quittez la partie."
		
os.system("Pause")