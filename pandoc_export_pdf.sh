#!/bin/bash

pandoc "$1"\
	--include-in-header "/home/guillermo/Documentos/git/tesis/markdown/latex_header.tex" \
	-V papersize:a4 \
	-V geometry:margin=2.5cm \
	-V fontsize=11pt \
    	-V mainfont="Liberation Serif" \
	-V linkcolor:blue \
	--bibliography "markdown/bibliografia.bib" \
	--csl "markdown/apa-6th-edition.csl" \
	--pdf-engine=xelatex \
	-V lang=es \
	-o "$2"


