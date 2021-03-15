#!/bin/bash

pandoc "$1"\
	--bibliography "markdown/bibliografia.bib" \
	--csl "markdown/apa-no-ampersand.csl" \
	--filter pandoc-crossref \
	--filter pandoc-citeproc \
	--reference-doc "markdown/reference.docx" \
	--lua-filter="markdown/pagebreak.lua" \
	--filter pandoc-docx-pagebreak \
	-o "$2"
