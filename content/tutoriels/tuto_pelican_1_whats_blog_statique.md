Title: C'est quoi un blog statique? Comment ca fonctionne?
Date: 2018-10-26
Modified: 2018-10-26
Category: tutoriels
Tags: tutoriels, pelican, blog statique
Slug: explication-blog-statique
Lang: fr
Authors: Julien Nuellas
Summary: Un blog statique, c'est quoi et comment ça marche? Découvrez le concept de blog statique, ses avantages et ses inconvénients ainsi que son fonctionnement.

Un blog statique? Mais qu'est-ce que tu me racontes? Si je veux un blog, je me tourne vers Wordpress et puis on en parle plus.
Effectivement, ce n'est pas une mauvaise solution. Un blog statique n'est pas la nouvelle génération de blogs qu'il faut prendre à tout pris, mais elle a le mérite d'exister et de présenter notamment de nombreux avantages, et également des inconvénients. Dans tous les cas, comprendre ce qu'est un blog statique (et un site statique plus globalement) ne peut vous apportez qu'un choix plus éclairé quant à la solution que vous choisirez pour mettre en place votre blog.

Comme ce post est le premier d'un tutoriel dédié à la création d'un blog statique, je me permets de rappeler le plan du tutoriel:

1. [Présentation du tutoriel et de ces objectifs]({filename}tuto_pelican_0_introduction.md)
2. **Un blog statique, c'est quoi et comment ça fonctionne?**
3. [Mettre en place GitHub Pages pour l'hébergement d'un blog statique]({filename}tuto_pelican_2_githubpages_setup.md)
4. [Utiliser Pelican pour son blog statique]({filename}tuto_pelican_3_installer_pelican.md)
5. [Utiliser Travis pour automatiser le déploiement de son blog statique]({filename}tuto_pelican_4_installer_travis.md)
6. [Mettre en place un thème sur son blog statique Pelican]({filename}tuto_pelican_5_installer_theme.md)

Au travers cet article, il s'gira donc de définir le concept de blog statique puis d'en présenter ces avantages et ces inconvénients. Ensuite, il décrira de façon macro comment un blog statique fonctionne et s'attardera sur le générateur de sites statiques **Pelican**, car c'est celui-ci que nous utiliserons dans le tutoriel.

Et si vous avez des remarques, suggestions ou compléments à la fin de l'article, n'hésitez pas à laisser un commentaire!

Maintenant que tout est plus clair, rentrons dans le vif du sujet.

## Pour commencer, c'est quoi un blog statique?

