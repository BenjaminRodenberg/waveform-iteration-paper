all: FP fQN rQN
FP: FP.pdf
fQN: fQN.pdf
rQN: rQN.pdf

# Rule to generate .tex files from .csv files
%.tex: data/%.csv
	python3 make-table-from-template.py $<

# Rule to generate .pdf files from .tex files
%.pdf: %.tex
	latexmk -interaction=nonstopmode -pdf -bibtex -shell-escape $<

name=main
derived_data= data/contour_0.001.csv data/contour_0.0001.csv data/contour_1e-05.csv data/contour_1e-06.csv data/contour_1e-07.csv data/times_reduced.csv
auxiliary_files= 

clean_nopdf:
	rm -rf *.log *.out *.aux *.bbl *.blg *.fdb_latexmk *.fls *.idx *.ilg *.ind *.lof *.lol *.lot *.run.xml *.toc *-blx.bib *.loa
	
clean:
	rm -rf *.log *.out *.aux *.bbl *.blg *.fdb_latexmk *.fls *.idx *.ilg *.ind *.lof *.lol *.lot *.run.xml *.toc *-blx.bib *.loa *.pdf
