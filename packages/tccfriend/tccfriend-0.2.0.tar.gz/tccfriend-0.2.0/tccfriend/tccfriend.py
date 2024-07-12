import pyrebase
import sys
from itertools import cycle
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QGridLayout,QLineEdit
import matplotlib as matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import  QLabel,  QVBoxLayout, QWidget,  QGridLayout, QScrollArea
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

#Copyright (c) 2002-2011 John D. Hunter; All Rights Reserved

# ajout version cryptée:
import base64
import secrets
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

KDF_ALGORITHM = hashes.SHA256()
KDF_LENGTH = 32
KDF_ITERATIONS = 120000

#La variable salt sera le sel pour la cryptographie:
global salt
salt = b"le sel"

global password

def encrypt(plaintext: str, password: str) -> (bytes, bytes):
    # Derive a symmetric key using the passsword and a fresh random salt.
    kdf = PBKDF2HMAC(
        algorithm=KDF_ALGORITHM, length=KDF_LENGTH, salt=salt,
        iterations=KDF_ITERATIONS)
    key = kdf.derive(password.encode("utf-8"))

    # Encrypt the message.
    f = Fernet(base64.urlsafe_b64encode(key))
    ciphertext = f.encrypt(plaintext.encode("utf-8"))

    return ciphertext

def decrypt(ciphertext: bytes, password: str, salt: bytes) -> str:
    # Derive the symmetric key using the password and provided salt.
    kdf = PBKDF2HMAC(
        algorithm=KDF_ALGORITHM, length=KDF_LENGTH, salt=salt,
        iterations=KDF_ITERATIONS)
    key = kdf.derive(password.encode("utf-8"))

    # Decrypt the message
    f = Fernet(base64.urlsafe_b64encode(key))
    plaintext = f.decrypt(ciphertext)

    return plaintext.decode("utf-8")


firebaseConfig = {

  "apiKey": "AIzaSyDMx_ejVc9I1M4WoAxgJjzHWsYvx0fYDgo",

  "authDomain": "freetcc-4ffb8.firebaseapp.com",

  "databaseURL": "https://freetcc-4ffb8-default-rtdb.europe-west1.firebasedatabase.app",

  "projectId": "freetcc-4ffb8",

  "storageBucket": "freetcc-4ffb8.appspot.com",

  "messagingSenderId": "55141602566",

 "appId": "1:55141602566:web:92a6af1a5b5c803dca7a87",

  "measurementId": "G-TEJXKX7GK1"

}
#Variables de FireBase:


#Variables des instances de classes des fenêtres:

InstancePrintGraphClass = [1]

#global gestion



firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db=firebase.database()
storage=firebase.storage()

#La variable globale qui va recevoir le retour de la Base de donnée (un objet):
global results
#La copie de la variable results sous forme d'une liste de liste (pour chaque graph) contenant une chaine pour
# le titre d'un graph et un dictionnaire pour le point d'un graph:
#Cette copie était nécessaire en raison d'un disfonctionnement de la variable results qui contenait l'objet firebase
#dans certains cas.

copie_results= []

def GetText(FileName):
    f = open(FileName, "r")
    chaine = f.readline()
    text =""
    text += chaine

    while chaine:
        chaine = f.readline()
        text += chaine
    f.close()
    return text

#recupération du CSS de l'ensemble des variables de style:

WindowBackground = "*{background: '#28b5d1';}"


StyleTitre = """    *{
            border: 4px solid '#1B8BA1';
            background: '#6DBCCC';
            border-radius: 15px;
            font-size: 25px;
            color: 'black';
            padding: 15px 0;
            margin: 10px 10px;
        }"""


StyleScrollGraph= """    *{
            border: 4px solid 'white';
            background: '#6DBCCC';
            border-radius: 15px;
            font-size: 17px;
            color: 'black';
            padding: 15px 0;
            margin: 10px 10px;
        }"""


StyleText =  """*{border: 4px solid 'white';\n
            background: '#6DBCCC';\n
            border-radius: 15px;
            font-size: 20px;
            color: 'black';
            padding: 15px 0;
            margin: 10px 10px;}"""




StyleScrollGraphHover = """    *{
            border: 4px solid 'white';
            background: '#6DBCCC';
            border-radius: 15px;
            font-size: 17px;
            color: 'black';
            padding: 15px 0;
            margin: 10px 10px;
        }
        *:hover{
            background: '#22CCEE';
        }
"""


StyleHover = """     *{
            border: 4px solid 'white';
            background: '#6DBCCC';
            border-radius: 15px;
            font-size: 20px;
            color: 'black';
            padding: 15px 0;
            margin: 10px 10px;
        }
        *:hover{
            background: '#22CCEE';
        }
"""


Licence = """CE LOGICIEL EST UN PROTOTYPE. Il a été developpé à des fins éducatives et n'est pas destiné à un
 veritable usage privé ou public.La base de donnée utilisée n'est pas garantie et a l'heure de son
 deploiement elle n'est même pas sécurisée.La licence de TCC FRIEND est BSD, copiée ci-dessous:

                                                     Copyright (c) 2023, Nicolas T. nterce@gmail.com
        All rights reserved.\n"
        Redistribution and use in source and binary forms, with or without
        modification, are permitted provided that the following conditions are met:

        * Redistributions of source code must retain the above copyright
          notice, this list of conditions and the following disclaimer.
        * Redistributions in binary form must reproduce the above copyright
          notice, this list of conditions and the following disclaimer in the
          documentation and/or other materials provided with the distribution.
        * Neither the name of the University of California, Berkeley nor the
          names of its contributors may be used to endorse or promote products
          derived from this software without specific prior written permission.

        THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND ANY
        EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
        WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
        DISCLAIMED. IN NO EVENT SHALL THE AUTHOR AND CONTRIBUTORS BE LIABLE FOR ANY
        DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
        (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
        LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
        ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
        (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
        SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."""


