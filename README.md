# SAÉ Web/BD - Festiut’O

## Notre équipe

### Développeur 1

- Nom : BOURREAU
- Prénom : QUENTIN
- Identifiant Github : [BOURREAUQuentin](https://github.com/BOURREAUQuentin)

### Développeur 2

- Nom : CHHUM--MOXEL
- Prénom : LOANN
- Identifiant Github : [loannchhum](https://github.com/loannchhum)

### Développeur 3

- Nom : PREVOST
- Prénom : Maverick
- Identifiant Github : [MaverickPrevost](https://github.com/MaverickPrevost)

### Développeur 4

- Nom : JACQUET
- Prénom : Noa
- Identifiant Github : [NoaJacquet](https://github.com/NoaJacquet)

## Introduction

WEB :  BD 
SAE Web/BD
Festiut’O

Cette SAÉ s'inscrit dans le cours de Web et de Base de données, en se reposant sur les ressources suivantes :
- R3.01 : Développement Web
- R3.07 : SQL dans un langage de programmation

Le sujet repose principalement sur le développement d'une application web nommée Festiut'O.En partant d’un besoin exprimé par un client, l’objectif est donc de modéliser et implémenter une base de données, de proposer un maquettage pour une application graphique, mais également de développer une application Web sur une partie du système d’informations.

## Nos choix

### Le respect des bonnes pratiques

Pour respecter les bonnes pratiques de programmation et de gestion de projet vu à l’IUT, nous avons tout d'abord crée un référentiel GitHub commun. En effet, celui-ci a permis de faciliter la collaboration, la gestion du code source, la communication au sein de l'équipe, mais également de suivre notre avancée sur cette SAÉ.

Lien du GitHub : [Lien vers le GitHub](https://github.com/QuentinBOURREAU/SAE-Festiut-O)

### Le lancement du site
Pour lancer le projet, le mieux est d’avoir un environnement virtuel (virtualenv). Effectivement, dans celui-ci, vous pourrez installer les packages que vous voulez, sans avoir besoin d’être administrateur ; et les installations et mises à jour dans le virtualenv d’une application n’affectera pas celui d’une autre.
	
Une fois récupéré le projet, vous avez simplement à suivre ces commandes pour la créer si vous ne l'avez pas encore fait :

```python
cd Festiut-O
```
Ceci va créé un répertoire venv
```python
virtualenv -p python3 venv
```
il faut maintenant activer le venv dans votre shell
```python
source venv/bin/activate
```

Puis, il faut installer toutes les bibliotèques de notre site contenues dans le fichier requirements.txt en tapant cette commande :
```python
pip install -r requirements.txt
```

Une fois ceci fait ou si vous aviez déjà votre virtualenv, vous avez juste à taper cette commande pour lancer le site :

```python
flask run
```

Puis, vous allez sur le lien suivant qui vous affichera le site uniquement une fois la commande dernière lancée et toujours active :

```python
http://localhost:5000/
```

#

BOURREAU Quentin / CHHUM--MOXEL Loann / PREVOST Maverick / JACQUET Noa - BUT Informatique 2.3