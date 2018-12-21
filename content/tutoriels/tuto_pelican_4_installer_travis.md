Title: Déployer son blog statique Pelican en production
Date: 2018-11-16
Modified: 2018-11-16
Category: tutoriels
Tags: tutoriels
Slug: deployer-pelican-en-production
Lang: fr
Authors: Julien Nuellas
Summary: Découvrez comment déployer automatiquement votre blog statique Pelican avec Travis CI et GitHub Pages.

Maintenant que notre hébergement sur GitHub Pages est en place et que Pelican est correctement installé, il est désormais temps de s'attaquer au processus de déploiement.

Comme cet article correspond à la cinquième partie du tutoriel dédié à la création d'un blog statique, je me permets de rappeler la structure de ce dernier:

1. [Présentation du tutoriel et de ces objectifs]({filename}tuto_pelican_0_introduction.md)
2. [Un blog statique, c'est quoi et comment ça fonctionne?]({filename}tuto_pelican_1_whats_blog_statique.md)
3. [Mettre en place GitHub Pages pour l'hébergement d'un blog statique]({filename}tuto_pelican_2_githubpages_setup.md)
4. [Utiliser Pelican pour son blog statique]({filename}tuto_pelican_3_installer_pelican.md)
5. **Utiliser Travis pour automatiser le déploiement de son blog statique**
6. [Mettre en place un thème sur son blog statique Pelican]({filename}tuto_pelican_5_installer_theme.md)

Dans cet article, nous nous attacherons à configurer Travis CI afin que ce dernier déploie automatiquement le blog lorsqu'une pull request est faite sur la branche Master. 

**Travis CI** est un logiciel pour mettre en place de l'[intégration continue](https://fr.wikipedia.org/wiki/Int%C3%A9gration_continue). Il permet de compiler, tester et déployer un code source.

La mise en place se déroulera en cing principales étapes:

1. Mettre à jour le fichier publishconf.py
2. Nous allons activer Travis CI sur le repository Git Hub
3. Nous allons faire quelques petites modifications dans le fichier Makefile
4. Ensuite, nous intègrerons le fichier .travis.yml au sein du projet
5. Et enfin, nous vérifirons que tout fonctionne correctement

## Mettre à jour le fichier publishconf.py
---

Nous allons déployer notre site en production. De ce fait, il s'agit du fichier publishconf.py qui sera considéré dans le déploiement et non le fichier pelicanconf.py.

Regardons de plus près ce fichier:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'tutoriel-pelican.jn-blog.com'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""

```

Comme expliqué auparavant, le fichier reprend les configurations présentes dans le fichier pelicanconf.py et va surcharger ce dernier. Il va notamment activer automatiquement la génération des flux ATOM et changer la prise en charge des urls. Au lieu de se baser sur une approche relative, il va récupérer le nom de domaine indiqué dans la variable **SITEURL**
Il y a également des variables pour contenir les informations contenant la mise en place de Google Analytics et le système de commentaires via Disqus. Ces sujets pourront faire l'objet d'un autre article si cela vous intéresse. N'hésitez pas à le préciser dans les commentaires.

Pour le déploiement, la seule modification que nous allons apporter concerne la variable SITEURL. Nous avons en effet activer le protocole https dans github pages et il est important de le rappeler ici sinon cela risque de créer certains problèmes lors de la récupérations d'éléments au moment du chargement (notamment les fichiers statiques). Modifions donc la variable de cette façon:

```python
SITEURL = 'https://tutoriel-pelican.jn-blog.com'
```

Rien de plus à ajouter sur ce fichier. Nous pouvons donc passer à la suite.

## Activer Travis CI sur le repository Git Hub
---

Tout d'abord, si vous n'avez pas de compte [Travis CI](https://travis-ci.org/), il est temps d'en créer un. Vous pouvez utiliser votre compte Github pour la création. Cela aura pour effet de synchroniser automatiquement votre repository github avec votre compte.

Une fois le compte créé et synchronisé, il vous suffit d'identifier le nom du repository contenant votre blog et d'activer Travis CI

![activation de Travis sur le repository]({filename}/images/tuto-pelican-travis-activation-repo.png)

Et voilà, le travail est fait! Simple, Basique...

![lien gif simple](https://media.giphy.com/media/9Jcw5pUQlgQLe5NonJ/giphy.gif)

## Ajustement du fichier MakeFile
---

Comme expliqué dans le précédent article, le fichier Makefile généré lors de la création du projet permet de simplifier les actions réalisées sur ce dernier.

C'est ce fichier qui nous permet notamment de générer les fichiers html et de les servir sur un serveur local via les commandes ```make html && make serve```

Ce fichier contient également une commande permettant de publier sur github. Il s'agit de la commande ```make publish github``` et se trouve vers la fin du fichier Makefile:

```Makefile
github: publish
	ghp-import -m "Generate Pelican site" -b $(GITHUB_PAGES_BRANCH) $(OUTPUTDIR)
	git push origin $(GITHUB_PAGES_BRANCH)
```

Pour que cette commande fonctionne avec Travis CI, il va falloir y apporter quelques modifications.

### Autoriser Travis CI à déployer via un access token

Avant tout, pour que Travis soit en capacité de réaliser une action de déploiement sur le repository github, il va falloir lui associer un access token. La manière la plus simple de le faire est la suivante:

1. Il faut créer un token d'accès personnalisé sur Github. Voici un lien décrivant le processus à suivre: [https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/)

Lors de la création du token, n'oubliez pas de cocher la case *repo* si vous êtes sur un repository privé ou au moins *public repo* si vous êtes sur un repository public:
[https://docs.travis-ci.com/user/deployment/pages/#setting-the-github-token](https://docs.travis-ci.com/user/deployment/pages/#setting-the-github-token)

2. Une fois la clef obtenue:
    * Il suffit de retourner dans Travis CI dans la partie *Settings* du repository cible

    ![onglet Settings dans Travis CI]({filename}/images/tuto-pelican-travis-settings-repo.png)

    * Dans la section *Environment Variables*, il faut ensuite ajouter la variable **GITHUB_TOKEN** avec comme valeur le token qui vient d'être généré.

    ![onglet Settings dans Travis CI]({filename}/images/tuto-pelican-travis-github-token.png)

Il est désormais temps de modifier légèrement la commande make publish github.

### Modifier les actions de la commande make publish github

Voici les modifications à apporter. (J'ai conservé les commandes initiales en les ajoutant comme commentaires).

```Makefile
github: publish
	# ghp-import -m "Generate Pelican site" -b $(GITHUB_PAGES_BRANCH) $(OUTPUTDIR)
	# git push origin $(GITHUB_PAGES_BRANCH)
	ghp-import -n $(OUTPUTDIR)
	@git push -fq https://$(GITHUB_TOKEN)@github.com/JN-Blog/tutoriel-pelican.git master:gh-pages
```

Sans rentrer dans les détails, la commande va utiliser le module [ghp-import](http://docs.getpelican.com/en/stable/tips.html#publishing-to-github) pour automatiser le déploiement du site vers la branche gh-pages. Le push vers le repository github utilise le token d'accès que nous venons de créer. Il faudra adapter bien évidemment l'url github en fonction de votre repository github.

## Création du fichier .travis.yml
---

Le dernière étape consite à créer le fichier **.travis.yml** à la racine du répertoire qui contiendra l'ensemble des directives que Travis devra réaliser.

Voici les indications que doit contenir le fichier:

```yml
language: python
python:
  - "3.6" # la version de Python utilisée

branches:
  only:
    - master

install:
  - pip3 install -r requirements.txt
  - pip3 install ghp-import

script:
  - make publish github

deploy:
  provider: pages
  repo: JN-Blog/tutoriel-pelican # Le nom du repository utilisé
  target_branch: gh-pages
  skip_cleanup: true
  github_token: $GITHUB_TOKEN
  local_dir: output
  on:
    branch: master
```

Ce fichier va globalement indiquer à Travis:

* D'installer la version de Python utilisée
* De cibler uniquement la branche master de notre repository
* D'installer l'ensemble des éléments nécessaires (Pelican, Markdown, ghp-import)
* De lancer le script ```make publish github```
* De configurer les instructions de déploiement afin que le répertoire output soit poussé sur la branche gh-pages du repository (avec un clean en amont si cette branche contenait déjà un ancien répertoire)

## Déploiement de notre blog en production
---

Et voilà! tous les éléments sont mis en place pour déployer notre site en production.
Envoyons notre code à jour sur github dans notre branche source (une fois le commit enregistré)

```
git push origin source
```

Il est temps désormais de déployer notre blog en faisant notre première pull request.

![créer une pull request sur github]({filename}/images/tuto-pelican-travis-pull-request.png)

Une fois créée, avant de pouvoir confirmer le *merge*, Travis CI va lancer un test et valider (ou invalider) que le processus de déploiement est fonctionnel.

![lancement d'un test Travis lors d'une pull request sur github]({filename}/images/tuto-pelican-travis-pull-request-check.png)

Et si tout se passe bien (mais il n'y a pas de raison), un message de validation de test devrait apparaître une fois le test terminé permettant ainsi de confirmer le merge.

![lancement d'un test Travis lors d'une pull request sur github]({filename}/images/tuto-pelican-travis-pull-request-validated.png)

Et une fois confirmé et le merge réalisé, Travis CI va s'apercevoir que le code sur la branche master a été mis à jour et va lancer la procédure de déploiement tout seul comme un grand.

![lancement d'un test Travis lors d'une pull request sur github]({filename}/images/tuto-pelican-travis-deploy.png)

La magie opère enfin et le site est accessible à l'adresse de votre nom de domaine.

![lancement d'un test Travis lors d'une pull request sur github]({filename}/images/tuto-pelican-travis-production.png)

Elle est pas belle la vie? Cela demande un peu de configuration au départ je vous l'accorde mais désormais, une simple pull request vous permet de mettre à jour votre blog sur votre environnement de production avant d'avoir en amont vérifier que tout soit opérationnel.

Votre blog est désormais créé, hébergé et déployé! Il ne vous reste plus qu'à écrire vos articles.
Mais avant de terminer ce tutoriel, j'aimerais voir avec vous une dernière chose. En effet, nous n'avons pas encore parlé de l'apparence du blog. Pour le moment, le blog utilise le thème d'origine. Nous verrons donc dans le prochain article comment installer un autre thème:

[Installer un thème sur son blog Pelican]({filename}tuto_pelican_5_installer_theme.md)