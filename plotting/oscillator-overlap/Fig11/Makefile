main: main.tex
	python3 preproc.py data/contour_data.csv
	latexmk -interaction=nonstopmode -pdf -bibtex -shell-escape $^
	
name=main
derived_data= data/contour_0.001.csv data/contour_0.0001.csv data/contour_1e-05.csv data/contour_1e-06.csv data/contour_1e-07.csv data/times_reduced.csv
auxiliary_files= $(name).log $(name).out $(name).aux $(name).bbl $(name).blg $(name).fdb_latexmk $(name).fls $(name).idx $(name).ilg $(name).ind $(name).lof $(name).lol $(name).lot $(name).run.xml $(name).toc $(name)-blx.bib $(name).loa

clean_nopdf:
	rm -rf $(derived_data)
	rm -rf $(auxiliary_files)
	
clean:
	rm -rf $(derived_data)
	rm -rf $(auxiliary_files) $(name).pdf