CoursTCC = """Apprendre l'anxiété : Psychopédagogie

Une première étape importante pour surmonter un problème psychologique est d'en apprendre davantage à son sujet, ce que l'on appelle la "psychoéducation".

Apprendre à connaître votre problème peut vous apporter le réconfort de savoir que vous n'êtes pas seul et que d'autres ont trouvé des stratégies utiles pour le surmonter.
 Vous pouvez même trouver utile que les membres de votre famille et vos amis en apprennent également davantage sur votre problème. Certaines personnes trouvent que le simple
 fait de mieux comprendre leurs problèmes constitue un grand pas vers la guérison.

Par exemple, une personne souffrant de fréquentes attaques de panique commencerait par apprendre ce qu'est une attaque de panique (voir Trouble panique). En se renseignant
 sur la panique, elle découvrirait que, bien qu'une attaque de panique soit une expérience inconfortable, elle est temporaire et sans danger.

Un thérapeute TCC est en mesure de fournir des informations utiles sur votre problème particulier, mais vous pouvez également trouver des informations par vous-même auprès
 de sources réputées dans les librairies et sur Internet.

La psychoéducation est une première étape essentielle, mais il est important de se rappeler qu'elle n'est qu'une partie d'un plan de traitement complet.
Stratégies de relaxation

Apprendre à détendre son corps peut être un élément utile de la thérapie. La tension musculaire et la respiration superficielle sont toutes deux liées au stress et à l'anxiété
(et parfois à la dépression). Il est donc important de prendre conscience de ces sensations corporelles et de pratiquer régulièrement des exercices pour apprendre à se détendre.

Deux stratégies souvent utilisées dans le cadre de la TCC sont la respiration calme, qui consiste à ralentir consciemment la respiration, et la relaxation musculaire progressive,
 qui consiste à contracter et détendre systématiquement différents groupes de muscles. Comme pour toute autre compétence, plus vous pratiquerez ces stratégies de relaxation,
plus elles seront efficaces et rapides. D'autres stratégies de relaxation utiles comprennent l'écoute de musique calme, la méditation, le yoga et les massages.

Il est toutefois important de comprendre que l'objectif de la relaxation n' est pas d'éviter ou d'éliminer l'anxiété (car l'anxiété n'est pas dangereuse), mais de rendre un peu
 plus facile la gestion de ces sentiments.
Réflexion réaliste

Pour gérer efficacement les émotions négatives, il faut identifier les pensées négatives et les remplacer par des pensées réalistes et équilibrées. Étant donné que nos pensées
 ont un impact important sur la façon dont nous nous sentons, changer nos pensées inutiles en pensées réalistes ou utiles est un élément clé pour se sentir mieux. "Penser de
façon réaliste" signifie porter un regard équilibré et juste sur soi-même, sur les autres et sur le monde, sans être excessivement négatif ou positif. Par exemple :
Pensée inutile et irréaliste 	Une pensée plus réaliste et plus équilibrée
Je fais toujours tout foirer, je suis un tel raté. Qu'est-ce qui ne va pas chez moi ? 	Tout le monde fait des erreurs, y compris moi - je ne suis qu'un être humain. Tout ce que
 je peux faire maintenant, c'est faire de mon mieux pour réparer la situation et tirer les leçons de cette expérience.
Je ne peux pas le faire. Je suis trop anxieuse. Pourquoi je n'arrive pas à contrôler mon anxiété ? 	C'est normal et normal d'être anxieux. Ce n'est pas dangereux, et cela ne doit
 pas m'arrêter. Je peux me sentir anxieuse et aller quand même à la fête.
Les étapes d'une réflexion réaliste

Sachez ce que vous pensez ou vous dites. La plupart d'entre nous n'ont pas l'habitude de prêter attention à la façon dont nous pensons, même si nous sommes constamment affectés
par nos pensées. Le fait de prêter attention à vos pensées (ou monologue intérieur) peut vous aider à déterminer le type de pensées que vous avez habituellement.

Une fois que vous êtes plus conscient de vos pensées, essayez d'identifier les pensées qui vous font vous sentir mal, et déterminez s'il s'agit de pensées problématiques qui doivent
 être remises en question. Par exemple, si vous vous sentez triste en pensant à votre grand-mère qui se bat contre un cancer, cette pensée n'a pas besoin d'être remise en question
car il est tout à fait normal de se sentir triste en pensant à un être cher qui souffre. Mais si vous vous sentez triste après qu'un ami a annulé votre déjeuner et que vous commencez
 à penser qu'il y a manifestement quelque chose qui ne va pas chez vous et que personne ne vous aime, cela pose problème car cette pensée est extrême et ne repose pas sur la réalité.

Prêtez attention à l'évolution de votre émotion, aussi minime soit-elle. Lorsque vous remarquez que vous êtes de plus en plus bouleversé ou angoissé, demandez-vous : "Qu'est-ce que
 je me dis en ce moment ?" ou "Qu'est-ce qui me fait me sentir bouleversé ?".

Lorsque vous avez l'habitude d'identifier les pensées qui conduisent à des émotions négatives, commencez à examiner ces pensées pour voir si elles sont irréalistes et inutiles.
L'une des premières choses à faire est de voir si vous êtes tombé dans les pièges de la pensée (par exemple, catastrophisme ou surestimation du danger), qui sont des façons trop
 négatives de voir les choses. Vous pouvez également vous poser une série de questions pour remettre en question vos pensées négatives (voir Remettre en question les pensées
négatives), comme "Quelles sont les preuves que cette pensée est vraie ?" et "Est-ce que je confonds une possibilité avec une probabilité ? C'est peut-être possible, mais est-ce
 probable ?"

Enfin, après avoir remis en question une pensée négative et l'avoir évaluée de manière plus objective, essayez de trouver une autre pensée plus équilibrée et plus réaliste. Cela peut
 contribuer à réduire votre détresse. En plus de trouver des énoncés réalistes, essayez de trouver des énoncés d'adaptation rapides et faciles à retenir (p. ex., "Cela m'est déjà
arrivé et je sais comment le gérer") et des énoncés positifs (p. ex., "Il faut du courage pour affronter les choses qui me font peur").

Il peut également être particulièrement utile de noter vos pensées réalistes ou vos affirmations utiles pour faire face à la situation sur une fiche ou une feuille de papier. Gardez
 ensuite cette carte sur vous pour vous rappeler ces affirmations lorsque vous vous sentez trop bouleversé pour penser clairement.
Affronter ses peurs : Exposition

Il est normal de vouloir éviter les choses que vous craignez, car cela réduit votre anxiété à court terme. Par exemple, si vous avez peur des endroits petits et fermés comme les
ascenseurs, vous serez moins anxieux si vous prenez les escaliers. Cependant, l'évitement vous empêche d'apprendre que les choses que vous craignez ne sont pas aussi dangereuses
 que vous le pensez. Ainsi, dans ce cas, prendre les escaliers vous empêche d'apprendre que rien de mal n'arrive lorsque vous prenez l'ascenseur.

Dans la TCC, le processus d'affrontement des peurs s'appelle l'exposition - et c'est l'étape la plus importante pour apprendre à gérer efficacement son anxiété. L'exposition
consiste à entrer progressivement et de façon répétée dans des situations redoutées jusqu'à ce que vous vous sentiez moins anxieux. Vous commencez par des situations qui ne vous
 causent qu'un peu d'anxiété, puis vous passez progressivement à des situations qui vous causent beaucoup d'anxiété (voir Affronter ses peurs : exposition).

La première étape consiste à dresser une liste des situations, des lieux ou des objets qui vous font peur. Par exemple, si vous avez peur des araignées et que vous voulez surmonter
 cette peur pour pouvoir faire du camping avec des amis, la liste peut inclure : regarder des photos d'araignées, regarder des vidéos d'araignées, observer une araignée dans un
 aquarium et se tenir à l'autre bout de la pièce à côté d'une personne qui tient une araignée. Une fois la liste établie, classez-la de la moins effrayante à la plus effrayante.

En commençant par la situation qui vous cause le moins d'anxiété, pratiquez cette activité ou faites face à cette situation de façon répétée (par exemple, regarder des photos d'araignées)
jusqu'à ce que vous commenciez à vous sentir moins anxieux. Lorsque vous pouvez faire face à cette situation spécifique plusieurs fois sans ressentir beaucoup d'anxiété, vous êtes
prêt à passer à l'étape suivante de votre liste.

La TCC insiste sur l'importance de faire face à ses peurs de manière régulière. Plus vous vous entraînerez, plus vite vos peurs s'estomperont ! Le fait de connaître des succès
et de se sentir bien dans sa peau est un puissant facteur de motivation pour continuer.
Comment prévenir une rechute

Gérer efficacement son problème, c'est un peu comme faire de l'exercice - il faut se "maintenir en forme" et faire de la pratique des compétences utiles une habitude quotidienne.
 Cependant, il arrive que les gens retombent dans leurs vieilles habitudes, perdent les améliorations qu'ils ont apportées et fassent une rechute. Une rechute est un retour complet
 à toutes vos anciennes façons de penser et de vous comporter avant d'avoir appris de nouvelles stratégies pour gérer votre problème. Bien qu'il soit normal que les gens
fassent des écarts (un bref retour aux anciennes habitudes) en période de stress, de mauvaise humeur ou de fatigue, une rechute n'est certainement pas nécessaire. Voici quelques
 conseils sur la façon de prévenir les défaillances et les rechutes :

Continuez à mettre en pratique vos compétences en matière de TCC ! C'est le meilleur moyen d'éviter une rechute. Si vous vous exercez régulièrement, vous serez en mesure de faire
 face à toutes les situations auxquelles vous serez confronté.

Conseil : établissez un calendrier pour vous-même en indiquant les compétences que vous allez travailler chaque semaine.

Sachez à quel moment vous êtes plus susceptible de faire une rechute (p. ex. en période de stress ou de changement) et vous serez moins susceptible d'en faire une. Il est également
 utile de dresser une liste des signes avant-coureurs (p. ex., pensées plus anxieuses, disputes fréquentes avec des proches) qui vous indiquent que votre anxiété pourrait augmenter.
 Une fois que vous savez quels sont vos signes avant-coureurs ou vos " signaux d'alarme ", vous pouvez établir un plan d'action pour y faire face. Il peut s'agir, par exemple,
de mettre en pratique certaines techniques de TCC, comme la respiration calme ou la remise en question de vos pensées négatives.

N'oubliez pas que, comme tout le monde sur terre, vous êtes un travail en cours ! Un bon moyen de prévenir les défaillances futures est de continuer à relever de nouveaux défis.
Vous risquez moins de retomber dans vos vieilles habitudes si vous cherchez continuellement des moyens nouveaux et différents de surmonter votre anxiété.

Si vous avez eu une défaillance, essayez de comprendre quelle situation vous y a conduit. Cela peut vous aider à élaborer un plan pour faire face aux situations difficiles à l'avenir.
 Gardez à l'esprit qu'il est normal d'avoir des défaillances occasionnelles et que vous pouvez en tirer de nombreuses leçons.

La façon dont vous pensez à votre défaillance a un impact énorme sur votre comportement ultérieur. Si vous pensez que vous êtes un raté et que vous avez réduit à néant tous vos efforts,
 vous êtes plus susceptible d'arrêter d'essayer et de rechuter. Au contraire, il est important de garder à l'esprit qu'il est impossible de désapprendre toutes les compétences et
de revenir à la case départ (c'est-à-dire avoir de l'anxiété et ne pas savoir comment la gérer), car vous savez comment gérer votre anxiété. Si vous avez une défaillance, vous pouvez
 vous remettre sur la bonne voie. C'est comme faire du vélo : une fois que vous savez en faire, vous ne l'oubliez pas ! Il se peut que vous soyez un peu rouillé, mais il ne faudra
pas longtemps avant que vous soyez aussi bon qu'avant.

Rappelez-vous que les défaillances sont normales et peuvent être surmontées. Ne vous culpabilisez pas et ne vous traitez pas d'" idiot " ou de " perdant ", car cela n'aide pas. Soyez
gentil avec vous-même, et réalisez que nous faisons tous des erreurs parfois !

Enfin, veillez à vous récompenser pour tout le travail que vous faites. Une récompense peut consister à sortir pour un bon repas ou à s'offrir une petite gâterie. La gestion de l'anxiété
 n'est pas toujours facile ou amusante, et vous méritez une récompense pour vos efforts !

"""