Un blog (ou un site d'ailleurs) statique n'est constitué uniquement que de fichiers entièrement statique (merci captain Obious!)

![thanks captain obvious gif](https://media.giphy.com/media/3o7abonV6K9irq7kaY/giphy.gif)

Et oui, faut pas aller chercher très loin... En effet, plus de langages serveurs (php, python, ...), plus de bases de données ou autres scripts exécutés sur le serveur, tout est 100% statique et délivré par un serveur web.

Ainsi, le blog ne sera constitué que de fichiers html, d'images, de css et éventuellement de javascript. 

Alors super, maintenant qu'on sait ce que c'est, en quoi c'est intéressant de construire son blog en utilisant cette approche?

## Les avantages d'un blog statique

Je vois personnellement trois gros avantages:

### La rapidité

En effet, le serveur n'a plus besoin de récupérer des informations dans une base de données pour construire les pages. Il ne fait rien d'autres que délivrer des pages HTML et les médias qui lui sont associés.

### La sécurité

L'autre énorme avantage d'un site statique réside dans la sécurité. Il n'y a quasiment aucuns risques de se faire pirater (injection SQL, injection de fichiers, ...) et aucun script n'est réalisé côté serveur. Ce ne sont que des fichiers statiques qui sont délivrés au navigateur.
Il n'existe aucun risque de se faire planter son blog après 3 ans d'existences et de tout perdre bêtement.

### Souplesse

Enfin, le dernier avantage non négligeable concerne la souplesse de ce type de blog.
Le fait d'avoir un site statique rend l'**hébergement** beaucoup plus simple et moins cher. Dans ce tuto, il ne nous coûtera pas 1 seul centime! Le seul coût concernera l'achat du nom de domaine.
De plus, un site statique offre une très bonne capacité à tenir la **charge**. Je ne l'ai peut être pas assez dit, mais un site statique n'est composé que de fichiers statiques... Oui, mais du coup, et je me répète encore, pas de scripts exécutés sur le serveurs et cela permet d'économiser des ressources serveurs importantes!

Pour terminer avec la souplesse d'un blog statique (si je ne vous ai pas encore convaincu), la sauvegarde et la restauration se font facilement. Un simple archivage de fichiers suffit et il n'est pas nécessaire de faire des exports ou imports de base de données qui peuvent être des tâches parfois délicates.

Ouahhhh, c'est super un site statique. Pourquoi tout le monde ne l'utilise pas alors? Et bien, comme toute solution, il n'y a pas forcément que des avantages.

## Les inconvénients d'un blog statique

Effectivement, un blog statique présente certains inconvénients qu'il ne faut pas négliger.

### Prise en main

Premièrement, la prise en main n'est pas aussi facile qu'un CMS de type Wordpress. En effet, il n'y a pas d'interface d'administration user-friendly de type [wysiwyg](https://fr.wikipedia.org/wiki/What_you_see_is_what_you_get) (WhatYouSeeIsWhatYouGet) qui permet de tous gérer en quelques clics. Il ne faut pas avoir peur de faire quelques lignes de commande (même si cela n'est pas compliqué en soit et ne doit pas vous effrayer plus que ça).

### Et mes commentaires?

En effet, le fait de ne pas avoir de base données pour un blog limite les intéractions avec les lecteurs, ce qui est profondément pénalisant lorsque l'on considère qu'un blog est avant tout un outil d'échanges et de partage.
Cependant, il est possible de passer par des systèmes externes pour la gestion de commentaires qui s'interface très bien avec les moteurs de site statique. Nous apprendrons à en mettre un en place dans ce tutoriel. 
Cependant, le fait de faire appel à un outil externe crée une certaine dépendance envers celui-ci et peut s'avérer impactant (si le service tombe par exemple).

### Comment je fais pour être contacté?

Il est également plus difficile de créer un espace de contact. Cela peut s'avérer être un frein lorsque c'est l'un de ces objectifs principaux.
Cela n'est cependant pas impossible et des méthodes existe pour mettre en place cela.

Alors convaincu et prêt à se lancer dans la mise en place d'un blog statique? Suivez le guide et approfondissons un peu en décrivant brièvement comment cela fonctionne.

## Comment met-on ça en place?

On va se servir d'un générateur de site statique.

### C'est quoi un générateur de sites statiques?

Et bien comme son nom l'indique, ça permet de gérer des fichiers statiques. Il va permettre de générer des menus, mettre en place de la pagination, etc... un vrai site web finalement de façon simple, rapide et à moindre coût.

La particularité principale d'un générateur de sites statiques réside dans son moteur de templates. Pour faire simple, cela permet de créer des gabarits (ou structure) de pages web dans lequel va être diffusé votre contenu écrit dans un format Markdown la plupart du temps.
Ensuite lorsque vous souhaitez publier/ mettre à jour votre site suite à la création d'un nouveau contenu, le générateur va créer les fichiers html qui composeront votre site.

Il existe une multitude de générateurs de sites statiques. En voici une liste non exhaustive:

* [Jekyll](https://jekyllrb.com/) (écrit en Ruby)
* [Pelican](http://docs.getpelican.com/en/stable/) (écrit en Python)
* [Hugo](https://gohugo.io/) (écrit en Go)
* [Hyde](http://ringce.com/hyde/) (écrit en Python)
* [Octopress](http://octopress.org/) (écrit en Ruby)
* [Middleman](https://middlemanapp.com/) (écrit en Ruby)
...

Pour ce tutoriel, il s'agira de mettre en place un blog statique en utilisant **Pelican**. Ce n'est pas parce que c'est le meilleur mais parce que c'est celui-ci que j'utilise car il est écrit en Python et qu'il utilise le moteur de template [Jinja2](http://jinja.pocoo.org/). Je trouve notamment sa documentation complète et claire ce qui est un point non négligeable.

Mais vous pourriez tout aussi bien utiliser un autre outil comme **Jekyll** par exemple qui est également très populaire, notamment pour sa simplicité d'intégration avec GitHub Pages.

## Présentation de Pelican

Pelican est donc un logiciel écrit en Python sous licence AGPL. Il permet de générer des sites statiques (non??? Vraiment???) et offre notamment dans sa version 3 de nombreuses fonctionnalités:
* Il permet de rédiger des articles de blogs et des pages aux formats [reStructuredText](https://fr.wikipedia.org/wiki/ReStructuredText) ou [Markdown](https://fr.wikipedia.org/wiki/Markdown) en utilisant l'éditeur de texte de votre choix
* Il permet de gérer les thèmes par l'intermédiaire du système de template Jinja2
* Il inclut une interface de ligne de commande ([CLI](https://fr.wikipedia.org/wiki/CLI)) permettant de générer facilement votre site.
* Permet de publier des articles dans plusieurs langues
* Permet d'intégrer des outils externes comme Twitter, Google Analytics, etc...
* Génère des flux Atom et RSS
* ...

Il s'agit donc d'un outil complet avec lequel on va pouvoir s'amuser.

Afin de résumer un peu son fonctionnement et de ce qui a été dit dans les deux dernières parties, voici un schéma très simple résumant la façon dont Pelican génére un site statique:

![blog_static_fonctionnement]({filename}/images/blog_statique_fonctionnement.jpg)

Le répertoire source contient deux principaux répertoire (nous reviendrons sur les autres fichiers par la suite):
* Un répertoire **theme** qui contient l'ensemble des éléments propres aux thèmes sélectionné. Il s'agit principalement des templates (ou gabarits) des différentes pages ainsi que les fichiers statics (css, javacript, images, ...)
* Un répertoire **content** qui contient l'ensemble du contenu dans des fichiers au format .md (Markdown) ou .rst (reStructuredText).

Au moment de la génération du site par Pelican, ce dernier crée un répertoire output contenant l'ensemble des fichiers html du site ainsi qu'un dossier pour les statics. Et c'est ce répertoire qui sera hébergé sur un serveur web.

Maintenant que vous en savez un peu plus sur ce qu'est un blog statique (ces avantages, ces inconvénients et son fonctionnement global), j'espère que vous avez hâte de passer à l'action et de vous salir un peu les mains car le prochain article de ce tutoriel va consister à mettre en place la structure qui va héberger et délivrer notre blog statique.

Si vous êtes prêt, il est temps de passer à la partie suivante de ce tutoriel:

[Tutoriel pour apprendre à héberger son site statique avec GitHub Pages]({filename}tuto_pelican_2_githubpages_setup.md)