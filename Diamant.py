################################################################################################################
#                                               SAE 1.01 - DIAMANTS                                            #
#                                               INF1-B                                                         #
#                                               PESENTI Aymeric                                                #
#                                               RUBIO Ilan                                                     #
################################################################################################################

from random import *

piege = ["araignée", "araignée", "araignée", "serpent", "serpent", "serpent", "lave", "lave", "lave", "boulet",
         "boulet", "boulet", "bélier", "bélier", "bélier"]

relique = ["relique"]

tresors = [1, 2, 3, 4, 5, 5, 7, 7, 9, 11, 11, 13, 14, 15, 17]

pioche_du_jeu = []

joueurs_restant = []

joueurs_parti = []

table_de_jeu = []

relique_sorti = 0


def creation_joueur():
    """
    Demande le nombre de joueurs et leurs noms, puis ajoute autant de joueur dans la liste l_joueurs
    avec leur nom respectif

    Params: Aucun
    Returns:  la liste des joueurs restant (liste)
    """
    nombre = int(input("Entrer le nombre de joueur pour la partie : "))
    
    for i in range(nombre):
        nom = input("Entrer le nom du joueur pour la partie : ")
        joueurs_restant.append([nom, 0, 0, 0, 0])       # [nom joueur, rubis tour, rubis coffre, valeur relique, action]


def creation_pioche(t, p, r):
    """
    Créer la pioche du jeu de la manche
    à partir des pioches relique, trésors et piège

    Params: t liste trésors
            p liste piège
            r liste relique
    Returns: la pioche (liste)
    """            
    pioche_du_jeu.extend(t) # ajoute tous les trésors dans la pioche
    
    pioche_du_jeu.extend(p) # ajoute tous les pièges dans la pioche
    
    pioche_du_jeu.extend(r) # ajoute toutes les reliques dans la pioche
    
    shuffle(pioche_du_jeu)  # mélange la pioche

    return pioche_du_jeu


def piocher_carte(pioche, board):
    """
    Prend pioche_du_jeu et tire la première carte de cette pioche, la retire de la pioche
    et l’ajoute à la table_de_jeux.

    Params : pioche liste, qui correspond à la pioche du jeu
             board liste, qui correspond aux éléments présents sur la table de jeu
    Returns : table de jeu apres pioche (liste)
    """

    carte_piochee = pioche.pop(0)   # prend la première carte de la pioche et la supprime de la pioche
    
    board.append(carte_piochee)     # ajoute la carte piochée sur la table de jeu
    
    return board


def action_tresor(carte_piochee, listej_restant, board):
    """
    Divise la valeur du trésor de manière eéquitable entre chaque joueur restant

    Params : carte_piochee variable, qui correspond à la carte piochee
             listej_restant liste, qui correspond à la liste des joueurs restants dans la partie
             board liste, qui correspond à la table de jeu
    Returns : la liste des joueurs restant et la table de jeu (2 liste)
    """
    part = board.pop(len(board)-1)      # enlève le trésor de la table de jeu
    if len(listej_restant) > 0:         # distribue de manière équitable la valeur du trésor s'il reste des joueurs
        part = part // len(listej_restant)
        reste = carte_piochee % len(listej_restant)
    
        for joueur in listej_restant:
            joueur[1] += part
    
        board.append(reste)             # ajoute à la table de jeu la valeur restante après le partage équitable
    
    return listej_restant, board


def action_piege(carte_piochee, listej_restant, board, listej_partant):
    """
    Si le piège de la carte piochée est déjà présent sur la table de jeu, alors tous les joueurs restant perdent
    leurs rubis gagnés durant la manche. De plus, une des deux cartes est supprimé de la liste des pièges. 

    Sinon, rien ne se passe, la carte reste sur le board.

    Params : carte_piochee variable, qui correspond à la carte piochee
             listej_restant liste, qui correspond à la liste des joueurs restants dans la partie
             board liste, qui correspond à la table de jeu
             listej_partant liste, qui correspond à la liste des joueurs partant de la partie
    Returns : liste des joueurs parti, liste des joueurs restant, liste des piège dans la pioche (3 liste)
    """
    nb = board.count(carte_piochee)           # compte le nombre de fois où le piège est présent sur la table de jeu
    if nb > 1:                                # si la carte est présente deux fois
        for joueur in listej_restant:         # supprime les rubis gagnés pendant la manche à tous les joueurs
            joueur[1] = 0
        
        listej_partant.extend(listej_restant)    
        listej_restant.clear()
        piege.remove(carte_piochee)          # supprime une fois de la liste piège la carte piège pioché en double

    return listej_partant,piege, listej_restant 

