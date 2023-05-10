# Simulateur de Parties d'Échecs PGN

## Table des matières

* [Introduction](#introduction)
* [Installation](#installation)
* [Utilisation](#utilisation)
* [Détail du Code](#detail-du-code)
* [Conclusion](#conclusion)

## Introduction

Bienvenue dans le projet de simulateur de parties d'échecs PGN! Ce projet permet de lire un fichier PGN, de le traduire en une structure de données interne (AST), puis de simuler la partie d'échecs à l'aide d'une interface graphique basée sur Tkinter et de la bibliothèque Chess. Grâce à cette interface, vous pourrez naviguer dans votre partie pour voir analyser vos coups.

## Installation

Pour installer ce projet, vous devez cloner le dépôt à partir du lien fourni, puis installer les dépendances nécessaires. Assurez-vous d'avoir Python installé sur votre machine.
Il est également d'avoir deux librairies pour faire fonctionner le projet. Vous aurez besoin de la librairie chess ainsi que de tkinter. 

```bash
git clone <lien du dépôt>
pip install chess
pip install tkinter
```

## Utilisation

Pour utiliser ce projet, exécutez le script principal du projet comme suit:
```
python main.py fichier.pgn
```

> Veillez à mettre l'affichage de votre ordinateur en mode jour. 

Le script principal du projet fera les opérations suivantes:

1. Lire le fichier PGN.
2. Effectuer une analyse lexicale et syntaxique du fichier PGN, créant un arbre de syntaxe abstraite (AST).
3. Visiter l'AST pour créer une représentation interne de la partie d'échecs.
4. Afficher la partie d'échecs sur une interface graphique, en permettant de naviguer à travers les coups.

## Détail du Code

Le projet se compose de plusieurs composants principaux:

1. pgn_lexer.py: Ce fichier contient le code pour l'analyse lexicale du fichier PGN. Il transforme le texte du fichier en une série de tokens.
2. pgn_parser.py: Ce fichier contient le code pour l'analyse syntaxique des tokens, créant un AST.
3. pgn_visitor.py: Ce fichier contient le code pour visiter l'AST et créer une représentation interne de la partie d'échecs.
4. pgn_interface.py: Ce fichier contient le code pour l'interface graphique, qui affiche la partie d'échecs et permet de naviguer à travers les coups.
5. utils.py: Ce fichier contient des fonctions utilitaires pour convertir les mouvements dans le format approprié pour la bibliothèque Chess.


## Conclusion

Ce projet a été une excellente occasion d'explorer le fonctionnement interne de l'analyse de texte et de la représentation de données complexes. En travaillant sur ce projet, nous avpns pu approfondir notre compréhension de concepts tels que l'analyse lexicale et syntaxique, la création d'AST, la visite d'AST et la création d'interfaces graphiques en Python. Nous espérons que vous trouverez ce projet utile et instructif!
