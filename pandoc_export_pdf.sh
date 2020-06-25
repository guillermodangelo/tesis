#!/bin/bash

pandoc "$1"\
	--bibliography "markdown/bibliografia.bib" \
	--csl "markdown/apa.csl" \
	--pdf-engine=xelatex \
	-o "$2"