# pour l'IA

phrases = []



app = QApplication(sys.argv)


class Identification:
    def __init__(self):

        self.window = QWidget()
        self.window.setWindowTitle("TCC Friend: Inscription")
        self.window.setFixedWidth(500)
        self.window.setStyleSheet(WindowBackground)
        self.grid = QGridLayout()
        self.window.setLayout(self.grid)



        #titre :
        self.label = QLabel("Identification")
        self.label.setStyleSheet(StyleTitre)
        self.grid.addWidget(self.label,0,0,1,2)

        #Qlabel de l'email
        self.label2 = QLabel("Email:")
        self.label2.setStyleSheet(StyleText)
        self.grid.addWidget(self.label2,2,0,1,2)

        #QLineEdit de la saisie du mail
        self.SaisieMail = QLineEdit()
        self.SaisieMail.setStyleSheet(StyleHover)
        self.SaisieMail.resize(150, 40)
        self.grid.addWidget(self.SaisieMail ,3,0,1,2)

        #Qlabel du password:
        self.label3 = QLabel("Password:")
        self.label3.setStyleSheet(StyleText)
        self.grid.addWidget(self.label3,4,0,1,2)

        #QLineEdit de la saisie du password
        self.SaisiePasswd = QLineEdit()
        self.SaisiePasswd.setStyleSheet(StyleHover)
        self.SaisiePasswd.resize(150, 40)
        self.grid.addWidget(self.SaisiePasswd ,5,0,1,2)

        #Boutton de Login:
        self.BouttonIdentification = QPushButton("Envoi")
        self.BouttonIdentification.setStyleSheet(StyleHover)
        self.grid.addWidget(self.BouttonIdentification ,6,0,1,2)
        self.BouttonIdentification.clicked.connect(lambda x:self.LogIn())

        #Boutton d'enregistrement:
        self.BouttonEnregistrement= QPushButton("Enregistrement")
        self.BouttonEnregistrement.setStyleSheet(StyleHover)
        self.grid.addWidget(self.BouttonEnregistrement ,8,0,1,2)
        self.BouttonEnregistrement.clicked.connect(lambda x:self.Enregistrement())



        self.window.show()
        app.exec()

    def Enregistrement(self):
        enregistrement= Enregistrement()
    def LogIn(self):
        self.Email = self.SaisieMail.text()
        self.psswrd = self.SaisiePasswd.text()
        global password
        password = self.SaisiePasswd.text()
        user = auth.sign_in_with_email_and_password(password=self.psswrd, email=self.Email)
        print("***********************************************")
        print('Utilisateur logé avec succes ')
        print("***********************************************")
        print('Info de l\'utilisateur:')
        print(auth.current_user)
        print("***********************************************")
        print(auth)
        global gestion
        gestion= Gestion()


class Class_bouttons:
    #cette classe permet de mémoriser et de conserver une valeur de "numbutton" fixe pour chaque boutton.
    def __init__(self,nom_classe_hebergeuse,NomBoutton,numbutton):
        self.NomBoutton=NomBoutton
        self.numGraph=numbutton
        print("***********************************************")
        print("Creation  d'un boutton de la classe bouttons au rang :" + str(self.numGraph))
        print("***********************************************")
        #Création du boutton:
        self.BouttonGraphique = QPushButton(self.NomBoutton)
        self.BouttonGraphique.setStyleSheet(StyleHover)
        #Celui-ci est rattaché à la grille de la fenêtre gestion, au rang numgraph:
        gestion.grid.addWidget(self.BouttonGraphique ,self.numGraph,0,1,2)#le numero de ligne dans la grille est
                                                                                        #numGraph

        self.numGraph=self.numGraph - 4#ici on enleve le numero de ligne du boutton pour avoir les index dans la BDD
        #numGraph correspond désormais à un index dans la BDD.



        self.BouttonGraphique.clicked.connect(lambda x:instance_PrintGraphClass(self.numGraph))

