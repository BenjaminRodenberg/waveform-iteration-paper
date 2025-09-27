main: main.tex
	latexmk -interaction=nonstopmode -pdf -bibtex -shell-escape $^
	
name=main
auxiliary_files= $(name).log $(name).out $(name).aux $(name).bbl $(name).blg $(name).fdb_latexmk $(name).fls $(name).idx $(name).ilg $(name).ind $(name).lof $(name).lol $(name).lot $(name).run.xml $(name).toc $(name)-blx.bib $(name).loa

clean_nopdf:
	rm -rf $(auxiliary_files)
	
clean:
	rm -rf $(auxiliary_files) $(name).pdf

