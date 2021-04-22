#!/bin/bash

pandoc "$1"\
	--bibliography "markdown/bibliografia.bib" \
	--csl "markdown/apa-no-ampersand.csl" \
	--filter pandoc-crossref \
	--citeproc \
	--reference-doc "markdown/reference.docx" \
	--lua-filter="markdown/pagebreak.lua" \
	-o "$2"
