Title: Installer un thème sur son blog statique Pelican
Date: 2018-11-18
Modified: 2018-11-18
Category: tutoriels
Tags: tutoriels
Slug: installer-un-theme-pelican
Lang: fr
Authors: Julien Nuellas
Summary: Découvrez comment installer un thème sur son blog Pelican

Notre blog est désormais installé et déployé et il est désormais possible d'écrire tous les articles souhaités.
Seulement, le thème principal n'est pas vraiment attractif et il serait sympa d'avoir la possibilité de le changer. C'est ce que nous allons découvrir dans cet article.

Il s'agit du sixième article d'un tutoriel dédié à la mise en place d'un blog statique. Dans cette logique, je me permets d'en rappeler la structure globale:

1. [Présentation du tutoriel et de ces objectifs]({filename}tuto_pelican_0_introduction.md)
2. [Un blog statique, c'est quoi et comment ça fonctionne?]({filename}tuto_pelican_1_whats_blog_statique.md)
3. [Mettre en place GitHub Pages pour l'hébergement d'un blog statique]({filename}tuto_pelican_2_githubpages_setup.md)
4. [Utiliser Pelican pour son blog statique]({filename}tuto_pelican_3_installer_pelican.md)
5. [Utiliser Travis pour automatiser le déploiement de son blog statique]({filename}tuto_pelican_4_installer_travis.md)
6. **Mettre en place un thème sur son blog statique Pelican**

Dans cet article, nous verrons donc où trouver le thème de nos rêves et verrons une façon simple d'en mettre un en place.

## Ou trouver un thème Pelican
---

Il existe de nombreux thèmes pour Pelican et il y a de fortes chances que vous trouviez votre bonheur.

Il est possible de les visualiser sur le site [www.pelicanthemes.com](http://www.pelicanthemes.com/).
Chaque thème contient une petite description ainsi qu'un imprim écran permettant d'obtenir un aperçu.
Et bien évidemment, chaque thème présenté contient un lien vers son repository github.

Il existe également un repository github contenant l'ensemble des codes sources des [thèmes pelican](https://github.com/getpelican/pelican-themes).

Voyons ensuite une méthode pour en installer un sur le blog tutoriel-pelican.

## Préparer son projet à recevoir un thème
---

Il existe plusieurs façon d'installer un thème Pelican. Pour ma part, j'ai privilégié la méthode qui installe le thème sélectionné au sein d'un répertoire *themes* du projet source.
Pourquoi? Je trouve ce choix intéressant pour trois raisons:

* Le thème est directement lié au projet
* Il est possible d'en installer plusieurs, de supprimer ou d'en ajouter un facilement
* Il est possible de personnaliser au fur et à mesure le thème sélectionné

Voyons comment procéder désormais.

### Création du répertoire thème

La première chose à faire est de créer le répertoire *themes* à la racine du projet. Au sein de ce répertoire, nous allons créer deux répertoires supplémentaires, **dist** et **src**.

```
themes/
    |- dist/
    |- src/
```

Le répertoire **dist** contiendra les fichiers qui seront utilisés lors du déploiement tandis que le répertoire **src** contiendra les fichiers sources du thème téléchargé sur lesquels il sera possible d'apporter des modifications et de tester avant de répliquer les fichiers sur le répertoire **dist**.

Dans cette logique, il n'est pas nécessaire de versionner le répertoire **src**. Ajoutons donc ce répertoire au sein du fichier .gitignore:

```
...
themes/src
```

### Ajoutons quelques modifications sur le fichier pelicanconf.py

Il est maintenant nécessaire d'indiquer à Pelican l'endroit où il devra récupérer le thème.
Pour faire cela, il suffit juste de rajouter une variable ```THEME``` au sein du fichier **pelicanconf.py** et d'y indiquer le chemin:

```python
THEME = "themes/dist"
```

Et voilà, le projet est prêt à recevoir notre thème.

## Installer un thème sur notre blog statique
---

### Cloner le code source du thème choisi

Pour le blog **tutoriel pelican**, mon choix s'est porté sur le thème [blue-penguin](https://github.com/jody-frankowski/blue-penguin/tree/c5e23e7753367b5beacce87b732cd1567c4818f9).

La première étape consiste à cloner le code source du thème au sein du répertoire **src**/

```
git clone https://github.com/jody-frankowski/blue-penguin.git themes/src
```

Le thème est désormais installé au sein du répertoire **src**.

Pour le moment, nous n'allons pas apporter de modifications sur ce thèmes et nous l'utiliserons tel quel. Nous pouvons donc simplement copier les fichiers au sein du répertoire **dist**:

```
cp -a themes/src/* themes/dist
```

Il suffit désormais de lancer votre thème en local pour vous apercevoir que votre blog n'a plus la même apparence.

### Ajouter les paramétrages nécessaires

Le fait d'avoir lancé le site en local nous a permis de constater que ce nouveau thème a bien été pris en compte.

En lisant le README du repository, on s'aperçoit qu'il est possible d'ajouter quelques configurations afin de personnaliser notamment le menu.
Pour ma part, je rajoute uniquement la variable **MENUITEMS** permettant de rajouter les liens vers ce blog et vers la documentation Pelican au sein du menu.

```python
MENUITEMS = (
    ('JN-Blog', 'https://www.jn-blog.com/'),
    ('Docs Pelican', 'http://docs.getpelican.com/en/stable/'),
)
```

Libre à vous d'apporter les modifications que vous souhaitez. Chaque thème comporte son lot de modifications afin de proposer la meilleure expérience possible.
Le thème est désormais installé et correctement paramétré. La structure mis en place permet de modifier et personnaliser facilement le thème.
Il ne reste plus qu'un petit déploiement afin de tout envoyer sur l'environnement de production.

![deploiement d'un theme pelican]({filename}/images/tuto-pelican-theme-production.png)

## Un dernier mot pour la route
---

J'espère que ces articles vous ont intéressés.
Nous avons vu ensemble au travers de ces articles et de ce [projet fil rouge](https://tutoriel-pelican.jn-blog.com) comment mettre en place un blog statique en utilisant **Pelican** comme générateur de sites statiques, **Github Pages** pour l'hébergement et **Travis CI** pour l'automatisation du déploiement.

N'hésitez pas à intervenir dans les commentaires afin d'avoir votre avis sur ce tutoriel et votre retour d'expérience. Vous avez certainement d'autres approches sur certains sujets et l'intérêt est de justement pouvoir les partager.

Si vous souhaitez également d'autres articles sur ce sujet comme par exemple mettre en place un système de commentaires, n'hésitez à me le notifier.

Il ne me reste plus qu'à vous souhaiter une bonne aventure en tant que bloggueur et j'espère avoir l'occasion de vous lire prochainement!
