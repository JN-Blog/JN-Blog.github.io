Title: Utiliser GitHub Pages pour héberger son blog statique
Date: 2018-10-26
Modified: 2018-10-26
Category: tutoriels
Tags: tutoriels
Slug: heberger-un-blog-statique-avec-github-pages
Lang: fr
Authors: Julien Nuellas
Summary: Découvrez toutes les étapes pour configurer GitHub Pages et héberger votre blog statique facilement. Ne soyez pas effrayé, ce n'est pas très compliqué!

Maintenant que nous avons découvert ce qu'est un [blog statique]({filename}tuto_pelican_1_whats_blog_statique.md) et comment cela fonctionne, il est temps de commencer à se retrousser les manches.

Avant d'aller plus loin, puisque cet article est le troisième d'un tutoriel dédié à la création d'un blog statique, je me permets de rappeler le plan de ce dernier:

1. [Présentation du tutoriel et de ces objectifs]({filename}tuto_pelican_0_introduction.md)
2. [Un blog statique, c'est quoi et comment ça fonctionne?]({filename}tuto_pelican_1_whats_blog_statique.md)
3. **Mettre en place GitHub Pages pour l'hébergement d'un blog statique**
4. [Utiliser Pelican pour son blog statique]({filename}tuto_pelican_3_installer_pelican.md)
5. [Utiliser Travis pour automatiser le déploiement de son blog statique]({filename}tuto_pelican_4_installer_travis.md)
6. [Mettre en place un thème sur son blog statique Pelican]({filename}tuto_pelican_5_installer_theme.md)

Pour rappel, ce tutoriel se base sur la construction d'un blog statique que vous pouvez déjà découvrir à l'adresse suivante: https://www.tutoriel-pelican.jn-blog.com

Dans cet article, nous découvrirons ce qu'est GitHub Pages puisque nous allons l'utiliser au sein de notre projet. Ensuite, nous le configurerons complètement pour qu'il puisse accueillir la structure de notre blog statique.

Commençons donc par présenter GitHub Pages.

## GitHub Pages: qu'est-ce que c'est?
---

[GitHub Pages](https://pages.github.com/) est un service d'hébergement de sites statiques conçu pour fonctionner à partir de l'un de vos repository GitHub. Il a été conçu dans l'idée de pouvoir facilement héberger et rendre accessible des projets qu'une personne ou une organisation souhaite rendre disponible (site vitrine, documentation, prototype, blog, etc...)

Je pense qu'à la vue de cette explication, cette solution paraît parfaite pour héberger notre blog vous ne pensez pas?

Avant d'aller plus loin, il est judicieux que vous ayez une compréhension basique de ce que sont Git et GitHub. Pour ceux qui connaissent déjà, ne serait-ce que le fonctionnement basique (pas besoin d'être un expert), vous pouvez directement passer à la section suivante.

## Quelques mots sur Git et GitHub
---

GitHub est un service web qui permet d'héberger et gérer le développement de logiciels. Pour cela, il utilise le [logiciel de gestion de versions Git](https://fr.wikipedia.org/wiki/Logiciel_de_gestion_de_versions).

Ne soyez pas effrayé par ces concepts qui peuvent vous paraître obscure. Pour faire simple, Git est l'un des logiciels (parmi d'autres) qui permet à des développeurs de collaborer de manière intelligente et structurée sur un même projet de développement. C'est un outil incontournable et extrêmement puissant pour toute personne travaillant sur des projets de développement, qu'ils soient importants ou petits.

Et il est très pertinent pour la suite du tutoriel d'avoir une compréhension basique de son fonctionnement. Et si vous avez ne serait-ce qu'un minimum d'intérêt pour le développement (ce qui semble être le cas si la mise en place d'un blog statique vous intéresse), vous ne pouvez pas ignorer plus longtemps ce type d'outils. Croyez-moi, après la première utilisation, vous ne pourrez plus vous en passer.