class BouttonNouveauGraph:
    def __init__(self,hauteur):
        self.HauteurBoutton = hauteur
        print("***********************************************")
        print("Creation du boutton pour le nouveau graph:")
        print("***********************************************")
        print("La valeur de HauteurBoutton est :"+ str(self.HauteurBoutton))
        #Boutton pour le nouveau graph:
        #PrintGraphClass est lancée avec le code 99 pour lancer un graph vide.


        self.BouttonNouveauGraph = QPushButton("Nouveau Graph")
        self.BouttonNouveauGraph.setStyleSheet(StyleHover)
        gestion.grid.addWidget(self.BouttonNouveauGraph, self.HauteurBoutton, 0, 1, 2)

        self.BouttonNouveauGraph.clicked.connect(lambda x: instance_PrintGraphClass(None))
class Gestion:
    def __init__(self):
        #Fenêtre et paramètres:
        self.gestion = QWidget()
        self.gestion.setFixedWidth(500)
        self.gestion.setStyleSheet(WindowBackground)
        self.grid = QGridLayout()
        self.gestion.setLayout(self.grid)

        #Boutton "SignOut":
        self.BouttonSignOut = QPushButton("SignOut")
        self.BouttonSignOut.setStyleSheet(StyleHover)
        self.grid.addWidget(self.BouttonSignOut ,1,0,1,2)
        self.BouttonSignOut.clicked.connect(lambda x:self.SignOut())

        #Boutton "Info TCC":
        self.BouttonInfoTCC = QPushButton("Infos sur la TCC")
        self.BouttonInfoTCC.setStyleSheet(StyleHover)
        self.grid.addWidget(self.BouttonInfoTCC ,2,0,1,2)
        self.BouttonInfoTCC.clicked.connect(lambda x:self.Infos())


        #Boutton "Commencer":
        self.BouttonCommencer = QPushButton("Commencer")
        self.BouttonCommencer.setStyleSheet(StyleHover)
        self.grid.addWidget(self.BouttonCommencer, 3, 0, 1, 2)
        self.BouttonCommencer.clicked.connect(lambda x:self.Commencer())


        self.gestion.show()




    def SignOut(self):



        auth.current_user= None
        print("***********************************************")
        print("L'utilisateur a quitté avec succès.")
        print("***********************************************")
        self.gestion.close()
        sys.exit()




    def Commencer(self):
        #self.gestion.close()
        #del gestion
        #gestion= Gestion()
        self.HauteurBoutton = 4
        #Get sur la base de données au niveau de l'utilisateur:
        global results
        results = db.child("users").child(auth.current_user['localId']).get()
        if results.val() != None:
            print("***********************************************")
            print("Retour de FireBase dans la variable results:")
            print("***********************************************")
            print("Le type de la variable results est :" + str((type(results))))
            print("***********************************************")
            print("la valeur de results.val() est " + str(type(results.val())))
            print("Le dir de la classe est:" + str(dir(results)))
            # copie de cette variable results sous forme de liste dans la variable glogale copie_results:
            global copie_results
            copie_results = results.val().copy()
            print("La variable copie_results contient : "+ str(copie_results))
            #Boucle for sur le retour de la Base de données:
            for result in results.each():
                liste_valeurs = result.val()
                print("***********************************************")
                print("Analyse du retour du graph :" + liste_valeurs[0] )
                print("***********************************************")

                print("La clé est :" + str(result.key()) + "La valeur est :" + str(result.val()))
                print("***********************************************")
                print("La valeur de self.HauteurBoutton est :" + str(self.HauteurBoutton))
                print("***********************************************")

                #Un boutton est créé pour chaque graph avec la classe Class_bouttons qui gardera en mémoire
                #des données précises.
                Class_bouttons(self, liste_valeurs[0], self.HauteurBoutton)
                self.HauteurBoutton = self.HauteurBoutton + 1
            #Le boutton pour un nouveau graph est rajouté à la fin:
            self.Boutton_nouveauG =BouttonNouveauGraph(self.HauteurBoutton)
        else:
            #sinon copie_results est une liste vide:
            copie_results =[]
            self.Boutton_nouveauG =BouttonNouveauGraph(self.HauteurBoutton)

    def Infos(self):
        instance_cours = Cours_TCC()

class Cours_TCC:
    def __init__(self):
        #fenêtre et paramètres:
        self.CoursWindow = QWidget()  # creation d'une fenêtre
        self.CoursWindow.setFixedWidth(1000)
        self.CoursWindow.setStyleSheet(WindowBackground)
        self.CoursWindow.setFixedHeight(1000)
        self.grid = QGridLayout()
        self.CoursWindow.setLayout(self.grid)

        #Récupération du fichier texte "cours_TCC.txt" dans le fichier py
        self.TextCours= CoursTCC

        #Qlabel du texte:
        self.LabelText = QLabel(self.TextCours)
        self.LabelText.setStyleSheet(StyleScrollGraph)

        #Fabrication du scroll:
        self.scroll = QScrollArea()
        #Widget qui va contenir le "layout" de boite
        self.widget = QWidget()
        #Layout de boite verticale :
        self.vbox = QVBoxLayout()
        #Ajout du texte dans le Layout de la boite:
        self.vbox.addWidget(self.LabelText)
        #Ajout du layout de vbox au Widget créé plus haut
        self.widget.setLayout(self.vbox)
        #Paramètres du scroll vertical:
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        #Paramètres du scroll Horizontal:
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        #"Linkage" du scroll au widget
        self.scroll.setWidget(self.widget)
        #Ajout du scroll à la grille de la fenêtre principale:
        self.grid.addWidget(self.scroll,4,0,1,2)


        self.CoursWindow.show()
class Enregistrement:
    def __init__(self):
        # Fenêtre et paramètres de fenêtre:
        self.enregitrement = QWidget()
        self.enregitrement.setWindowTitle("TCC Friend: Enregitrement")
        self.enregitrement.setFixedWidth(500)
        self.enregitrement.setStyleSheet(WindowBackground)
        self.grid = QGridLayout()
        self.enregitrement.setLayout(self.grid)

        # Qlabel "Enregristrement"
        self.label = QLabel("Enregistrement")
        self.label.setStyleSheet(StyleTitre)
        self.grid.addWidget(self.label, 0, 0, 1, 2)
        # Qlabel "Email"
        self.label2 = QLabel("Email:")
        self.label2.setStyleSheet(StyleText)
        self.grid.addWidget(self.label2, 2, 0, 1, 2)
        # QlineEdit de saisie de mail
        self.SaisieMail = QLineEdit()
        self.SaisieMail.setStyleSheet(StyleHover)
        self.SaisieMail.resize(150, 40)
        self.grid.addWidget(self.SaisieMail, 3, 0, 1, 2)
        # Qlabel "Password"
        self.label3 = QLabel("Password:")
        self.label3.setStyleSheet(StyleText)
        self.grid.addWidget(self.label3, 4, 0, 1, 2)
        # QlineEdit de saisie de password
        self.SaisiePasswd = QLineEdit()
        self.SaisiePasswd.setStyleSheet(StyleHover)
        self.SaisiePasswd.resize(150, 40)
        self.grid.addWidget(self.SaisiePasswd, 5, 0, 1, 2)
        # Boutton d'enregistrement
        self.BouttonEnregistrement = QPushButton("Envoi")
        self.BouttonEnregistrement.setStyleSheet(StyleHover)
        self.grid.addWidget(self.BouttonEnregistrement, 6, 0, 1, 2)
        self.BouttonEnregistrement.clicked.connect(lambda x: self.SignIn())
        # Affichage fenêtre:
        self.enregitrement.show()

    def SignIn(self):
        self.Email = self.SaisieMail.text()
        self.psswrd = self.SaisiePasswd.text()
        global password
        password = self.SaisiePasswd.text()
        user = auth.create_user_with_email_and_password(password=self.psswrd,
                                                                                        email=self.Email)
        user = auth.sign_in_with_email_and_password(password=self.psswrd,
                                                                                    email=self.Email)
        # db.child("users").set(auth.current_user['localId'])
        print("***********************************************")
        print('Utilisateur enregistré avec succes ')
        print("***********************************************")
        print('Info de l\'utilisateur:')
        print(auth.current_user)
        print("***********************************************")
        print(auth)
        # Lancement de la fenêtre Gestion (classe Gestion du fichier gestion.py)
        global gestion
        gestion = Gestion()




