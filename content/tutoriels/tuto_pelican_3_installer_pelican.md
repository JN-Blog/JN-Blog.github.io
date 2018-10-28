Title: JN-Blog: Installer et configurer Pelican pour son blog statique
Date: 2018-10-28
Modified: 2018-10-28
Category: tutoriels
Tags: tutoriel, pelican, blog statique
Slug: installer-pelican-pour-un-blog-statique
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

## Installer Python et créer son environnement virtuel

## Installer Pelican et Markdown

## Créer un projet Pelican

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