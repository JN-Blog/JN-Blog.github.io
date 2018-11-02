Title: JN-Blog: Installer et configurer Pelican pour son blog statique
Date: 2018-10-28
Modified: 2018-10-28
Category: tutoriels
Tags: tutoriel, pelican, blog statique
Slug: installer-pelican-pour-un-blog-statique
Lang: fr
Authors: Julien Nuellas
Summary: Découvrez comment installer et configurer Pelican pour votre propre blog statique. Toutes les étapes sont décrites et expliquées.

# Installer et configurer Pelican pour son blog statique

Après avoir découvert ce qu'est un site statique et avoir installé notre environnement de production via GitHub Pages, nous allons désormais mettre en place la structure de notre blog statique en utilisant le générateur de site statique [Pelican](http://docs.getpelican.com/en/stable/).

Comme cet article constitue la troisième partie d'un tutoriel dédié à la création d'un blog statique, je me permets de rappeler la structure de ce dernier:
1. [Un blog statique, c'est quoi et comment ça fonctionne?]({filename}tuto_pelican_2_githubpages_setup.md)
2. [Mettre en place GitHub Pages pour l'hébergement d'un blog statique]({filename}tuto_pelican_2_githubpages_setup.md)
3. **Utiliser Pelican pour son blog statique]**
4. [Utiliser Travis pour automatiser le déploiement de son blog statique]({filename}tuto_pelican_4_installer_travis.md)
5. [Mettre en place un thème sur son blog statique Pelican]({filename}tuto_pelican_5_installer_theme.md)

Nous verrons donc dans cet article comment installer Pelican et le configurer de manière basique. Nous écrirons également notre premier article et publirons notre blog en local.

Pour cela, nous ferons appel à quelques connaissances liées à l'environnement Python. En effet, Pelican est un générateur de sites statiques construit en Python et cela demande donc quelques connaissances sur son environnement de fonctionnement. Je tâcherai tout au long de ce tutoriel d'apporter un maximum d'explication mais je ne souhaite pas non plus diluer l'objectif de cet article en dérivant sur des explications précises sur l'environnement Python. Par contre, si vous êtes intéressé par en apprendre plus sur ce sujet, faîtes le moi savoir dans les commentaires et je serai râvi de prendre le sujet à coeur et en faire des articles annexes.

Maintenant que l'on sait ce que l'on va faire dans cet article, il est temps de débuter les hostilités.

## Cloner le repository et mettre créer la branche source

La première chose à faire est de cloner le repository en local dans le répertoire souhaité. Pour notre projet fil rouge, il s'agit de la commande suivante:

```
git clone https://github.com/JN-Blog/tutoriel-pelican.git
```

Il suffit de récupérer l'url de votre repository et remplacer l'url ci-dessous par la votre.
Une fois le repository cloné, nous créeons la branche source qui sera notre branche principale de développement et nous nous positionnons dessus:

```
git checkout -b source
```

Si vous lancer désormais la commande ```git branch```, vous devriez obtenir le résultat suivant:

```
master
* source
```

L'asterix à côté de la branche source prouve que vous êtes positionné sur la bonne branche. Nous sommes désormais prêt à installer notre environnement de développement.

## Installer Python et créer son environnement virtuel

Si vous n'avez pas encore installer Python sur votre ordinateur, il est temps de le faire désormais. Voici le lien officiel pour télécharger la dernier version: https://www.python.org/downloads/

Une fois installé, nous allons installer notre environnement virtuel à la racine de votre répertoire:

```
python3 -m venv env
```

Une fois notre environnement virtuel installé, il ne nous reste plus qu'à l'activer:

```
source env/bin/activate
```

Nous sommes désormais prêt à installer Pelican

## Installer Pelican et Markdown

Pour installer Pelican, rien de plus de simple, il suffit d'installer pip, le gestionnaire de paquet Python:

```
pip install pelican
```

Et comme nous allons écrire en format Markdown, nous allons également l'installer:

```
pip install Markdown
```

Et voilà, nous avons installer tous les éléments nécessaires pour créer notre blog statique.
Et comme on aime bien les choses propres, on va:

1. Créer notre fichier requirements.txt avec toutes les dépendances associées à notre projet:
```
pip freeze > requirements.txt
```