import time


def instance_PrintGraphClass(key):
    global InstancePrintGraphClass
    if InstancePrintGraphClass != [1]:
        InstancePrintGraphClass.fen_graph.close()
        del InstancePrintGraphClass
    InstancePrintGraphClass =PrintGraphClass(key)


class PrintGraphClass:
    def __init__(self, key):
        if key != None:
            self.key = key
        print("***********************************************")
        print("On a appuyé sur un boutton ..")
        print("PrintgraphClass est lancée, l'argument est " + str(key))
        print("***********************************************")

        # la variable key 99 est la clé renvoyée pour un nouveau graph. Si la liste des graphs est vide le numero du graph dans la BDD sera 0:
        if key == None and results.val() is None:
            self.numero_graph = 0
            self.FenetreNouveauGraph()
        # sinon si la BDD contient déjà des valeurs le numero du graph dans la BDD sera len(results.val()), (le (nouveau)  dernier element de la BDD):
        elif key == None:
            self.numero_graph = len(results.val())
            self.FenetreNouveauGraph()
        # sinon on récupère la liste de points correspondant au graph demandé:
        else:
            print("Le numero du graph est :" + str(key))
            print("copie_results vaut:" + str(copie_results))
            self.numero_graph = key
            #La variable liste_points contient tous les points du graph
            self.liste_points =copie_results[self.numero_graph]
            print("La liste des points du nouveau graph est bien:")
            print(self.liste_points )
            self.PrintGraph()  # lancement de PrintGraph
    def FenetreNouveauGraph(self):
        #Qwidget ,Layout en grille et nom de la fenêtre:
        self.fen_graph = QWidget()
        self.fen_graph.setStyleSheet(WindowBackground)
        self.grid = QGridLayout()
        self.fen_graph.setLayout(self.grid)
        self.fen_graph.setWindowTitle("Nouveau Graph")

        #Qlabel du titre du nouveau graph:
        self.label_titre_nouveau_graph = QLabel("Nom du Nouveau Graph:")
        self.label_titre_nouveau_graph.setStyleSheet(StyleText)
        self.grid.addWidget(self.label_titre_nouveau_graph,1,0,1,2)

        #QLineEdit du nom ud nouveau graph
        self.titre_nouveau_g_ins = QLineEdit()
        self.titre_nouveau_g_ins.setStyleSheet(StyleHover)
        self.titre_nouveau_g_ins.resize(150, 40)
        self.grid.addWidget(self.titre_nouveau_g_ins ,2,0,1,2)

        #Boutton de lancement du nouveau graph:
        self.Boutton_nouveau_titre =  QPushButton("Envoi")
        self.Boutton_nouveau_titre.setStyleSheet(StyleHover)
        self.grid.addWidget(self.Boutton_nouveau_titre,3,0,1,2)
        self.Boutton_nouveau_titre.clicked.connect(lambda x:self.GestionNouveauTitre())
        self.fen_graph.show()

    def GestionNouveauTitre(self):
        #Creation d'un nouveau graph: liste_points est une liste vide
        self.liste_points=[]
        #On lui ajoute le titre:
        self.liste_points.append(self.titre_nouveau_g_ins.text())
        self.PrintGraph()

    def PrintGraph(self):
        #Fenêtre Layout et style:
        self.fen_graph=  QWidget()
        self.fen_graph.resize(900,800)
        self.fen_graph.setWindowTitle(self.liste_points[0])
        self.grid = QGridLayout()
        self.fen_graph.setLayout(self.grid)
        self.fen_graph.setStyleSheet(WindowBackground)

        #Qlabel du titre : self.liste_point[0] contient le titre du graph
        self.label3 = QLabel(self.liste_points[0])
        self.label3.setStyleSheet(StyleTitre)
        self.grid.addWidget(self.label3,0,0,1,1)

        #QLabel du graphique:
        self.titre = QLabel("Cliquez Graph Switch pour commencer")
        self.titre.setStyleSheet(StyleText)
        self.grid.addWidget(self.titre, 2, 0, 1, 1)

        #Boutton du Nouveau point du graph:
        self.BouttonNouveauPoint = QPushButton("Nouveau Point")
        self.BouttonNouveauPoint.setStyleSheet(StyleHover)
        self.grid.addWidget(self.BouttonNouveauPoint, 2, 1, 1, 1)
        self.BouttonNouveauPoint.clicked.connect(lambda x:CreationListeInsertion({} ,0,self.numero_graph))

        #Boutton de "switch" du graph
        self.BouttonGraph2 = QPushButton("Graph Switch")
        self.BouttonGraph2.setStyleSheet(StyleHover)
        self.grid.addWidget(self.BouttonGraph2 ,3,0,1,1)
        # creation d'une liste circulaire:
        self.liste_des_clicks = [0,1,2]
        self.cicle= cycle(self.liste_des_clicks)
        #La fonction va lancer la fonction de dessin du graph avec une variable circulaire next(self.cicle))
        #qui pourra prendre comme argument 0 , 1 ou 2 :
        self.BouttonGraph2.clicked.connect(lambda x:self.plot(next(self.cicle)))

        #Preparation du graphique:
        self.fig, self.ax = plt.subplots()

        #Cadre pour le graphique:
        self.canvas = FigureCanvas(self.fig)
        self.grid.addWidget(self.canvas,1,0,1,1)



        #Variables qui vont recevoir les chaines d'émotions négatives et émotions résultats:
        self.les_x=0
        #Axe des x du graphique:
        self.xaxis=[]
        #Emotions négatives
        self.yaxis=[]
        #Emotions résultats:
        self.emotions_resultats = []
        #Création d'un scroll pour recevoir la liste des bouttons construits a partir de chaque exposition:
        self.scroll = QScrollArea()
        #Widget receptacle
        self.widget = QWidget()
        self.widget.resize(900,900)
        #Layout à l'interieur du widget:
        self.vbox = QVBoxLayout()
        #Paramètres du scroll:
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        self.grid.addWidget(self.scroll, 1, 1, 1, 1)
        self.widget.setLayout(self.vbox)


        if self.liste_points[1:]: # on enlève le titre (index 0), donc si liste_points contient des points:
            for points in self.liste_points[1:]:
                BouttonDePoint(self,self.les_x,points)

                self.xaxis.append(self.les_x)
                print("------------------------------------------------------------------------")
                print("On rajoute le point emotion négative :"+ str(points['emotion']) )
                #Ajout de l'element emotions négative à la liste correspondante:
                self.yaxis.append(int(points['emotion']))
                print("On rajoute le point emotion résultat :" + str(points['emotion_resultat']))
                #Ajout de l'element emotions résultat à la liste correspondante:
                self.emotions_resultats.append(int(points['emotion_resultat']))
                print(self.yaxis,self.xaxis)
                self.les_x += 1
        #Si la liste est vide, plot avec l'argument 0:
        else:
            self.plot(0)

        #lancement du module d'IA:
        self.IATCC()

        self.fen_graph.show()



    def IATCC(self):

        if len(self.xaxis) < 3 :
            #Qlabel d'IA:
            self.LabelIA = QLabel("Pas assez de données de graph pour lancer une IA")
            self.LabelIA.setStyleSheet(StyleText)
            self.grid.addWidget(self.LabelIA, 4, 0, 1, 2)
        else :
            #try:
            #lancement du module d'IA
            print("***********************************************")
            print(print("La chaine d'emotions negatives envoyée au module d'IA est " + str(self.yaxis)))
            print("***********************************************")
            self.IA = IATCC( self.yaxis,self.emotions_resultats)
            self.IA.lancement()
            self.TextIA =""
            #La variable phrases contient les phrases à afficher après analyse.
            for i in phrases:
                self.TextIA += i + "\n"
            #Qlabel d'IA:
            self.LabelIA = QLabel(self.TextIA)
            self.LabelIA.setStyleSheet(StyleScrollGraph)
            self.grid.addWidget(self.LabelIA, 4, 0, 1, 2)







    def plot(self,param): # dessin du graph en fonction du paramètre circulaire de valeur 0 ,1 ou 2:
        print("***********************************************")
        print("Plot du graph ..")
        print("xaxis vaut:"+str(self.xaxis))
        print("yaxis vaut:" +str(self.yaxis))
        print("***********************************************")
        if param ==0:
            #Qlabel du titre:
            self.titre = QLabel(" Graph émotions resultats")
            self.titre.setStyleSheet(StyleText)
            self.grid.addWidget(self.titre, 2,0, 1, 1)
            #Netoyage du graph:
            self.ax.clear()
            #Dessin du graph:
            self.ax.plot(self.xaxis, self.emotions_resultats)

        if param ==1:
            #Qlabel du titre:
            self.titre = QLabel(" Graph émotions négative")
            self.titre.setStyleSheet(StyleText)
            self.grid.addWidget(self.titre, 2,0, 1, 1)
            #Netoyage du graph:
            self.ax.clear()
            #Dessin du graph:
            self.ax.plot(self.xaxis, self.yaxis)

        if param == 2:
            #Qlabel du titre:
            self.titre = QLabel(" Graph émotions négative et émotions résultats")
            self.titre.setStyleSheet(StyleText)
            self.grid.addWidget(self.titre, 2,0, 1, 1)
            #Netoyage du graph:
            self.ax.clear()
            #Dessin du graph (les deux courbes):
            self.ax.plot(self.xaxis, self.emotions_resultats)
            self.ax.plot(self.xaxis, self.yaxis)

        self.canvas.draw()



