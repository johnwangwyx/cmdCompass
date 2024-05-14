" Copyright (C) 2012-2018 Free Software Foundation, Inc.
"
" Copying and distribution of this file, with or without modification,
" are permitted in any medium without royalty provided the copyright
" notice and this notice are preserved.

" Vim syntax file
" Language:    mom
" Maintainer:  Peter Schaffter (peter@schaffter.ca)
" Last Change: So 06 Mär 2005 17:28:13 CET
" Filenames:   *.mom
" URL:         http://www.cvjb.de/comp/vim/mom.vim
" Note:        Remove or overwrite troff syntax for *.mom-files with filetype/filedetect.
" Version:     0.1
"
" Mom: Macro set for easy typesetting with troff/nroff/groff.

" For version 5.x: Clear all syntax items
" For version 6.x: Quit when a syntax file was already loaded
if version < 600
	syntax clear
elseif exists("b:current_syntax")
	finish
endif

" Mom is case sensitive
syn case match

" Synchronization, I know it is a huge number, but normal texts can be
" _very_ long ;-)
syn sync lines=1000

" Characters allowed in keywords
if version >= 600
	setlocal iskeyword=@,#,$,%,48-57,.,@-@,_,\\,{,},192-255
else
	set iskeyword=@,#,$,%,48-57,.,@-@,_,\\,{,},192-255
endif

" mom/groff macros and requests (the initial dot or single-quote)
"
" Highlighting carries through to EOL; macro names, requests and
" arguments are contained
syn match startRequest /^\s*\(\.\|'\)\s*.*$/ contains=momMacro,groffCommentLine,groffRequest,momRegister,groffNoLineBreak,momInteger,groffUnit,momString,momSpecialParam,groffDelimiter,groffRegister,groffPreprocessor,groffBraces

" mom macros
syn region momMacro start=/^\s*\(\.\|'\)\s*\zs[A-Z0-9_(){}\[\]]\+/ end=/\s\+\|$/

" mom registers and strings
syn match momRegister /\(\$\|#\)[A-Za-z][_0-9A-Za-z]*/ contains=momRegisterStart

syn match momRegisterStart /#\|\$/ contained

" mom comment region
syn region momCommentRegion matchgroup=startRequest start='\<\.\(COMMENT\)\|\(SILENT\)\>' end='\<\.\(COMMENT\s\+OFF\)\|\(SILENT\s\+OFF\)\>' skip='$'

" groff requests
syn match groffRequest /^\s*\(\.\|'\)\s*\zs[a-z0-9]\+/

" groff comment region
syn region groffCommentLine start='\(\\!\)\|\(\\"\)\|\(\\#\)' end='$' contains=momTodo
syn region groffCommentRegion start="^\s*\.\s*ig" matchgroup=startRequest end="^\.\.$" contains=startRequest

" Preprocessor requests
syn match groffPreprocessor /[^A-Z]\zs\(EQ\s*$\|EN\s*$\|GS\s*$\|GE\s*$\|GF\s*$\|PS\s*$\|PE\s*$\|R1\s*$\|R2\s*$\|TS\s*$\|TE\s*$\|TH\s*$\)/ contained
syn match groffPreprocessor /[^A-Z]\zs\(G1\s*$\|G2\s*$\|IS\s*$\|IE\s*$\|cstart\s*$\|cend\s*$\)/ contained

" Preprocessor requests for refer
syn match groffPreprocessor /\(\[\s*$\|\]\s*$\)/ contained

" Quoted strings
syn region momString matchgroup=startRequest start='"\zs' end='"\|$' contains=groffNoLineBreak,groffGreek,groffSpecialChar,momInteger,momFloatEN,momFloatDE,momBracketRegion,momBracketError,momSpecialMove contained

" Special characters
syn match groffSpecialChar '\\\((\|\[\)[-+A-Za-z0-9*<>=~!\/]\+\]*'

" Greek symbols
syn match groffGreek '\\(\*[A-Za-z]\+'

" Hyphenation marks
syn match groffHyphenation '\\%'

" Masking of line breaks
syn match groffNoLineBreak /\\\s*$/ contains=groffBraces

" groff number and string register delimiters
syn region groffDelimiter start=/\\*\\\(n+*\|\*\)\((\|\[\)\</ end=/\(\s\|\]\|$\)/ contains=momRegister,groffRegister,groffOperators

" groff registers
syn match groffRegister /\\\((\|\[\)\zs\.*[a-z]\+/

" groff operators
syn match groffOperators /\(+\|-\|\/\|\*[^[]\)/ contained

" Units (of measure)
syn match groffUnit '[-+]\=\([0-9]\|]\)\+\zs[icPpvusfz]\=' contained

" Braces
syn match groffBraces /\(\\{\|\\}\)/ contained

" Error
syn match groffError '\\\[ \+[[:print:]]\+ \+[[:print:]]\+\]'

" For version 5.7 and earlier: only when not done already
" For version 5.8 and later: only when an item doesn't have highlighting yet
if version >= 508 || !exists("did_mom_syn_inits")
	if version < 508
		let did_mom_syn_inits = 1
		command -nargs=+ HiLink hi link <args>
	else
		command -nargs=+ HiLink hi def link <args>
	endif

HiLink groffError               Error
HiLink groffBraces              darkmagenta
HiLink groffCommentLine		darkcyan
HiLink groffCommentRegion	cyan
HiLink groffDelimiter		cyan
HiLink groffGreek		cyan
HiLink groffHyphenation		cyan
HiLink groffNoLineBreak		cyan
HiLink groffOperators		white
HiLink groffPreprocessor	brown
HiLink groffRegister		darkgreen
HiLink groffRequest		magenta
HiLink groffSpecialChar		darkcyan
HiLink groffUnit		brown
HiLink momCommentRegion		darkcyan
HiLink momMacro			red
HiLink momRegister		green
HiLink momRegisterStart         magenta
HiLink momSpecialParam		red
HiLink momString		white
HiLink startRequest		yellow
	delcommand HiLink
endif

let b:current_syntax = "mom"

" vim:ts=8:sw=4:nocindent:smartindent:
