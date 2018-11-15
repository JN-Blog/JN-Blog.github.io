Title: Installer et configurer Pelican pour son blog statique
Date: 2018-10-28
Modified: 2018-10-28
Category: tutoriels
Tags: tutoriel, pelican, blog statique
Slug: installer-pelican-pour-un-blog-statique
Lang: fr
Authors: Julien Nuellas
Summary: Découvrez comment installer et configurer Pelican pour votre propre blog statique. Toutes les étapes sont décrites et expliquées.

Après avoir découvert ce qu'est un site statique et avoir installé notre environnement de production via GitHub Pages, nous allons désormais mettre en place la structure de notre blog statique en utilisant le générateur de site statique [Pelican](http://docs.getpelican.com/en/stable/).

Comme cet article constitue la quatrième partie d'un tutoriel dédié à la création d'un blog statique, je me permets de rappeler la structure de ce dernier:

1. [Présentation du tutoriel et de ces objectifs]({filename}tuto_pelican_0_introduction.md)
2. [Un blog statique, c'est quoi et comment ça fonctionne?]({filename}tuto_pelican_1_whats_blog_statique.md)
3. [Mettre en place GitHub Pages pour l'hébergement d'un blog statique]({filename}tuto_pelican_2_githubpages_setup.md)
4. **Utiliser Pelican pour son blog statique**
5. [Utiliser Travis pour automatiser le déploiement de son blog statique]({filename}tuto_pelican_4_installer_travis.md)
6. [Mettre en place un thème sur son blog statique Pelican]({filename}tuto_pelican_5_installer_theme.md)

Nous verrons donc dans cet article comment installer Pelican et le configurer de manière basique. Nous écrirons également notre premier article et publirons notre blog en local.

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

Pour installer Pelican, rien de plus de simple, il suffit d'utiliser pip, le gestionnaire de paquet Python.
Attention à bien avoir activé votre environnement virtuel au préalable.

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

2. Créer notre fichier .gitignore et y ajouter les éléments que l'on ne souhaite pas committer à savoir notre environnement virtuel et prenons un peu d'avance en y ajoutant le répertoire __pycache__/ et output/:

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

![repertoire initial d'un projet Pelican]({filename}/images/tuto-pelican-pelican-repertoire.png)

## Mettre en place les premières configurations

Parmi les éléments installés, deux fichiers essentiels sont apparus. Il s'agit des fichiers:

* pelicanconf.py
* publishconf.py

Il s'agit des fichiers de configurations du blog. pelicanconf.py est le fichier de configuration principale et publishconf.py sera utilisé uniquement pour le déploiement en production et viendra ajouter ou écraser des configurations présentes dans pelicanconf.py.

### Quelques ajustements sur pelicanconf.py

Alors comment attaquer le morceau?
Premièrement, je vous invite à prendre quelques minutes pour examiner la [documentation](http://docs.getpelican.com/en/stable/settings.html) et décourvir toutes les possibilités.

En fonction des réponses aux questions, vous devez retrouver de votre côté un contenu similaire:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Julien Nuellas'
SITENAME = 'tutoriel-pelican'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
```

Il s'agit des configurations basiques. Globalement, on retrouve:

* ```AUTHOR```: Le nom de l'auteur du blog
* ```SITENAME```: le nom du blog
* ```SITEURL```: l'URL du blog en environnement de développement. Cette variable sera écrasé par l'url de votre site en production via le fichier publishconf.py
* ```PATH```: le nom du dossier contenant vos contenus
* ```TIMEZONE``` et ```DEFAULT_LANG```: les configurations basiques du fuseau horaire et du langage principal.
* Ensuite, il y a les variables servant à activer ou désactiver les flux Atom et RSS. On laissera ici à None car on ne souhaite pas les générer pour l'environnement de développement
* ```LINKS```: cette variable contient un tuple de tuples contenant des liens devant apparaître dans le header
* ```SOCIAL```: dans la même logique que la variable LINKS, il s'agit des liens de vos réseaux sociaux devant apparaître dans la section social.
* ```DEFAULT_PAGINATION```: définit le nombre d'articles maximum à intégrer dans une page.

Ainsi, le fichier de configuration contient tout ce qu'il y a de nécessaire pour fonctionner correctement dans un premier temps.
Je vous propose cependant d'ajouter quelques éléments supplémentaires

#### Configurations des URLs

Personnellement, j'aime bien définir la tête de mes urls. Je trouve que c'est un éléments non négligeables qui participe à la cohérence dans le processus de navigation. Je vous propose donc de rajouter les variables suivantes:

```python
# URL Settings
ARTICLE_URL = 'articles/{slug}/'
ARTICLE_SAVE_AS = 'articles/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
CATEGORY_URL = 'categorie/{slug}/'
CATEGORY_SAVE_AS = 'categorie/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

CATEGORIES_SAVE_AS = 'categories.html'
TAGS_SAVE_AS = 'tags.html'
INDEX_SAVE_AS = 'index.html'

AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = ''
```

#### Configuration des éléménts statiques

Vous intègrerez certainement des images dans vos articles et pour cela, il vous faut un endroit où les entreposer.
Je vous propose donc de stocker ces éléments dans un répertoire que nous nommerons **images** au sein du répertoire **content**.

```
content
    |- images
...
```

Une fois créé, il est nécessaire d'indiquer à Pelican le chemin où récupérer ces statics.
Il faut pour cela utiliser la variable STATIC_PATHS au sein du fichier de configuration:

```python
STATIC_PATHS = [
    'images',
]
```

cette variable contient une liste de répertoire par rapport au répertoire indiquer dans la variable ```PATH```, donc dans notre cas le repertoire **content**. Ces répertoires seront copiés dans le répertoire **output** sans modifications et pourront être utilisés en production. Par défault, Pelican inclus déjà le répertoire **images** mais c'est toujours bon de savoir comment faire!

Avant d'aller plus loin, nous allons ajouter quelques éléments supplémentaires. En effet, un CNAME a été enregistré et Pelican aura besoin d'y accéder dans le répertoire **output**. De plus, il paraît judicieux de rajouter un robot.txt lorsque l'on souhaite travailler son référencement dans les moteurs de recherche.
Et enfin, afin de personnaliser un peu, nous rajouterons un favicon également.
Je vous propose dans le répertoire **content** d'ajouter un répertoire **extra** avec les fichiers **robots.txt** et **CNAME** et le **favicon**:

```
content
    |- images
    |- extra
        |- robots.txt
        |- CNAME
        |- favicon.png
...
```

Et dans le fichier pelicanconf.py, nous allons rajouter ces éléments dans la variable STATIC_PATHS et ajouter la variable EXTRA_PATH_METADATA comme ceci:

```python
STATIC_PATHS = [
    'images',
    'extra/robots.txt',
    'extra/CNAME',
    'extra/favicon.png',
]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.png': {'path': 'favicon.png'}
}
```

Petits bonus:
* Si vous ne connaissez par très bien le fonctionnement d'un fichier robots.txt mais que vous souhaitez être référencé sur l'ensemble des moteurs, voici la configuration:
```
User-agent: *
Disallow: 
```

* Votre fichier CNAME doit contenir uniquement votre nom de domaine. Pour le projet du tutoriel:
```
tutoriel.jn-blog.com
```

Et voilà, notre configuration de base est faîte. Nous allons pouvoir créer notre premier article!

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