class BouttonDePoint:
    def __init__(self,InstancePrintGraphClass,NumeroBoutton,points):
        self.NumeroPoint= NumeroBoutton +1
        self.point=points
        self.InstancePrintGraphClass = InstancePrintGraphClass
        self.numeroGraph = self.InstancePrintGraphClass.numero_graph

        #Fabrication du boutton
        self.BouttonListePoints= QPushButton(
        "Situation " + str(self.NumeroPoint) + " :" +
        str(decrypt(str.encode(self.point["situation"]),password,salt)) + "\n" +
        "Emotion :" + str(self.point["emotion"]) + "\n" +

        "Pensées automatiques :" + str(decrypt(str.encode(self.point["pensées_auto"]),password,salt)) + "\n" +
        "Confirmation des pensées automatiques :" + str(decrypt(str.encode(self.point["confirmation"]),password,salt)) + "\n"
        + "Preuves contraires :" +
        str(decrypt(str.encode(self.point["preuves_contraires"]),password,salt)) + "\n" +
        "Pensées adaptées :" + str(decrypt(str.encode(self.point["pensée_adaptée"]),password,salt)) + "\n" +
        "Emotion resultat :" + str(self.point["emotion_resultat"]) + "\n")
        self.BouttonListePoints.setStyleSheet(StyleScrollGraphHover)

        #Insertion du point dans la vbox de l'objet InstancePrintGraphClass:
        self.InstancePrintGraphClass.vbox.addWidget(self.BouttonListePoints)
        #Le point lancera la fonction ListeInsertion avec en paramètre le dictionnaire du point et le numero de sa place
        #Dans le graph:
        self.BouttonListePoints.clicked.connect(lambda x:CreationListeInsertion(self.point,self.NumeroPoint,self.numeroGraph))