Si vous êtes intéressé, je vous recommande ce cours Openclassrooms: [Gérez votre code avec Git et GitHub](https://openclassrooms.com/fr/courses/2342361-gerez-votre-code-avec-git-et-github) qui vous apportera de manière très ludique les fondamentaux pour utiliser correctement Git. C'est un cours qui ne dure pas longtemps et qui est très bien construit. Avec ce cours, vous aurez largement les connaissances pour suivre la suite du tutoriel. Et vraiment, ne soyez pas effrayé par la difficulté de l'exercice, c'est très simple et le temps investi à apprendre à utiliser ce type d'outils sera largement rentabilisé par la suite.

Ca y est? Vous avez installé git sur votre PC, vous avez ouvert un compte sur GitHub, créé votre premier repository et joué avec quelques branches? Alors, vous êtes prêt pour la suite du tutoriel!

## Présentation de la logique de fonctionnement
---

Voici donc la logique de fonctionnement que je vous propose.
Nous allons travailler avec un repository et trois branches différentes:

* source
* master
* gh-pages

La branche source sera celle où la *vie* va avoir lieu. C'est sur cette dernière que nous travaillerons en local avant de pousser le code sur GitHub.
Ensuite, lorsque nous souhaiterons déployer une nouvelle version du site suite à un nouvel article par exemple, nous ferons une pull request vers la branche master. Durant cette pull request, Travis réalisera un test automatique afin de savoir s'il n'y a pas d'erreurs qui se sont glissées dans le code par rapport à la précédente version. 
Si le test est positif, alors nous confirmons le merge de la branche source vers la branche master. Une fois la branche master à jour, Travis intervient encore une fois pour générer automatiquement le site et le déployer sur la branche gh-pages. Elle est pas belle la vie?

Voici un petit schéma pour illustrer mes propos:

![logique de déploiement]({filename}/images/tuto-pelican-methodo-deploiement.png)

Encore une fois, ce n'est pas la seule logique de fonctionnement. J'ai vu certaines personnes travailler avec deux repositories par exemple: un pour travailler et concevoir le blog et l'autre uniquement pour le déploiement, ce qui est une solution judicieuse également. J'ai simplement peur d'ajouter un risque de confusion supplémentaire en travaillant avec deux repositories.

D'autres personnes intervertissent la branche gh-pages et master dans la logique de fonctionnement. Ainsi, c'est la branche master sur laquelle GitHub Pages se base pour le déploiement et la branche gh-pages ou un autre nom qui contient la version du code à jour. C'est d'autant plus intéressant que si vous n'utilisez pas de nom de domaine personnalisé et que vous avez nommé votre repository USERNAME.github.io, vous n'avez pas la possibilité de choisir une autre branche que master comme origine de déploiement.

Alors pourquoi intervertir les deux me demanderiez-vous? Et bien principalement pour une convention de nommage. La branche master est la plupart du temps la branche par défaut, celle qui contient le code complet et stable et que l'on voit directement lorsque l'on arrive sur un repository. Cela peut paraître absurde mais si vous créez un blog avec plusieurs contributeurs et auteurs qui ont l'habitude - tellement l'habitude que cela relève du domaine de l'inconcsient - de fonctionner ainsi, cela risque de provoquer des erreurs comme pousser un code non testé sur la branche qui sert au déploiement. Et boom, le site est cassé...

Maintenant que la logique est expliquée, créons notre repository.

## Créer son repository GitHub Pages
---

Nous allons voir dans cette partie comment configurer GitHub Pages et plus globalement son environnement de travail où l'on installera par la suite Pelican.

### Création du repository

Tout d'abord et en toute logique, nous allons créer notre repository sur GitHub.
Pour ce projet, nous nommerons le repository tutoriel-pelican et nous allons l'initialiser avec un README.md.

![creation d'un repository github]({filename}/images/tuto-pelican-githubpages-create.png)

### Création de la branche gh-pages

Une fois le repository créé, il faut désormais créer la branche gh-pages en complément de la branche master initialement créée.
Pour cela, rien de plus simple, il suffit:

* De cliquer sur le bouton indiquant la branche sélectionnée
* Dans le champ de recherche, écrire *gh-pages*
* Cliquer ensuite le bouton indiqué pour créer la branche gh-pages à partir de la branche master

![ajout d'une branche au sein d'un repository github]({filename}/images/tuto-pelican-ghpages-branch-creation.png)

### Vérifier les informations de configurations de GitHub Pages

Une fois la branche gh-pages créée, rendez-vous dans la partie **settings** afin de vérifier la configuration initiale de GitHub Pages.
Pour cela, il suffit de cliquer sur l'onglet settings.

![aller dans l'onglet configuration d'un reposotiry github pages]({filename}/images/tuto-pelican-settings-button.png)

Une fois arrivé, dans la partie configuration, il suffit de descendre un peu afin d'arriver sur la partie GitHub Pages.

![GitHub Pages configuration]({filename}/images/tuto-pelican-ghpages-settings-global.png)

Comme vous pouvez le constater, GitHub Pages est déjà activé et la branche associée à l'hébergement est déjà la branche gh-pages. Cette configuration initiale s'est automatiquement mise en place lorsque nous avons créé la branche gh-pages. En effet, GitHub a directement compris que nous souhaitions utiliser GitHub Pages au sein de ce repository afin d'héberger un site statique et il a directement sélectionné la branche gh-pages. Comme quoi, respecter les conventions n'est pas totalement dénué d'intérêt!

Cependant, si cela ne s'est pas créé automatiquement, il suffit juste de sélectionner la branche gh-pages et d'enregistrer ce choix.

Et voilà, désormais tout site hébergé poussé au sein de cette branche sera désormais accessible via l'url indiquée. Dans notre cas, il s'agit de l'url **https://jn-blog.github.io/tutoriel-pelican/**

Cela ne fait pas très vendeur vous ne pensez pas? un peu difficile à retenir, et on a du mal à identifier le thème et l'objectif du site au travers de cette url. 
A la limite, nous aurions pu un peu mieux faire si nous avions nommé notre repository JN-Blog/JN-Blog.github.io. En effet, l'url aurait été **https://jn-blog.github.io**. Cela permet d'avoir une url qui ne fonctionne pas avec un répertoire mais cela implique d'autres problèmes:

1. En effet, jn-blog c'est parlant pour le blog que vous lisez actuellement car c'est son nom, mais on ne retrouve pas le thème du blog qui consiste à proposer des tutoriels autour de Pelican. Il aurait donc fallu créer une nouvelle organisation qui s'appellerait tutoriel-pelican et créer un repository tutoriel-pelican.github.io. On aurait ainsi eu tutoriel-pelican/tutoriel-pelican.github.io et le site aurait été accessible à l'adresse https://tutoriel-pelican.github.io. Cela devient plus parlant mais on n'est toujours pas sur un nom facile à retenir et à écrire.
2. L'autre point négatif consiste au fait qu'en adoptant ce choix, seule la branche master du repository peut servir d'hébergement. Et il n'est donc pas possible d'utiliser la branche gh-pages pour cela, ce qui est un peu problématique (pour moi en tout cas) car cela ne permet pas de respecter les conventions de nommage.

Donc mon conseil, mais encore une fois, ce n'est que le mien - et je ne prétends pas détenir la vérité absolue -, c'est de choisir cette option si vous n'avez pas prévu de mettre en place un nom de domaine personnalisé. En effet, dans ce cadre-là, je pense qu'il est plus judicieux d'avoir un site accessible à l'adresse ORGANISATION.github.io que ORGANISATION.github.io/NOM_REPOSITORY.

Mais bon, si vous désirez créer votre propre blog, il y a tout de même de forte chance que vous ayez envie de choisir le nom de domaine de ce dernier. Et c'est ce que nous allons voir dans la partie suivante.

### Mise en place d'un domaine personnalisé

Maintenant que notre repository est créé et que GitHub Pages est mis en place, la prochaine étape consiste à associer notre nom de domaine sur cet hébergement et pour cela il va falloir faire un enregistrement CNAME. 

Si vous n'êtes pas familier avec ce terme, sachez juste qu'un enregistrement CNAME permet de faire pointer un nom de domaine vers un autre nom de domaine hôte. C'est un peu comme les adresses postales de type CEDEX. Vous allez envoyer un chèque à votre Banque via une adresse Paris CEDEX par exemple. Mais finalement, cette adresse sera redirigée vers le siège social situé dans une autre ville comme Levallois-Perret. Pour revenir au monde du digital, si vous souhaitez que votre blog soit accessible à l'adresse www.mon-blog.com et que votre adresse github pages soit username.github.io/mon-blog, il va falloir faire un enregistrement CNAME pour que votre domaine www.mon-blog.com soit redirigé vers l'adresse username.github.io/mon-blog. 

Et pour en revenir à notre projet de blog tutoriel-pelican, nous allons faire en sorte que le domaine tutoriel-pelican.jn-blog.com redirige vers jn-blog.github.io/tutoriel-pelican. Pourquoi tutoriel-pelican.jn-blog.com? Parce que je suis déjà propriétaire du domaine jn-blog.com et que travailler avec un sous-domaine comme celui-ci me parait pertinent. Mais j'aurai pu également acheter le domaine tutoriel-pelican.com et faire en sorte que ce soit www.tutoriel-pelican.com qui redirige vers jn-blog.github.io/tutoriel-pelican. L'opération reste la même au final.

Cette opération se fait auprès de votre fournisseur DNS. Les interfaces sont différentes mais la plupart du temps, l'opération est bien cadrée et il suffit d'indiquer au travers d'un formulaire son sous-domaine et le nom de domaine hôte.

Une commande CNAME ressemble à ça:
```
NOM_DOMAINE IN CNAME NOM_HOTE
```

Dans notre cas, on aura:
```
tutoriel-pelican IN CNAME jn-blog.gituhb.io.
```

Une fois cela fait, il va falloir un peu patienter car l'opération peut prendre quelques heures à être propagée.

Pour terminer la configuration, rien de plus simple. Il suffit juste de retourner dans les settings de votre repository GitHub et ajouter votre domaine à l'endroit indiqué. Je vous recommande également d'activer le protocole https. Cela vous apporte un niveau de sécurité supplémentaire et les domaines accessibles en https sont favorisés en termes de référencement naturel. Dans la même logique, cette activation demande la mise en place d'un certificat SSL du côté de GitHub et cela peut demander un peu de temps.

![configuration github pages terminés]({filename}/images/tuto-pelican-settings-global-done.png)

Notre configuration de GitHub Pages est désormais terminée! Notre repository est prêt à accueillir notre blog ainsi qu'à le servir sur notre domaine personnalisé.
Nous allons dans la prochaine étape installer notre blog et mettre en place ses configurations initiales:

[Mettre en place Pelican pour son blog statique]({filename}tuto_pelican_3_installer_pelican.md)