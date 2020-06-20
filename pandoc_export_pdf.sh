#!/bin/bash

pandoc "$1"\
	--include-in-header "markdown/latex_header.tex" \
	-V papersize:a4 \
	-V geometry:margin=2.5cm \
	-V fontsize=11pt \
    	-V mainfont="Liberation Serif" \
	-V linkcolor:blue \
	--bibliography "markdown/bibliografia.bib" \
	--csl "/home/guillermo/Documentos/git/tesis/markdown/apa.csl" \
	--pdf-engine=xelatex \
	-Vlang=es-419 \
	-o "$2"
