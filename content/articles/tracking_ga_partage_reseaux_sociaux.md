Title: Challenge: Mesurer l'engagement de son contenu via le volume de partage sur les réseaux sociaux grâce à Google Analytics
Date: 2018-12-19
Modified: 2018-12-22
Category: articles
Tags: challenge
Slug: tracking_partage_reseaux_sociaux_avec_google_analytics
Lang: fr
Authors: Julien Nuellas
Cover: /images/img_summary_production_par_petits_lots.jpg
Summary: Lorsque l'on souhaite mesurer l'engagement des utilisateurs envers son contenu, il est important d'analyser le volume de partage de ce dernier sur les réseaux sociaux. Cet article propose une façon simple et flexible de remonter cette donnée sur Google Analytics

J'adore résoudre les problèmes! C'est pourquoi j'ai envie à travers ce blog de me lancer des challenges. Je trouve l'approche intéressante pour plusieurs raisons:
1. Cela permet de partir d'un sujet concret
2. Cela permet de débattre!

En effet, pour un même problème, il y aura forcément plusieurs solutions. Cela permet donc de prendre un parti pris au travers de l'exercice et échanger ensemble selon votre propre approche également.

Pour ce challenge, je vous propose de partir du contexte suivant:

Charlie est un voyagiste qui propose des itinéraires éco-responsables uniquement en Asie du Sud Est. Au lancement de son activité, il a créé un blog afin de pouvoir partager sa passion sur cette région, véhiculer ses valeurs et construire une communauté autour de tout ça.

Pour mesurer son activité et l'engagement de ses lecteurs envers son contenu, il installé le code de suivi de Google Analytics qui me permet notamment de visualiser la durée par session, le nombre de pages vues par session, le taux de rebond, etc...
Mais il aimerait également visualiser l'engagement de ses lecteurs via leur volonté de partager sur les réseaux sociaux un contenu qui les a intéressé. Au delà de la notion liée à l'intérêt porté par le lecteur sur le contenu, il y a également la notion de viralité qui rentre en jeu dans l'action de partage.