Vous devriez retrouver un contenu similaire dans votre fichier requirements.txt:
```
blinker==1.4
docutils==0.14
feedgenerator==1.9
Jinja2==2.10
Markdown==3.0.1
MarkupSafe==1.0
pelican==3.7.1
Pygments==2.2.0
python-dateutil==2.7.5
pytz==2018.7
six==1.11.0
Unidecode==1.0.22
```

Il s'agit des dépendances du projet. En effet, vous n'avez installé que Markdown et Pelican mais ce dernier a besoin de ces autres paquets pour fonctionner.

2. Créer notre fichier .gitignore et y ajouter les éléments que l'on ne souhaite pas commitez à savoir notre environnement virtuel et prenons un peu d'avance en y ajoutant le répertoire __pycache__/ et output/:

```
touch .gitignore
```

Et le contenu de notre fichier ressemble à cela:

```
env/
__pycache__/
output/
```

Vous pouvez bien sûr faire votre premier commit et pousser le tout sur GitHub (dans votre branche source).
Nous sommes désormais prêt à créer notre projet Pelican.

## Créer un projet Pelican

Une fois tout installé, nous allons pouvoir créer notre squelette de projet sous Pelican.
Pour cela, rien de plus simple, à l'installation de Pelican, des commandes ont également été installées.

Il vous suffit donc de lancer la commande suivante:

```
pelican-quickstart
```

Une fois lancé vous allez devoir répondre à une série de questions:

1. Where do you want to create your new website? [.]
-> Taper .

2. What will be the tilte of this website?
-> Indiquez le nom de votre blog. Pour le projet de ce tutoriel, il s'agit de tutoriel-pelican

3. What will be the author of this web site?
-> Indiquez votre nom et prénom

4. What will be the default language of this web site?[fr]
-> Tapez la langue que vous utiliserez pour votre blog

5. Do you want to specify a URL prefix? e.g, http://example.com (Y/n)
-> Si vous avez un nom de domaine personnalisé, tapez Y

6. What is your URL prefix? (see above example; no trailing slash)
-> Tapez votre nom de domaine selon l'exemple indiqué dans la question précédent : https://tutoriel-pelican.jn-blog.com

7. Do you want to enable article pagination? (Y/n)
-> Tapez Y

8. How many articles per page do you want? [10]
-> Laissez à 10. Vous pourrez de toute façon modifier par la suite

9. What is your time zone? [Europe/Paris]
-> Indiquez le fuseau horaire souhaité.

10. Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n)
-> Tapez **Y**. Nous utiliserons le Makefile pour générer le site.

11. Do you want an auto-reload & simpleHTTP script to assist with theme and site development. (Y/n)
-> Vous pouvez répondre n

12. Do you want to upload your website using FTP? (y/N)
-> Tapez N

13. Do you want to upload your website using SSH? (y/N)
-> Tapez N

14. Do you want to upload your website using Dropbox (y/N)
-> Tapez N

15. Do you want to upload your website using S3 (y/N)
-> Tapez N

16. Do you want to upload your website using Rackspace Cloud Files (y/N)
-> Tapez N

17. Do you want to upload your website using GitHub Pages (y/N)
-> Tapez y. C'est la solution que nous avons choisie dans ce tutoriel.

18. Is this your personal page (username.github.io)? (y/N)
-> Vous pouvez taper y

Et voilà! Si vous examinez un peu votre répertoire, vous vous apercevez que tous les fichiers nécessaires ont été automatiquement générés!

![repertoire initial d'un projet Pelican]({filename}/images/tuto-pelican-repertoire.png)

## Mettre en place les premières configurations

### gitignore et requirements.txt
### peliconf.py
### content extra (favicon, CNAME et robots.txt)

## Créer notre premier articles

## Publier notre site en local

<!-- ### Cloner le repository en local

Une fois le repository créé, nous allons le cloner sur notre machine dans le répertoire dedié au blog:

```
git clone https://ta-race.git 
```

Un fois cloné, nous créeons les branches source et gh-pages en plus de la branche master:

```
git branch source
git branch gh-pages
```

Désormais, si nous lançons la commande ```git branch```, nous pouvons constater que le repository possède trois branches:

```
* master
source
gh-pages
```

Une fois créée, nous pouvons désormais toutes les pousser sur GitHub:

```
git push origin HEAD
```

Maintenant, retournant sur GitHub dans notre repository pour continuer la configuration. -->