def action_carte(board, listej_restant, listej_partant):
    """
    Fait action en fonction de la dernière carte sur la table de jeu.
    Si c'est un piège, alors il appelle la fonction action_piege.
    Si c'est un trésor, alors il appelle la fonction action_tresor.
    Si c'est une relique, alors rien ne se passe.
    
    Params : board liste, qui correspond à la table de jeu
             listej_restant liste, qui correspond à la liste des joueurs restants dans la partie
             listej_partant liste, qui correspond à la liste des joueurs partant de la partie

    Returns : la liste des joueurs restant et la table de jeu (2 liste)
   """
    if board[len(board)-1] in piege:            # vérifie si c'est un piège
        action_piege(board[len(board)-1], listej_restant, board, listej_partant)           

    elif board[len(board)-1] in tresors:        # vérifie si c'est un trésor
        action_tresor(board[len(board)-1], listej_restant, board)

    return listej_restant, board


def repartition_reste(board, l_depart):
    """
    Calcule le reste et le repartie à chaque joueur
    Params: board liste, qui correspond à la table de jeu
            l_depart liste, qui correspond aux joueurs qui veulent partir
    Returns: l_depart (liste)
    """
    somr = 0
    l_nb = []
    for nb in board:                                    # Fait la somme de tous les rubis présents sur la table de jeu
        if nb not in piege and nb not in relique:
            somr += nb
            l_nb.append(nb)
    for nombre in l_nb:                                 # Enlève tous les rubis présents sur la table de jeu
        board.remove(nombre)
    r_tableau = somr % len(l_depart)
    board.append(r_tableau)                             # Ajoute sur la table de jeu la valeur restante, si il y en a, après le partage
                                                        # de la somme des rubis
    somr //= len(l_depart)                              
    for pjoueur in l_depart:                            # Distribue équitablement entre les joueurs partant les rubis de la somme
        pjoueur[2] += pjoueur[1] + somr
        pjoueur[1] = 0

    return l_depart

def action_relique(joueur,board):
    """
    Enleve la relique de la table de jeu et ajoute au joueur l'equivalent en rubis dans son coffre
    Params: joueur liste, qui correspond à l'inventaire du joueur qui part
            board liste, qui correspond à la table de jeu
    Returns: la table de jeu, joueur ayant récupéré relique (2 liste)
    """
    global relique_sorti        # compte le nombre de relique sorti de la pioche
    relique_sorti += 1
    if relique_sorti <= 3:      # En fonction du nombre déjà sortie, ajoute plus ou moins de rubis
        joueur[2] += 5
    else:
        joueur[2] += 10
   
    relique.remove("relique")   # enlève une relique de la liste des reliques
    board.remove("relique")     # retire les reliques de la table de jeu
    
    return board, joueur


def depart_joueurs(listej_restant, listej_parti, board):
    """
    Pour chaque joueur décidant de partir, va leur donner leur part des rubis sur le board
    puis les placer dans la liste des joueurs parti
    Params: listej_restant liste, qui correspond à la liste des joueurs restants dans la partie
            listej_parti liste, qui correspond à la liste des joueurs ne participant plus à la manche
            board liste, qui correspond à la table de jeu
    Returns: listej_restant, listej_parti, table de jeu (3 liste)
    """
    l_depart = []       # liste des joueurs voulant partir
    li_depart = []      # liste des indices des joueurs voulant partir
    for ijoueur in range(len(listej_restant)):      # ajoute aux listes l_depart et li_depart les joueurs voulant partir
        joueur = listej_restant[ijoueur]
        if joueur[4] == 1:
            l_depart.append(joueur)
            li_depart.append(ijoueur)
    li_depart.reverse()

    for ind in li_depart:           # supprime les joueurs de la liste des joueurs restant en fonction de leur indice
        listej_restant.pop(ind)

    repartition_reste(board, l_depart) 

    listej_parti.extend(l_depart) # ajoute à la liste des partis les joueurs qui veulent partir

    if len(l_depart) == 1:    # si un seul joueur veut partir pendant ce tour, alors s'il y a une relique
        pos = 0               # sur la table de jeu, il la récupère
        
        while pos < len(board):
            if board[pos] in relique:
                action_relique(l_depart[0],board)
            else:
                pos += 1    

    return listej_restant, listej_parti, board