class ListeInsertion1:
    def __init__(self, point ,NumeroPoint, numeroGraph):
        #self.point contient le dictionnaire du point:
        self.point=point
        #self.NumeroPoint contient l'index du point dans la liste du graph:
        self.NumeroPoint = NumeroPoint
        self.numeroGraph = numeroGraph
        #Paramètres de fenêtre:
        self.fen_insertion=  QWidget()
        self.fen_insertion.setStyleSheet(WindowBackground)
        self.fen_insertion.resize(900,800)
        #Si le point vaut 0 alors il s'agit de l'ajout d'un nouveau point:
        if self.NumeroPoint == 0:
            #Titre de fenêtre et Qlabel de titre correspondants:
            self.fen_insertion.setWindowTitle("Nouveau Point pour: " +InstancePrintGraphClass.liste_points[0])
            self.label_titre_point = QLabel("Nouveau Point pour: " + InstancePrintGraphClass.liste_points[0])

        else : #Sinon il s'agit de la réécriture d'un point précis dans la liste:
            #Titre de fenêtre et Qlabel de titre correspondants:
            self.fen_insertion.setWindowTitle("Correction du point " + str(self.NumeroPoint)+" pour " + InstancePrintGraphClass.liste_points[0])
            self.label_titre_point = QLabel("Correction du point " + str(self.NumeroPoint)+" pour " + InstancePrintGraphClass.liste_points[0])
        #Style des deux Qlabels du dessus.
        self.label_titre_point.setStyleSheet(StyleTitre)
        self.grid_insertion = QGridLayout()
        self.grid_insertion.addWidget(self.label_titre_point, 4, 0, 1, 1)

        self.grid_insertion1 = QGridLayout()
        #scroll de la fenêtre:
        self.scroll2 = QScrollArea()
        #Qwidget qui va être encadré par le scroll
        self.widget_insertion = QWidget()
        self.widget_insertion.resize(900, 900)

        #Layout de vbox:
        self.vboxlayout =  QVBoxLayout()
        #Layout de grille contenu dans le layout de vbox:
        self.vboxlayout.addLayout(self.grid_insertion)

        #Paramètres du scroll:
        self.scroll2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll2.setWidgetResizable(True)
        #Ajout du scroll2 au widget_insertion
        self.scroll2.setWidget(self.widget_insertion)
        #Linkage du scroll à grid_insertion1
        self.grid_insertion1.addWidget(self.scroll2, 1, 1, 1, 1)
        #insertion de widget_insertion dans le layout de vboxlayout
        self.widget_insertion.setLayout(self.vboxlayout)
        #insertion de la fenêtre globale dans le layout de la grille grid_insertion1
        self.fen_insertion.setLayout(self.grid_insertion1)


        #Ensemble des Qlabels et des QlineEdit pour ajouter le point:
        self.situation = QLabel("Situation:")
        self.situation.setStyleSheet(StyleScrollGraph)
        self.grid_insertion.addWidget(self.situation,5,0,1,1)

        self.situation_ins = QLineEdit()
        self.situation_ins.setStyleSheet(StyleScrollGraphHover)
        self.situation_ins.resize(150, 40)
        self.grid_insertion.addWidget(self.situation_ins ,6,0,1,1)

        self.emo_label = QLabel("Emotion (chiffre entre 0 et 10):")
        self.emo_label.setStyleSheet(StyleScrollGraph)
        self.grid_insertion.addWidget(self.emo_label,7,0,1,1)

        self.emo_ins = QLineEdit()
        self.emo_ins.setStyleSheet(StyleScrollGraphHover)
        self.emo_ins.resize(150, 40)
        self.grid_insertion.addWidget(self.emo_ins ,8,0,1,1)

        self.pensee_auto = QLabel("Pensées automatiques:")
        self.pensee_auto.setStyleSheet(StyleScrollGraph)
        self.grid_insertion.addWidget(self.pensee_auto,9,0,1,1)

        self.pensee_auto_ins = QLineEdit()
        self.pensee_auto_ins.setStyleSheet(StyleScrollGraphHover)
        self.pensee_auto_ins.resize(150, 40)
        self.grid_insertion.addWidget(self.pensee_auto_ins ,10,0,1,1)

        self.conf_label = QLabel("Confirmation:")
        self.conf_label.setStyleSheet(StyleScrollGraph)
        self.grid_insertion.addWidget(self.conf_label,11,0,1,1)

        self.conf_label_ins = QLineEdit()
        self.conf_label_ins.setStyleSheet(StyleScrollGraphHover)
        self.conf_label_ins.resize(150, 40)
        self.grid_insertion.addWidget(self.conf_label_ins ,12,0,1,1)

        self.preuves_contr = QLabel("Preuves contraires:")
        self.preuves_contr.setStyleSheet(StyleScrollGraph)
        self.grid_insertion.addWidget(self.preuves_contr,13,0,1,1)

        self.preuves_contr_ins = QLineEdit()
        self.preuves_contr_ins.setStyleSheet(StyleScrollGraphHover)
        self.preuves_contr_ins.resize(150, 40)
        self.grid_insertion.addWidget(self.preuves_contr_ins ,14,0,1,1)

        self.pensee_adap = QLabel("Pensées adaptées:")
        self.pensee_adap.setStyleSheet(StyleScrollGraph)
        self.grid_insertion.addWidget(self.pensee_adap,15,0,1,1)

        self.pensee_adap_ins = QLineEdit()
        self.pensee_adap_ins.setStyleSheet(StyleScrollGraphHover)
        self.pensee_adap_ins.resize(150, 40)
        self.grid_insertion.addWidget(self.pensee_adap_ins ,16,0,1,1)

        self.emo_result = QLabel("Emotions résultats (chiffre entre 0 et 10):")
        self.emo_result.setStyleSheet(StyleScrollGraph)
        self.grid_insertion.addWidget(self.emo_result,17,0,1,1)

        self.emo_result_ins = QLineEdit()
        self.emo_result_ins.setStyleSheet(StyleScrollGraphHover)
        self.emo_result_ins.resize(150, 40)
        self.grid_insertion.addWidget(self.emo_result_ins ,18,0,1,1)

        if point != {}:
            #Si il s'agit de la correction d'un point, récupération des données du dictionnaire du point
            #Et inscriptions de celles-ci dans chaque case:
            self.situation_ins.setText( decrypt(self.point["situation"],password,salt))
            self.emo_ins.setText(str(self.point["emotion"]))
            self.pensee_auto_ins.setText(decrypt(self.point["pensées_auto"],password,salt))
            self.conf_label_ins.setText(decrypt(self.point["confirmation"],password,salt))
            self.preuves_contr_ins.setText(decrypt(self.point["preuves_contraires"],password,salt))
            self.pensee_adap_ins.setText(decrypt(self.point["pensée_adaptée"],password,salt))
            self.emo_result_ins.setText(str(self.point["emotion_resultat"]))

        #Boutton d'envoi des attributs:
        self.BouttonRetourAttribut= QPushButton("Envoi")
        self.BouttonRetourAttribut.setStyleSheet(StyleHover)
        self.grid_insertion.addWidget(self.BouttonRetourAttribut ,19,0,1,2)
        self.BouttonRetourAttribut.clicked.connect(lambda x:self.RetourAttributs(self.NumeroPoint,self.numeroGraph))

        self.fen_insertion.show()

    def RetourAttributs(self,NumeroPoint,numeroGraph):
        #Récupération de tous les attributs dans des variables:
        self.situation = self.situation_ins.text()
        if self.situation == "":
            self.situation = "vide"

        self.emotion= self.emo_ins.text()
        if self.emotion == "":
            self.emotion = 0
        else :
            self.emotion = int(self.emotion)

        self.pensee_auto =self.pensee_auto_ins.text()
        if self.pensee_auto == "":
            self.pensee_auto = "vide"

        self.confirmation = self.conf_label_ins.text()
        if self.confirmation == "":
            self.confirmation = "vide"

        self.preuves_contraires = self.preuves_contr_ins.text()
        if self.preuves_contraires == "":
            self.preuves_contraires = "vide"

        self.pensee_adaptee = self.pensee_adap_ins.text()
        if self.pensee_adaptee == "":
            self.pensee_adaptee = "vide"

        self.emotion_resultat= int(self.emo_result_ins.text())
        if self.emotion_resultat== "":
            self.emotion_resultat = 0
        else :
            self.emotion_resultat = int(self.emotion_resultat)

        #On les mets dans un point:
        self.nouveau_point= { 'situation': encrypt(self.situation,password).decode("utf-8"),'emotion': self.emotion, 'pensées_auto':encrypt(self.pensee_auto,password).decode("utf-8"),'confirmation':encrypt(self.confirmation,password).decode("utf-8"),'preuves_contraires':encrypt(self.preuves_contraires,password).decode("utf-8"),'pensée_adaptée':encrypt(self.pensee_adaptee,password).decode("utf-8"),'emotion_resultat':self.emotion_resultat}

        if NumeroPoint == 0 :
            #On rajoute le point a la liste de points:
            InstancePrintGraphClass.liste_points.append(self.nouveau_point)
        else :
            #Sinon on le remplace à l'index voulu:
            InstancePrintGraphClass.liste_points[NumeroPoint] = { 'situation': encrypt(self.situation,password).decode("utf-8"),'emotion': self.emotion, 'pensées_auto': encrypt(self.pensee_auto,password).decode("utf-8"),'confirmation':encrypt(self.confirmation,password).decode("utf-8"),'preuves_contraires':encrypt(self.preuves_contraires,password).decode("utf-8"),'pensée_adaptée':encrypt(self.pensee_adaptee,password).decode("utf-8"),'emotion_resultat':self.emotion_resultat}

        #On remplace le graph de la BDD par la nouvelle série  de points avec un set sur FireBase:
        print("*******************************************************")
        print("Set FireBase la liste de point du graph suivant:")
        ########moment crucial: copie sur la Base de données FireBase avec un set:
        db.child("users").child(auth.current_user['localId']).child(InstancePrintGraphClass.numero_graph).set(InstancePrintGraphClass.liste_points)
        #Traitement particulier du cas ou il s'agit du tout premier graphique:
        if numeroGraph ==0 :
            print("*******************************************************")
            print("Ajout du nouveau point à la variable self.nouveau_graph:")
            print("Ajout du titre suivant :" + str(InstancePrintGraphClass.liste_points[0]) )
            print("Ajout du point suivant :" + str(self.nouveau_point) )

            self.nouveau_graph= []
            self.nouveau_graph.append(InstancePrintGraphClass.liste_points[0])
            self.nouveau_graph.append(self.nouveau_point)
            copie_results.append(self.nouveau_graph)
            #Ici je relance "Commencer" dans gestion pour avoir une mise à jour des bouttons dans la fenêtre gestion
            gestion.Commencer()

        #Sinon pour la modification du point ou la creation du point d'un graph déjà existant:
        else :
            print("La variable copie_results a été transformée au rang :" + str(numeroGraph))
            print("Par le graph :" + str(InstancePrintGraphClass.liste_points))
            if len(copie_results) != numeroGraph -1:
                copie_results.append([])
                if NumeroPoint == 0:
                    # Ici je relance "Commencer" dans gestion pour avoir une mise à jour des bouttons dans la fenêtre gestion
                    gestion.Commencer()

            #copie de la liste de point augmentée du nouveau point dans la variable globale copie_results:
            copie_results[numeroGraph] = InstancePrintGraphClass.liste_points


        self.fen_insertion.close()
        InstancePrintGraphClass.fen_graph.close()

        instance_PrintGraphClass(InstancePrintGraphClass.numero_graph)


