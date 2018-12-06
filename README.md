# Le manuel de référence canonique de Csound

[![Build status](https://travis-ci.org/csound/manual.svg?branch=master)](https://travis-ci.org/csound/manual)

Le manual de référence de Csound est écrit en [DocBook](http://tdg.docbook.org/tdg/4.5/docbook.html) v4.
Pour apprendre à utiliser Docbook aller sur [docbook.org](http://docbook.org).

Si vous rencontrez des problèmes ou si vous avez des suggestions, ouvrez
[un ticket](https://github.com/csound/manual/issues), ou faites
[un fork de cet entrepôt et un pull request](https://guides.github.com/activities/forking/).


## Outils nécessaires

En plus d'autres outils spécifiques à ce qu'on construit, on a besoin de
Docbook, [Python](https://www.python.org) avec [Pygments](http://pygments.org)
v2.1 ou ultérieure ;
et [xsltproc](http://xmlsoft.org/XSLT/xsltproc2.html).

### Linux

Pour installer DocBook, les feuilles de style requises et xsltproc, sur un système
basé sur Debian (y compris Ubuntu), exécuter

```sh
sudo apt-get install -y docbook docbook-xsl xsltproc
```

Python est préinstallé sur la plupart des distributions Linux. Si
l'on a pas Python, aller sur https://docs.python.org/2/using/unix.html pour
apprendre comment installer Python ou le construire à partir des sources.

Pour installer Pygments v2.1 ou ultérieure, exécuter

```sh
sudo pip install 'pygments>=2.1'
```

ou si l'on a pas [pip](https://pip.pypa.io/),

```sh
sudo easy_install 'pygments>=2.1'
```

### MacOS

La manière la plus simple d'installer DocBook est sans doute via [Homebrew](http://brew.sh).
Pour installer Homebrew, suivre les instructions sur
https://brew.sh). Puis taper `brew install docbook` dans un terminal, suivi de
`brew install docbook-xsl`, pour installer les feuilles de style XSL de
DocBook.

Pour installer Pygments v2.1 ou ultérieure, taper dans un terminal


```sh
sudo easy_install 'pygments>=2.1'
```

Python et xsltproc sont préinstallés sur macOS.

### Windows

La manière la plus simple d'installer DocBook est sans doute via
[Cygwin](https://www.cygwin.com). Pour installer Cygwin aller sur
https://www.cygwin.com
et télécharger et exécuter un installeur pour la dernière version de Cygwin.

Pour installer Python, aller sur https://www.python.org/downloads/windows/ et
télécharger et exécuter un installeur de Python 2.7. Ne pas oublier d'ajouter
python.exe dans le path de Windows.

Aller sur http://pygments.org/download/ pour apprendre comment installer Pygments.


## Construire le manuel

Exécuter `make ⟨cible⟩` pour construire une `⟨cible⟩`. Par exemple, pour
construire une collection de pages HTML, exécuter `make html`.

On peut voir cette
erreur : “La variable XSL_BASE_PATH doit renseigner le répertoire d'installation
des feuilles de style XSL.” Pour indiquer à `make` où trouver les feuilles de
style XSL de DocBook, exécuter

```sh
make XSL_BASE_PATH=path/to/docbook/stylesheets ⟨cible⟩
```

au lieu de `make ⟨cible⟩`.

Si un message d'erreur indiquant que `CsoundDocumentLexer` est introuvable
pour construire une `⟨cible⟩`, c'est que vous utilisez probablement Pygments
v2.0.2 ou antérieure, et vous avez besoin de
[Pygments v2.1 ou ultérieure](#Outils nécessaires).

### HTML

Exécuter `make html` (ou seulement `make`) pour créer un répertoire nommé html
contenant une collection de fichiers HTML.


### PDF

En plus des [outils nécessaires](#outils-nécessaires), la construction des
fichiers PDF nécessitent [FOP d'Apache](https://xmlgraphics.apache.org/fop/). Il
peut être aussi nécessaire de télécharger et d'installer un [Java Runtime
Environment](http://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html).

Pour installer FOP sur Linux, exécuter


```sh
sudo apt-get install -y fop
```

Pour installer FOP sur macOS avec [Homebrew](https://brew.sh), exécuter

```sh
brew install fop
```

Exécuter `make pdf` pour créer un fichier PDF adapté à l'impression sur du
[papier letter](https://en.wikipedia.org/wiki/Letter_(paper_size)).

Exécuter `make pdfA4` pour créer un fichier PDF adapté à l'impression sur du
[papier A4](https://en.wikipedia.org/wiki/ISO_216#A_series).


### Aide HTML compilée

On ne peut construire une [aide HTML compilée]
(https://en.wikipedia.org/wiki/Microsoft_Compiled_HTML_Help) que sur Windows.
En plus des [outils nécessaires](#outils-nécessaires) il faut utiliser le HTML Help
Workshop. Pour installer le HTML Help Workshop, aller sur
https://go.microsoft.com/fwlink/?LinkId=14188 pour télécharger htmlhelp.exe et
double-cliquer ensuite sur htmlhelp.exe.

Exécuter `make htmlhelp` pour créer un fichier d'aide HTML compilée (.chm).


## Editer le manuel

DocBook est en [XML](https://en.wikipedia.org/wiki/XML). Lorsque l'on écrit du
XML, il ne faut pas oublier de fermer les balises. Voici du XML valide :

```xml
<para>texte</para>
```

alors que celui-ci ne l'est pas :

```xml
<para>texte</ERROR>
```

DocBook v4 a une [définition de type de document
(DTD)](http://docbook.org/xml/4.5/) qui décrit les éléments valides de DocBook
et leurs attributs. Voir [_DocBook: The Definitive
Guide_](http://tdg.docbook.org/tdg/4.5/docbook.html) pour en savoir plus.


### Ajouter une entrée d'opcode

En général, une entrée pour un nouvel opcode nommé `newopcodename` sera un
fichier XML nommé newopcodename.xml contenant

```xml
<refentry id="newopcodename">
    <!-- More mark-up… -->
</refentry>
```

On peut commencer à documenter un opcode en prenant une entrée existante comme
modèle. Toutes les entrées des opcodes sont dans le [répertoire opcodes](opcodes).
On peut aussi utiliser [opcodes/templates.xml](opcodes/template.xml) comme point
de départ.

Pour incorporer une nouvelle entrée dans le manuel :

1. Ajouter l'entrée comme une entité dans 
[manual.xml](manual.xml). Par exemple, si l'on
dépose newopcodename.xml dans le répertoire opcodes, il faut ajouter cette entité
dans manual.xml :

    ```xml
    <!ENTITY opcodesnewopcodename SYSTEM "opcodes/newopcodename.xml">
    ```
    
2. Utiliser l'entité pour ajouter l'entrée de l'opcode à
[opcodes/top.xml](opcodes/top.xml). Les entrées
des opcodes y étant rangées par ordre alphabétique, trouver où insérer l'opcode
dans la liste et ajouter :

    ```xml
    &opcodesnewopcodename;
    ```

3. Faire un lien vers cet opcode depuis une section appropriée du manuel. Par
exemple, si `newopcodename` doit être inclus avec les opcodes de traitement
spectral en temps réel, ajouter un
[élément `link`](http://tdg.docbook.org/tdg/4.5/link.html) à
[spectral/realtime.xml](spectral/realtime.xml), comme ceci :

    ```xml
    <link linkend="newopcodename"><citetitle>newopcodename</citetitle></link>
    ```
Répéter cette étape pour chaque section dans laquelle votre opcode devrait être
inclus.

4. On peut aussi utiliser facultativement un [élément 
`refentryinfo`](https://github.com/csound/manual/search?q=refentryinfo+path%3Aopcodes+filename%3Atemplate.xml)
pour que l'opcode soit correctement référencé dans la [référence
rapide](https://csound.github.io/docs/manual/MiscQuickref.html). Utiliser une des
catégories dans [categories.py](categories.py). Si l'on omet
l'élément `refentryinfo`, l'opcode sera référencé dans la catégorie
[Divers](https://github.com/csound/manual/search?q=Miscellaneous+filename%3Acategories.py).)

5.Si possible, ajouter un [élément `link`](http://tdg.docbook.org/tdg/4.5/link.html)
à l'opcode dans la section appropriée de [Opcodes
Overview](https://csound.github.io/docs/manual/PartOpcodesOverview.html).


## Maintenance

Il y a plusieurs cibles pour préparer les fichiers d'une distribution. Bien
mettre à jour le numéro de version dans
[manual.xml](https://github.com/csound/manual/search?q=csoundversion+filename%3Amanual.xml)
et dans
[Makefile](https://github.com/csound/manual/search?q=VERSION+filename%3AMakefile)
afin que les fichiers soient générés avec ce numéro. Il est aussi utile de mettre à jour
la section [Les nouveautés …](preface/whatsnew.xml) pour chaque
distribution.
