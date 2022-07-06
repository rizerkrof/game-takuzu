#!/usr/bin/env python3


# -*- coding: utf-8 -*-
"""
Created on Fri May 27 19:39:25 2022

@author: lacou
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QAction, QToolBar,  QLabel,  QGridLayout,  QHBoxLayout, QVBoxLayout, QPushButton, QMessageBox
from PyQt5.QtCore import  QCoreApplication, Qt, QSize
from PyQt5.QtGui import QIcon, QKeySequence, QFont, QPixmap
import random

class Fenetre(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Takuzu")

        ### Les sous-menus ###

        self.action1 = QAction(QIcon("layout-4.png"), "Grille 4x4", self)
        self.action1.triggered.connect(self.initGrid4)
        self.action1.setShortcut(QKeySequence('Ctrl+G'))

        self.action12 = QAction(QIcon("layout-6.png"), "Grille 6x6", self)
        self.action12.triggered.connect(self.initGrid6)
        self.action12.setShortcut(QKeySequence('Ctrl+X'))

        self.action13 = QAction(QIcon("block--pencil.png"), "Choisir Taille", self)
        #self.action13.triggered.connect(self.resolutionButtonClick)
        self.action13.setShortcut(QKeySequence('Ctrl+C'))


        self.action2 = QAction(QIcon("traffic-light-green.png"), "Niveau Débutant", self)
        self.action2.triggered.connect(self.initLevelD)
        self.action2.setShortcut(QKeySequence('Ctrl+D'))

        self.action22 = QAction(QIcon("traffic-light-red.png"), "Niveau Intermédiaire", self)
        self.action22.triggered.connect(self.initLevelI)
        self.action22.setShortcut(QKeySequence('Ctrl+I'))


        self.action3 = QAction(QIcon("dummy-happy.png"), "Résolution", self)
        #self.action3.triggered.connect(self.onMyToolBarButtonClick)
        self.action3.setShortcut(QKeySequence('Ctrl+S'))


        self.action4 = QAction(QIcon("books-brown.png"), "Règles du jeu", self)
        self.action4.triggered.connect(self.Propos)
        self.action4.setShortcut(QKeySequence('Ctrl+R'))

        self.action41 = QAction(QIcon("animal-monkey.png"), "Qui ?", self)
        self.action41.triggered.connect(self.Qui)
        self.action41.setShortcut(QKeySequence('Ctrl+E'))


        self.action5 = QAction(QIcon("bomb.png"), "Quitter", self)
        self.action5.triggered.connect(self.Quitter)
        self.action5.setShortcut(QKeySequence('Ctrl+Q'))


        ### Les menus ###

        self.menuGrille = self.menuBar().addMenu("Grille")
        self.menuGrille.addAction(self.action1)
        self.menuGrille.addSeparator()
        self.menuGrille.addAction(self.action12)
        self.menuGrille.addSeparator()
        self.menuGrille.addAction(self.action13)

        self.menuJouer = self.menuBar().addMenu("Jouer")
        self.menuJouer.addAction(self.action2)
        self.menuJouer.addSeparator()
        self.menuJouer.addAction(self.action22)

        self.menuRésolution = self.menuBar().addMenu("Résolution")
        self.menuRésolution.addAction(self.action3)

        self.menuPropos = self.menuBar().addMenu("A propos")
        self.menuPropos.addAction(self.action4)
        self.menuPropos.addSeparator()
        self.menuPropos.addAction(self.action41)

        self.menuQuitter = self.menuBar().addMenu("Quitter")
        self.menuQuitter.addAction(self.action5)


        # Les toolbars ###

        self.toolbar = QToolBar("Ma toolbar")
        self.toolbar.setIconSize(QSize(16,16))
        self.addToolBar(self.toolbar)

        self.button1_action = QAction(QIcon("layout-4.png"), "Grille 4x4", self)
        self.button1_action.setToolTip("Grille 4x4")
        self.button1_action.triggered.connect(self.initGrid4)

        self.button2_action = QAction(QIcon("layout-6.png"), "Grille 6x6", self)
        self.button2_action.setStatusTip("Grille 6x6")
        self.button2_action.triggered.connect(self.initGrid6)

        self.button3_action = QAction(QIcon("traffic-light-green.png"), "Niveau débutant", self)
        self.button3_action.setToolTip("Niveau débutant")
        self.button3_action.triggered.connect(self.initLevelD)

        self.button4_action = QAction(QIcon("traffic-light-red.png"), "Niveau intermédiaire", self)
        self.button4_action.setToolTip("Niveau intermédiaire")
        self.button4_action.triggered.connect(self.initLevelI)

        self.button5_action = QAction(QIcon("dummy-happy.png"), "Résolution", self)
        self.button5_action.setToolTip("Résolution")

        self.button6_action = QAction(QIcon("books-brown.png"), "Règles du jeu", self)
        self.button6_action.setToolTip("Règles du jeu")
        self.button6_action.triggered.connect(self.Propos)

        self.button7_action = QAction(QIcon("animal-monkey.png"), "Qui ?", self)
        self.button7_action.setToolTip("Qui ?")
        self.button7_action.triggered.connect(self.Qui)

        self.button8_action = QAction(QIcon("bomb.png"), "Quitter", self)
        self.button8_action.setToolTip("Quitter")
        self.button8_action.triggered.connect(self.Quitter)

        self.toolbar.addAction(self.button1_action)
        self.toolbar.addAction(self.button2_action)
        self.toolbar.addAction(self.button3_action)
        self.toolbar.addAction(self.button4_action)
        self.toolbar.addAction(self.button5_action)
        self.toolbar.addAction(self.button6_action)
        self.toolbar.addAction(self.button7_action)
        self.toolbar.addAction(self.button8_action)


        ### Plateau de jeu au lancement de l'application ###

        self.g4=None
        self.g6=None

        self.image = QLabel('Takuzu')
        self.image.setPixmap(QPixmap('takuzu.jpg'))
        self.image.setAlignment(Qt.AlignCenter)
        self.titre = QLabel("Jeu : Le Takuzu")
        self.titre.setStyleSheet(" color :orangered ; font-size: 44px")
        self.titre.setAlignment(Qt.AlignCenter)

        self.label1 = QLabel("Pour jouer, sélectionnez une grille ou un niveau à partir du menu")
        self.label1.setStyleSheet(' color :orangered ; font-size: 24px')
        self.label1.setAlignment(Qt.AlignCenter)

        self.labelnoms = QLabel("Par Noémie Lacourt et Sergio Machado")
        self.labelnoms.setStyleSheet(' color :orangered ; font-size: 16px')
        self.labelnoms.setAlignment(Qt.AlignCenter)

        self.boardLayout = QVBoxLayout()
        self.boardLayout.addWidget(self.titre)
        self.boardLayout.addWidget(self.image)
        self.boardLayout.addWidget(self.label1)
        self.boardLayout.addWidget(self.labelnoms)
        self.setGeometry(400,75,1000,700)
        self.widget = QWidget()
        self.widget.setLayout(self.boardLayout)

        self.setCentralWidget(self.widget)


    ### Plateau de jeu selon la grille sélectionnée ###

    def initGrid4(self):
        self.g4=True
        self.g6=False
        self.D=True
        self.I=False
        self.initialisation(4,6)

    def initGrid6(self):
        self.g4=False
        self.g6=True
        self.D=True
        self.I=False
        self.initialisation(6,6)

    ### Changement de plateau de jeu selon le niveau sélectionné ###
    def initLevelD(self):
        self.D=True
        self.I=False
        if self.g4==None and self.g6==None:
            self.initialisation(6,6)
        else :
            self.popup = QMessageBox(QMessageBox.Information,'Attention', 'En changeant de niveau vous allez réinitialiser la partie, êtes-vous sûr ? ' )
            self.popup.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            self.popup.show()
            if self.popup.exec()==QMessageBox.Ok:
                if self.g4==True:
                    self.initialisation(4,6)
                elif self.g6==True:
                    self.initialisation(6,6)
                else : self.initialisation(6,6)

    def initLevelI(self):
        self.D=False
        self.I=True
        if self.g4==None and self.g6==None:
            self.initialisation(6,3)
        else :
            self.popup = QMessageBox(QMessageBox.Information,'Attention', 'En changeant de niveau vous allez réinitialiser la partie, êtes-vous sûr ? ' )
            self.popup.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            self.popup.show()
            if self.popup.exec()==QMessageBox.Ok:
                if self.g4==True:
                    self.initialisation(4,3)
                elif self.g6==True:
                    self.initialisation(6,3)
                else : self.initialisation(6,3)


    ### Fonctions d'initialisation du plateau selon la grille et le niveau choisis ###

    def initialisation(self,g,n):
        self.j=g
        self.gridLayout = QGridLayout()
        self.Grid(self.j)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setContentsMargins(0,0,0,0)

        self.vies = n
        self.indices=n
        self.labelGrid = QLabel("GRILLE : "+str(g)+'x'+str(g))
        if n==6:
            self.labelLevel = QLabel("NIVEAU : Débutant")
        if n==3:
            self.labelLevel = QLabel("NIVEAU : Intermédiaire")
        self.labelvie = QLabel("VIES : "+str(self.vies))
        self.labelindice = QLabel("INDICES : "+str(self.indices))
        self.textLayout = QHBoxLayout()
        self.textLayout.addWidget(self.labelGrid)
        self.textLayout.addWidget(self.labelLevel)
        self.textLayout.addWidget(self.labelindice)
        self.textLayout.addWidget(self.labelvie)

        self.HLayout = QHBoxLayout()
        self.buttonHint=QPushButton("Indice", self)
        self.buttonHint.setFixedSize(250, 100)
        self.buttonHint.clicked.connect(self.giveIndices)
        self.buttonCheck = QPushButton("VERIFIER", self)
        self.buttonCheck.setFixedSize(250, 100)
        self.buttonCheck.clicked.connect(self.verifier)
        self.HLayout.addWidget(self.buttonHint)
        self.HLayout.addWidget(self.buttonCheck)

        self.label3 = QLabel("Les indices et vérifications seront affichés ici")
        self.label3.setAlignment(Qt.AlignCenter)
        self.label3.setStyleSheet(' background-color : coral')
        self.label3.setFont(QFont ('Arial Font', 9))
        self.label3.setFixedHeight(50)

        self.boardLayout = QVBoxLayout()
        self.boardLayout.addLayout(self.gridLayout)
        self.boardLayout.addLayout(self.textLayout)
        self.boardLayout.addLayout(self.HLayout)
        self.boardLayout.addWidget(self.label3)

        if self.j==4:
            self.setGeometry(200,75,700,500)
        if self.j == 6:
            self.setGeometry(150,75,1000,700)
        self.widget = QWidget()
        self.widget.setLayout(self.boardLayout)
        self.setCentralWidget(self.widget)

    def Grid(self,n):
        self.tabVal4 =["0","1","1","0","1","0","1","0","0","1","0","1","1","0","0","1"]
        self.tabVal6 =["1","0","0","1","1","0","1","0","1","0","1","0","0","1","1","0","0","1","1","1","0","1","0","0","0","0","1","0","1","1","0","1","0","1","0","1"]
        self.tabVal = [ "" for _ in range(n*n)]
        for rIndex in random.sample(range(n*n), 12 if n == 6 else 6):
            self.tabVal[rIndex] = self.tabVal4[rIndex] if self.j==4 else self.tabVal6[rIndex]
        self.putListInButtons(self.tabVal, n)
        nomsLignes=["A","B","C","D","E","F"]
        nomsColonnes=["1","2","3","4","5","6"]
        for i in range (self.j):
            self.labelLignes=QLabel(nomsLignes[i])
            self.labelLignes.setFixedSize(100, 60)
            self.labelLignes.setStyleSheet(' color :orangered')
            self.labelLignes.setFont(QFont ('Arial Font', 10))
            self.labelLignes.setAlignment(Qt.AlignCenter)
            self.gridLayout.addWidget(self.labelLignes, i+1, 0)
            self.labelColonnes=QLabel(nomsColonnes[i])
            self.labelColonnes.setFixedSize(250, 60)
            self.labelColonnes.setStyleSheet(' color :orangered')
            self.labelColonnes.setFont(QFont ('Arial Font', 10))
            self.labelColonnes.setAlignment(Qt.AlignCenter)
            self.gridLayout.addWidget(self.labelColonnes, 0, i+1)

    def putListInButtons(self,liste, n):
        for i in range (n):
            for j in range (n):
                self.button = QPushButton(str(liste[i*n+j]), self)
                self.button.clicked.connect(self.onClick)
                self.button.setFont(QFont ('Arial Font', 10))
                self.button.setFixedSize(250, 100)
                if str(liste[i*n+j]) != "":
                    self.button.setEnabled(False)
                    self.button.setStyleSheet(' color :black ; background-color : lightgrey')
                self.gridLayout.addWidget(self.button, i+1, j+1)

    ### Fonctions de jeu ###

    # Fonction de mise à jour des boutons du plateau cliqués
    def onClick(self):
        valeur = self.sender().text()
        indiceVal=self.gridLayout.indexOf(self.sender())
        if valeur == "":
            self.sender().setText("0")
            self.tabVal[indiceVal]="0"
        elif valeur == "0":
            self.sender().setText("1")
            self.tabVal[indiceVal]="1"
        else :
            self.sender().setText("")
            self.tabVal[indiceVal]=""

    # Fonctions utiles pour le fonctionnememnt des fonctions de validité d'un coup et des indices
    def lignes_colonnes(self):
        if self.j==4:
            L1=[0,1,2,3]
            L2=[4,5,6,7]
            L3=[8,9,10,11]
            L4=[12,13,14,15]
            C1=[0,4,8,12]
            C2=[1,5,9,13]
            C3=[2,6,10,14]
            C4=[3,7,11,15]
            self.L_C=[L1,L2,L3,L4,C1,C2,C3,C4]
        elif self.j==6:
            L1=[0,1,2,3,4,5]
            L2=[6,7,8,9,10,11]
            L3=[12,13,14,15,16,17]
            L4=[18,19,20,21,22,23]
            L5=[24,25,26,27,28,29]
            L6=[30,31,32,33,34,35]
            C1=[0,6,12,18,24,30]
            C2=[1,7,13,19,25,31]
            C3=[2,8,14,20,26,32]
            C4=[3,9,15,21,27,33]
            C5=[4,10,16,22,28,34]
            C6=[5,11,17,23,29,35]
            self.L_C=[L1,L2,L3,L4,L5,L6,C1,C2,C3,C4,C5,C6]
        self.Lrempli=[]
        self.Crempli=[]

        for i in range (len(self.L_C)):
            for j in range (len(self.L_C[i])):
                self.L_C[i][j]=self.tabVal[self.L_C[i][j]]

    def updateBarreInfos(self,text) :
        self.label3.deleteLater()
        self.label3 = QLabel(text)
        self.label3.setAlignment(Qt.AlignCenter)
        self.label3.setFixedHeight(50)
        self.label3.setStyleSheet(' background-color : coral')
        self.label3.setFont(QFont ('Arial Font', 9))
        self.boardLayout.addWidget(self.label3)

    # Fonction validité d'un coup
    def valide(self):
        self.lignes_colonnes()
        L_C=self.L_C
        Lrempli=self.Lrempli
        Crempli=[]=self.Crempli=[]

        for i in range (len(L_C)):
            for j in range (len(L_C[i])-2):    # Trois 0 ou 1 à la suite
                if L_C[i][j]!= "" and L_C[i][j]==L_C[i][j+1]==L_C[i][j+2]:
                    return 1

        for LC in L_C:                         # Nb 0 != Nb 1
            if not "" in LC and (LC.count("0")!=LC.count("1") or LC.count("0") > self.j/2 or  LC.count("1") > self.j/2)  :
                return 2

        for l in L_C[:self.j]:    # Deux fois la même ligne
            if not "" in l:
                Lrempli.append(l)
        for i in range (len(Lrempli)-1):
            for j in range (i+1,len(Lrempli)):
                if Lrempli[i]==Lrempli[j]:
                    return 3

        for c in L_C[self.j:]:    # Deux fois la même colonne
            if not "" in c:
                Crempli.append(c)
        for i in range (len(Crempli)-1):
            for j in range (i+1,len(Crempli)):
                if Crempli[i]==Crempli[j]:
                    return 4
        return 0

    # Fonction de vérfication d'un coup (coup valide/coup correct)
    def verifier(self):
        if all([ s == self.tabVal[i] for i, s in enumerate(self.tabVal4 if self.j==4 else self.tabVal6)]):
            self.popup = QMessageBox(QMessageBox.Information,"PARTIE GAGNEE","Bravo tout est découvert!")
            self.popup.show()
        if self.valide() != 0:
            self.updateVies()
            if self.valide()==1:
                self.updateBarreInfos("Coup invalide : 3 fois de suite un 0 ou un 1")
            elif self.valide()==2:
                self.updateBarreInfos("Coup invalide : trop de 0 ou 1 dans une ligne/colonne")
            elif self.valide()==3:
                self.updateBarreInfos("Coup invalide : deux lignes indentiques")
            elif self.valide()==4:
                self.updateBarreInfos("Coup invalide : deux colonnes indentiques")
        else:
            for i in range (len(self.tabVal)):
                if self.tabVal[i]!="" and (self.tabVal[i]!=self.tabVal4[i] if self.j==4 else self.tabVal[i]!=self.tabVal6[i]):
                    self.updateBarreInfos("Coup valide mais incorrect")
                    break
                elif self.tabVal[i]!="" and (self.tabVal[i]==self.tabVal4[i] if self.j==4 else self.tabVal[i]==self.tabVal6[i]):
                    self.updateBarreInfos("Coup valide et correct")

    # Fonction de mise à jour des vies
    def updateVies(self):
        if self.vies!=0:
            self.vies-=1
            self.labelvie.deleteLater()
            self.labelvie = QLabel("VIES : "+str(self.vies))
            self.textLayout.addWidget(self.labelvie)
            self.boardLayout.addLayout(self.textLayout)
        elif self.vies==0:
            self.popup = QMessageBox(QMessageBox.Information,"Plus de vies","Vous n'avez plus de vies, la partie est finie"+'\n'+'Voulez vous retenter votre chance ?')
            self.popup.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            self.popup.show()
            if self.popup.exec()==QMessageBox.Yes:
                if self.D==True and self.I==False:
                    self.initialisation(self.j,6)
                    self.popup.close()
                else:
                    self.initialisation(self.j,3)
            else:
                self.popup.close()
                self.Quitter()


    # Fonction attribuant des indices
    def giveIndices(self):
        self.updateIndices()
        self.lignes_colonnes()
        L_C=self.L_C
        Lignes=L_C[:self.j]
        Colonnes=L_C[self.j:]
        for i in range (len(L_C)):
            for j in range (len(L_C[i])-1):
                if L_C[i][j]!= "" and L_C[i][j]==L_C[i][j+1]:
                    if (j!=0 and L_C[i][j-1]== "") or (j+1!=self.j-1 and L_C[i][j+2]== ""):
                        self.updateBarreInfos("Il ne peut pas y avoir plus de deux 0 ou deux 1 d'affilé")

        for i in range (len(L_C)):
            for j in range (len(L_C[i])-2):
                if L_C[i][j]!= "" and L_C[i][j]==L_C[i][j+2] and L_C[i][j+1]=="":
                    self.updateBarreInfos("Entre deux 0 il ne peut y avoir qu'un 1, de même, entre deux 1 il ne peut y avoir qu'un 0")

        for i in range (len(L_C[:self.j])):
            if Lignes[i].count("")==1 or ((Lignes[i].count("0")==self.j/2 or Lignes[i].count("1")==self.j/2) and Lignes.count("")>=1):
                self.updateBarreInfos("Il y a autant de 0 et de 1 dans une ligne")
        for i in range (len(L_C[self.j:])):
            if Colonnes[i].count("")==1 or ((Colonnes[i].count("0")==self.j/2 or Colonnes[i].count("1")==self.j/2) and Colonnes[i].count("")>=1) :
                self.updateBarreInfos("Il y a autant de 0 et de 1 dans une colonne")

        l=0
        for i in range (len(Lignes)):
            for j in range (len(Lignes)):
                if "" not in Lignes[i] and Lignes[j].count("")==2:
                    for a in range (self.j):
                        if Lignes[j][a]!="" and Lignes[i][a]==Lignes[j][a]:
                            l+=1
        if l==4:
            self.updateBarreInfos("Il ne peut pas y avoir deux fois la même ligne")

        c=0
        for i in range (len(Colonnes)):
            for j in range (len(Colonnes)):
                if "" not in Colonnes[i] and Colonnes[j].count("")==2:
                    for a in range (self.j):
                        if Colonnes[j][a]!="" and Colonnes[i][a]==Colonnes[j][a] :
                            c+=1
        if c==4:
            self.updateBarreInfos("Il ne peut pas y avoir deux fois la même colonne")

    # Fonction de mise à jour du compteur d'indices
    def updateIndices(self):
        if self.indices>0 :
            self.indices-=1
            self.labelindice.deleteLater()
            self.labelindice = QLabel("INDICES : "+str(self.indices))
            self.textLayout.addWidget(self.labelindice)
            self.labelvie.deleteLater()
            self.labelvie = QLabel("VIES : "+str(self.vies))
            self.textLayout.addWidget(self.labelvie)
            self.boardLayout.addLayout(self.textLayout)

        if self.indices==0:
            self.buttonHint.setEnabled(False)

    def resolutionButtonClick(self):
        print("clicked")

    def Propos(self):
        self.popup = QMessageBox(QMessageBox.Information,'Infos du jeu', 'Règles du jeu: \n\n1. Dans une ligne, il doit y avoir autant de 0 que de 1 \n\n2. Dans une colonne, il doit y avoir autant de 0 que de 1 \n\n3. Il ne peut pas y avoir deux lignes identiques dans une grille \n\n4. Il ne peut pas y avoir deux colonnes identiques dans une grille \n\n5. Dans une ligne ou une colonne, il ne peut y avoir plus de deux 0 ou deux 1 à la suite (on ne peut pas avoir trois 0 de suite ou trois 1 de suite) ' )
        self.popup.show()

    def Qui(self):
        self.popup = QMessageBox(QMessageBox.Information,'Qui ?', 'Jeu crée par: \n\nLacourt Noémie SpeD \n\nMachado Sergio SpeD' )
        self.popup.show()

    def Quitter(self):
        window.close()

app = QCoreApplication.instance()
if app is None:
    app = QApplication(sys.argv)
window = Fenetre()
window.show()
app.exec_()
# Projet_final.py
# Affichage de Projet_final.py
