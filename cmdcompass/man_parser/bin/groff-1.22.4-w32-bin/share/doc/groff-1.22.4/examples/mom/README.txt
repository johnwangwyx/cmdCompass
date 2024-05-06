    -*- mode: text; coding: utf-8; -*-
    Copyright (C) 2004-2018 Free Software Foundation, Inc.

    Copying and distribution of this file, with or without modification,
    are permitted in any medium without royalty provided the copyright
    notice and this notice are preserved.

========================================================================

The files in this directory show mom in action.

If you have downloaded and untarrred a version of mom from her
homepage, you'll see that none of the example files come with
corresponding PDF (.pdf) files, as they do with pre-compiled
versions of groff, or groff built from source.

I haven't included the PDF output because I want to keep the mom
archive as lean as possible.  To view the PDF output, process the
files with pdfmom(1).

    pdfmom mom-pdf.mom > mom-pdf.pdf
    pdfmom sample_docs.mom > sample_docs.pdf
    pdfmom slide-demo.mom > slide-demo.pdf
    pdfmom -k letter.mom > letter.pdf
    pdfmom -k mon_premier_doc.mom > mon_premier_doc.pdf
    pdfmom -k typesetting.mom > typesetting.pdf

The files themselves
--------------------

All are set up for US letter papersize except mom-pdf.mom and
mon_premier_doc.mom, which uses A4.

***typesetting.mom**

The file, typesetting.mom, demonstrates the use of typesetting tabs,
string tabs, line padding, multi-columns and various indent styles,
as well as some of the refinements and fine-tuning available via
macros and inline escapes.

Because the file also demonstrates a cutaround using a small picture
of everybody's favourite mascot, Tux, the PDF file, penguin.pdf has
been included in the directory.

***sample_docs.mom***

The file, sample_docs.mom, shows examples of three of the document
styles available with the mom's document processing macros, as well
as demonstrating the use of COLLATE.  It also shows off some of
mom's PDF features, including a PDF outline and clickable links in
the printable Table of Contents.

The last sample, set in 2 columns, demonstrates mom's flexibility
when it comes to designing documents.

The PRINTSTYLE of this file is TYPESET, to give you an idea of mom's
default behaviour when typesetting a document.

If you'd like to see how mom handles exactly the same file when the
PRINTSTYLE is TYPEWRITE (ie typewritten, double-spaced), simply
change .PRINTSTYLE TYPESET to .PRINTSTYLE TYPEWRITE near the top of
the file.

***letter.mom***

This is just the tutorial example from the momdocs, ready for
previewing.

***slide-demo.mom***

The file, slide-demo.mom, demonstrates a slide presentation with
PAUSE and TRANSITION effects.  The .pdf created by pdfmom should be
opened in Presentation Mode in a PDF reader (e.g. Okular, Evince,
Acroread).  Note that not all transition effects are available in
all PDF readers.

***mon_premier_doc.mom***

The file, mon_premier_doc.mom, is a simple example in French showing
the use of common elements: section headings, paragraphs, lists, table
of contents and clickable links.  It should be generated with option -k
as there are some accented letters.

A few settings were also changed for this French document:
ATTRIBUTE_STRING is used to replace "by" by "par" in the document
header (where the title and the author are displayed).
TOC_HEADER_STRING is used to modity the Table of Content title to
"Table des matières". And finally, INDENT_FIRST_PARAS is used to
indent the first paragraph of a section -- this is the usual
convention in French typesetting.

***mom-pdf.mom***

The manual, Producing PDFs with mom and groff.

***mom.vim***

The vim syntax highlighting rules are based on those provided by
Christian V. J. Brüssow (cvjb@cvjb.de).  Copy mom.vim file to your
~/.vim/syntax directory; then, if your vim isn't already set up to
do so, enable mom syntax highlighting with

  :syntax enable
or
  :syntax on

***elvis_syntax.new***

For those who use the vi clone, elvis, you can paste this file into
your elvis.syn.  Provided your mom documents have the extension
.mom, they'll come out with colorized syntax highlighting.  The
rules in elvis_syntax aren't exhaustive, but they go a long way to
making mom files more readable.
