#!/bin/bash

pandoc "$1"\
	--bibliography "markdown/bibliografia.bib" \
	--csl "markdown/apa-no-ampersand.csl" \
	--filter pandoc-crossref \
	--citeproc \
	--pdf-engine=xelatex \
	-o "$2"