class IATCC:
    def __init__(self,chaine_negative,chaine_positive):
        global phrases
        phrases= []
        print("Creation de l'instance de IATCC")
        self.chaine_n= chaine_negative[-3:]
        self.chaine_p = chaine_positive[-3:]
        print("Chaine émotions négatives de départ:\n "+ str(self.chaine_n))
        print("Chaine émotions résultats de départ:\n "+ str(self.chaine_p))
    def parcours_ligne(self,liste_emotions, chainage_conditions):

        if not chainage_conditions:
            return
        else:
            case_contenu = chainage_conditions[0]  # preparation du contenu d'une case
            case_contenu = case_contenu.split("-")  # on "slice" avec les "-"

        if len(liste_emotions) != 0 and isinstance(liste_emotions[0],
                                                   int):  # recursion ici si la liste d'émotions contient des chiffres

            if case_contenu[0] == "sup" and liste_emotions[0] > int(case_contenu[1]):
                print("t")
                return self.parcours_ligne(liste_emotions[1:], chainage_conditions[1:])

            if case_contenu[0] == "inf" and liste_emotions[0] < int(case_contenu[1]):
                print("t")
                return self.parcours_ligne(liste_emotions[1:], chainage_conditions[1:])

            if case_contenu[0] == "bt" and int(case_contenu[1]) < liste_emotions[0] < int(case_contenu[2]):
                print("t")
                return self.parcours_ligne(liste_emotions[1:], chainage_conditions[1:])

            if case_contenu[0] == "null":
                print("t")
                self.parcours_ligne(liste_emotions[1:], chainage_conditions[1:])


        elif case_contenu[

            0] == "ph":  # sinon, lecture de phrase ici et recursion sur liste vide à la fin de la condition
            print("Chaine émotions résultats de départ:\n " + str(self.chaine_p))
            print("IA: phrase atteinte.")
            global phrases
            print(case_contenu[1])
            # impression à racorder
            for i in phrases:
                #Si la phrase a déjà été lue, on ne fait rien:
                if i == case_contenu[1]:
                    #Ici on enlève le préfixe de la liste des émotions "positives"
                    self.chaine_p.pop(0)
                    #Et on continue la récursion pour mettre un autre préfixe
                    self.parcours_ligne([], chainage_conditions[1:])

            #Sinon on l'ajoute:
            phrases += [case_contenu[1]]

            self.parcours_ligne([], chainage_conditions[1:])

        elif case_contenu[0] == "add":  # sinon, lecture de add ici et recursion sur liste vide à la fin de la condition
            print("add")
            print("la case est:")
            print(chainage_conditions[0])
            ajout = case_contenu[1]
            self.chaine_p.insert(0, ajout)  # ajout d'un élément sur la chaine d'emotions positives
            self.parcours_ligne([], chainage_conditions[1:])

        elif isinstance(liste_emotions[0], str):  # cas du chainage sur la chaine positive
            print("IA :conditions chainage remplies")
            # print("liste contenu[0]= " + case_contenu[0])
            if liste_emotions[0] != case_contenu[0]:
                print("Chainage negatif")
            if liste_emotions[0] == case_contenu[0]:
                print("Chainage positif")
                self.parcours_ligne(liste_emotions[1:], chainage_conditions[1:])
    def lancement(self):

        print("Le fichier est " + "reglesn.py")
        self.lecture_fichier("reglesn.py")

        print("Le fichier est " + "reglesp.py")
        self.lecture_fichier("reglesp.py")


    def lecture_fichier(self,nom_fichier):
        if nom_fichier == "reglesn.py":
            print("Travail sur la chaine émotions négatives : " + str(self.chaine_n))
            liste_emotions_copy = self.chaine_n.copy()
            f="""bt-1-5|bt-1-5|bt-1-5|ph-Vous êtes sur un palier, continuez l'entrainement, L'émotion va baisser|add-cogn1.
sup-4|bt-1-5|bt-1-5|ph-L'émotion négative a baissé il y a peu,vous êtes sur la bonne voie.|add-cogn2.
inf-2|bt-1-5|bt-1-5|ph-Il semble qu'il y ait une inégalité dans vos choix d'expositions, Essayez de rester sur des situations similaires|add-cogn1.
inf-3|sup-4|bt-1-5|ph-Il semble qu'il y ait une inégalité dans vos choix d'expositions, Essayez de rester sur des situations similaires|add-cogn2.
sup-5|sup-4|bt-1-5|ph-L'émotion négative a baissé il y a peu,persistez jusqu'à la faire baisser à 2.
null|null|sup-5|ph-L'émotion negative est peut être trop forte,Il est conseillé de commencer autour de 4.
null|inf-5|bt-4-6|ph-Lémotion négative a remonté, peut être que la situation n'était pas adaptée.
null|sup-4|bt-4-6|ph-Lémotion négative est peut être trop forte, choisissez plutôt une situation moins difficile.
inf-3|inf-3|inf-3|ph-Vous pouvez confirmer l'entraînement,mais vous avez quasiment resolu le problème.
sup-2|inf-3|inf-3|ph-Vous pouvez confirmer l'entraînement, vous êtes sur la bonne voie.
null|sup-2|inf-3|ph-Excellent!Vous arrivez bientôt à bout de cette situation, continuez!.
"""

        elif nom_fichier == "reglesp.py":
            print("Travail sur la chaine émotions négatives : " + str(self.chaine_p))
            f = """cogn1|inf-4|inf-4|inf-4|ph-Votre TCC est correctement menée.
cogn2|inf-2|inf-2|inf-2|ph-Vos cognition negatives semblent très éloignées de la réalité.
"""
            liste_emotions_copy = self.chaine_p.copy()
        self.total_ligne= []
        for chaine in f.splitlines():
            chaine= chaine[:-1]
            self.total_ligne += [chaine]
        ####################################################
        for ligne in self.total_ligne:
            #Découpage des cases de la ligne:
            cases = ligne.split("|")
            #Parcours de la ligne avec la liste de émotions:
            self.parcours_ligne(liste_emotions_copy, cases)


def CreationListeInsertion(point,NumeroPoint,numeroGraph):
    global ListeInsertion
    test_existance = 'ListeInsertion' in globals()
    if test_existance :
        ListeInsertion.fen_insertion.close()

    ListeInsertion= ListeInsertion1(point,NumeroPoint,numeroGraph)

if __name__ == '__main__':
    debut = Identification()

def tccfriend():
    debut = Identification()
