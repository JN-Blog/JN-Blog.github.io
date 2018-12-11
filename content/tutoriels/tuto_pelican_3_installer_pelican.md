Title: Installer et configurer Pelican pour son blog statique
Date: 2018-10-28
Modified: 2018-10-28
Category: tutoriels
Tags: tutoriels
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

Nous sommes désormais prêt à installer Pelican.

## Installer Pelican et Markdown

Pour installer Pelican, rien de plus de simple, il suffit d'utiliser pip, le gestionnaire de paquet Python.
Attention à bien avoir activer votre environnement virtuel au préalable.

```
pip install pelican
```

Et comme nous allons écrire en format Markdown, nous allons également l'installer:

```
pip install Markdown
```

Et voilà, nous avons installer tous les éléments nécessaires pour créer notre blog statique.
Et comme on aime bien les choses propres, nous allons dans un premier temps, créer notre fichier requirements.txt avec toutes les dépendances associées à notre projet:

```
pip freeze > requirements.txt
```

Vous devriez retrouver un contenu similaire dans votre fichier requirements.txt:

```txt
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

Ensuite, nous créons notre fichier .gitignore et y ajoutons les éléments que l'on ne souhaite pas committer à savoir notre environnement virtuel. Prenons également un peu d'avance en y ajoutant les répertoires pycache et output:

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
-> Laissez à 10. Vous pourrez de toute façon le modifier par la suite

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

Ce sont les fichiers de configurations du blog. pelicanconf.py est le fichier de configuration principale et publishconf.py sera utilisé uniquement pour le déploiement en production et viendra ajouter ou écraser des configurations présentes dans pelicanconf.py.

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

Personnellement, j'aime bien définir la forme de mes urls. Je trouve que c'est un élément non négligeable qui participe à la cohérence dans le processus de navigation. Je vous propose donc de rajouter les variables suivantes:

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
content/
    |- images/
...
```

Une fois créé, il est nécessaire d'indiquer à Pelican le chemin où récupérer ces statics.
Il faut pour cela utiliser la variable STATIC_PATHS au sein du fichier de configuration:

```python
STATIC_PATHS = [
    'images',
]
```

cette variable contient une liste de répertoire par rapport au répertoire indiqué dans la variable ```PATH```, donc dans notre cas le répertoire *content*. Ces éléments seront copiés dans le répertoire *output* sans modification et pourront être utilisés en production. Par défault, Pelican inclus déjà le répertoire *images* mais c'est toujours bon de savoir comment faire!

Avant d'aller plus loin, nous allons ajouter quelques éléments supplémentaires. En effet, un CNAME a été enregistré et Pelican aura besoin d'y accéder dans le répertoire *output*. De plus, il paraît judicieux de rajouter un robot.txt lorsque l'on souhaite travailler son référencement dans les moteurs de recherche.
Et enfin, afin de personnaliser un peu, nous rajouterons un favicon également.
Je vous propose d'ajouter dans le répertoire *content* un répertoire *extra* avec les fichiers *robots.txt* et *CNAME* et le *favicon*:

```
content/
    |- images/
    |- extra/
        |- robots.txt
        |- CNAME
        |- favicon.ico
...
```

Et dans le fichier pelicanconf.py, nous allons rajouter ces éléments dans la variable STATIC_PATHS et déclarer la variable EXTRA_PATH_METADATA comme ceci:

```python
STATIC_PATHS = [
    'images',
    'extra/robots.txt',
    'extra/CNAME',
    'extra/favicon.ico',
]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
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
tutoriel-pelican.jn-blog.com
```

Et voilà, notre configuration de base est faîte.

## Publier notre site en local

Maintenant que tout est en place il serait judicieux de voir si tout fonctionne correctement.
Pour cela, rien de plus simple, il suffit de déployer notre site en local avec la commande:

```
make html && make serve
```

En effet, lorsque nous avons répondu à la question *10. Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n)*, Pelican a automatiquement généré un fichier Makefile afin de faciliter ce type d'opération.
Cette commande va générer les fichiers html et lancer un serveur web en local. (Pour stopper le serveur un simple Ctrl + C suffit).

En nous rendant à l'adresse ```http://localhost:8000/```, il est désormais possible d'accéder à son site.

![publication du site en local]({filename}/images/tuto-pelican-local-site.png)

## Créer notre premier articles

Voyons désormais comment écrire un article.
Il suffit pour cela de créer un fichier au format md à la racine du répertoire *content*.

```
content/
    |- images/
    |- extra/
        |- robots.txt
        |- CNAME
        |- favicon.png
    |- article.md
...
```

Pour aider Pelican à récupérer les informations nécessaires pour chaque article afin de générer correctement les fichiers html, nous allons utiliser les **métadatas**. Voici à quoi doit ressembler le début de votre article:

```
Date: 2018-11-16
Modified: 2018-11-16
Category: tutoriels
Tags: tutoriel, pelican, blog statique
Slug: mon-premier-article
Lang: fr
Authors: Julien Nuellas
Summary: Premier article sur blog tutoriel pelican
```

Cela permet à Pelican de récupérer les informations nécessaires pour le traîtement. En détaillant un peu, on a:

* la date de l'article
* la dernière date de modification de l'article
* la catégorie associée à l'article
* les tags associés à l'article
* le slug qui permettra d'alimenter l'url de la page de l'article
* la langue dans laquelle l'article sera écrit
* l'auteur de l'article
* une brève description de l'article

Pour plus d'informations, n'hésitez pas à aller explorer la [documentation](http://docs.getpelican.com/en/stable/content.html).

Une fois les metadatas renseignées, il suffit d'écrire son article:

```
Title: Premier article sur le blog tutoriel pelican
Date: 2018-11-16
Modified: 2018-11-16
Category: tutoriels
Tags: tutoriel, pelican, blog statique
Slug: mon-premier-article
Lang: fr
Authors: Julien Nuellas
Summary: Premier article sur blog tutoriel pelican

Bonjour tout le monde, ceci est mon premier article.

## Ceci est la première partie de mon article

Pelican, c'est vraiment fun.

## Ceci est la deuxième partie de mon article

Et markdown, c'est tellement simple à utiliser!
La syntaxe est simple à prendre en main et on peut faire tout ce qu'on veut. Voici une [cheat sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) qui vous permettra d'en savoir un peu plus.
```

Et voilà le travail est fait. Un petit coup de ```make html && make serve``` pour admirer le travail.

![publication du site en local]({filename}/images/tuto-pelican-local-site-avec-article.png)

Dans cet article, nous avons vu beaucoup de choses:

* Comment installer Pelican dans son repository et créer un projet
* Comment configurer Pelican de façon basique
* Comment générer et servir son blog statique en local
* Comment écrire un article

A ce stade du tutoriel, il nous reste encore deux choses importantes à voir:

* Comment déployer notre site en production sur github pages.
* Comment installer un thème. En effet, le thème de base ne vous convient peut être pas et vous aurez certainement l'envie de personnaliser un peu votre blog.

Alors commençons par voir comment déployer notre site en production dans le prochain article du tutoriel:

[Déployer son blog statique en production]({filename}tuto_pelican_4_installer_travis.md)