**Le défi lancé au travers de cet article est donc de proposer une solution (parmi tant d'autres) pour évaluer l'engagement des lecteurs de ce blog via le partage du contenu sur les réseaux sociaux.**

Avant d'aller plus loin, voyons ensemble quelques contraintes supplémentaires à laquelle la solution doit faire face.

# La solution doit respecter certaines contraintes

Afin de répondre à ce challenge, je me suis fixé quelques contraintes supplémentaires. En effet, le sujet étant large et digne d'intérêt pour plusieurs personnes - que ce soit quelqu'un ayant un blog personnel et qui souhaite évaluer la pertinence de son contenu, ou alors un professionnel s'étant lancé dans la production de contenu car cela fait partie de sa stratégie marketing -, j'ai pour objectif de proposer une solution la plus simple et la plus adaptable possible. Ainsi, la solution devra:

* Pouvoir s'intégrer sur tous les types d'architecture possible à partir du moment où un code de suivi Google Analytics a été implémenté sur le site.
* Minimiser le paramétrage sur Google Analytics. Utiliser les rapports existants le plus possible
* Proposer un script le plus facilement adaptable en fonction de l'implémentation des boutons de partage sur votre site.

Maintenant que tout est clair et défini, intéressons nous plus en détail aux objectifs analytiques liés au tracking de ces actions de partage.

# Concrètement, comment j'évalue l'engagement de mes lecteurs via le partage sur les réseaux sociaux?

C'est effectivement une question digne d'intérêt. Evaluer l'engagement et la viralité de mon contenu via le partage sur les réseaux sociaux, c'est bien mais concrètement, quelles sont les questions sous-jacente?

## Quel est le volume de partage de mon contenu sur les réseaux sociaux sur une période donnée?

Tout d'abord, Charlie a envie d'évaluer la pertinence de son contenu en général suivant la tendance globale de partage de ce dernier sur les réseaux sociaux. Cela lui donnera notamment une évolution sur le long terme et permettra d'évaluer cette tendance en fonction des actions prises.

## Quels sont les réseaux sociaux les plus utilisés pour partager mon contenu?

Un autre point intéressant, Charlie a envie de connaître quelles sont les plateformes priorisées chez ses lecteurs. Cela lui permettra notamment d'adapter son contenu en conséquence et de prioriser sa communication sur les plateformes les plus utilisées par sa communauté.

## Quels sont les contenus les plus partagés sur les réseaux sociaux sur une période donnée?

Ensuite, Charlie a bien évidemment besoin de visualiser le degré d'engagement de ses lecteurs via le partage sur les réseaux sociaux par article et type de contenu. Cela lui permettra notamment d'identifier quel type de contenu intéresse le plus les lecteurs et a le plus de chance d'être viral.

# Comment répond-on à ces question dans Google Analytics?

Google Analytics propose quelques rapports déjà construits permettant de répondre à ces questions. Et comme l'une de mes contraintes consiste à minimiser les paramétrages sur la plateforme, la solution s'attachera à alimenter ce dernier et ne demandera pas la création d'un rapport personnalisé.

## Les rapports Evènements de Google Analytics

Au sein de la section Comportement, Google Analytics propose une série de rapports sur les **évènements**. 

![rapports evenements google analytics]({filename}/images/trackin_ga_share_rapport_event_menu.png)

Un évènement correspond à des actions uniques liées à un contenu et qui ne demande pas le chargement d'une nouvelle page. Ainsi, le partage d'un article constitue bien un évènement.

Pour ce challenge, les rapports qui vont nous intéresser seront les rapports:

* Comportement > Evenements > Principaux événements
* Comportement > Evenements > Pages

### Le rapport Principaux évènement

Sans trop rentrer dans les détails, ce rapport permet d'évaluer les performances de vos évènements selon 3 dimensons principales:

* Catégorie d'évènement
* Action d'évènement
* Libellé d'évènement

Pour ce challenge, voici ce que je vous propose d'associer en face de ces 3 dimensions:

* Catégorie d'évènement = **"engagement"**. Cela permettra de regrouper tous les évènements d'engagement s'il en existe d'autres (par exemple, l'écriture d'un commentaire). Il s'agit de plus d'une catégorie par défaut.
* Action d'évènement = **"share"**. Cela permettra de regrouper tous vos évènements d'actions de partage au sein d'un même endroit et de les différencier de vos autres évènements d'engagement. Il s'agit également d'une action par défaut.
* Libellé d'évènement = **nom du réseau social**. Cette dimension vous permettra de différencier vos évènements en fonction de chaque réseau social.

Dans notre cas, en partant du principe que le partage sur les réseaux sociaux constituent votre seul évènement d'engagement, il pourrait être intéressant par exemple d'utiliser ce rapport avec comme dimension principale le libellé d'évènement et comme dimension secondaire les pages.
Cela vous permettra d'identifier par réseau social, les articles les plus partagés.

### Le rapport évènements par page

Ce rapport propose de mesurer la performance de vos évènements avex comme dimension principale la pages (dans notre cas, l'article). Si vous ajoutez comme dimension secondaire le libellé d'évènement, vous aurez ainsi le volume de partage par page et par réseau social. 
vec ces deux rapports, vous avez déjà donc déjà un peu de matière pour analyser l'engagement de vos lecteurs sur votre contenu.

Donc, si nous faisons le point par rapport au challenge de départ. Les questions analytiques ont été définies et nous avons également identifié les rapports qui vont nous permettrent d'y répondre. La prochaine étape, c'est donc de trouver un moyen de nourrir ces rapports.

![souris en dessin animé qui demande à manger](https://media.giphy.com/media/11NLstLWNHhNC0/giphy.gif)

## Objectifs
## Contraintes

# 


J'ai une activité en tant que voyagiste. Je propose des voyages personnalisés en Asie du Sud Est. Dans une volonté de me créer de la visibilité et avoir la possibilité d'échanger avec mon marché, j'ai décidé de créer un blog qui présente la beauté de cette région du monde et décrit les voyages qui ont été organisés.
Afin de mesure