     -*- mode: text; coding: utf-8; -*-
    Copyright (C) 2014-2018 Free Software Foundation, Inc.

    Copying and distribution of this file, with or without modification,
    are permitted in any medium without royalty provided the copyright
    notice and this notice are preserved.

========================================================================

Les fichiers dans ce répertoire vous permettent de voir mom en pleine
action.

Si vous avez téléchargé et décompressé une version de mom depuis sa
page d'accueil, vous verrez qu'aucun exemple n'est accompagné du
fichier PDF (.pdf) correspondant, comme c'est le cas sur les versions
pré-compilées de groff, ou groff compilé à partir des sources.

Je n'ai pas inclu les PDF parce que je voulais conserver l'archive mom
aussi petite que possible. Pour générer les PDF, traitez les fichiers
avec pdfmom(1).

    pdfmom mom-pdf.mom > mom-pdf.pdf
    pdfmom sample_docs.mom > sample_docs.pdf
    pdfmom slide-demo.mom > slide-demo.pdf
    pdfmom -k letter.mom > letter.pdf
    pdfmom -k mon_premier_doc.mom > mon_premier_doc.pdf
    pdfmom -k typesetting.mom > typesetting.pdf

Les fichiers
------------

Tous les fichiers sont configurés pour le format lettre US, exceptés
mom-pdf.mom et mon_premier_doc.mom, qui utilisent le format A4.

***typesetting.mom**

Le fichier typesetting.mom montre l'utilisation d'éléments de
composition typographique: tabulations, tabulations intégrées dans des
chaînes de caractères, remplissage de lignes, texte sur plusieurs
colonnes et différents styles d'indentation; ainsi que certaines
subtilités et réglages précis disponibles via des macros et des
échappements en ligne ("inline escape", des commandes insérées
directement dans le texte, par opposition aux macros).

Comme ce fichier montre également l'utilisation d'une petite image au
milieu d'un texte et que cette image est la mascotte favorite de tout
le monde -- Tux, le fichier PDF de cette image, penguin.pdf, a été
ajouté dans ce répertoire.

***sample_docs.mom***

Le fichier sample_docs.mom montre en exemple les trois styles de
documents apportés par les macros de formattage de document de mom,
ansi que l'utilisation de COLLATE. Il montre également certaines
fonctionnalités PDF de mom dont l'écriture d'une ébauche de nouvelle
ou des liens cliquables dans une table des matières.

Le dernier exemple démontre, par un texte séparé en deux colonnes, la
souplesse de mom pour la conception de document.

Le PRINTSTYLE de ce fichier est TYPESET et vous donne une idée du
comportement par défaut de mom pour la composition typographique de
document.

Si vous souhaitez voir comment mom traite le même fichier quand
PRINTSTYLE est TYPEWRITE (c'est-à-dire dactylographié, avec espace
double) remplacez .PRINTSTYLE TYPESET par .PRINTSTYLE TYPEWRITE au
début du fichier.

***letter.mom***

Ceci est simplement l'exemple du tutorial de momdocs, prêt à être vu.

***slide-demo.mom***

Le fichier slide-demo.mom montre une présentation de diapositives
avec des effets PAUSE et TRANSITION.  Le fichier .pdf généré avec
pdfmom devrait être ouvert en mode Présentation d'un lecteur PDF
(Okular, Evince, Acroread).  Notez que pas tous les effets de
transition sont disponibles pour tous les lecteurs PDF.  

***mon_premier_doc.mom***

Le fichier mon_premier_doc.mom est un exemple simple en français
montrant l'utilisation d'éléments de formattage courants: titres de
section, paragraphes, listes, table des matières et liens PDF
cliquables. Il doit être généré avec l'option -k du fait de la
présence de caractères accentués.

Un certain nombre de réglages ont également été changés pour ce
document en français:  ATTRIBUTE_STRING est utilisé pour remplacer
"by" par "par" en tête de document (là où le titre et l'auteur sont
affichés). TOC_HEADER_STRING sert à modifier le titre de la table des
matières en "Table des matières" plutôt que "Table of Content". Enfin,
le paramètre de configuration INDENT_FIRST_PARAS est activé afin
d'indenter le premier paragraphe de chaque section -- ceci est l'usage
en typographie française.

***mom-pdf.mom***

Le manuel "Producing PDFs with mom and groff".

***mom.vim***

Les règles de coloration syntaxique vim sont baséés sur celles
fournies par Christian V. J. Brüssow (cvjb@cvjb.de). Copiez le fichier
mom.vim dans votre répertoire ~/.vim/syntax directory; ensuite,
autorisez la coloration syntaxique si ce n'est pas encore le cas:

  :syntax enable
ou
  :syntax on

***elvis_syntax.new***

Ceux qui utilisent elvis, le clone de vi, peuvent directement
copier-coller le contenu de ce fichier dans leur elvis.syn. Tous les
fichiers ayant l'extension .mom auront la coloration syntaxique.  Les
règles dans elvis_syntax ne sont pas exhaustive, mais aideront
beaucoup à rendre les fichiers mom plus lisibles.
