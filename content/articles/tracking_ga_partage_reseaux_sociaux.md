Title: Challenge: Tracker les partages de son contenu avec Google Analytics
Date: 2018-12-19
Modified: 2018-12-22
Category: articles
Tags: tutoriels
Slug: tracking_partage_reseaux_sociaux_avec_google_analytics
Lang: fr
Authors: Julien Nuellas
Cover: /images/img_summary_production_par_petits_lots.jpg
Summary: Lorsque l'on souhaite mesurer l'engagement des utilisateurs envers son contenu, il est important d'analyser le volume de partage de ce dernier sur les réseaux sociaux. Cet article propose au travers d'un challenge, une façon simple et flexible de remonter cette donnée sur Google Analytics

J'adore résoudre les problèmes! C'est pourquoi j'ai envie à travers ce blog de me lancer des challenges. Je trouve l'approche intéressante pour plusieurs raisons:
1. Cela permet de partir d'un sujet concret
2. Cela permet de débattre!

En effet, pour un même problème, il y aura forcément plusieurs solutions. Cela permet donc de prendre un parti pris au travers de l'exercice et échanger ensemble selon votre propre approche également.

Pour ce challenge, je vous propose de partir du contexte suivant:

Charlie est un voyagiste qui propose des itinéraires éco-responsables uniquement en Asie du Sud Est. Au lancement de son activité, il a créé un blog afin de pouvoir partager sa passion sur cette région, véhiculer ses valeurs et construire une communauté autour de tout ça. Son blog, c'est www.asia-dream.com.

Pour mesurer son activité et l'engagement de ses lecteurs envers son contenu, il installé le code de suivi de Google Analytics qui me permet notamment de visualiser la durée par session, le nombre de pages vues par session, le taux de rebond, etc...
Mais il aimerait également visualiser l'engagement de ses lecteurs via leur volonté de partager sur les réseaux sociaux un contenu qui les a intéressés. Au-delà de la notion liée à l'intérêt porté par le lecteur sur le contenu, il y a également la notion de viralité qui rentre en jeu dans l'action de partage.

