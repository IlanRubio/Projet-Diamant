
<h1 style="text-align: center;">SAE 1.01 - Diamant</h1> 

Ce document README a pour but de présenter le jeu Diamant.
Il permet de comprendre comment lancer le jeu, les différents problèmes
rencontrés lors de sa conception.


## Le document README suivra un plan :

* ### Comment faire fonctionner le jeu et jouer une partie ?
* ### Les différentes étapes lors de la conception du jeu


## Comment faire fonctionner le jeu et jouer une partie ?

### Comment lancer le jeu ?

Pour lancer le jeu, la version sans interface graphique, il suffit d'exécuter le programme,
la console s'ouvrira, elle affichera les différents éléments qui vous permettront de faire 
les choix dans votre partie, ou encore les éléments nécessaires à votre prise de décision 
comme la table de jeu, votre inventaire et la carte piochée.

### Comment jouer à Diamant ?

Une fois que vous avez lancé le jeu, vous devrez entrer le nombre de joueurs présents dans cette 
partie, ainsi que les différents noms de chaque joueur. Pour jouer et permettre un bon déroulement de la partie, 
il est conseillé d'avoir une personne supplémentaire ne jouant pas cette partie, qui sera l'arbitre de la partie.

L'arbitre de la partie devra alors suivre les instructions affichées dans la console et faire les propositions aux
joueurs lorsque c'est à leur tour. 
Une partie dure 5 manches, c'est assez rapide, donc réfléchissez bien lorsque vous faites vos choix.


## Les différentes étapes lors de la conception du jeu

### Le travail accompli 

Pour réaliser ce projet de création du jeu Diamant, nous avons procédé en plusieurs étapes nous permettant de travailler 
efficacement. Nous avons réparti notre travail en 4 étapes majeures.

Dans un premier temps, nous avons cherché comment jouer au jeu Diamant, les différentes règles afin de
recréer le jeu de la manière la plus fiable possible au jeu original. Lors de cette étape, nous avons établi
la liste des règles du jeu dans les moindres détails, et nous avons éclairci les détails que nous ne comprenions pas 
de la même façon. Cela nous a permis de partir sur une base commune afin de pouvoir essayer de créer le jeu en étant en accord sur les règles.

Dans un deuxième temps, nous avons réfléchi aux différentes fonctions nécessaires pour permettre la création du jeu. Une fois
les fonctions en tête, nous avons alors précisé explicitement quel rôle aurait chaque fonction, les différentes actions qu'elles devront réaliser.
Ainsi que les différents paramètres dont ces fonctions ont besoin afin de remplir leurs rôles.

Dans un troisième temps, nous avons commencé à écrire les fonctions à l'aide des différentes docstring écrit auparavant. Grâce aux étapes précédentes,
celle-ci fut assez rapide, il suffisait juste de mettre en place et d'écrire les lignes de codes nécessaires pour qu'elles soient fonctionnelles.

Enfin, dans un quatrième et dernier temps, nous avons testé les fonctions individuellement puis ensemble, afin de voir si tout fonctionner.
Durant ses tests, nous avons pu voir les différents problèmes de nos fonctions, ainsi que les différentes fonctions ou encore les différentes valeurs 
qu'ils pouvaient manquer pour un meilleur fonctionnement du jeu. 




### Les problèmes rencontrés lors de la création du jeu

Comme nous le savions avant de lancer notre jeu, les différentes fonctions n'étaient pas parfaites dès le début.
En effet, certaines fonctions n'avaient aucun problème, comme la fonction permettant de créer la pioche.
Mais la plupart des fonctions possédaient des erreurs, soit d'inattention, soit des problèmes auxquelles nous n'avions pas pensé.
Afin de bien comprendre ces erreurs, nous avons testé ces fonctions les unes après les autres de manière individuelle, puis collective.
De plus, pour bien comprendre d'où venaient nos erreurs, nous avons utilisé le site PythonTutor qui nous a permis de voir les différentes étapes
lors de l'appel de la fonction.
Une de nos erreurs courantes était avec les listes que nous avons utilisées dans les différentes boucles.
Par exemple, nous faisions : 

````
for i range(len(liste)-1):
    liste.pop(i)
````
Cela entrainait une modification de la taille de la liste et supprimer les mauvaises valeurs, et aussi 
la boucle continuait alors que la liste était finie, ce qui entrainait l'erreur suivante : 
````
list index out of range
````
Nous nous sommes alors rendus compte qu'une des solutions pour régler ce problème était de défiler la liste, mais 
en partant de la fin tout en diminuant l'indice petit à petit. Ainsi même si la liste devient plus petite, la taille de la liste ne sera 
plus un problème, lorsque l'on supprime un élément, ce sera le dernier et à chaque fois on fera appel au dernier élément de celle-ci.
````
for i in range(-1,-len(liste),-1):
    liste.pop(i)
````

## Jeu avec interface graphique

Nous avons commencé à créer une interface graphique qui n'est pas terminée. Cette interface graphique ne permet pas encore 
de pouvoir jouer au jeu. Actuellement, l'interface graphique permet uniquement à l'utilisateur de renseigner le nombre de joueurs
voulant jouer, ainsi que les pseudonymes de chaque joueur. Vous pouvez seulement les renseigner le bouton confirmer n'est pas encore 
configuré et le jeu ne peut pas se lancer. Par contre, vous pouvez quitter le jeu sans problème en appuyant sur le bouton "Quitter le jeu", 
depuis n'importe quelle page du jeu. Vous pouvez également quitter le jeu depuis n'importe quelle fenêtre en appuyant sur votre touche Echap.

**Auteur :** Pesenti Aymeric et Rubio Ilan INF1B