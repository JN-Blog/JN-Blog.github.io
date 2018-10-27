Title: JN-Blog Tutoriel: mettre en place un blog statique avec Pelican
Date: 2018-10-26
Modified: 2018-10-26
Category: tutoriels
Tags: tutoriel, pelican, blog statique
Slug: tutoriel-creer-un-blog-statique
Authors: Julien Nuellas
Summary: Vous avez envie de créer un blog et vous êtes tenté par la solution du blog statique? Alors ce tutoriel est fait pour vous.

# Mettre en place un blog statique 

Quand on débute l'écriture d'un blog, il faut bien commencer par quelque part. Et quoi de plus logique que de débuter l'aventure de ce blog par un tutoriel expliquant la mise en place d'un blog statique lorsque la solution que l'on a choisie est justement un blog statique? 

![gif ça fait sens](https://media.giphy.com/media/d3mlE7uhX8KFgEmY/giphy.gif)

En effet, comme expliqué en présentation, l'objectif de ce blog est de pouvoir partager et échanger sur des sujets où chacun à acquis de l'expérience. 
Et c'est pourquoi je vous attend nombreux dans la section commentaire afin de pouvoir partager votre retour d'expérience sur votre propre mise en place d'un blog statique.
Et j'insiste sur le fait que je ne prétend pas avoir la solution ultime (existe-t-elle vraiment finalement?) mais une solution pertinente par rapport à des objectifs définis.

Alors justement, que va couvrir ce tutoriel?
L'objectif de ce dernier est de structurer les différentes étapes liées à la mise en place d'un blog statique et proposer un workflow facile et fiable dans le temps. Pour cela, je vais vous proposer de travailler avec trois principaux outils:
* [Pelican](http://docs.getpelican.com/en/stable/) comme générateur de sites statiques
* [GitHub Pages](https://pages.github.com/) pour l'hébergement
* [Travis CI](https://travis-ci.org/) pour automatiser le déploiement

Le premier avantage à tout ça, vous pouvez créer un blog **gratuitement** sans dépenser un seul euro. Elle est pas belle la vie? A la limite, la seule dépense qui peut vous intéresser est l'achat de votre propre nom de domaine (ce qui représente environ 15 euros par an).

Alors, prêt pour l'aventure?

Tout au long de ce tutoriel, nous allons créer pas à pas un blog. Ce blog va s'appeler **Blog Pelican - un blog statique, un blog magique** et est accessible à l'adresse suivante: https://tutoriel-pelican.jn-blog.com.
Vous pouvez d'ors et déjà vous y rendre, cela vous permettra de voir ce à quoi nous allons aboutir à la fin du tutoriel.

Mais avant de rentrer directement dans le vif du sujet, voici comment on va procéder. Ce tutoriel comportera différents articles selon le schéma suivant:

## 1. [Un blog statique, c'est quoi? Et pourquoi choisir cette solution?]({filename}tuto_pelican_1_whats_blog_statique.md)

Effectivement, on ne va pas rentrer dans le dur avant de comprendre ce qu'est un site statique et de savoir quels sont ces avantages et ces inconvénients. Ca serait dommage de vous rendre compte à la fin, après avoir tout mis en place que finalement, le blog statique n'est pas la situation idéale dans votre cas.
J'en profiterai également pour vous présenter **Pelican** plus particulièrement car il s'agit de ce générateur de sites statiques qui sera utilisé dans ce tutoriel.

## 2. [Mettre en place son repository GitHub Pages]({filename}tuto_pelican_2_githubpages_setup.md)

La seconde partie de ce tutoriel évoquera la mise en place du repository **GitHub Pages**. Je vous présenterai:
* Ce qu'est **GitHub Pages** en quelques lignes.
* La logique de fonctionnement que nous allons utiliser pour gérer le blog
* La configuration du repository.
* La mise en place d'un nom de domaine.

## 3. [Installer Pelican]({filename}tuto_pelican_3_installer_pelican.md)

On va ensuite rentrer dans le vif du sujet et installer Pelican dans notre environnement de travail. On en profiterai pour mettre en place les configurations basiques que j'ai jugé pertinente. Il ne s'agit pas encore une fois de la seul façon de procéder et vous découvrirez avec le temps que Pelican offre de nombreuses possibilités en terme de configuration. L'idée étant de partir d'une base simple et fonctionnelle.
On écrira même un premier article test que nous déploierons en local afin de vérifier que tout fonctionne correctement.

## 4. [Mise en place de Travis et du workflow de déploiement]({filename}tuto_pelican_4_installer_travis.md)

L'étape suivante consistera à mettre en place le déploiement automatisé avec Travis. L'objectif étant qu'à chaque fois que vous écrivez un nouvel article et que vous souhaitez publier, vous n'ayez qu'à pousser votre projet sur GitHub Pages, puis historiser la publication via une pull request(pour conserver un certain historique). Travis se chargera de tester le projet et déployer la nouvelle version du blog si tout se passe bien.

## 5. [Mettre en place un thème Pelican]({filename}tuto_pelican_5_installer_theme.md)

A ce stade, le blog sera fonctionnel et la plus grande partie du travail aura été effectué. Il ne restera plus qu'à styliser un peu le blog. Pour cela, nous utiliserons l'un des nombreux thèmes proposés. Une fois installé, vous aurez un blog clef en main et vous pourrez écrire tous les posts que vous souhaitez sur votre propre blog construit par vos soins. Elle est pas belle la vie?

Bien sûr, ce tutoriel va s'enrichir avec le temps et de nouveaux chapitres verront le jour. Vous découvrirez ainsi comment mettre en place un système de commentaires, ou encore mettre en place Google Analytics afin de suivre les performances et la popularité de votre blog. Et puis, finalement ce tutoriel évoluera également en fonction de vos questions et besoin. Alors n'hésitez pas à écrire des commentaires afin d'avoir vos retours sur ce dernier. Cela me permettra d'affiner le contenu suite à votre retour d'expérience.

C'est parti? Allez, c'est par ici alors:

Un blog statique? C'est quoi et ca sert à quoi?