**Le défi lancé au travers de cet article est donc de proposer une solution (parmi tant d'autres) pour évaluer l'engagement des lecteurs de ce blog via le partage du contenu sur les réseaux sociaux.**

Avant d'aller plus loin, voyons ensemble quelques contraintes supplémentaires à laquelle la solution doit faire face.

## La solution doit respecter certaines contraintes

Afin de répondre à ce challenge, je me suis fixé quelques contraintes supplémentaires. En effet, le sujet étant large et digne d'intérêt pour plusieurs personnes - que ce soit quelqu'un ayant un blog personnel et qui souhaite évaluer la pertinence de son contenu, ou alors un professionnel s'étant lancé dans la production de contenu car cela fait partie de sa stratégie marketing -, j'ai pour objectif de proposer une solution la plus simple et la plus adaptable possible. Ainsi, la solution devra:

* Pouvoir s'intégrer sur tous les types d'architecture possible à partir du moment où un code de suivi Google Analytics a été implémenté sur le site.
* Minimiser le paramétrage sur Google Analytics. Utiliser les rapports existants le plus possible
* Proposer un script le plus facilement adaptable en fonction de l'implémentation des boutons de partage sur votre site.

Maintenant que tout est clair et défini, intéressons-nous plus en détail aux objectifs analytiques liés au tracking de ces actions de partage.

## Concrètement, comment j'évalue l'engagement de mes lecteurs via le partage sur les réseaux sociaux?

C'est effectivement une question digne d'intérêt. Evaluer l'engagement et la viralité de mon contenu via le partage sur les réseaux sociaux, c'est bien mais concrètement, quelles sont les questions sous-jacente?

### Quel est le volume de partage de mon contenu sur les réseaux sociaux sur une période donnée?

Tout d'abord, Charlie a envie d'évaluer la pertinence de son contenu en général suivant la tendance globale de partage de ce dernier sur les réseaux sociaux. Cela lui donnera notamment une évolution sur le long terme et permettra d'évaluer cette tendance en fonction des actions prises.

### Quels sont les réseaux sociaux les plus utilisés pour partager mon contenu?

Un autre point intéressant, Charlie a envie de connaître quelles sont les plateformes priorisées chez ses lecteurs. Cela lui permettra notamment d'adapter son contenu en conséquence et de prioriser sa communication sur les plateformes les plus utilisées par sa communauté.

### Quels sont les contenus les plus partagés sur les réseaux sociaux sur une période donnée?

Ensuite, Charlie a bien évidemment besoin de visualiser le degré d'engagement de ses lecteurs via le partage sur les réseaux sociaux par article et type de contenu. Cela lui permettra notamment d'identifier quel type de contenu intéresse le plus les lecteurs et a le plus de chance d'être viral.

## Comment répond-on à ces question dans Google Analytics?

Google Analytics propose quelques rapports déjà construits permettant de répondre à ces questions. Et comme l'une de mes contraintes consiste à minimiser les paramétrages sur la plateforme, la solution s'attachera à alimenter ce dernier et ne demandera pas la création d'un rapport personnalisé.

### Les rapports Evènements de Google Analytics

Au sein de la section Comportement, Google Analytics propose une série de rapports sur les **évènements**. 

![rapports evenements google analytics]({filename}/images/trackin_ga_share_rapport_event_menu.png)

Un évènement correspond à des actions uniques liées à un contenu et qui ne demande pas le chargement d'une nouvelle page. Ainsi, le partage d'un article constitue bien un évènement.

Pour ce challenge, les rapports qui vont nous intéresser seront les rapports:

* Comportement > Evenements > Principaux événements
* Comportement > Evenements > Pages

#### Le rapport Principaux évènement

Sans trop rentrer dans les détails, ce rapport permet d'évaluer les performances de vos évènements selon 3 dimensions principales:

* Catégorie d'évènement
* Action d'évènement
* Libellé d'évènement

Pour ce challenge, voici ce que je vous propose d'associer en face de ces 3 dimensions:

* Catégorie d'évènement = **"engagement"**. Cela permettra de regrouper tous les évènements d'engagement s'il en existe d'autres (par exemple, l'écriture d'un commentaire). Il s'agit de plus d'une catégorie par défaut.
* Action d'évènement = **"share"**. Cela permettra de regrouper tous vos évènements d'actions de partage au sein d'un même endroit et de les différencier de vos autres évènements d'engagement. Il s'agit également d'une action par défaut.
* Libellé d'évènement = **nom du réseau social**. Cette dimension vous permettra de différencier vos évènements en fonction de chaque réseau social.

Dans notre cas, en partant du principe que le partage sur les réseaux sociaux constitue votre seul évènement d'engagement, il pourrait être intéressant par exemple d'utiliser ce rapport avec comme dimension principale le libellé d'évènement et comme dimension secondaire les pages.
Cela vous permettra d'identifier par réseau social, les articles les plus partagés.

#### Le rapport évènements par page

Ce rapport propose de mesurer la performance de vos évènements avec comme dimension principale la pages (dans notre cas, l'article). Si vous ajoutez comme dimension secondaire le libellé d'évènement, vous aurez ainsi le volume de partage par page et par réseau social. 
Avec ces deux rapports, vous avez déjà donc déjà un peu de matière pour analyser l'engagement de vos lecteurs sur votre contenu.

Donc, si nous faisons le point par rapport au challenge de départ, à savoir Charlie qui souhaite intégrer l'action de partager son contenu sur les réseaux sociaux pour analyser plus précisément l'engagement de ses lecteurs.
Les questions analytiques ont été définies et nous avons également identifié les rapports qui vont nous permettre d'y répondre. La prochaine étape, c'est donc de trouver un moyen de les nourrir.

![souris en dessin animé qui demande à manger](https://media.giphy.com/media/11NLstLWNHhNC0/giphy.gif)

## Mettre en place le tracking d'évènement sur les boutons de partage

Il est désormais temps de mettre en place le tracking des évènements de partage sur le blog de Charlie. Pour cela Google propose une *event command* avec une syntaxe spécifique. Le petit point d'attention à avoir sur ce sujet, c'est que cette syntaxe diffère en fonction du type de code de suivi que vous utilisez. En effet, il y a trois principales façons de tracker son site avec Google Analytics.

### Quelques précisions sur l'implémentation initiale afin de resituer la solution qui va suivre

Google Analytics propose encore trois façon d'implémenter Google Analytics sur son site:

* Via la librairie **analytics.js**. Il s'agit de l'ancienne version du code de suivi mais qui est toujours opérationnelle.
* Via la librairie **gtag.js**. Il s'agit de la nouvelle version du code de suivi qui est désormais proposé par défaut.
* Via le Google Tag Manager. Google analytics a pu être installé via l'interface de Google Tag Manager. Il est basé sur la même infrastructure que la librairie gtag.js par ailleurs.

Dans notre cas, Charlie a implémenté le code de suivi **gtag.js**. Pourquoi? Tout simplement parce que c'est le code de suivi proposé par défaut lorsque l'on installe Google Analytics sur son site et qu'au vu de ses besoins, il n'a pas forcément besoin d'utiliser un Tag Manager. 
Cet article proposera donc une solution sur cette base d'implémentation (la plus fréquente finalement).

### Présentation de la syntaxe de l'*event command*

Sans rentrer dans les détails (pour plus d'information, la [documentation Google](https://developers.google.com/analytics/devguides/collection/gtagjs/events) est excellente!), voici à quoi ressemble:

```javascript
gtag('event', <action>, {
  'event_category': <category>,
  'event_label': <label>,
  'value': <value>
});
```

L'objectif est donc de déclencher cette fonction javascript au moment du clic sur un bouton de partage.
Dans notre cas, après lecture de la documentation, afin de pouvoir visualiser la donnée comme elle a été présentée précédemment, la syntaxe sera la suivante:

```javascript
gtag('event', 'share', {method : 'NOM_RESEAU_SOCIAL'})
```

La valeur ```NOM_RESEAU_SOCIAL``` sera différente en fonction du réseau social associé à chaque bouton.

Bon le décor est planté, voyons maintenant comment implémenter ça sur le blog de Charlie.

## Intégration du tracking d'évènement sur le blog de Charlie

Comme décrit précédemment, l'objectif est de déclencher cet *event command* lorsqu'un lecteur clique sur un bouton de partage sur l'un de ces articles. Examinons de plus près ces pages articles et ces boutons.

### La structure des URLs des pages articles du blog de Chalie

Comme la majorité des blogs, celui de Charlie ne contient pas que des pages d'articles. Il y a notamment, une homepage, une page archives, une page *A propos*, etc...
Cependant, chaque type de page possède une structure d'url bien définie. Pour les pages articles, elles sont constituées ainsi:

www.asia-dream.com/articles/NOM_ARTICLE

Pour chaque page article, on aura donc comme élément récurrent dans l'URL celui-ci : **/articles/**
Et c'est sur ces pages, et uniquement celles-ci, où les boutons de partage sont présents. Parlons en un peu de ces boutons justement!

### Les boutons de partage sur le blog de Charlie

Sur chaque article, Charlie a intégré des boutons de partage sur Linkedin, Facebook et Twitter.
Voici l'élément html associé:

```html
<section>
    <p id="post-share-links">
        <a href="URL_DE_PARTAGE_TWITTER" class="twitter" target="_blank" title="Share on Twitter">
            <i class="fa fa-twitter fa-lg"></i>
        </a>
        <a href="URL_DE_PARTAGE_FACEBOOK" class="facebook" target="_blank" title="Share on Facebook">
            <i class="fa fa-facebook fa-lg"></i>
        </a>
        <a href="URL_DE_PARTAGE_LINKEDIN" class="linkedin" target="_blank" title="Share on LinkedIn">
            <i class="fa fa-linkedin fa-lg"></i>
        </a>
    </p>
</section>
```

Pour simplifier, j'ai volontairement supprimé la structure des urls de partage au niveau des attributs ```href```.
Ce bout de code là, Charlie pense le répéter peut-être plusieurs fois dans chaque article (en début et en fin par exemple). 
Ce qui est important ici pour la suite, c'est que chaque bouton / lien est associé à une classe identifiant le réseau social correspondant. C'est notamment sur cet élément que la solution qui suit va se baser.
Voyons comment intégrer ces *event commands*.

### Intégration des *events commands* via un script javascript

Pour intégrer ces évènements, je vous propose la solution suivante que je décrirai ensuite morceau par morceau:

```javascript
// ------------------------------------------------
// ----- Déclaration de l'objet / de la classe -----
// ------------------------------------------------

class SocialButton {
    
    // A chaque instanciation, on récupère:
    //   --> La classe de l'élément html (this.name)
    //   --> L'ensemble des éléments HTML associés (this.buttons)
    //   --> On applique l'event command adéquate sur chaque bouton 
    //       via la méthode trackShareAction

    constructor(name) {
        this.name = name;
        this.buttons = document.getElementsByClassName(this.name);
        this.trackShareAction(this.buttons, this.name);
    }

    // La méthode trackShareAction a pour objectif de déclencher
    // l'event command sur chaque bouton récupéré

    trackShareAction(buttonElts, name) {
        for (let buttonElt of buttonElts) {
            buttonElt.addEventListener("click", () => {
                gtag('event', 'share', {method : name})
            });
        }
    }
}

// ------------------------------------------------
// ---------------- Initialisation ----------------
// ------------------------------------------------

// On cible les URLS où créer les instances 
// (uniquement les pages articles)
const url = new URL(document.location.href);
const pathRegex = /^\/articles\/.*\/$/

if (pathRegex.test(url.pathname)) {
    window.onload = () => {
        // Une fois l'ensemble des éléments chargés, on crée une instance
        // de la classe SocialButton pour chaque réseau social
        const facebook = new SocialButton("facebook");
        const twitter = new SocialButton("twitter");
        const linkedin = new SocialButton("linkedin");
    }    
}
```

### Pourquoi ce script?

Parmi les contraintes du challenge, il est noté que la mise en place puisse s'intégrer et s'adapter facilement dans la plupart des environnements.

Et c'est normalement le cas pour ce script. Il suffit de l'ajouter en bas de chaque page du site (avant la fermeture de la balise body) et faire quelques ajustements nécessaires. Voyons justement de quoi il s'agit.

### La classe SocialButton

Si vous n'êtes pas très à l'aise avec le javascript, considérez cette partie comme le moteur regroupant les différentes actions qui seront effectuées sur les boutons de partage. Mais la bonne nouvelle c'est que cette partie n'a pas besoin d'être modifiée!

### La partie *Initialisation*

Pour modéliser, la logique de cette partie, je vous propose d'appréhender ce script selon cette logique:

1. On définit dans un premier temps sur quel type de page on doit agir (ici, les pages articles). Pour cela, on utilise une expression régulière ```/^\/articles\/.*\/$/```. Cela signifie toutes les urls dont l'uri (ce qui suit le nom de domaine) ressemble à **/articles/QUELQUE_CHOSE**.

    Il s'agit du code suivant:

    ```javascript
    // On cible les URLS où créer les instances 
    // (uniquement les pages articles)
    const url = new URL(document.location.href);
    const pathRegex = /^\/articles\/.*\/$/
    ```

    Si par exemple, demain Charlie change la structure d'url de ces articles comme cela: www.asia-dream.com/posts/NOM_ARTICLE. Il suffira alors de modifier la variable ```pathRegex``` de cette façon : ```/^\/posts\/.*\/$/```

2. Si l'url sur laquelle l'internaute se trouve valide cette expression régulière ```if (pathRegex.test(url.pathname)) {}```...

3. ...Alors, lorsque tous les éléments de la page sont chargés, pour chaque bouton de partage, on crée une instance de SocialButton en transmettant la classe associée au bouton: ```const bouton = new SocialButton('CLASSE_BOUTON')```

Sur le blog de Charlie, il y a un bouton de partage pour facebook, un pour twitter et un pour linkedin, d'où les trois instances dans le script. Mais si demain, imaginons qu'il rajoute un bouton de partage sur Pinterest: 

```html
<a href="URL_DE_PARTAGE_PINTEREST" class="pinterest" target="_blank" title="Share on Pinterest">
    <i class="fa fa-pinterest fa-lg"></i>
</a>
```

on aurait alors une nouvelle instance:

```javascript
const pinterest = new SocialButton("pinterest")
```

Et voilà! Il n'y a rien besoin de plus.

## Une solution parmi tant d'autres

Comme expliqué au départ, il s'agit bien évidemment d'une solution parmi tant d'autres! Et pour enrichir le débat, n'hésitez pas à proposer votre approche du challenge dans les commentaires!
Cela permettra d'apporter d'autres éléments très intéressants j'en suis certain.
De plus, si vous vous retrouvez à devoir résoudre ce type de problématique de votre côté et que vous rencontrez quelques difficultés, je me ferai un plaisir de vous aider.