def demander_coup_joueur_terminal(listej_restant, listej_parti):
    """
    Demande au joueur s'il continue ou s'il rentre.
    Il entre le coup sous la forme d'un entier, si c'est 0 alors le joueur continue à jouer la manche,
    si c'est 1, alors le joueur rentre.

    Params :listej_restant liste, qui correspond à la liste des joueurs restants dans la partie
            listej_parti liste, qui correspond à la liste des joueurs ne participant plus à la manche
    Returns: listej_restant, listej_parti (2 liste)
    """
    retour = 0
    for num_joueurs in listej_restant:   # demande à tous les joueurs s'ils veulent continuer

        reponse = int(input((num_joueurs[0]+", vous avez actuellement "+ str(num_joueurs[1])+" rubis sur vous et "+ \
            str(num_joueurs[2])+" rubis dans votre coffre. Voulez vous continuer l'expedition ? Entrez 0 pour continuer et 1 pour rentrer : ")))

        if reponse == 1:
            num_joueurs[4] = 1
            retour += 1

    if retour > 0:          # Regarde si au moins un joueur veut rentrer
        depart_joueurs(listej_restant, listej_parti, table_de_jeu)

    return listej_restant, listej_parti

def lancer_manche():
    """
    Initialise les données et lance une manche.
    C'est à dire que la fonction fait appel aux fonctions nécessaire pour le fonctionnement d'une manche.
    Params : None 
    Returns : None
    """
    creation_pioche(tresors, piege, relique)
    while len(joueurs_restant) > 0:
        demander_coup_joueur_terminal(joueurs_restant, joueurs_parti)
        if len(joueurs_restant) > 0:
            piocher_carte(pioche_du_jeu, table_de_jeu)
            print('\n',table_de_jeu[len(table_de_jeu)-1] ," a été piochée.",'\n')
            action_carte(table_de_jeu, joueurs_restant, joueurs_parti)
            print("Le plateau de jeu à la fin du tour se compose de : " , table_de_jeu, '\n')


def fin_manche():
    """
    Réinitialise les données après la fin de la manche.
    C'est à dire, que la fonction remet les différentes listes par défauts.
    Params : None 
    Returns : table de jeu, pioche du jeu, joueurs restant, joueurs parti, relique (5 liste)
    """
    for carte in table_de_jeu:
        if carte == "relique":
            relique.remove("relique")
    
    relique.append("relique")
    table_de_jeu.clear()
    pioche_du_jeu.clear()
    joueurs_restant.extend(joueurs_parti)
    joueurs_parti.clear()
    
    for joueur in joueurs_restant:
        joueur[4] = 0
    print('\n',"Cette manche est terminée.")
    
    return table_de_jeu, pioche_du_jeu, joueurs_restant, joueurs_parti, relique


def fin_jeu():
    """
    Fini la partie et affiche le gagnant de la partie.
    Params : None 
    Returns : None
    """
    gagnant = []
    max = 0
    for joueur in joueurs_restant:      # calcule le gagnant en fonction du nombre de rubis 
        if joueur[2] > max:             # qu'il possèede dans son coffre
            max = joueur[2]
            if gagnant != []:
                gagnant.pop(0)
            gagnant.append(joueur[0])
        elif joueur[2] == max:
            gagnant.append(joueur[0])
    if len(gagnant) == 1:
        print('\n','\n',"Le gagnant de la partie est ", gagnant[0],"avec ", max, " rubis.")
    else :
        print('\n','\n',"Les gagnants ex aequo sont ", ', '.join(gagnant), "avec ", max," rubis.")




def lancer_jeu():
    """
    Lance la partie et fait appel au fonction lancant et terminant les manches
    ainsi que la fonction permettant de finir le jeu.
    Params : None 
    Returns : None
    """
    print('\n','\n',"Bienvenue dans le jeu Diamants !!!",'\n','\n')
    creation_joueur()
    print('\n',"Bonne partie, amusez vous bien et que le meilleur ou la meilleure gagne !")
    for i in range(5):
        print('\n', '\n', "Début de la manche", i+1," :",'\n', '\n')
        lancer_manche()
        fin_manche()
    fin_jeu()

lancer_jeu()
