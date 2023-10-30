import pickle, os
from random import randrange

dict={}
print("\t\tBienvenu dans le jeu\n")
nom=(input("Entrer ton nom : ")).lower()
name=""
for caractere in nom :
    if caractere !=" ":
        name+=caractere
dict[name]={'score':0}

def foncFichEcrire(dat):
    with open("Roulette.txt", "wb") as ouvrFich :
        pickle.dump(dat, ouvrFich)

def nombreSorti():
    nbrHas=randrange(0,101)
    with open("Roulette.txt", "rb") as ouvrFich :
        lire=pickle.load(ouvrFich)
        for name in lire.keys():
             print(f"Hello {name}, Bienvenue dans le jeu BevaHasard et bonne chance")
    while True :
        tot= lire.get(name, {'score': 0})['score']
        print("Vous avez 4 chance pour trouver ce nombre")
        for i in range(1,5):
            nmbr=(input("Quel est le nombre qui est choisi au hasard ")) 
            while(not nmbr.isdigit() or int(nmbr)<0 or int(nmbr)>100):
                nmbr=input("Erreur le nombre doit etre dans cette intervalle 0 a 100 : ")
            nbrConv=int(nmbr)
            if(nbrConv>nbrHas):
                print("Le nombre saisir est superieur")
                print("Il te reste {} chance".format(4-i))
            elif(nbrConv<nbrHas):
                print("Le nombre saisir est inferieur")
                print("Il te reste {} chance".format(4-i))
            else :
                print("Bingo! Vous avez gagne🏆🥇")                                                     
                print("Ton ancien score est",tot)
                tot+=(5-i)*30
                print("Ton nouveau score est : ", tot) 
                lire[name]['score'] += tot
                foncFichEcrire(lire)
                break
            chance=(4-i)
            if(chance==0):
                print("Vous avez perdu😭😭😭") 
                print("Le nombre qui a ete sorti est",nbrHas)
        choix = input("Saisir 'k' pour arrêter et n'importe quelle touche pour continuer : ")
        #nbrHas=randrange(0,101)
        os.system('cls')
        if choix.lower() == 'k':
            print("J'espere que t'as bien rigoler avec nous😁")
            break
foncFichEcrire(dict)
nombreSorti()
