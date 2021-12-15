#!/bin/bash

pandoc "$1"\
	--bibliography "markdown/bibliografia.bib" \
	--csl "markdown/apa-no-ampersand.csl" \
	--filter pandoc-crossref \
	--citeproc \
	--reference-doc "markdown/reference_v2.docx" \
	--lua-filter="markdown/pagebreak.lua" \
	-o "$2"
