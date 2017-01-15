# Au sujet du manuel 

[![Build status](https://travis-ci.org/csound/manual-fr.svg?branch=master)](https://travis-ci.org/csound/manual-fr)

Le manual de référence de Csound est écrit en Docbook-XML. On peut trouver plus
d'information sur Docbook-XML en consultant les liens suivants :

http://docbook.org/
http://www.sagehill.net/book-description.html

Si vous rencontrez des problèmes ou si vous avez des suggestions, rapportez les
sur la liste de messagerie des développeurs de Csound.


# Construire le manuel

Pour construire le manuel, différents outils sont nécessaires selon le format
de la cible désirée. Toutes les cibles nécessitent xsltproc et il faut que les
DTD de Docbook XML soient installées et trouvables par xsltproc. Les feuilles
de style de Docbook XSL doivent aussi être installées. L'endroit où se trouvent
les feuilles de style peut être indiqué via la variable XSL_BASE_PATH :

    $ make XSL_BASE_PATH=chemin/vers/installation/xsl <cible>

Le chemin par défaut est /usr/share/xml/docbook/stylesheet/nwalsh/

Sous Linux, la plupart des distributions incluent ces programmes ou les rendent
disponibles dans des entrepôts de paquets pour les distributions respectives.

Sous Windows, on peut trouver xsltproc dans l'environnement Cygwin
(http://www.cywgin.com). Une version compilée nativement pour Windows est
disponible ici :

http://zlatkovic.com/libxml.en.html

Mac OS 10.5 (leopard) inclue xsltproc.

(NOTE : Si vous travaillez sous OSX ou OS9 et si vous trouvez xsltproc pour ces
plateformes ou un autre processeur XSLT convenant, mettez à jour cette
documentation SVP.)

Le manuel est réalisé en utilisant make avec le Makefile inclus. Par exemple
pour faire la version html (canonique), la seule commande nécessaire est :

    $ make html

Pour démarrer une nouvelle construction, utiliser

    $ make clean

Les autres cibles comprennent pdf, pdfA4 et htmlXO. Consulter le Makefile pour
la distribution et les autres cibles.


## HTML 

Utiliser :

    $ make html

Nécessite : Python (pour générer la version avec cadres et mettre à jour la
            référence rapide)


## PDF 

Utiliser :

    $ make pdf

ou

    $ make pdfA4

Nécessite : 

* Apache FOP (http://xmlgraphics.apache.org/fop/)
* Java Advanced Imaging Library (https://jai.dev.java.net/binary-builds.html)
* Un environnement Java Runtime pour exécuter les éléments ci-dessus.

FOP peut avoir besoin de beaucoup de mémoire, il est donc recommandé d'éditer le
fichier fop.sh et d'ajouter "-Xmx384m" à la dernière ligne, ce qui donne :

    $ JAVACMD -Xmx384m -classpath "$LOCALCLASSPATH" $FOP_OPTS org.apache.fop.apps.Fop "$@"

Cela augmente la quantité de mémoire maximale que la VM peut utiliser à 384 Moctets,
qui seront nécessaires pour que FOP puisse s'exécuter, car le manuel est conséquent.


## HTMLHELP 

Utiliser :

    $ make htmlhelp

Nécessite : Microsoft HTML Help Workshop
              (http://msdn.microsoft.com/library/default.asp?url=/library/en-us/htmlhelp/html/hwMicrosoftHTMLHelpDownloads.asp)

Cette cible compile un fichier .chm de Windows, un format qui a remplacé WinHelp.


# Editer le manuel

## Modifier une entrée

En général gardez en tête le fait que ces fichiers sont du XML et doivent être
valides. Toutes les balises ouvertes doivent être fermées, comme
<para>Mon information</para>.

De plus la DTD de Docbook-XML décrit ce qui est bien formé pour le document, ce
qui veut dire que certaines balises ne sont permises qu'à l'intérieur d'autres
balises. Pour plus d'information sur les balises valides de Docbook, consulter
"Docbook: The Definitive Guide" par Norm Walsh, disponible sur
http://docbook.org/.


## Ajouter une entrée pour un opcode 

La meilleure façon de commencer est de prendre une entrée existante et de
l'utiliser comme canevas. Toutes les entrées d'opcode sont rangées dans le
répertoire opcodes. Vous pouvez baser votre entrée sur une entrée existante
ou utiliser opcodes/templates.xml.

Pour incorporer une nouvelle entrée dans le manuel, quelques éléments sont
nécessaires.

1. Ajouter l'entrée comme une entité dans manual.xml. Par exemple, si vous
mettez le fichier myOpcodeEntry.xml dans le répertoire opcodes, vous devez
ajouter cette ligne dans manual.xml:

    <!ENTITY opcodesmyopcodeentry SYSTEM "opcodes/myOpcodeEntry.xml">

2. Ajouter l'entrée dans opcodes/top.xml en utilisant l'entité. C'est ce qui
ajoutera l'entrée dans le manuel de référence. Les entrées sont classées par
ordre alphabétique. Il faut donc trouver la place de votre opcode dans la
liste et l'y insérer :

    &opcodesmyopcodeentry;

La ligne ci-dessus utilise l'entité définie dans le fichier manual.xml
(pensez-y comme une directive #include).

3. Après cela, il vous faudra sans doute trouver la section d'entête depuis
laquelle l'opcode doit être référencé. Par exemple, si myOpcodeEntry doit se
trouver dans la même catégorie que les opcodes pvs dans spectral/realtime.xml,
il sera ajouté dans ce fichier comme :
    
    <link linkend="myOpcodeEntry"><citetitle>My Opcode Entry</citetitle></link>

L'attribut linkend ci-dessus pointe vers un ID docbook. L'ID "myOpcodeEntry"
doit être défini dans myOpcodeEntry.xml, probablement au niveau supérieur sous
la forme :

    <refentry id="myOpcodeEntry">

Répétez l'étape 3 pour chaque section dans laquelle vous pensez que l'opcode
doit être rangé.

4. Ajouter la balise info appropriée afin que l'opcode soit correctement rangé
dans la référence rapide. S'il n'y a pas de balise info l'opcode apparaitra sous
la rubrique "Divers". Consultez les catégories disponibles dans quickref-fr.py.

5. Si possible référencer l'opcode dans la section adéquate de la partie II du
manuel, et ajouter les références croisées nécessaires.

6. Pour transformer le fichier de l'exemple myOpcodeEntry.csd en
myOpcodeEntry.csd.xml (dans examples-xml), utiliser le script csd2docbook.py ou
csd2docbook2.py. Le premier utilise l'API de Csound pour contruire une liste
des opcodes tandis que le second utilise le fichier opcode_list.txt (qui contient
une liste similaire au résultat de la commande 'csound -z'). Par exemple :
$ python csd2docbook2.py -f genarray_i.csd crée le fichier genarray_i.csd.xml
à partir de genarray_i.csd pour référence dans l'entrée de l'opcode genarray_i.


# Pour la publication

Il y a plusieurs cibles préparant les fichiers d'une distribution. Il ne faut
pas oublier de changer le numéro de version afin que les fichiers et les
contenus soient générés avec ce numéro. On doit le changer à la fois dans
manual.xml et dans le Makefile. Il est aussi utile de mettre à jour la section
"Les nouveautés de Csound x.xx" pour chaque distribution.

## Conseils pour l'édition XML

* Il faut échapper les symboles "<" et ">" lorsqu'on les utilisent dans du texte
à l'intérieur de balises XML. Les entités correspondantes sont "&lt;" et "&gt;".
* La balise refsect1 se termine par le chiffre 1, pas la lettre l.
* On peut tester un fichier XML en l'ouvrant dans un navigateur web (comme
Firefox, Mozilla, Internet Explorer, etc.). La plupart des navigateurs affichent
le fichier XML s'il est correct ou bien donnent un message d'erreur si le fichier
XML n'est pas valide, en précisant où se trouve l'erreur.

L'utilisaion d'un éditeur dédié à XML facilite l'édition du manuel. Emacs en mode
sgml ou Kate en mode XML ou jEdit en mode XML aident beaucoup.


