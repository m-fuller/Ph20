#Generate completed assignment PDF
.PHONY : pdf
pdf : document.tex *.png
	pdflatex $<

# Generate plots
%.png : ode.py
	python $<

#Generate version control log
vc.log : 
	git log > $@

.PHONY : clean
clean : 
	rm -f *.png
	rm *.pdf
